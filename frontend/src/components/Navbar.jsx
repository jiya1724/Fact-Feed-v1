import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="w-full flex justify-between items-center p-6 bg-black bg-opacity-30 backdrop-blur-md fixed top-0 left-0 z-50">
      <h1 className="text-2xl font-bold">FactFeed AI</h1>
      <div className="md:hidden" onClick={() => setIsOpen(!isOpen)}>
        <button className="focus:outline-none">
          <span className="text-white text-3xl">&#9776;</span>
        </button>
      </div>
      <nav className={`flex-col md:flex-row md:flex space-y-4 md:space-y-0 md:space-x-6 absolute md:static top-20 right-6 bg-black bg-opacity-90 md:bg-transparent p-4 md:p-0 rounded-lg md:rounded-none ${isOpen ? 'flex' : 'hidden'}`}>
        <Link to="/" className="hover:text-purple-400">Home</Link>
        <Link to="/submit" className="hover:text-purple-400">Submit News</Link>
        <Link to="/logout" className="hover:text-red-400">Logout</Link>
      </nav>
    </header>
  );
};

export default Navbar;
