
import React, { useState, useEffect } from "react";
import Navbar from "./Navbar";

interface Article {
  title: string;
  content: string;
  source: string;
  published_at: string;
  category: string;
  author: string;
  url:string;
}

function Aggregator() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/news")
      .then((response) => response.json())
      .then((data) => {
        console.log("Article URLs:", data.map(a => a.url));
        setArticles(data);
        setLoading(false);
      })
  
      .catch((error) => {
        console.error("Error fetching articles:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="text-center text-white pt-20">Loading...</div>;
  if (articles.length === 0) return <div className="text-center text-white pt-20">No articles found.</div>;

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white">
      <Navbar />
      <div className="pt-32 px-4 max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-10">News Aggregator</h1>
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {articles.map((article, index) => (
            <div key={index} className="bg-white bg-opacity-10 backdrop-blur-sm p-6 rounded-xl shadow-lg hover:scale-105 transition-transform">
              <h2 className="text-2xl font-semibold mb-2">{article.title}</h2>
              <p className="text-gray-300 mb-2">{article.content}</p>
              <p className="text-sm text-gray-400">Source: {article.source}</p>
              <p className="text-sm text-gray-400">
                Published: {new Date(article.published_at).toLocaleString()}
              </p>
              <p className="text-sm text-gray-400">Category: {article.category}</p>
              <p className="text-sm text-gray-400">Author: {article.author}</p>
              <a 
  href={article.url || "#"} 
  target="_blank" 
  rel="noopener noreferrer"
  className="inline-block mt-4 px-4 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 transition-colors"
  onClick={(e) => !article.url && e.preventDefault()}
>
  {article.url ? "Read full article" : "No link available"}
</a>


            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Aggregator;
