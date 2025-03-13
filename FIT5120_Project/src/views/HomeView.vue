<template>
  <div class="home-container">
    <h1>UV Index Tracker</h1>

    <!-- Manual Search Input -->
    <div class="search-container">
      <input v-model="location" type="text" placeholder="Enter location" />
      <button @click="fetchWeatherData">Search</button>
    </div>

    <!-- Display Weather & UV Data in a Row -->
    <div v-if="weatherData" class="info-row">
      <!-- Location Section -->
      <div class="info-item">
        <h2 class="location-name">{{ weatherData.location }} <span class="icon">📍</span></h2>
      </div>

      <!-- Weather Section -->
      <div class="info-item">
        <p class="weather">
          <span v-html="weatherIcon"></span>
          {{ weatherData.temperature }}°C - {{ weatherData.weather }}
        </p>
      </div>

      <!-- UV Index Section -->
      <div class="info-item uv-index">
        <h2 :class="uvClass">{{ weatherData.uvIndex }}</h2>
      </div>

      <!-- UV Warning Section -->
      <div class="info-item" v-if="weatherData.uvIndex >= 6">
        <p class="uv-warning">⚠️ <strong>Pay Attention to Sun Protection!</strong></p>
      </div>
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
const weatherIcon = ref('')

// OpenWeather API Key (Replace with your own)
const OPENWEATHER_API_KEY = '06a8a6ffd268af3a2afd6c6b4a669221'

// Fetch Weather & UV Index Data
// Fetch Weather & UV Index Data
const fetchWeatherData = async () => {
  if (!location.value.trim()) {
    alert('Please enter a valid location.')
    return
  }

  try {
    // 1️⃣ Get Latitude & Longitude
    const geoResponse = await fetch(
      `https://api.openweathermap.org/geo/1.0/direct?q=${location.value}&limit=1&appid=${OPENWEATHER_API_KEY}`,
    )
    const geoData = await geoResponse.json()

    if (!geoData.length) {
      alert('Location not found')
      return
    }

    const { lat, lon, name } = geoData[0]

    // 2️⃣ Get Weather Data (Temperature, Description, Sunrise, Sunset)
    const weatherResponse = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${OPENWEATHER_API_KEY}&units=metric`,
    )
    const weatherInfo = await weatherResponse.json()

    const sunrise = weatherInfo.sys.sunrise * 1000 // Convert to milliseconds
    const sunset = weatherInfo.sys.sunset * 1000
    const currentTime = Date.now() // Get current timestamp

    // 🌤 Set the Weather Icon
    setWeatherIcon(weatherInfo.weather[0].main)

    // 3️⃣ Get UV Index Forecast
    const uvResponse = await fetch(
      `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${OPENWEATHER_API_KEY}`,
    )
    const uvData = await uvResponse.json()

    // 4️⃣ Find the Closest UV Index for Current Time
    let currentUV = 0 // Default: 0 if nighttime
    if (currentTime >= sunrise && currentTime <= sunset) {
      // Only set UV index if the sun is up
      const closestUv = uvData.list.find((item) => {
        const forecastTime = new Date(item.dt * 1000).getHours()
        const currentHour = new Date().getHours()
        return forecastTime === currentHour
      })
      currentUV = closestUv?.main?.uvi ?? 0 // Use forecast UV or default to 0
    }

    // 5️⃣ Calculate Sunshine Duration (Using Sunrise & Sunset)
    const sunshineDuration = ((sunset - sunrise) / (1000 * 60 * 60)).toFixed(1) // Convert to hours

    // 6️⃣ Store Data in `weatherData`
    weatherData.value = {
      location: name,
      temperature: weatherInfo.main.temp,
      weather: weatherInfo.weather[0].description,
      uvIndex: currentUV === 0 ? '0 (Nighttime)' : currentUV, // If 0, show Nighttime
      sunshineDuration: sunshineDuration,
    }
  } catch (error) {
    console.error('Error fetching data:', error)
    alert('Error retrieving data')
  }
}

// 🌤 **Function to Set Weather Icon**
const setWeatherIcon = (condition) => {
  const iconMap = {
    Clear: '☀️',
    Clouds: '☁️',
    Rain: '🌧️',
    Drizzle: '🌦️',
    Thunderstorm: '⛈️',
    Snow: '❄️',
    Mist: '🌫️',
    Fog: '🌫️',
  }

  weatherIcon.value = iconMap[condition] || '🌤️' // Default to partly cloudy
}

// UV Index Styling
const uvClass = ref('')
const setUVClass = (uvIndex) => {
  if (uvIndex <= 2) uvClass.value = 'low'
  else if (uvIndex <= 5) uvClass.value = 'moderate'
  else if (uvIndex <= 7) uvClass.value = 'high'
  else if (uvIndex <= 10) uvClass.value = 'very-high'
  else uvClass.value = 'extreme'
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
/* Centered Row for Location, Weather, UV Index, and Warning */
.info-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background: rgba(255, 255, 255, 0.2);
  padding: 15px;
  border-radius: 15px;
  backdrop-filter: blur(5px);
  width: 90%;
  max-width: 800px;
  color: white;
}

/* Individual Sections */
.info-item {
  text-align: center;
  flex: 1;
}

/* Location Styling */
.location-name {
  font-size: 1.5rem;
  font-weight: bold;
}

/* Weather Styling */
.weather {
  font-size: 1.2rem;
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
