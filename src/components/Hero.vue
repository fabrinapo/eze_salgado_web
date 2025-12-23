<script setup lang="ts">
const scrollToContact = () => {
  document.getElementById('services')?.scrollIntoView({ behavior: 'smooth' });
};
</script>

<template>
  <section class="relative h-screen w-full flex items-center justify-center overflow-hidden">
    
    <div class="absolute inset-0 z-0">
      <img 
        src="/img/eze_salgado_bio3.webp" 
        alt="Ezequiel Salgado Live"
        class="w-full h-full object-cover object-center"
      />
      <div class="absolute inset-0 bg-patagonia/60 mix-blend-multiply"></div>
      <div class="absolute bottom-0 w-full h-32 bg-gradient-to-t from-patagonia to-transparent"></div>
    </div>

    <div class="relative z-10 container mx-auto px-6 text-center flex flex-col items-center">
      
      <div class="w-24 h-1 bg-brass mb-8 shadow-[0_0_15px_rgba(197,160,101,0.5)]"></div>

      <h1 class="font-western text-5xl md:text-7xl lg:text-9xl text-mist uppercase tracking-wider drop-shadow-xl mb-6">
        Ezequiel<br/>
        <span class="text-clay">Salgado</span>
      </h1>
      
      <p class="font-sans text-xl md:text-2xl text-brass/90 font-bold tracking-[0.2em] uppercase mb-10 border-y border-brass/30 py-4 max-w-2xl">
        Harmonica Player &bull; Patagonia &bull; Blues
      </p>

      <div class="flex flex-col md:flex-row gap-6">
        <button 
          @click="scrollToContact"
          class="bg-clay hover:bg-white text-patagonia font-western text-lg px-10 py-4 rounded-sm border border-transparent shadow-lg shadow-clay/20 transition-all uppercase tracking-widest font-bold"
        >
          Contactar
        </button>
      </div>

    </div>
    
    <div class="absolute bottom-10 animate-bounce">
      <span class="text-brass/50 text-2xl">↓</span>
    </div>

  </section>
</template>