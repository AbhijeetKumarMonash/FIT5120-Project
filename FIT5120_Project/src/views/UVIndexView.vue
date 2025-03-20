<template>
  <div class="trends-container">
    <h1 font="bold">UV Index Trends in Australia</h1>

    <!-- Display the graph -->
    <!-- <img v-if="graphUrl" :src="graphUrl" alt="UV Index Heatmap" class="graph-frame" />
    <p v-else>Loading...</p> -->

    <div id="chart">
      <div v-if="loading">Loading...</div>
      <apexchart
        v-else
        type="heatmap"
        height="350"
        :options="chartOptions"
        :series="series"
      ></apexchart>
    </div>

    <!-- Data Explanation Section -->
    <div class="graph-explanation">
      <h2>Understanding the UV Index Heatmap</h2>
      <p>
        This heatmap presents the <strong>average monthly UV index</strong> for different Australian
        states and territories from <strong>2018-2020</strong>. Higher UV index values indicate
        stronger ultraviolet radiation, which increases the risk of <strong>skin cancer</strong>.
      </p>

      <h3>🔍 Key Insights:</h3>
      <ul>
        <li>
          🌞 <strong>Queensland (QLD) and Western Australia (WA)</strong> experience consistently
          high UV levels throughout the year.
        </li>
        <li>
          ❄️ <strong>Winter months (June-August)</strong> exhibit lower UV levels, but sun
          protection remains crucial.
        </li>
        <li>
          ☀️ <strong>Summer (December-February)</strong> sees a significant rise in UV exposure,
          requiring extra sun safety precautions.
        </li>
      </ul>

      <h3>☀️ UV Protection Measures</h3>
      <p>
        To mitigate UV exposure risks and reduce the likelihood of skin damage, follow these tips:
      </p>
      <ul>
        <li>🧴 <strong>Apply SPF 50+ sunscreen</strong> every 2 hours.</li>
        <li>🕶️ <strong>Wear UV-protective sunglasses and hats.</strong></li>
        <li>🌳 <strong>Seek shade</strong> between 10 AM - 4 PM.</li>
        <li>
          👕 <strong>Use protective clothing</strong> like long sleeves and UV-resistant fabrics.
        </li>
        <li>📅 <strong>Monitor UV index reports</strong> before planning outdoor activities.</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// const graphUrl = ref('')

// const fetchGraph = async () => {
//   try {
//     const response = await fetch('https://fit5120-project-1.onrender.com/api/uv_index_trends')
//     const data = await response.json()
//     if (data.status === 'success') {
//       graphUrl.value = data.graph_url
//     }
//   } catch (error) {
//     console.error('Error fetching UV Index graph:', error)
//   }
// }

// onMounted(fetchGraph)

const loading = ref(true);
const series = ref([]);
// const chartOptions = ref({
//   chart: {
//     height: 350,
//     type: 'heatmap',
//   },
//   stroke: {
//     width: 0
//   },
//   plotOptions: {
//     heatmap: {
//       radius: 0,
//       enableShades: false, 
//       colorScale: {
//         ranges: [
//           { from: 0, to: 0.5, color: "#f7fcf0" },
//           { from: 0.5, to: 1, color: "#e0f3db" },
//           { from: 1, to: 1.5, color: "#ccebc5" },
//           { from: 1.5, to: 2, color: "#a8ddb5" },
//           { from: 2, to: 2.5, color: "#7bccc4" },
//           { from: 2.5, to: 3, color: "#4eb3d3" },
//           { from: 3, to: 3.5, color: "#2b8cbe" },
//           { from: 3.5, to: 4, color: "#08589e" }
//         ]
//       }
//     }
//   },
//   dataLabels: {
//     enabled: true,
//     style: {
//       colors: ['#000'] // text color
//   },
//   xaxis: {
//     type: 'category',
//     categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
//   },
//   title: {
//     text: "Average Monthly UV Index (2018-2020) - Australian States & Territories"
//   }
//   }});

// **get uv index**

const chartOptions = ref({
  chart: {
    height: 350,
    type: "heatmap",
  },
  plotOptions: {
    heatmap: {
      enableShades: false, // Disable gradient shading
      colorScale: {
        ranges: [
          { from: 0, to: 0.5, color: "#f5e695" },  // Bright yellow
          { from: 0.5, to: 1, color: "#FEC44F" },  // Yellow-orange
          { from: 1, to: 1.5, color: "#FE9929" },  // Light orange
          { from: 1.5, to: 2, color: "#EC7014" },  // Dark orange
          { from: 2, to: 2.5, color: "#CC4C02" },  // Reddish-brown
          { from: 2.5, to: 3, color: "#8C2D04" }   // Dark brown
        ],
      },
    },
  },
  dataLabels: {
    enabled: true,
    style: {
      colors: ["#fff"], // White text on colored background
    },
  },
  xaxis: {
    categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
  },
  title: {
    text: "Average Monthly UV Index (2018-2020) - Australian States & Territories",
  },
});



const fetchData = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5001/api/uv_index");
    const result = await response.json();

    console.log("API Response Data:", result);

    if (!Array.isArray(result.data)) {
      throw new Error("API data is not an array");
    }

    // Group data by location
    const groupedData = result.data.reduce((acc, item) => {
      if (!acc[item.location]) {
        acc[item.location] = new Array(12).fill(null);
      }
      acc[item.location][item.month - 1] = parseFloat(item.uv_index.toFixed(2)); // Keep two decimal places
      return acc;
    }, {});

    // Convert data to ApexCharts format
    series.value = Object.entries(groupedData).map(([location, uv_values]) => ({
      name: location,
      data: uv_values.map((uv, index) => ({
        x: chartOptions.value.xaxis.categories[index], // Month name
        y: uv || 0 // Ensure there's a value
      }))
    }));

    loading.value = false;

  } catch (error) {
    console.error("Error fetching UV Index data:", error);
  }
};


onMounted(fetchData);
</script>

<style scoped>
.trends-container {
  text-align: center;
  max-width: 1600px;
  margin: 20px auto;
  padding: 20px;
  padding-top: 70px;
}

/* Graph Display */
.graph-frame {
  width: 100%;
  height: 600px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  margin-bottom: 20px;
  border: 2px solid #ddd;
}

/* Explanation Section */
.graph-explanation {
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.graph-explanation h2 {
  color: #fa831b;
  font-size: 1.8rem;
  margin-bottom: 10px;
}

.graph-explanation h3 {
  color: #0275d8;
  font-size: 1.5rem;
  margin-top: 15px;
}

.graph-explanation p {
  font-size: 1.2rem;
  line-height: 1.6;
}

.graph-explanation ul {
  list-style-type: none;
  padding: 0;
}

.graph-explanation ul li {
  font-size: 1.1rem;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
}

.graph-explanation ul li::before {
  content: '✔️';
  margin-right: 8px;
}
</style>
