import { useEffect, useState } from "react";

import axios from "axios";

import toast from "react-hot-toast";

import { ClipLoader } from "react-spinners";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Legend
} from "recharts";

function Dashboard() {

  const [data, setData] = useState(null);

  useEffect(() => {

    fetchPrediction();

  }, []);

  const fetchPrediction = async () => {

    try {

      const response = await axios.get(
        "http://localhost:5000/predict"
      );

      console.log(response.data);

      setData(response.data);

      toast.success("Forecast data loaded!");

    } catch (error) {

      console.log(error);

      toast.error("Failed to load forecast!");

    }

  };

  if (!data) {

    return (

      <div className="flex justify-center items-center h-screen bg-slate-950">

        <ClipLoader
          color="#22c55e"
          size={80}
        />

      </div>
    );
  }

  return (

    <div className="p-10">

      {/* HEADER */}

      <div className="flex justify-between items-center mb-10">

        <div>

          <h1 className="text-5xl font-bold">
            Order Prediction Dashboard
          </h1>

          <p className="text-slate-400 mt-3 text-lg">
            AI Powered Sales Forecasting
          </p>

        </div>

        {/* DOWNLOAD BUTTON */}

        <a
          href="http://localhost:5000/download-forecast"
          className="bg-green-500 px-6 py-3 rounded-xl font-bold hover:bg-green-600 transition"
        >

          Download Forecast CSV

        </a>

      </div>

      {/* KPI CARDS */}

      <div className="grid md:grid-cols-4 gap-6 mb-10">

        <div className="bg-slate-900 p-6 rounded-2xl hover:scale-105 transition duration-300">

          <p className="text-slate-400">
            Predicted Sales
          </p>

          <h2 className="text-4xl font-bold text-green-400 mt-4">
            {data.predicted_sales}
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl hover:scale-105 transition duration-300">

          <p className="text-slate-400">
            Model
          </p>

          <h2 className="text-3xl font-bold text-cyan-400 mt-4">
            {data.model}
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl hover:scale-105 transition duration-300">

          <p className="text-slate-400">
            RMSE
          </p>

          <h2 className="text-4xl font-bold text-orange-400 mt-4">
            {data.rmse}
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl hover:scale-105 transition duration-300">

          <p className="text-slate-400">
            R² Score
          </p>

          <h2 className="text-4xl font-bold text-purple-400 mt-4">
            {data.r2_score}
          </h2>

        </div>

      </div>

      {/* ACTUAL VS PREDICTED */}

      <div className="bg-slate-900 p-8 rounded-2xl mb-10">

        <h2 className="text-3xl font-bold mb-8">
          Actual vs Predicted Sales
        </h2>

        <ResponsiveContainer width="100%" height={400}>

          <LineChart data={data.chart_data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="date" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Line
              type="monotone"
              dataKey="sales"
              stroke="#22c55e"
              strokeWidth={3}
              name="Actual Sales"
            />

            <Line
              type="monotone"
              dataKey="predicted_sales"
              stroke="#3b82f6"
              strokeWidth={3}
              name="Predicted Sales"
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

      {/* FUTURE FORECAST */}

      <div className="bg-slate-900 p-8 rounded-2xl">

        <h2 className="text-3xl font-bold mb-8">
          7-Day Future Forecast
        </h2>

        <ResponsiveContainer width="100%" height={400}>

          <LineChart data={data.future_forecast}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="date" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Line
              type="monotone"
              dataKey="forecast"
              stroke="#f97316"
              strokeWidth={4}
              name="Forecasted Sales"
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}

export default Dashboard;