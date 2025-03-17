<template>
  <div class="trends-container">
    <h1 font="bold">Skin Cancer Trends in Australia</h1>

    <!-- Display the graph -->
    <iframe :src="graphUrl" class="graph-frame" frameborder="0"></iframe>

    <!-- Data Explanation Section -->
    <div class="graph-explanation">
      <h2>Understanding the Trends</h2>
      <p>
        This graph illustrates the increasing trend of
        <strong>skin cancer cases across Australian states and territories</strong>. The data
        highlights a steady rise in reported melanoma cases over the years, emphasizing the critical
        need for <strong>UV protection measures</strong>.
      </p>

      <h3>🔍 Key Insights:</h3>
      <ul>
        <li>
          📈 <strong>Increasing Cases:</strong> New South Wales and Queensland report the highest
          cases, indicating higher sun exposure risks.
        </li>
        <li>
          🌞 <strong>Seasonal Variation:</strong> Cases peak in summer due to increased outdoor
          activities and UV radiation exposure.
        </li>
        <li>
          📊 <strong>State-wise Differences:</strong> Tasmania and Northern Territory report lower
          cases, likely due to climate and population differences.
        </li>
      </ul>

      <h3>☀️ Why UV Protection is Important?</h3>
      <p>Excessive UV exposure increases <strong>skin cancer risks</strong>. To reduce exposure:</p>
      <ul>
        <li>🧴 <strong>Apply SPF 50+ sunscreen</strong> every 2 hours.</li>
        <li>🕶️ <strong>Wear UV-protective sunglasses and hats.</strong></li>
        <li>🌳 <strong>Seek shade</strong> between 10 AM - 4 PM.</li>
        <li>👨‍⚕️ <strong>Regular skin check-ups</strong> for early melanoma detection.</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const graphUrl = ref('')

onMounted(async () => {
  try {
    const response = await fetch('https://fit5120-project-1.onrender.com/api/skin_cancer_trends')
    const data = await response.json()
    if (data.status === 'success') {
      graphUrl.value = data.graph_url
    }
  } catch (error) {
    console.error('Error loading graph:', error)
  }
})
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
  color: #d9534f;
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
