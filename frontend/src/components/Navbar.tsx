import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="w-full flex justify-between items-center p-6 bg-black bg-opacity-30 backdrop-blur-md fixed top-0 left-0 z-50">
      <h1 className="text-2xl font-bold text-white">FactFeed AI</h1>

      {/* Mobile Menu Toggle Button */}
      <div className="md:hidden" onClick={() => setIsOpen(!isOpen)}>
        <button className="focus:outline-none">
          <span className="text-white text-3xl">&#9776;</span>
        </button>
      </div>

      {/* Navigation Links */}
      <nav className={`md:flex md:flex-row space-y-4 md:space-y-0 md:space-x-6 
          absolute md:static top-20 right-6 bg-black bg-opacity-90 md:bg-transparent 
          p-4 md:p-0 rounded-lg md:rounded-none ${isOpen ? 'flex flex-col' : 'hidden md:flex'}`}>

        <Link to="/" className="hover:text-purple-400 text-white">Home</Link>
        <Link to="/submit" className="hover:text-blue-400 text-white">Verify News</Link>
        <Link to="/detect" className="hover:text-red-400 text-white">Fake News Detector</Link>
        <Link to="/summarizer" className="hover:text-green-400 text-white">Summarizer</Link>
        <Link to="/logout" className="hover:text-yellow-400 text-white">Logout</Link>
      </nav>
    </header>
  );
};

export default Navbar;
