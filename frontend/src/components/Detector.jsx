import React, { useState } from 'react';
import Navbar from './Navbar';

const FakeNewsDetector = () => {
  const [description, setDescription] = useState('');
  const [sourceUrl, setSourceUrl] = useState('');
  const [verification, setVerification] = useState('');
  const [loading, setLoading] = useState(false);

  const API_BASE_URL = "http://127.0.0.1:5000"; // Change if deployed online

  const handleVerify = async () => {
    if (!description.trim()) {
      alert("Please enter a news description to verify.");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: description, url: sourceUrl }) // Sending URL if needed
      });

      const data = await response.json();
      if (response.ok) {
        setVerification(data.prediction);
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
        <h2 className="text-3xl font-bold mb-4 text-center">Verify News</h2>
        <p className="text-center mb-6 text-gray-300">Check if a news article is real or fake</p>

        {/* Description Input */}
        <div className="mb-4">
          <label className="block mb-1">Description*</label>
          <textarea className="w-full p-2 rounded bg-black bg-opacity-30 focus:outline-none" 
            placeholder="Enter news description" rows="4" 
            value={description} onChange={(e) => setDescription(e.target.value)}>
          </textarea>
        </div>

        {/* Source URL Input */}
        <div className="mb-4">
          <label className="block mb-1">Source URL</label>
          <input type="text" className="w-full p-2 rounded bg-black bg-opacity-30 focus:outline-none" 
            placeholder="Enter source URL (future feature)" 
            value={sourceUrl} onChange={(e) => setSourceUrl(e.target.value)} />
        </div>

        {/* Verify Button */}
        <button onClick={handleVerify} className="w-full bg-purple-600 hover:bg-purple-700 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg">
          {loading ? "Verifying..." : "Verify News"}
        </button>

        {/* Display Verification Result */}
        {verification && (
          <div className="mt-4 p-4 bg-gray-800 rounded">
            <h3 className="text-xl font-semibold">Verification Result:</h3>
            <p>{verification}</p>
          </div>
        )}
      </main>
    </div>
  );
};

export default FakeNewsDetector;
