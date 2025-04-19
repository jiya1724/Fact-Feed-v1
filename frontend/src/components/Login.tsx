import { Link, useNavigate } from 'react-router-dom';
import { FcGoogle } from 'react-icons/fc';

function Login() {
  const navigate = useNavigate();

  const handleGoogleLogin = () => {
    // Implement your Google authentication logic here
    console.log('Signing in with Google...');
    // After successful authentication, you can navigate to home
    // navigate('/');
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-900 via-black to-blue-900 text-white flex flex-col justify-center">
      <div className="max-w-md mx-auto px-4 py-8 w-full">
        <div className="bg-white bg-opacity-10 p-8 rounded-lg shadow-lg">
          <h2 className="text-3xl font-bold mb-6 text-center">Welcome Back</h2>
          
          {/* Email/Password Form */}
          <form className="space-y-6">
            <div>
              <label htmlFor="email" className="block text-sm font-medium mb-1">
                Email
              </label>
              <input
                id="email"
                name="email"
                type="email"
                required
                className="w-full bg-white bg-opacity-20 rounded-lg px-4 py-2 border border-white border-opacity-30 focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="your@email.com"
              />
            </div>
            
            <div>
              <label htmlFor="password" className="block text-sm font-medium mb-1">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="w-full bg-white bg-opacity-20 rounded-lg px-4 py-2 border border-white border-opacity-30 focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="••••••••"
              />
            </div>
            
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <input
                  id="remember-me"
                  name="remember-me"
                  type="checkbox"
                  className="h-4 w-4 rounded bg-white bg-opacity-20 border-white border-opacity-30 focus:ring-purple-500"
                />
                <label htmlFor="remember-me" className="ml-2 block text-sm">
                  Remember me
                </label>
              </div>
              
              <div className="text-sm">
                <a href="#" className="text-purple-300 hover:text-purple-200">
                  Forgot password?
                </a>
              </div>
            </div>
            
            <button
              type="submit"
              className="w-full bg-purple-600 hover:bg-purple-700 py-2 px-4 rounded-lg transition transform hover:scale-105 hover:shadow-lg"
            >
              Sign in
            </button>
          </form>
          
          {/* Divider */}
          <div className="relative my-6">
        
            <div className="relative flex justify-center text-sm">
              <span className=" px-2 text-gray-300 font-semibold">
                Or continue with
              </span>
            </div>
          </div>
          
          
          <button
            onClick={handleGoogleLogin}
            className="w-full bg-white bg-opacity-10 hover:bg-opacity-20 text-white py-2 px-4 rounded-lg flex items-center justify-center space-x-2 transition transform hover:scale-105 hover:shadow-lg"
          >
            <FcGoogle className="text-xl" />
            <span>Sign in with Google</span>
          </button>
          
          
          <div className="mt-6 text-center text-sm">
            <span className="text-gray-300">Don't have an account? </span>
            <Link to="/signup" className="text-purple-300 hover:text-purple-200 font-medium">
              Sign up
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;