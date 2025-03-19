<template>
  <div class="about-container">
    <div class="container">
      <div class="text-center">
        <br />
        <br />
        <br />
        <h1 class="about-title">About Us</h1>
      </div>


      <!-- Replace Image with Embedded YouTube Video -->
      <div class="row justify-content-center">
        <div class="col-12 video-container">
          <iframe
            width="90%"
            height="300"
            src="https://www.youtube.com/embed/SlXptZfWjJM"
            title="Importance of UV Protection"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
      </div>

      <div class="row justify-content-center">
        <div class="col-md-10 col-lg-8 about-us-section">
          <h2>Our Mission</h2>
          <p>
            Our mission is to promote <strong>sun protection and UV awareness</strong>. With
            increasing cases of <strong>skin cancer</strong> due to prolonged sun exposure, this
            website helps users track real-time <strong>UV index levels</strong> and get
            <strong>personalized sun safety recommendations</strong>.
          </p>

          <h2>Why is UV Awareness Important?</h2>
          <ul class="about-list">
            <li>🌞 Prolonged sun exposure can cause skin damage and increase cancer risk.</li>
            <li>🧴 Using SPF 50+ sunscreen reduces UV damage and aging effects.</li>
            <li>👕 Wearing UPF-rated clothing, hats, and sunglasses ensures better protection.</li>
            <li>📡 Knowing the UV Index helps make informed outdoor activity decisions.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Ensure YouTube Video is Centered and Responsive */
.video-container {
  width: 100%;
  max-width: 800px;
  margin: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  margin-top: 40px;
}

iframe {
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}
h2 {
  color: orange;
  font-weight: bold;
  margin-top: 15px;
  margin-bottom: 15px;
}
/* Ensure Background Covers Entire Screen Properly */
.about-container {
  width: 100vw; /* Full screen width */
  height: 100vh; /* Full screen height */
  background-image: url('@/assets/skybg.jpeg'); /* Ensure correct image path */
  background-size: cover; /* Ensures full background */
  background-position: center; /* Centers the image */
  background-repeat: no-repeat; /* Prevents repeating */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  color: white;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  padding-top: 60px;
}

/* Ensure Full Width and Centering */
.container {
  max-width: 100%;
  padding: 20px;
}

/* Increase Image Size */
.about-image {
  width: 100%;
  max-height: 400px; /* Limits height */
  object-fit: cover; /* Ensures image doesn't stretch */
  border-radius: 10px;
}

/* Properly Align Text */
.about-us-section {
  background: rgba(0, 0, 0, 0.6); /* Dark semi-transparent background */
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  width: 90%;
  max-width: 1500px; /* Ensures it doesn't go too wide */
  margin: auto; /* Centers the text container */

}

/* Fix Text Being Cut Off */
.about-us-section p {
  word-wrap: break-word;
  white-space: normal;
  overflow-wrap: break-word;
  font-size: 1.2rem;
  margin-bottom: 15px;
  line-height: 1.6;
}

/* Fix List Alignment */
.about-list {
  list-style-type: none;
  padding: 0;
  font-size: 1.1rem;
  text-align: left;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.about-list li {
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 1000px;
  padding-left: 150px;
}
</style>
