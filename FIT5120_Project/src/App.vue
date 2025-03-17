<script setup>
import Header from './components/Header.vue'
</script>

<template>
  <div class="main-container">
    
    <main class="content">
      <Header />
      <router-view></router-view>
    </main>
  </div>
</template>

<style scoped>
/* Ensure Full Width and No Gaps */
.main-container {
  width: 100vw;/* Force full width */
  min-height: 100vh; /* Ensure it fills the viewport */
  display: flex;
  flex-direction: column;
  align-items: center; 
  justify-content: flex-start;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

/* Ensure Content Fills Entire Width */
.content {
  flex: 1;
  width: 100%; /* Ensures full width */
  text-align: center;
}
</style>
