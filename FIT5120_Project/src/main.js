import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import VueApexCharts from "vue3-apexcharts";


const app = createApp(App)
app.use(router) // Ensure Vue Router is used
app.use(VueApexCharts);
app.mount('#app') // Mount the app
