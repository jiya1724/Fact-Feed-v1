import { Link } from 'react-router-dom';
import Navbar from './Navbar';

export default function Logout() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white flex flex-col items-center">
      <Navbar />
      <main className="pt-40 w-full max-w-lg bg-white bg-opacity-10 p-8 rounded-xl shadow-lg text-center">
        <h2 className="text-3xl font-bold mb-4">You're Logged Out</h2>
        <p className="mb-6">We hope to see you again soon!</p>
        <Link to="/" className="bg-purple-600 hover:bg-purple-700 px-6 py-2 rounded-xl inline-block">
          Go Back Home
        </Link>
      </main>
    </div>
  );
}
