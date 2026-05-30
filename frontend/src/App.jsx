import { useState } from "react";

import {
  BrowserRouter,
  Routes,
  Route,
  NavLink
} from "react-router-dom";

import {
  FaChartLine,
  FaDatabase,
  FaRobot,
  FaBars,
  FaMoon,
  FaSun
} from "react-icons/fa";

import { Toaster } from "react-hot-toast";

import Dashboard from "./pages/Dashboard";
import Analytics from "./pages/Analytics";
import Predictions from "./pages/Predictions";

function App() {

  const [sidebarOpen, setSidebarOpen] = useState(true);

  const [darkMode, setDarkMode] = useState(true);

  return (

    <BrowserRouter>

      <Toaster />

      <div
        className={`min-h-screen flex ${
          darkMode
            ? "bg-slate-950 text-white"
            : "bg-slate-100 text-black"
        }`}
      >

        {/* SIDEBAR */}

        <div
          className={`${
            sidebarOpen ? "w-72" : "w-24"
          } ${
            darkMode
              ? "bg-slate-900 border-slate-800"
              : "bg-white border-slate-300"
          } p-8 border-r transition-all duration-300`}
        >

          <h1 className="text-3xl font-bold mb-6">
            Forecast AI
          </h1>

          {/* TOGGLE SIDEBAR */}

          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="mb-6"
          >

            <FaBars size={24} />

          </button>

          {/* THEME BUTTON */}

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="mb-10 flex items-center gap-3 bg-green-500 px-4 py-2 rounded-xl text-white"
          >

            {darkMode
              ? <FaSun />
              : <FaMoon />}

            {sidebarOpen && (
              darkMode
                ? "Light"
                : "Dark"
            )}

          </button>

          {/* NAVIGATION */}

          <div className="space-y-8">

            <NavLink
              to="/"
              className={({ isActive }) =>
                `flex items-center gap-4 transition ${
                  isActive
                    ? "text-green-400"
                    : "hover:text-green-400"
                }`
              }
            >

              <FaChartLine />

              {sidebarOpen && (
                <span>Dashboard</span>
              )}

            </NavLink>

            <NavLink
              to="/analytics"
              className={({ isActive }) =>
                `flex items-center gap-4 transition ${
                  isActive
                    ? "text-green-400"
                    : "hover:text-green-400"
                }`
              }
            >

              <FaDatabase />

              {sidebarOpen && (
                <span>Analytics</span>
              )}

            </NavLink>

            <NavLink
              to="/predictions"
              className={({ isActive }) =>
                `flex items-center gap-4 transition ${
                  isActive
                    ? "text-green-400"
                    : "hover:text-green-400"
                }`
              }
            >

              <FaRobot />

              {sidebarOpen && (
                <span>ML Predictions</span>
              )}

            </NavLink>

          </div>

        </div>

        {/* PAGE CONTENT */}

        <div className="flex-1">

          <Routes>

            <Route
              path="/"
              element={<Dashboard />}
            />

            <Route
              path="/analytics"
              element={<Analytics />}
            />

            <Route
              path="/predictions"
              element={<Predictions />}
            />

          </Routes>

        </div>

      </div>

    </BrowserRouter>
  );
}

export default App;