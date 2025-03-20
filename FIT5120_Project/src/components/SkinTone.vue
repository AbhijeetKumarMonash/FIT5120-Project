<template>
  <div class="skin-tone-container">
    <h2>Select Your Skin Tone</h2>
    <div class="skin-tone-buttons">
      <button
        v-for="(tone, index) in skinTones"
        :key="index"
        :class="tone.class"
        @click="selectedTone = tone"
      >
        {{ tone.label }}
      </button>
    </div>

    <div v-if="selectedTone" class="skin-tone-info">
      <h3>{{ selectedTone.label }}</h3>
      <p>{{ getUvAdvice(selectedTone.type) }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { defineProps, watch } from "vue";

const selectedTone = ref(null);


const props = defineProps({
  uvIndex: Number, 
});

// 💡 
const skinTones = ref([
  { label: "Type 1: Very Fair", class: "type1", type: 1 },
  { label: "Type 2: Fair", class: "type2", type: 2 },
  { label: "Type 3: Medium", class: "type3", type: 3 },
  { label: "Type 4: Olive", class: "type4", type: 4 },
  { label: "Type 5: Brown", class: "type5", type: 5 },
  { label: "Type 6: Dark Brown/Black", class: "type6", type: 6 },
]);

// 💡 
const uvAdviceMap = {
  1: {
    low: "Your skin burns easily. Use SPF50+ and avoid direct sun exposure.",
    moderate: "Avoid prolonged exposure. Apply SPF50+ and wear protective clothing.",
    high: "Stay in the shade, wear a hat, and use SPF50+.",
    veryHigh: "Limit sun exposure. Use SPF50+, sunglasses, and protective clothing.",
    extreme: "Avoid the sun completely. SPF50+ is a must, along with full protection.",
    default: "Your skin is highly sensitive to the sun. Always use SPF50+ and limit sun exposure.",
  },
  2: {
    low: "Your skin is prone to sunburn. Use SPF50+ and seek shade.",
    moderate: "Use SPF50+, wear a hat, and reapply sunscreen every 2 hours.",
    high: "Avoid direct sun from 10 AM - 4 PM. SPF50+ and sunglasses recommended.",
    veryHigh: "Protect your skin with SPF50+, hat, and sunglasses. Avoid extended exposure.",
    extreme: "Limit sun exposure, use SPF50+, and cover up as much as possible.",
    default: "Your skin needs strong protection. Apply SPF50+ and avoid midday sun.",
  },
  3: {
    low: "Moderate sun sensitivity. Use SPF30+ if exposed for long periods.",
    moderate: "Use SPF30+ and wear a hat if staying outside for extended periods.",
    high: "Protect your skin. Use SPF50+, seek shade, and wear sunglasses.",
    veryHigh: "Reapply SPF50+ every 2 hours. Limit sun exposure.",
    extreme: "Avoid the sun when possible. Full protection is recommended.",
    default: "You may tan easily but still need SPF30+ for protection.",
  },
  4: {
    low: "Minimal sun sensitivity. SPF30+ recommended for prolonged exposure.",
    moderate: "Use SPF30+ and avoid direct sun exposure for long periods.",
    high: "Protect your skin with SPF50+ and seek shade when necessary.",
    veryHigh: "Use SPF50+, wear protective clothing, and avoid long sun exposure.",
    extreme: "Even with darker skin, SPF50+ and full coverage is advised.",
    default: "Your skin tans but still requires SPF30+ to prevent long-term damage.",
  },
  5: {
    low: "Rarely burns, but UV damage can still occur. SPF30+ is recommended.",
    moderate: "Use SPF30+ if outside for extended periods.",
    high: "SPF30+ and sunglasses are advised, especially for long exposure.",
    veryHigh: "UV damage can occur. Use SPF50+ and limit sun exposure.",
    extreme: "Long exposure may cause skin damage. SPF50+ is necessary.",
    default: "Your skin is naturally protected but still needs SPF30+.",
  },
  6: {
    low: "Deeply pigmented skin, but UV damage can still happen. SPF30+ advised.",
    moderate: "Use SPF30+ for long outdoor stays.",
    high: "SPF30+ still needed, and sunglasses recommended.",
    veryHigh: "UV exposure over time can cause damage. SPF50+ and coverage advised.",
    extreme: "Even with dark skin, prolonged UV exposure can be harmful. Protect yourself.",
    default: "Your skin provides natural protection, but SPF30+ is still recommended.",
  },
};


const getUvAdvice = (skinType) => {
  const uv = props.uvIndex;
  console.log("Received UV in getUvAdvice:", uv);
  if (uv === null || uv === undefined) { 
      console.log("00000000000000000000000", uv);
      return uvAdviceMap[skinType].default;
      }
  if (uv <= 2) return uvAdviceMap[skinType].low;
  if (uv <= 5) return uvAdviceMap[skinType].moderate;
  if (uv <= 7) return uvAdviceMap[skinType].high;
  if (uv <= 10) return uvAdviceMap[skinType].veryHigh;
  return uvAdviceMap[skinType].extreme;
};
</script>

<style scoped>
.skin-tone-container {
width: 90%;
max-width: 400px;
background: rgba(255, 255, 255, 0.2);
padding: 20px;
border-radius: 15px;
text-align: center;
backdrop-filter: blur(5px);
margin: 20px auto;
}

.skin-tone-buttons {
display: flex;
flex-wrap: wrap;
gap: 10px;
justify-content: center;
}

button {
padding: 12px;
width: 100px;
font-weight: bold;
border: none;
border-radius: 5px;
cursor: pointer;
color: white;
}

/* skin tone */
.type1 { background: #eab798; }
.type2 { background: #e1a280; }
.type3 { background: #c68055; }
.type4 { background: #ba7339; }
.type5 { background: #9f553b; }
.type6 { background: #744f3c; }

.skin-tone-info {
margin-top: 20px;
padding: 15px;
background: rgba(255, 255, 255, 0.3);
border-radius: 10px;
color: black;
}

.skin-tone-info h3 {
font-size: 18px;
font-weight: bold;
color: rgb(80, 80, 80);
}
.skin-tone-container p {
font-size: 14px;
color: rgb(80, 80, 80);
}
.skin-tone-container h2 {
color: rgb(80, 80, 80);
}

.skin-tone-container button:hover {
opacity: 0.8;
}
</style>