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
/* Ensure Full Width and Height */
.main-container {
  width: 100vw; /* Full screen width */
  height: 100vh; /* Full screen height */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* Center content vertically */
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* Prevents unwanted horizontal scroll */
}

/* Ensure Content Takes Full Width */
.content {
  flex: 1; /* Make it fill the remaining space */
  width: 100%; /* Ensure it fills the full width */
  text-align: center;
}
</style>
