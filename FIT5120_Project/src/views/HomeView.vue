<template>
  <div class="home-container">
    <h1>UV Index Tracker</h1>
    <div class="search-container">
      <input type="text" v-model="location" placeholder="Enter location" />
      <button @click="searchUVIndex">Search</button>
    </div>

    <div class="uv-index-display">
      <h2>UV Index Criteria</h2>
      <div class="uv-scale">
        <div class="low">Low (0-2)</div>
        <div class="moderate">Moderate (3-5)</div>
        <div class="high">High (6-7)</div>
        <div class="very-high">Very High (8-10)</div>
        <div class="extreme">Extreme (11+)</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const location = ref('')

const searchUVIndex = () => {
  alert(`Searching UV index for: ${location.value}`)
}
</script>

<style scoped>
/* Ensure Home Page Stretches Fully */
.home-container {
  width: 90%; /* Takes most of the available width */
  max-width: 1200px; /* Prevents excessive stretching */
  margin: auto;
  padding: 100px 10px;
  text-align: center;
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.search-container input {
  padding: 10px;
  width: 60%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-container button {
  padding: 10px 20px;
  background-color: #ff7f00;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.uv-index-display {
  margin-top: 30px;
  width: 100%;
}

.uv-scale {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  width: 100%;
}

.uv-scale div {
  padding: 12px;
  width: 80%;
  text-align: center;
  font-weight: bold;
  color: white;
  border-radius: 5px;
}

.low {
  background: green;
}
.moderate {
  background: yellow;
  color: black;
}
.high {
  background: orange;
}
.very-high {
  background: red;
}
.extreme {
  background: purple;
}
</style>
