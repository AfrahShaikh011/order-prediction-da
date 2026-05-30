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

function Predictions() {

  const forecastData = [

    { day: "Day 1", forecast: 180 },

    { day: "Day 2", forecast: 190 },

    { day: "Day 3", forecast: 210 },

    { day: "Day 4", forecast: 205 },

    { day: "Day 5", forecast: 220 },

    { day: "Day 6", forecast: 240 },

    { day: "Day 7", forecast: 230 }
  ];

  return (

    <div className="p-10 text-white">

      {/* HEADER */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold">
          ML Predictions
        </h1>

        <p className="text-slate-400 mt-3 text-lg">
          AI Forecasting & Prediction Insights
        </p>

      </div>

      {/* MODEL INFO */}

      <div className="grid md:grid-cols-3 gap-6 mb-10">

        <div className="bg-slate-900 p-6 rounded-2xl">

          <p className="text-slate-400">
            Active Model
          </p>

          <h2 className="text-4xl font-bold text-cyan-400 mt-4">
            XGBoost
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl">

          <p className="text-slate-400">
            Prediction Accuracy
          </p>

          <h2 className="text-4xl font-bold text-green-400 mt-4">
            66.1%
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl">

          <p className="text-slate-400">
            Forecast Horizon
          </p>

          <h2 className="text-4xl font-bold text-orange-400 mt-4">
            7 Days
          </h2>

        </div>

      </div>

      {/* FORECAST CHART */}

      <div className="bg-slate-900 p-8 rounded-2xl">

        <h2 className="text-3xl font-bold mb-8">
          Future Forecast Trend
        </h2>

        <ResponsiveContainer
          width="100%"
          height={450}
        >

          <LineChart data={forecastData}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="day" />

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

export default Predictions;