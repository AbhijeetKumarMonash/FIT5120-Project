<template>
  <div class="home-container">
    <br />
    <br />
    <h1>UV Index Tracker</h1>

    <!-- Manual Search Input -->
    <div class="search-container">
      <input v-model="location" type="text" placeholder="Enter an Australian suburb code (e.g., 3000)" />
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

    <SkinTone :uvIndex="uvIndexComputed" />

    <!-- UV Index Criteria -->
    <div class="uv-index-display">
      <h2>UV Index Criteria</h2>
      <div class="uv-scale">
        <button
          v-for="(info, level) in uvInfoMap"
          :key="level"
          :class="[level, { selected: selectedUV === level }]"
          @click="selectUV(level)"
        >
          {{ info.label }}
        </button>
      </div>
      <div v-if="selectedUV" class="uv-info">
        <h3>{{ uvInfoMap[selectedUV].label }}</h3>
        <p>{{ uvInfoMap[selectedUV].description }}</p>
      </div>
      
    </div>
    
  </div>
</template>

--- ### **📌 JavaScript Logic (Fixed UV Index Handling)** ```vue
<script setup>
import SkinTone from '@/components/SkinTone.vue';
import { ref } from 'vue'
import { computed } from "vue";

const location = ref('')
const weatherData = ref('');

const weatherIcon = ref('')

const isValid = computed(() => /^\d{4}$/.test(location.value));

const uvIndexComputed = computed(() => {
  if (!weatherData.value || typeof weatherData.value.uvIndex !== "number") {
    return null; // 
  }
  return weatherData.value.uvIndex;
});



// OpenWeather API Key (Replace with your own)
const OPENWEATHER_API_KEY = '06a8a6ffd268af3a2afd6c6b4a669221'
const GOOGLE_MAPS_API_KEY = 'AIzaSyCHFOVKWeydFMRF6FL9iVbj1ooWuPuluP8'

// Fetch Weather & UV Index Data
const fetchWeatherData = async () => {
  if (!isValid.value) {
    alert('Please enter a valid 4-digit suburb code.')
    return;
  }
  if (!location.value.trim()) {
    alert('Please enter a valid suburb code.')
    return
  }

  // try {
  //   // 1️⃣ Get Latitude & Longitude
  //   const geoResponse = await fetch(
  //     `https://api.openweathermap.org/geo/1.0/direct?q=${location.value}&limit=1&appid=${OPENWEATHER_API_KEY}`,
  //   )
  //   const geoData = await geoResponse.json()

  //   if (!geoData.length) {
  //     alert('Location not found')
  //     return
  //   }

  //   const { lat, lon, name } = geoData[0]
    try {
      // 1️⃣ Get Latitude & Longitude from Google Geocode API
      const geoResponse = await fetch(
        `https://maps.googleapis.com/maps/api/geocode/json?address=${location.value},AU&key=${GOOGLE_MAPS_API_KEY}`
      )
      const geoData = await geoResponse.json()

      if (!geoData.results.length) {
        alert('Sorry!Location not found')
        return
      }

      // Extract lat & lon
      const { lat, lng: lon } = geoData.results[0].geometry.location

      // Extract city name (long_name where type is 'locality')
      let name = ""
      const addressComponents = geoData.results[0].address_components
      for (const component of addressComponents) {
        if (component.types.includes("locality")) {
          name = component.long_name
          break
        }
      }
      console.log(lat, lon, name)

    if (!name) {
      alert('City name not found')
      return
    }

    
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
      uvIndex: currentUV,
      sunshineDuration: sunshineDuration,
    }
    location.value = ''
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
const uvClass = computed(() => {
  const uv = weatherData.value.uvIndex;
  if (uv <= 2) return "low";
  if (uv <= 5) return "moderate";
  if (uv <= 7) return "high";
  if (uv <= 10) return "very-high";
  else return "extreme";
  
});

const uvInfoMap = {
  low: {
    label: "Low (0-2)",
    description: "Minimal risk. You can safely enjoy outdoor activities.",
  },
  moderate: {
    label: "Moderate (3-5)",
    description: "Moderate risk. Wear sunglasses and sunscreen should be applied every two hours, even on cloudy days.",
  },
  high: {
    label: "High (6-7)",
    description: "High risk. Seek shade during midday hours and use SPF 30+ sunscreen.",
  },
  "very-high": {
    label: "Very High (8-10)",
    description: "Very high risk. Wear protective clothing, sunglasses, and SPF 50+ sunscreen.",
  },
  extreme: {
    label: "Extreme (11+)",
    description: "Extreme risk! Avoid direct sunlight and use strong sun protection.",
  },
};
const selectedUV = ref("");

const selectUV = (level) => {
  selectedUV.value = level;
};



</script>

<style scoped>
/* Time Picker */
/* .search-container input[type='time'] {
  width: 20%;
  padding: 10px;
  border: none;
  border-radius: 20px;
  outline: none;
  font-size: 16px;
  text-align: center;
} */
/* Ensure Background Covers the Entire Screen */
.home-container {
  width: 100vw;
  min-height: 100vh;
  height: auto;
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
  overflow-y: auto;
  padding-top: 60px;

}

.home-container h1 {
  color: rgb(80, 80, 80); 
}

/* Fix Search Bar Alignment */
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  width: 100%;
  margin-bottom: 15px;
  margin-top: 15px;
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
  background-color: #ff8000e0;
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
  margin-top: 15px;  
  margin-bottom: 15px;
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
  color: rgba(184, 183, 183, 0.846);
}

.info-item p {
  color: rgb(80, 80, 80);
}

/* Ensure Content is Centered */
.uv-index-display {
  width: 90%;
  max-width: 400px;
  background: rgba(255, 255, 255, 0.2);
  padding: 20px;
  border-radius: 15px;
  text-align: center;
  backdrop-filter: blur(5px);
  margin-top: 10px;
}

.uv-index-display h2 {
  color: rgb(80, 80, 80);
}

/* UV Scale button */
.uv-scale {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 100%;
}

.uv-scale button {
  padding: 12px;
  width: 100%;
  text-align: center;
  font-weight: bold;
  color: white;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

/* UV Color Coding */
.low {
  background: rgba(163, 237, 163, 0.93);
}
.moderate {
  background: rgba(242, 242, 127, 0.93);
  color: black;
}
.high {
  background: rgba(245, 160, 99, 0.93);
}
.very-high {
  background: rgba(241, 111, 111, 0.93);
}
.extreme {
  background: rgba(237, 134, 237, 0.93);
}

.uv-scale button:hover {
  opacity: 0.8;
}

.uv-info {
  margin-top: 15px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  text-align: center;
}

.uv-info h3 {
  font-size: 18px;
  font-weight: bold;
  color: rgb(80, 80, 80);
}
.uv-info p {
  font-size: 14px;
  color: rgb(80, 80, 80);
}


/* Info Box */
.info-box {
  margin-top: 15px;
  padding: 12px;
  border-radius: 5px;
  color: white;
  font-size: 16px;
  text-align: center;
}

</style>