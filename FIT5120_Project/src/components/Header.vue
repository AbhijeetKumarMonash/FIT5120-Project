<template>
  <div class="fixed-top">
    <header class="header-container">
      <h1 class="logo">UV Protection</h1>
      <nav>
        <ul class="nav-links">
          <li>
            <router-link to="/" class="nav-link" active-class="active">Home</router-link>
          </li>
          <li>
            <router-link to="/about" class="nav-link" active-class="active">About Us</router-link>
          </li>
          <li>
            <router-link to="/faq" class="nav-link" active-class="active">FAQ</router-link>
          </li>
          <li>
            <router-link to="/trends" class="nav-link" active-class="active">Trends</router-link>
          </li>
          <li>
            <router-link to="/SkinCancerTrends" class="nav-link" active-class="active"
              >SkinCancerTrends</router-link
            >
          </li>
        </ul>
      </nav>
    </header>
  </div>
</template>

<style scoped>
/* Full width fixed header */
.fixed-top {
  width: 100vw; /* Ensure it takes the full viewport width */
  background-color: #0056b3;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
}

/* Header container styling */
.header-container {
  display: flex;
  justify-content: space-between; /* Space between title and nav */
  align-items: center;
  padding: 15px 20px;
  color: white;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Logo */
.logo {
  font-size: 1.75rem;
  font-weight: bold;
  margin: 0;
}

/* Navigation Links */
.nav-links {
  list-style: none;
  display: flex;
  gap: 20px; /* Spacing between Home and About Us */
  margin: 0;
  padding: 0;
}

/* Individual Nav Links */
.nav-link {
  text-decoration: none;
  color: #e6f2ff;
  font-weight: 500;
  padding: 8px 12px;
  border-radius: 5px;
  transition:
    color 0.2s,
    background-color 0.2s;
}

/* Hover and Active States */
.nav-link:hover {
  color: #ffffff;
}

.nav-link.active {
  background-color: white;
  color: #0056b3;
}
</style>
