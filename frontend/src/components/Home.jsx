import Navbar from './Navbar';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white">
      <Navbar />
      <div className="pt-40 max-w-4xl mx-auto px-4 space-y-8">
        <div className="bg-white bg-opacity-10 p-6 rounded-lg shadow-md text-center">
          <h2 className="text-3xl font-bold mb-4">Welcome to FactFeed AI</h2>
          <p className="text-gray-300">
            Your hub for verifying and sharing authentic news with the community. Stay informed. Stay smart.
          </p>
          <div className="mt-6">
            <Link to="/submit">
              <button className="bg-purple-600 hover:bg-purple-700 px-5 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg">
                Submit News
              </button>
            </Link>
          </div>
        </div>
        <div>
          <p className='text-yellow-400 p-4 text-center'>This homepage is temporary and  will later be used to display news aggregator feature...Hold my beer till final Eval!</p>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          {["AI-Powered Verification", "Summarized Insights", "Community Driven"].map((title, index) => (
            <div key={index} className="bg-white bg-opacity-10 p-4 rounded-lg text-center hover:scale-105 transition transform hover:shadow-xl">
              <h3 className="text-xl font-semibold mb-2">{title}</h3>
              <p className="text-gray-300">
                {index === 0 && "Detect fake news with our cutting-edge machine learning model."}
                {index === 1 && "Get concise summaries for quick understanding and sharing."}
                {index === 2 && "Share verified news to keep everyone informed and safe."}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Home;
