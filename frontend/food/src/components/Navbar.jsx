import { FaMapMarkerAlt } from "react-icons/fa";

const Navbar = () => {
  return (
    <nav className="fixed top-0 w-full z-50 
  bg-white/80 backdrop-blur-xl backdrop-saturate-150 
  border-b border-white/10 shadow-lg">
  {/* Content */}
      <div className="max-w-7xl mx-auto px-4 md:px-6 py-4 flex items-center justify-between">

        {/* LEFT: Logo Section */}
        <div className="flex items-center gap-3">
          <div className="bg-orange-500 p-2 rounded-lg flex items-center justify-center">
            <FaMapMarkerAlt className="text-white text-sm" />
          </div>

          <div className="text-2xl font-bold text-orange-500">
            <span className="text-black">Food</span>Bridge
          </div>
        </div>

        {/* CENTER: Navigation Links */}
        <ul className="hidden md:flex space-x-8 text-gray-700 font-medium">
          <li className="hover:text-orange-500 cursor-pointer transition">
            How It Works
          </li>
          <li className="hover:text-orange-500 cursor-pointer transition">
            Live Map
          </li>
          <li className="hover:text-orange-500 cursor-pointer transition">
            Leaderboard
          </li>
          <li className="hover:text-orange-500 cursor-pointer transition">
            About
          </li>
        </ul>

        {/* RIGHT: Buttons */}
        <div className="flex items-center space-x-4">
          <button className="text-black hover:text-orange-500 font-medium transition">
            Sign In
          </button>

          <button className="bg-orange-500 text-white px-5 py-2 rounded-xl font-semibold hover:bg-orange-600 transition duration-300">
            Get Started
          </button>
        </div>

      </div>
    </nav>
  );
};

export default Navbar;
