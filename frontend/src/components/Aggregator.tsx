import React, { useState, useEffect } from "react";

function Aggregator() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch articles from backend API (/api/news)
    fetch("http://127.0.0.1:5000/api/news")
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched Articles:", data);
        setArticles(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching articles:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  if (articles.length === 0) return <div>No articles found.</div>;

  return (
    <div className="min-h-screen bg-gray-100 text-black">
      <h1 className="text-3xl font-bold text-center py-6">News Aggregator</h1>
      <div className="max-w-4xl mx-auto grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {articles.map((article, index) => (
          <div key={index} className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold">{article.title}</h2>
            <p className="text-gray-600">{article.content}</p>
            <p className="text-sm text-gray-500">
              Source: {article.source} | Published:{" "}
              {new Date(article.published_at).toLocaleString()}
            </p>
            <p className="text-sm text-gray-500">Category: {article.category}</p>
            <p className="text-sm text-gray-500">Author: {article.author}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Aggregator;
