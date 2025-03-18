import Navbar from './Navbar';
import { Link, useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate(); // Hook for navigation

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white">
      <Navbar />
      <div className="pt-40 max-w-4xl mx-auto px-4 space-y-8">
        <div className="bg-white bg-opacity-10 p-6 rounded-lg shadow-md text-center">
          <h2 className="text-3xl font-bold mb-4">Welcome to FactFeed AI</h2>
          <p className="text-gray-300">
            Your hub for verifying and sharing authentic news with the community. Stay informed. Stay smart.
          </p>

          {/* Single Submit News Button */}
          <div className="mt-6">
            <Link to="/submit">
              <button className="bg-purple-600 hover:bg-purple-700 px-5 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg">
                Submit News
              </button>
            </Link>
          </div>
        </div>

        <div>
          <p className='text-yellow-400 p-4 text-center'>
            This homepage is temporary and will later be used to display news aggregator feature. HOLD ON!
          </p>
        </div>

        {/* Features Section with Clickable Boxes */}
        <div className="grid gap-6 md:grid-cols-3">
          <div 
            className="bg-white bg-opacity-10 p-4 rounded-lg text-center hover:scale-105 transition transform hover:shadow-xl cursor-pointer"
            onClick={() => navigate('/detect')}
          >
            <h3 className="text-xl font-semibold mb-2">AI-Powered Verification</h3>
            <p className="text-gray-300">Detect fake news with our cutting-edge machine learning model.</p>
          </div>

          <div 
            className="bg-white bg-opacity-10 p-4 rounded-lg text-center hover:scale-105 transition transform hover:shadow-xl cursor-pointer"
            onClick={() => navigate('/summarizer')}
          >
            <h3 className="text-xl font-semibold mb-2">Summarized Insights</h3>
            <p className="text-gray-300">Get concise summaries for quick understanding and sharing.</p>
          </div>

          <div className="bg-white bg-opacity-10 p-4 rounded-lg text-center hover:scale-105 transition transform hover:shadow-xl">
            <h3 className="text-xl font-semibold mb-2">Community Driven</h3>
            <p className="text-gray-300">Share verified news to keep everyone informed and safe.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
