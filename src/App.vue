<script setup lang="ts">
import { onMounted } from 'vue';
import Lenis from '@studio-freight/lenis'; 

// IMPORTACIÓN DE TODOS LOS COMPONENTES
import NavBar from './components/NavBar.vue';
import Hero from './components/Hero.vue';
import Trajectory from './components/Trajectory.vue'; // <--- AQUÍ ESTÁ EL RESCATADO
import Bio from './components/Bio.vue';
import News from './components/News.vue';
import Shows from './components/Shows.vue';
import Videos from './components/Videos.vue';
import Services from './components/Services.vue';
import Gear from './components/Gear.vue';
import TechRider from './components/TechRider.vue';
import Footer from './components/Footer.vue';

// Smooth Scroll
onMounted(() => {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true
  });
  function raf(time: number) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);
});
</script>

<template>
  <div class="bg-patagonia text-mist font-sans selection:bg-clay selection:text-white relative min-h-screen w-full overflow-x-hidden">
    
    <div class="fixed inset-0 pointer-events-none z-[100] opacity-[0.04] mix-blend-overlay"
         style="background-image: url('https://grainy-gradients.vercel.app/noise.svg');">
    </div>

    <NavBar />

    <main class="relative z-10">
      
      <Hero />
      
      <Trajectory /> 
      
      <Bio />

      <News />
      <Shows />

      <Videos />

      <Services /> 

      <Gear />
      
      <TechRider />

    </main>

    <Footer />

  </div>
</template>

<style>
/* 1. REGLA MAESTRA: PROHIBIDO EL SCROLL HORIZONTAL */
html, body {
  overflow-x: hidden !important;
  width: 100%;
  position: relative;
  margin: 0;
  padding: 0;
}

/* Configuración de Lenis Scroll (ya la tenías, déjala igual) */
html.lenis { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto; }
.lenis.lenis-smooth [data-lenis-prevent] { overscroll-behavior: contain; }
.lenis.lenis-stopped { overflow: hidden; }
</style>