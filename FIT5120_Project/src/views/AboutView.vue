<template>
  <div class="about-container">
    <h1>About Us</h1>
    <p>
      Our mission is to promote **sun protection and UV awareness**. With increasing cases of **skin
      cancer** due to prolonged sun exposure, this website helps users track real-time **UV index
      levels** and get **personalized sun safety recommendations**.
    </p>
    <h2>Why is UV Awareness Important?</h2>
    <ul>
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
  display: flex;
  flex-direction: column;
  align-items: center; /* Centers the text horizontally */
  justify-content: center; /* Centers the content vertically */
  width: 100%;
  max-width: 800px;
  margin: auto;
  padding: 40px;
  text-align: center;
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
</style>
