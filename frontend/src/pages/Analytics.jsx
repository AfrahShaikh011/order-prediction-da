import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  PieChart,
  Pie,
  Cell,
  Legend
} from "recharts";

function Analytics() {

  const monthlyData = [

    { month: "Jan", sales: 3200 },

    { month: "Feb", sales: 2800 },

    { month: "Mar", sales: 3900 },

    { month: "Apr", sales: 4200 },

    { month: "May", sales: 5100 },

    { month: "Jun", sales: 4800 }
  ];

  const pieData = [

    { name: "Online", value: 65 },

    { name: "Retail", value: 20 },

    { name: "Wholesale", value: 15 }
  ];

  const COLORS = [
    "#22c55e",
    "#3b82f6",
    "#f97316"
  ];

  return (

    <div className="p-10 text-white">

      {/* HEADER */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold">
          Analytics Dashboard
        </h1>

        <p className="text-slate-400 mt-3 text-lg">
          Sales Insights & Business Analytics
        </p>

      </div>

      {/* KPI SECTION */}

      <div className="grid md:grid-cols-3 gap-6 mb-10">

        <div className="bg-slate-900 p-6 rounded-2xl">

          <p className="text-slate-400">
            Total Revenue
          </p>

          <h2 className="text-4xl font-bold text-green-400 mt-4">
            $24.8K
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl">

          <p className="text-slate-400">
            Growth Rate
          </p>

          <h2 className="text-4xl font-bold text-cyan-400 mt-4">
            +18%
          </h2>

        </div>

        <div className="bg-slate-900 p-6 rounded-2xl">

          <p className="text-slate-400">
            Avg Daily Sales
          </p>

          <h2 className="text-4xl font-bold text-orange-400 mt-4">
            179
          </h2>

        </div>

      </div>

      {/* CHARTS */}

      <div className="grid lg:grid-cols-2 gap-10">

        {/* BAR CHART */}

        <div className="bg-slate-900 p-8 rounded-2xl">

          <h2 className="text-3xl font-bold mb-8">
            Monthly Sales
          </h2>

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <BarChart data={monthlyData}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="sales"
                fill="#22c55e"
                radius={[10, 10, 0, 0]}
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

        {/* PIE CHART */}

        <div className="bg-slate-900 p-8 rounded-2xl">

          <h2 className="text-3xl font-bold mb-8">
            Sales Distribution
          </h2>

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <PieChart>

              <Pie
                data={pieData}
                dataKey="value"
                nameKey="name"
                outerRadius={120}
                label
              >

                {pieData.map((entry, index) => (

                  <Cell
                    key={index}
                    fill={COLORS[index % COLORS.length]}
                  />

                ))}

              </Pie>

              <Tooltip />

              <Legend />

            </PieChart>

          </ResponsiveContainer>

        </div>

      </div>

    </div>
  );
}

export default Analytics;