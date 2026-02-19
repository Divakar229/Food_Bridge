import { FaMapMarkerAlt } from "react-icons/fa";

function SignupPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#FF5C00] via-[#FFA45B] to-[#7ED957] flex justify-center items-center p-4">
      
      <div className="w-[360px] bg-white p-7 rounded-3xl shadow-xl flex flex-col items-center text-center">

        {/* Logo */}
        <div className="flex items-center gap-3 mb-6">
          <div className="bg-orange-500 p-2 rounded-lg flex items-center justify-center">
            <FaMapMarkerAlt className="text-white text-sm" />
          </div>
          <div className="text-2xl font-bold text-orange-500">
            <span className="text-black">Food</span>Bridge
          </div>
        </div>

        {/* Heading */}
        <h2 className="text-xl font-semibold text-gray-800 mb-1">Create Account</h2>
        <p className="text-gray-500 text-sm mb-6">Join us to bridge food & kindness!</p>

        {/* Input Fields */}
        <input
          placeholder="Full Name"
          className="w-full border border-gray-300 p-3 rounded-lg mb-3 focus:border-orange-500 outline-none"
        />

        <input
          placeholder="Email Address"
          className="w-full border border-gray-300 p-3 rounded-lg mb-3 focus:border-orange-500 outline-none"
        />
        
        <input
          placeholder="Password"
          type="password"
          className="w-full border border-gray-300 p-3 rounded-lg mb-5 focus:border-orange-500 outline-none"
        />

        {/* Button */}
        <button className="w-full bg-orange-500 text-white p-3 rounded-lg font-semibold hover:bg-orange-600 transition">
          Sign Up
        </button>

        {/* Bottom small link */}
        <p className="text-sm text-gray-600 mt-4">
          Already have an account?{" "}
          <span className="text-orange-500 font-medium hover:underline cursor-pointer">
            Login
          </span>
        </p>

      </div>
    </div>
  );
}

export default SignupPage;
