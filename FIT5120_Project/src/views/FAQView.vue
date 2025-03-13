<template>
  <div class="home-container">
    <div class="faq-container">
      <h1 class="Faq">Frequently Asked Questions (FAQ)</h1>

      <div class="faq-list">
        <!-- FAQ Items -->
        <div v-for="(faq, index) in faqs" :key="index" class="faq-item">
          <button @click="toggleFAQ(index)" class="faq-question">
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
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

// FAQ Data
const faqs = ref([
  {
    question: 'What is the UV Index, and why is it important?',
    answer:
      'The UV Index measures the strength of ultraviolet radiation from the sun. High UV levels mean increased risk of skin damage, sunburn, and skin cancer.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'How can I check the UV Index for my location?',
    answer:
      'You can use our UV Tracker feature to check the real-time UV Index for your selected location. The color-coded system indicates the level of UV hazard.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'Why should I care about sun protection?',
    answer:
      'Prolonged exposure to UV radiation can cause skin damage, premature aging, and increase the risk of skin cancer. Proper sun protection reduces these risks.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'How does UV exposure impact Australia?',
    answer:
      'Australia has one of the highest rates of skin cancer in the world due to high UV radiation. Regular sun protection is necessary to reduce risks.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'How much sunscreen should I apply?',
    answer:
      'A general guideline is about a teaspoon per body part (face, arms, legs, etc.). Adjust based on skin type and UV intensity.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'Do I need to reapply sunscreen?',
    answer:
      'Yes! Sunscreen should be reapplied every 2 hours, especially after swimming or sweating.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'What type of clothing protects against UV radiation?',
    answer:
      'Wear UPF-rated clothing, wide-brim hats, and sunglasses to protect against UV rays. Dark-colored and tightly woven fabrics provide the best protection.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'Can I get enough vitamin D while protecting myself from the sun?',
    answer:
      'Yes! You can get vitamin D through a balanced approach—short sun exposure (before 10 AM or after 4 PM) and dietary sources.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
  {
    question: 'What is the best time to go outside safely?',
    answer:
      'The safest times are before 10 AM and after 4 PM when UV levels are lower. Use shade, clothing, and sunscreen when UV levels are high.',
    video: 'https://www.youtube.com/embed/9qzHaw8x6MA',
    open: false,
  },
])

// Toggle FAQ Visibility & Scroll to Question
const toggleFAQ = (index) => {
  faqs.value.forEach((faq, i) => {
    if (i !== index) faq.open = false // Close other questions
  })

  faqs.value[index].open = !faqs.value[index].open

  // Scroll to the expanded FAQ item **after** Vue updates the DOM
  if (faqs.value[index].open) {
    nextTick(() => {
      const faqElement = document.querySelectorAll('.faq-item')[index]
      if (faqElement) {
        faqElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start',
        })
      }
    })
  }
}
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
  margin: 50px auto;
  padding: 20px;
  background: rgba(255, 255, 255, 0.2);
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
  background: #0056b3;
  color: white;
  font-size: 18px;
  padding: 15px;
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
  background: #0056b3;
}

/* FAQ Answer Section */
.faq-answer {
  background: #e3e4e7;
  padding: 15px;
  margin-top: 5px;
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
