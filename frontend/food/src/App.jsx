import { Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";
import Dashboard from "./pages/Dashboard";
import SignupPage from "./pages/signup";

function App() {
  return (
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/signup" element={<SignupPage/>}/>
      </Routes>
  );
}

export default App;
