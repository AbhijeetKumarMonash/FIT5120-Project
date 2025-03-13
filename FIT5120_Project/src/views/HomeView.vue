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
        <p>☀️ Sunshine Duration: {{ weatherData.sunshineDuration }} hours</p>
      </div>

      <!-- UV Index Section -->
      <div class="info-item uv-index">
        <h2 :class="uvClass">{{ weatherData.uvIndex }}</h2>
      </div>

      <!-- UV Warning Section or Positive Message -->
      <div class="info-item">
        <p v-if="weatherData.uvIndex >= 5" class="uv-warning">
          ⚠️ <strong>Pay Attention to Sun Protection!</strong>
        </p>
        <p v-else class="uv-good-message">
          ✅ <strong>It's a great time to be outside! But stay safe! 😎</strong>
        </p>
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

--- ### **📌 JavaScript Logic (Fixed UV Index Handling)** ```vue
<script setup>
import { ref } from 'vue'

const location = ref('')
const weatherData = ref(null)
const weatherIcon = ref('')

// OpenWeather API Key (Replace with your own)
const OPENWEATHER_API_KEY = '06a8a6ffd268af3a2afd6c6b4a669221'

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

    // 3️⃣ Get UV Index Data (New API)
    const uvResponse = await fetch(
      `https://api.openweathermap.org/data/2.5/uvi?lat=${lat}&lon=${lon}&appid=${OPENWEATHER_API_KEY}`,
    )
    const uvData = await uvResponse.json()

    // 4️⃣ Check if it's daytime (Nighttime logic implemented)
    let currentUV = 0 // Default: 0 if nighttime
    if (currentTime >= sunrise && currentTime <= sunset) {
      currentUV = uvData.value || 0 // If UV data available, use it
    } else {
      currentUV = 0 // Nighttime, so UV index is 0
    }

    // 5️⃣ Calculate Sunshine Duration (Using Sunrise & Sunset)
    const sunshineDuration = ((sunset - sunrise) / (1000 * 60 * 60)).toFixed(1) // Convert to hours

    // 6️⃣ Store Data in `weatherData`
    weatherData.value = {
      location: name,
      temperature: weatherInfo.main.temp,
      weather: weatherInfo.weather[0].description,
      uvIndex: currentUV === 0 ? '0 (Nighttime)' : currentUV, // Show Nighttime if UV is 0
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
</script>

<style scoped>
/* Time Picker */
.search-container input[type='time'] {
  width: 20%;
  padding: 10px;
  border: none;
  border-radius: 20px;
  outline: none;
  font-size: 16px;
  text-align: center;
}
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
