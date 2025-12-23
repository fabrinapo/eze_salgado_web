<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const isOpen = ref(false);
const isScrolled = ref(false);

// Control del scroll para cambiar la navbar de transparente a sólida
const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

// Función para cerrar el menú al hacer clic en un enlace
const closeMenu = () => {
  isOpen.value = false;
};

const navLinks = [
  { name: 'Inicio', href: '#' },
  { name: 'Bio', href: '#bio' },
  { name: 'Shows', href: '#shows' },
  { name: 'Videos', href: '#videos' },
  { name: 'Servicios', href: '#services' },
  { name: 'Gear', href: '#gear' },
  { name: 'Contacto', href: '#contact' },
];
</script>

<template>
  <header 
    class="fixed top-0 left-0 w-full z-50 transition-all duration-500"
    :class="isScrolled ? 'bg-patagonia/95 backdrop-blur-sm py-4 shadow-lg shadow-black/20' : 'bg-transparent py-6'"
  >
    <div class="container mx-auto px-6 flex justify-between items-center">
      
      <a href="#" class="relative z-[60] font-western text-2xl md:text-3xl text-mist uppercase tracking-widest font-bold group">
        Eze<span class="text-clay group-hover:text-brass transition-colors">Salgado</span>
      </a>

      <nav class="hidden md:flex items-center space-x-8">
        <a 
          v-for="link in navLinks" 
          :key="link.name"
          :href="link.href" 
          class="font-sans text-sm uppercase tracking-[0.2em] text-mist hover:text-clay transition-all duration-300 relative group font-bold"
        >
          {{ link.name }}
          <span class="absolute -bottom-2 left-0 w-0 h-0.5 bg-clay group-hover:w-full transition-all duration-300"></span>
        </a>
      </nav>

      <button 
        @click="isOpen = !isOpen" 
        class="md:hidden relative z-[60] w-10 h-10 flex flex-col justify-center items-center group"
      >
        <span 
          class="block w-8 h-0.5 bg-mist mb-1.5 transition-all duration-300 group-hover:bg-clay"
          :class="{ 'rotate-45 translate-y-2': isOpen }"
        ></span>
        <span 
          class="block w-8 h-0.5 bg-mist mb-1.5 transition-all duration-300 group-hover:bg-clay"
          :class="{ 'opacity-0': isOpen }"
        ></span>
        <span 
          class="block w-8 h-0.5 bg-mist transition-all duration-300 group-hover:bg-clay"
          :class="{ '-rotate-45 -translate-y-2': isOpen }"
        ></span>
      </button>

      <transition
        enter-active-class="transition-all duration-500 ease-out"
        leave-active-class="transition-all duration-500 ease-in"
        enter-from-class="opacity-0 translate-x-full"
        enter-to-class="opacity-100 translate-x-0"
        leave-from-class="opacity-100 translate-x-0"
        leave-to-class="opacity-0 translate-x-full"
      >
        <div 
          v-if="isOpen" 
          class="fixed inset-0 z-50 bg-patagonia bg-opacity-[0.98] h-screen w-screen flex flex-col justify-center items-center"
        >
          
          <nav class="flex flex-col items-center space-y-6">
            <a 
              v-for="link in navLinks" 
              :key="link.name"
              :href="link.href" 
              @click="closeMenu"
              class="font-western text-6xl md:text-8xl uppercase font-black tracking-tight text-transparent text-stroke-mist hover:text-stroke-clay hover:text-clay transition-all duration-300 hover:translate-x-4"
            >
              {{ link.name }}
            </a>
          </nav>

          <div class="absolute bottom-12 flex items-center gap-8">
            <a href="https://www.instagram.com/eze_salgado/" target="_blank" class="text-mist hover:text-clay transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
              </svg>
            </a>
            <a href="#" class="text-mist hover:text-clay transition-colors"> <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z" />
              </svg>
            </a>
          </div>
          
        </div>
      </transition>

    </div>
  </header>
</template>

<style scoped>
/* Truco CSS para el efecto "Outline" (texto hueco con borde).
  Esto hace que las letras gigantes se vean modernas y no tan pesadas en estado normal.
*/
.text-stroke-mist {
  -webkit-text-stroke: 2px rgba(226, 226, 226, 0.8); /* Color Mist con opacidad */
}

.text-stroke-clay {
  -webkit-text-stroke: 2px #CD5D36; /* Color Clay */
}
</style>