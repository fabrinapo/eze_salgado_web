import { createApp } from 'vue'
import './style.css' // <--- IMPORTANTE: Aquí importamos los estilos de Tailwind
import App from './App.vue'
import { createHead } from '@vueuse/head' // Si instalaste @vueuse/head

const app = createApp(App)
const head = createHead()

app.use(head)
app.mount('#app')