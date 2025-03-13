<template>
  <div class="trends-container">
    <h1>Skin Cancer Trends</h1>

    <button @click="fetchGraph">Show Graph</button>

    <div v-if="graphUrl">
      <img :src="graphUrl" alt="Skin Cancer Trend Graph" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const graphUrl = ref(null)

const fetchGraph = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/generate_graph')
    const data = await response.json()
    graphUrl.value = 'http://127.0.0.1:5000' + data.graph_url
  } catch (error) {
    console.error('Error fetching graph:', error)
  }
}
</script>

<style scoped>
.trends-container {
  text-align: center;
  padding: 20px;
}

button {
  background-color: #ff7f00;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1.2rem;
  border-radius: 10px;
  margin-bottom: 20px;
}
</style>
