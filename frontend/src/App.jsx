import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import SubmitNews from './components/SubmitNews'; 
import Navbar from './components/Navbar';
import Logout from './components/Logout';

function App() {
  return (
    <>
      <Navbar /> {}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/submit" element={<SubmitNews />} />
        <Route path="/logout" element={<Logout/>}/>
      </Routes>
    </>
  );
}

export default App;
