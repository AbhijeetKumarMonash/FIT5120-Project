<template>
  <div class="trends-container">
    <h1 font="bold">UV Index Trends in Australia</h1>

    <!-- Display the graph -->
    <img v-if="graphUrl" :src="graphUrl" alt="UV Index Heatmap" class="graph-frame" />
    <p v-else>Loading...</p>

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

const graphUrl = ref('')

const fetchGraph = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/uv_index_trends')
    const data = await response.json()
    if (data.status === 'success') {
      graphUrl.value = data.graph_url
    }
  } catch (error) {
    console.error('Error fetching UV Index graph:', error)
  }
}

onMounted(fetchGraph)
</script>

<style scoped>
.trends-container {
  text-align: center;
  max-width: 1600px;
  margin: 20px auto;
  padding: 20px;
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
  color: #ff6600;
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
