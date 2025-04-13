import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import SubmitNews from './components/SubmitNews';
import FakeNewsDetector from './components/Detector'; // New component
import Summarizer from './components/Summarize'; // New component
import Aggregator from './components/Aggregator';
import Navbar from './components/Navbar';
import Logout from './components/Logout';

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/submit" element={<SubmitNews />} /> */}
        <Route path="/logout" element={<Logout />} />
        <Route path="/detect" element={<FakeNewsDetector />} /> {/* Fake News Detector */}
        <Route path="/summarizer" element={<Summarizer />} /> {/* Summarizer */}
        <Route path="/aggregator" element={<Aggregator />} />
        <Route path="/SubmitNews" element={<SubmitNews/>} />
        <Route path="*" element={<div>404 Not Found</div>} />
      </Routes>
    </>
  );
}

export default App;
