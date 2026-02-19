import { FaMapMarkerAlt } from "react-icons/fa";

function LoginPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#FF5C00] via-[#FFA45B] to-[#7ED957] flex justify-center items-center">
      
      <div className="w-[350px] bg-white p-6 rounded-2xl shadow-lg flex flex-col items-center text-center">

        
        <div className="flex items-center gap-3 mb-6">
          <div className="bg-orange-500 p-2 rounded-lg flex items-center justify-center">
            <FaMapMarkerAlt className="text-white text-sm" />
          </div>

          <div className="text-2xl font-bold text-orange-500">
            <span className="text-black">Food</span>Bridge
          </div>
        </div>
       <div className="flex flex-col items-center text-center mb-8 space-y-2">
  
  <span className="text-xs uppercase tracking-[0.2em] text-gray-400 font-semibold">
    Thank you for serving
  </span>
  <h1 className="text-xl font-bold text-gray-800 tracking-wide">
    Nourish &bull; Connect &bull; Serve
  </h1>
</div>
        
        <input 
          placeholder="Username"
          className="w-full border border-gray-300 p-2 rounded-lg mb-3"
        />

        <input 
          placeholder="Password"
          type="password"
          className="w-full border border-gray-300 p-2 rounded-lg mb-3"
        />

        <button className="w-full bg-orange-500 text-white p-2 rounded-lg font-semibold">
          Login
        </button>

<span className="relative group cursor-pointer text-gray-700 hover:text-orange-500 transition mt-3">
  Signup?
  <span className="absolute left-0 bottom-0 w-0 h-[2px] bg-green-500 transition-all duration-300 group-hover:w-full"></span>
</span>
      </div>

    </div>
  );
}

export default LoginPage;
