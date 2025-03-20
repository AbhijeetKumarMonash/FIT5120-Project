<template>
  <div class="home-container">
    <div class="faq-container">
      <h1 class="Faq">Frequently Asked Questions (FAQ)</h1>

      <div class="faq-list">
        <!-- FAQ Items -->

        <div v-for="(category, catIndex) in uniqueCategories" :key="catIndex">
          <h2 class="faq-category">{{ category }}</h2> 


          <div v-for="(faq, index) in filteredFaqs(category)" :key="index" class="faq-item">
            <button @click="toggleFAQ(faq)" class="faq-question">
              {{ faq.question }}
              <span v-if="faq.open">➖</span>
              <span v-else>➕</span>
            </button>

          <div v-if="faq.open" class="faq-answer">
            <p>{{ faq.answer }}</p>
            <iframe
              v-if="faq.video"
              :src="faq.video"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
              class="faq-video"
            ></iframe>
          </div></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick,computed } from 'vue'
const uniqueCategories = computed(() => {
  return [...new Set(faqs.value.map(faq => faq.category))]; // get category
});
const filteredFaqs = (category) => {
  return faqs.value.filter(faq => faq.category === category);
};

// FAQ Data
const faqs = ref([

  {
    category: "UV Basics",
    question: "How can I check the UV Index for my location?",
    answer: "You can use our UV Tracker feature to check the real-time UV Index for your selected location. The color-coded system indicates the level of UV hazard.",
    video: "https://www.youtube.com/embed/gpNEFHfDZ0c",
    open: false,
  },
  {
    category: "UV Basics",
    question: "How types of radiation differ, and how they can impact us?",
    answer: "The UV Index measures the strength of ultraviolet radiation from the sun. High UV levels mean increased risk of skin damage, sunburn, and skin cancer.",
    video: "https://www.youtube.com/embed/CHO2hL8uV5M?si=8aqrlSAlDsW78325",
    open: false,
  },
  {
    category: "UV Basics",
    question: "Does Australia have a problem with sunscreen?",
    answer: "Aussies are always out and about in the sun, and yet we're not wearing sunscreen as we should be. Learn about the light sunscreen options that can form the basis of your skincare routine.",
    video: "https://www.youtube.com/embed/me5qIipu-lM?si=Pf89DCf6zHeGpbhm",
    open: false,
  },
  {
    category: "Health & Protection",
    question: "Do Dark Skin People ACTUALLY NEED Sunscreen?",
    answer: "Yes, people with dark skin still need sunscreen. While higher melanin levels provide some natural protection (about SPF 13), they do not prevent UV damage, premature aging, or skin cancer. UV rays can still cause hyperpigmentation, sunburn, and increase the risk of skin cancer, even in darker skin tones.",
    video: "https://www.youtube.com/embed/qW4MTsXa4hw?si=Xp5sDUv3RlbVjE90",
    open: false,
  },
  {
    category: "Health & Protection",
    question: "Why should I care about sun protection?",
    answer: "Prolonged exposure to UV radiation can cause skin damage, premature aging, and increase the risk of skin cancer. Proper sun protection reduces these risks.",
    video: "https://www.youtube.com/embed/ZSJITdsTze0",
    open: false,
  },
  {
    category: "Health & Protection",
    question: "How does UV exposure impact Australia?",
    answer: "Australia has one of the highest rates of skin cancer in the world due to high UV radiation. Regular sun protection is necessary to reduce risks.",
    video: "https://www.youtube.com/embed/wHm0FzpQS4M",
    open: false,
  },
  {
    category: "Best Practices",
    question: "How much sunscreen should I apply?",
    answer: "A general guideline is about a teaspoon per body part (face, arms, legs, etc.). Adjust based on skin type and UV intensity.",
    video: "https://www.youtube.com/embed/j6wki7Bpw3w",
    open: false,
  },
  {
    category: "Best Practices",
    question: "Do I need to reapply sunscreen?",
    answer: "Yes! Sunscreen should be reapplied every 2 hours, especially after swimming or sweating.",
    video: "https://www.youtube.com/embed/j6wki7Bpw3w",
    open: false,
  },
  {
    category: "Best Practices",
    question: "What should I do according to different UV Index?",
    answer: "The UV Index indicates the level of sun exposure risk. At low levels (0-2), minimal protection is needed. When it's moderate (3-5), apply sunscreen and wear sunglasses. For high levels (6-7), wear protective clothing and avoid midday sun. At very high (8-10), stay in the shade, use SPF 30+, and limit outdoor activities. If it's extreme (11+), avoid direct sunlight and wear full protection. Always check the UV Index before going outside.",
    video: "https://www.youtube.com/embed/YGROFs5tFNA",
    open: false,
  },
  {
    category: "Best Practices",
    question: "What type of clothing protects against UV radiation?",
    answer: "Wear UPF-rated clothing, wide-brim hats, and sunglasses to protect against UV rays. Dark-colored and tightly woven fabrics provide the best protection.",
    video: "https://www.youtube.com/embed/YGROFs5tFNA",
    open: false,
  },
  {
    category: "Best Practices",
    question: "Can I get enough vitamin D while protecting myself from the sun?",
    answer: "Yes! You can get vitamin D through a balanced approach—short sun exposure (before 10 AM or after 4 PM) and dietary sources.",
    video: "https://www.youtube.com/embed/CAqRMr47KWk",
    open: false,
  },
  {
    category: "Best Practices",
    question: "What is the best time to go outside safely?",
    answer: "The safest times are before 10 AM and after 4 PM when UV levels are lower. Use shade, clothing, and sunscreen when UV levels are high.",
    video: "https://www.youtube.com/embed/AoUmVgPozSE",
    open: false,
  },
]);

// Toggle FAQ Visibility & Scroll to Question
const toggleFAQ = (faq) => {
  console.log("Clicked FAQ:", faq.question);

  faqs.value.forEach(item => {
    if (item !== faq) item.open = false;
  });

  faq.open = !faq.open;

  console.log("Toggled FAQ:", faq.question, "Open:", faq.open);

  if (faq.open) {
    nextTick(() => {
      const faqElements = document.querySelectorAll('.faq-item');
      const index = faqs.value.findIndex(item => item === faq); 
      if (faqElements[index]) {
        faqElements[index].scrollIntoView({
          behavior: 'smooth',
          block: 'start',
        });
      }
    });
  }
};


</script>

<style scoped>
h1 {
  margin: 0;
  color: #01152a;
}
/* Container Styling */
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
.faq-container {
  width: 90%;
  max-width: 1200px;
  margin-top: 40px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.225);
  border-radius: 10px;
  backdrop-filter: blur(5px);
  text-align: center;
  color: white;
  max-height: 80vh; /* Prevents overflowing beyond screen */
  overflow-y: auto; /* Allows scrolling */
}

/* FAQ List */
.faq-list {
  margin-top: 20px;
}


/* FAQ Question Button */
.faq-question {
  width: 100%;
  text-align: left;
  background: #015dbfe2;
  color: white;
  font-size: 18px;
  padding: 15px;
  margin: 10px;
  border: none;
  outline: none;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.3s;
}

/* Hover Effect */
.faq-question:hover {
  background: #4899ef;
}

/* FAQ Answer Section */
.faq-answer {
  background: #e3e4e7;
  padding: 15px;
  margin-top: 5px;
  margin-left: 10px;
  margin-right: 10px;
  border-radius: 5px;
  font-size: 16px;
  text-align: left;
  max-height: 400px;
  overflow-y: auto; /* Ensures long answers don't push everything down */
  transition: max-height 0.3s ease-in-out;
  color: black;
}

/* Video Wrapper */
.video-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  margin-top: 10px;
}

/* Responsive YouTube Video */
.faq-video {
  width: 100%;
  height: 250px;
  border-radius: 5px;
}

/* Adjust video size on smaller screens */
@media (max-width: 600px) {
  .faq-video {
    height: 180px;
  }
}
</style>
