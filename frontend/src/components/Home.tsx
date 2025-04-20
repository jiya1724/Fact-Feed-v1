import Navbar from './Navbar';
import { Link, useNavigate } from 'react-router-dom';

interface FeatureCardProps {
  title: string;
  description: string;
  onClick: () => void;
}



function FeatureCard({ title, description, onClick }:FeatureCardProps) {
  return (
    <div 
      className="bg-white bg-opacity-10 p-4 rounded-lg text-center hover:scale-105 transition transform hover:shadow-xl cursor-pointer"
      onClick={onClick}
    >
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p className="text-gray-300">{description}</p>
    </div>
  );
}

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

          {/* Buttons Section */}
          <div className="mt-6 flex justify-center space-x-4">
            <Link to="/detector">
              <button 
                aria-label="Verify News"
                className="bg-purple-600 hover:bg-purple-700 px-5 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg"
              >
                Verify News
              </button>
            </Link>

            <Link to="/summarizer">
              <button 
                aria-label="Summarize News"
                className="bg-green-600 hover:bg-green-700 px-5 py-2 rounded-xl transition transform hover:scale-105 hover:shadow-lg"
              >
                Summarize
              </button>
            </Link>
          </div>
        </div>

        {/* Features Section */}
        <section className="grid gap-6 md:grid-cols-3">
          <FeatureCard 
            title="AI-Powered Verification" 
            description="Detect fake news with our cutting-edge machine learning model."
            onClick={() => navigate('/detector')}
          />
          <FeatureCard 
            title="Summarized Insights" 
            description="Get concise summaries for quick understanding and sharing."
            onClick={() => navigate('/summarizer')}
          />
          <FeatureCard 
            title="News Aggregator" 
            description="Stay updated with verified news from multiple sources!"
            onClick={() => navigate('/aggregator')}
          />
        </section>
      </div>
    </div>
  );
}

export default Home;
