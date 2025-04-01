import React, { useState } from 'react';
import Navbar from './Navbar';

const Summarizer = () => {
  const [description, setDescription] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const API_BASE_URL = "http://127.0.0.1:5000"; // Change if deployed online

  const handleSummarize = async () => {
    if (!description.trim()) {
      alert("Please enter a news description to summarize.");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/summarize`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: description, num_sentences: 3 })
      });

      const data = await response.json();
      if (response.ok) {
        setSummary(data.summary);
      } else {
        alert("Error: " + data.error);
      }
    } catch (error) {
      alert("Failed to connect to the server!");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white">
      <Navbar />
      <main className="pt-40 w-full max-w-lg mx-auto px-4 bg-white bg-opacity-10 p-8 rounded-xl shadow-lg">
        <h2 className="text-3xl font-bold mb-4 text-center">Summarize News</h2>
        <p className="text-center mb-6 text-gray-300">Get a concise summary of your news article</p>

        <div className="mb-4">
          <label className="block mb-1">Description</label>
          <textarea className="w-full p-2 rounded bg-black bg-opacity-30 focus:outline-none" 
            placeholder="Enter news description" rows="4" 
            value={description} onChange={(e) => setDescription(e.target.value)}>
          </textarea>
        </div>

        <button onClick={handleSummarize} className="w-full bg-green-600 hover:bg-green-700 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg">
          {loading ? "Summarizing..." : "Summarize"}
        </button>

        {summary && (
          <div className="mt-4 p-4 bg-gray-800 rounded">
            <h3 className="text-xl font-semibold">Summary:</h3>
            <p>{summary}</p>
          </div>
        )}
      </main>
    </div>
  );
};

export default Summarizer;
