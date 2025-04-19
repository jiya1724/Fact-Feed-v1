import React from "react";
import { Route, Routes } from "react-router-dom"; // Remove BrowserRouter import
import Aggregator from "./components/Aggregator";
import Home from "./components/Home";
import Detector from "./components/Detector";
import Summarizer from "./components/Summarize";
import "./index.css";
import Login from "./components/Login";
import SignUp from "./components/Signup";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/aggregator" element={<Aggregator />} />
      <Route path="/detector" element={<Detector />} />
      <Route path="/summarizer" element={<Summarizer />} />
      <Route path="/login" element={<Login/>} />
      <Route path="*" element={<Home />} />
      <Route path="/signup" element={<SignUp/>} />
    </Routes>
  );
}

export default App;
