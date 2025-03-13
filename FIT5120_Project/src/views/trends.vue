<template>
  <div class="trend-container">
    <h1>Skin Cancer Trends</h1>

    <p class="description">
      The following graphs display trends in skin cancer cases over time, emphasizing the importance
      of sun protection.
    </p>

    <!-- Line Chart for Skin Cancer Cases -->
    <div class="chart-wrapper">
      <canvas id="skinCancerChart"></canvas>
    </div>

    <!-- Pie Chart for Cancer Type Distribution -->
    <div class="chart-wrapper">
      <canvas id="cancerTypeChart"></canvas>
    </div>

    <!-- Informational Text -->
    <div class="info-section">
      <h2>Understanding the Risk</h2>
      <p>
        Skin cancer cases have been rising due to increased UV exposure. This data highlights the
        importance of **UV protection measures** such as sunscreen, protective clothing, and limited
        sun exposure during peak UV hours.
      </p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import Chart from 'chart.js/auto'

// Sample Data (You can replace this with API data)
const skinCancerData = {
  years: ['2000', '2005', '2010', '2015', '2020', '2025'],
  cases: [50000, 75000, 120000, 180000, 250000, 300000],
}

const cancerTypeData = {
  labels: ['Melanoma', 'Basal Cell Carcinoma', 'Squamous Cell Carcinoma'],
  values: [30, 40, 30], // Percentage distribution
}

onMounted(() => {
  // 📊 Line Chart: Trend of Skin Cancer Cases
  new Chart(document.getElementById('skinCancerChart'), {
    type: 'line',
    data: {
      labels: skinCancerData.years,
      datasets: [
        {
          label: 'Skin Cancer Cases Over the Years',
          data: skinCancerData.cases,
          borderColor: '#ff5733',
          backgroundColor: 'rgba(255, 87, 51, 0.2)',
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  })

  // 📊 Pie Chart: Cancer Type Distribution
  new Chart(document.getElementById('cancerTypeChart'), {
    type: 'pie',
    data: {
      labels: cancerTypeData.labels,
      datasets: [
        {
          data: cancerTypeData.values,
          backgroundColor: ['#ff5733', '#ffbd33', '#33ff57'],
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  })
})
</script>

<style scoped>
/* 📌 Container Styling */
.trend-container {
  width: 90%;
  max-width: 900px;
  margin: 50px auto;
  padding: 20px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  backdrop-filter: blur(5px);
  text-align: center;
  color: white;
}

/* 📌 Charts Styling */
.chart-wrapper {
  width: 100%;
  height: 300px;
  margin: 20px auto;
}

/* 📌 Informational Section */
.info-section {
  margin-top: 30px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  text-align: center;
}

.info-section h2 {
  color: orange;
}

.description {
  font-size: 1.2rem;
}
</style>
