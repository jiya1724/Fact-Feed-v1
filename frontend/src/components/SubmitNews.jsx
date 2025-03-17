import React, { useState } from 'react';
import Navbar from './Navbar';

const SubmitNews = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [sourceUrl, setSourceUrl] = useState('');

  const handleVerify = () => alert('Verifying news...');
  const handleSubmit = () => alert('News submitted successfully!');

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white">
      <Navbar />
      <main className="pt-40 w-full max-w-lg mx-auto px-4 bg-white bg-opacity-10 p-8 rounded-xl shadow-lg">
        <h2 className="text-3xl font-bold mb-4 text-center">Submit News</h2>
        <p className="text-center mb-6 text-gray-300">Share verified news with the community</p>

        <div className="mb-4">
          <label className="block mb-1">Title</label>
          <input type="text" className="w-full p-2 rounded bg-black bg-opacity-30 focus:outline-none" placeholder="Enter news title" value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>

        <div className="mb-4">
          <label className="block mb-1">Description</label>
          <textarea className="w-full p-2 rounded bg-black bg-opacity-30 focus:outline-none" placeholder="Enter news description" rows="4" value={description} onChange={(e) => setDescription(e.target.value)}></textarea>
        </div>

        <div className="mb-4">
          <label className="block mb-1">Source URL</label>
          <input type="text" className="w-full p-2 rounded bg-black bg-opacity-30 focus:outline-none" placeholder="https://example.com/news" value={sourceUrl} onChange={(e) => setSourceUrl(e.target.value)} />
        </div>

        <div className="flex justify-between space-x-4">
          <button onClick={handleVerify} className="flex-1 bg-purple-600 hover:bg-purple-700 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg">
            Verify News
          </button>
          <button onClick={handleSubmit} className="flex-1 bg-green-600 hover:bg-green-700 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg">
            Submit News
          </button>
        </div>
      </main>
    </div>
  );
};

export default SubmitNews;
