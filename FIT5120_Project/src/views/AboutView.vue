<template>
  <div class="about-container">
    <h1>About Us</h1>
    <p class="about-text">
      Our mission is to promote **sun protection and UV awareness**. With increasing cases of **skin
      cancer** due to prolonged sun exposure, this website helps users track real-time **UV index
      levels** and get **personalized sun safety recommendations**.
    </p>
    <h2>Why is UV Awareness Important?</h2>
    <ul class="about-list">
      <li>🌞 **Prolonged sun exposure** can cause skin damage and increase cancer risk.</li>
      <li>🧴 Using **SPF 50+ sunscreen** reduces UV damage and aging effects.</li>
      <li>👕 Wearing **UPF-rated clothing, hats, and sunglasses** ensures better protection.</li>
      <li>📡 Knowing the **UV Index** helps make informed outdoor activity decisions.</li>
    </ul>
  </div>
</template>

<style scoped>
/* Centering About Page Content */
.about-container {
  width: 100vw; /* Full viewport width */
  height: 100vh; /* Full viewport height */
  background-image: url('@/assets/skybg.jpeg'); /* Make sure the image path is correct */
  background-size: cover; /* Ensures the image covers the entire screen */
  background-position: center; /* Centers the image */
  background-repeat: no-repeat; /* Prevents repeating */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  margin: 0;
  padding: 0;
}

/* Style for headings */
h1,
h2 {
  color: #ff7f00;
}

/* Style for list */
ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
  text-align: left;
  display: flex;
  align-items: center;
}
.about-text {
  font-size: 1.25rem;
  font-weight: bold;
  margin: 0;
  color: white;
}
.about-list {
  color: white;
}
</style>
