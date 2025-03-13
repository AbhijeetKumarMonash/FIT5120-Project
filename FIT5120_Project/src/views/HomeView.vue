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
/* Ensure Background Covers the Entire Screen */
.home-container {
  width: 100vw; /* Full viewport width */
  height: 100vh; /* Full viewport height */
  background-image: url('@/assets/skybg.jpeg'); /* Ensure correct image path */
  background-size: cover; /* Ensures the image covers the entire screen */
  background-position: center; /* Centers the image */
  background-repeat: no-repeat; /* Prevents repeating */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin: 0; /* Remove any default margin */
  padding: 0; /* Remove padding */
  overflow-x: hidden; /* Prevent horizontal scrolling */
}

/* Fix Search Bar Alignment */
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  width: 100%;
}

.search-container input {
  padding: 10px;
  width: 60%;
  border: none;
  border-radius: 20px;
  outline: none;
  font-size: 16px;
}

.search-container button {
  padding: 10px 20px;
  background-color: #ff7f00;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
}

/* Ensure Content is Centered */
.uv-index-display {
  width: 90%;
  max-width: 600px;
  background: rgba(255, 255, 255, 0.2);
  padding: 20px;
  border-radius: 15px;
  text-align: center;
  backdrop-filter: blur(5px);
}

/* UV Scale */
.uv-scale {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 100%;
}

.uv-scale div {
  padding: 12px;
  width: 100%;
  text-align: center;
  font-weight: bold;
  color: white;
  border-radius: 5px;
}

/* UV Color Coding */
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
