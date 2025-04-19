import React, { useState, useEffect } from "react";
import Navbar from "./Navbar";

// Helper to strip HTML tags and truncate to N chars
function getTruncatedText(html: string, maxLength: number) {
  // Remove HTML tags
  const div = document.createElement("div");
  div.innerHTML = html;
  const text = div.textContent || div.innerText || "";
  // Truncate if needed
  if (text.length > maxLength) {
    return text.slice(0, maxLength) + "...";
  }
  return text;
}

interface Article {
  title: string;
  content: string;
  source: string;
  published_at: string;
  category: string;
  author: string;
  url: string;
  image?: string;
}

const Aggregator = () => {
  const [articles, setArticles] = useState<Article[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Use relative URL if you have Vite proxy set up
  const API_BASE_URL = "";

  useEffect(() => {
    setLoading(true);
    setError(null);

    const fetchUrl =
      selectedCategory === "all"
        ? `/api/news`
        : `/api/news/filter?category=${selectedCategory}`;

    fetch(fetchUrl)
      .then((response) => {
        if (!response.ok) {
          return response.text().then((text) => {
            throw new Error(
              `API error: ${response.status} ${text.substring(0, 100)}...`
            );
          });
        }
        return response.json();
      })
      .then((data) => {
        setArticles(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Fetch error:", err);
        setError(err.message);
        setLoading(false);
      });
  }, [selectedCategory]);

  const CategoryFilter = ({
    selected,
    onChange,
  }: {
    selected: string;
    onChange: (category: string) => void;
  }) => {
    const [categories, setCategories] = useState<string[]>([]);

    useEffect(() => {
      fetch(`/api/categories`)
        .then((res) => {
          if (!res.ok) {
            return ["general", "technology", "politics", "environment"];
          }
          return res.json();
        })
        .then(setCategories)
        .catch(() => {
          setCategories(["general", "technology", "politics", "environment"]);
        });
    }, []);

    return (
      <div className="category-filters mb-8 flex flex-wrap gap-4">
        <button
          key="all"
          onClick={() => onChange("all")}
          className={`px-4 py-2 rounded-lg ${
            selected === "all"
              ? "bg-purple-600 text-white"
              : "bg-gray-800 hover:bg-gray-700 text-gray-300"
          }`}
        >
          All
        </button>
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => onChange(cat)}
            className={`px-4 py-2 rounded-lg ${
              selected === cat
                ? "bg-purple-600 text-white"
                : "bg-gray-800 hover:bg-gray-700 text-gray-300"
            }`}
          >
            {cat}
          </button>
        ))}
      </div>
    );
  };

  const ArticleCard = ({ article }: { article: Article }) => (
    <div className="bg-white bg-opacity-10 backdrop-blur-sm p-6 rounded-xl shadow-lg hover:scale-105 transition-transform">
      {article.image ? (
        <img
          src={article.image}
          alt={article.title}
          className="mb-4 rounded-lg h-48 w-full object-cover"
          onError={(e) => {
            (e.target as HTMLImageElement).style.display = "none";
          }}
        />
      ) : (
        <div className="mb-4 rounded-lg h-48 w-full bg-gray-800 flex items-center justify-center">
          <span className="text-gray-500">No image</span>
        </div>
      )}
      <h2 className="text-2xl font-semibold mb-2">{article.title}</h2>
      {/* Render truncated plain text content */}
      <p className="text-gray-300 mb-2">
        {getTruncatedText(article.content, 220)}
        {getTruncatedText(article.content, 220).endsWith("...") && (
          <a
            href={article.url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-purple-400 ml-1 underline"
          >
            Read more
          </a>
        )}
      </p>
      <div className="text-sm space-y-1">
        <p className="text-gray-400">Source: {article.source}</p>
        <p className="text-gray-400">Category: {article.category}</p>
        <p className="text-gray-400">Author: {article.author}</p>
        <p className="text-gray-400">
          Published: {new Date(article.published_at).toLocaleDateString()}
        </p>
      </div>
      <a
        href={article.url}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-4 inline-block px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-md transition-colors"
      >
        Read Full Article
      </a>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white">
      <Navbar />
      <div className="pt-32 px-4 max-w-6xl mx-auto">
        <CategoryFilter
          selected={selectedCategory}
          onChange={setSelectedCategory}
        />

        {loading && (
          <div className="text-center py-10">
            <p className="text-xl">Loading articles...</p>
          </div>
        )}

        {error && (
          <div className="text-center py-10 text-red-400">
            <p className="text-xl">Error loading articles</p>
            <p className="mt-2">Please check that your backend server is running.</p>
            <p className="mt-2 text-sm">{error}</p>
          </div>
        )}

        {!loading && !error && articles.length === 0 && (
          <div className="text-center py-10">
            <p className="text-xl">No articles found</p>
          </div>
        )}

        {!loading && !error && articles.length > 0 && (
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {articles.map((article, index) => (
              <ArticleCard key={index} article={article} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Aggregator;
