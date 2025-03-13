import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'

const app = createApp(App)
app.use(router) // Ensure Vue Router is used
app.mount('#app') // Mount the app
