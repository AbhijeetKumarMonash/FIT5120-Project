<script setup>
import Header from './components/Header.vue'
</script>

<template>
  <div class="main-container">
    <Header />
    <!-- Include the header for navigation -->
    <main class="content">
      <router-view></router-view>
      <!-- Loads HomeView or AboutView dynamically -->
    </main>
  </div>
</template>

<style scoped>
/* Full-page layout */
.main-container {
  width: 100vw; /* Full screen width */
  height: 100vh; /* Full screen height */
  display: flex;
  flex-direction: column;
  align-items: center; /* Center content horizontally */
}

/* Content layout fix */
.content {
  flex: 1; /* Make it fill the remaining space */
  width: 90%; /* Takes most of the available width */
  max-width: 1200px; /* Prevents content from stretching too much */
  padding: 40px 20px; /* Increases gap from the top */
  text-align: center; /* Align text in the center */
}
</style>
