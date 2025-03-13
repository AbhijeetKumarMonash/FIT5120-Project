<template>
  <div class="home-container">
    <h1>UV Index Tracker</h1>

    <!-- Manual Search Input -->
    <div class="search-container">
      <input v-model="location" type="text" placeholder="Enter location" />
      <button @click="fetchWeatherData">Search</button>
    </div>

    <!-- Display Searched Location Data -->
    <div v-if="weatherData" class="weather-info">
      <h2>{{ weatherData.location }}</h2>
      <p>{{ weatherData.temperature }}°C - {{ weatherData.weather }}</p>
      <p><strong>UV Index:</strong> {{ weatherData.uvIndex }}</p>
      <p><strong>Sunshine Duration:</strong> {{ weatherData.sunshineDuration }} hours</p>
    </div>

    <!-- UV Index Criteria -->
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
const weatherData = ref(null)

// OpenWeather API Key (Replace with your own)
const OPENWEATHER_API_KEY = '06a8a6ffd268af3a2afd6c6b4a669221'

// Fetch Weather & UV Index Data
const fetchWeatherData = async () => {
  if (!location.value.trim()) {
    alert('Please enter a valid location.')
    return
  }

  try {
    // 1️⃣ Get Latitude & Longitude from City Name (Free Geocoding API)
    const geoResponse = await fetch(
      `https://api.openweathermap.org/geo/1.0/direct?q=${location.value}&limit=1&appid=${OPENWEATHER_API_KEY}`,
    )
    const geoData = await geoResponse.json()

    if (!geoData.length) {
      alert('Location not found')
      return
    }

    const { lat, lon, name } = geoData[0]

    // 2️⃣ Get Weather Data (Temperature, Description) - Free API
    const weatherResponse = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${OPENWEATHER_API_KEY}&units=metric`,
    )
    const weatherInfo = await weatherResponse.json()

    // 3️⃣ Get UV Index (Free API - Deprecated but still works)
    const uvResponse = await fetch(
      `https://api.openweathermap.org/data/2.5/uvi?lat=${lat}&lon=${lon}&appid=${OPENWEATHER_API_KEY}`,
    )
    const uvData = await uvResponse.json()

    // 4️⃣ Calculate Sunshine Duration (Using Sunrise & Sunset)
    const sunrise = weatherInfo.sys.sunrise * 1000 // Convert to milliseconds
    const sunset = weatherInfo.sys.sunset * 1000
    const sunshineDuration = ((sunset - sunrise) / (1000 * 60 * 60)).toFixed(1) // Convert to hours

    // 5️⃣ Store Data in `weatherData`
    weatherData.value = {
      location: name,
      temperature: weatherInfo.main.temp,
      weather: weatherInfo.weather[0].description,
      uvIndex: uvData.value ?? 'N/A', // If missing, show "N/A"
      sunshineDuration: sunshineDuration,
    }
  } catch (error) {
    console.error('Error fetching data:', error)
    alert('Error retrieving data')
  }
}
</script>

<style scoped>
/* Ensure Background Covers the Entire Screen */
.home-container {
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/skybg.jpeg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
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

/* Weather Info Display */
.weather-info {
  background: rgba(255, 255, 255, 0.2);
  padding: 15px;
  margin-top: 10px;
  border-radius: 15px;
  backdrop-filter: blur(5px);
  font-size: 18px;
  color: white;
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
