<script setup lang="ts">
const services = [
  { 
    id: 1, 
    title: 'Harp Power Tour', 
    subtitle: 'Blues Eléctrico & Rock n Roll',
    desc: 'Show de alto impacto para festivales. Un recorrido eléctrico desde versiones de Pappo y ZZ Top hasta el Chicago Blues tradicional.', 
    img: 'https://i.ibb.co/6Rgr7tDx/Black-Cadillacs.jpg',
    cta: 'Ver Rider',
    link: '#rider',
    isPrimary: true // Flag para darle extra peso
  },
  { 
    id: 2, 
    title: 'Gitanos del Sur', 
    subtitle: 'World Music & Tango',
    desc: 'Propuesta acústica, íntima y refinada. Ejecución magistral de armónica cromática interpretando a Piazzolla y folklore argentino.', 
    img: 'https://i.ibb.co/6c39nZXS/Gitanos-del-sur.jpg',
    cta: null
  },
  { 
    id: 3, 
    title: 'Clases & Masterclass', 
    subtitle: 'Online & Presencial',
    desc: 'Formación integral en armónica diatónica y cromática. Desde niveles iniciales hasta técnicas avanzadas para encontrar tu propio tono.', 
    img: '/img/eze_salgado_bio.webp',
    cta: 'Empezar Clases',
    link: '#contact',
    isHighlight: true 
  }
];
</script>

<template>
  <section id="services" class="py-24 bg-patagonia relative overflow-hidden">
    <div class="container mx-auto px-6 md:px-12">
      
      <div class="text-center mb-20">
        <h2 class="font-western text-4xl md:text-6xl text-mist mb-4">Lo que Ofrezco</h2>
        <div class="h-1 w-24 bg-clay mx-auto"></div>
      </div>

      <div class="space-y-24"> 
        
        <article 
          v-for="(service, index) in services" 
          :key="service.id"
          class="flex flex-col md:flex-row items-center gap-12 group"
          :class="{ 'md:flex-row-reverse': index % 2 !== 0 }" 
        >
          <div class="w-full md:w-1/2 relative">
             <div class="relative aspect-square border-4 border-surface shadow-2xl">
               <div class="absolute inset-0 border border-white/10 m-2 z-10 pointer-events-none"></div>
               <img 
                 :src="service.img" 
                 :alt="service.title" 
                 class="w-full h-full object-cover filter contrast-125 saturate-50 group-hover:saturate-100 transition-all duration-700"
               />
             </div>
          </div>

          <div class="w-full md:w-1/2 text-left">
            <span class="text-clay font-bold tracking-widest uppercase text-sm mb-2 block">{{ service.subtitle }}</span>
            
            <h3 class="font-western text-5xl md:text-7xl text-mist mb-6 leading-none font-bold tracking-tight drop-shadow-md">
              {{ service.title }}
            </h3>

            <p class="font-sans text-lg text-mist/80 mb-8 font-light leading-relaxed border-l-2 border-brass/20 pl-6">
              {{ service.desc }}
            </p>
            
            <a 
              v-if="service.cta"
              :href="service.link || '#contact'" 
              class="inline-block px-8 py-3 bg-transparent border-2 border-brass text-brass hover:bg-brass hover:text-patagonia transition-all duration-300 font-sans font-bold uppercase tracking-widest"
              :class="{ 'bg-clay border-clay text-white hover:bg-white hover:text-clay': service.isHighlight }"
            >
              {{ service.cta }}
            </a>
          </div>

        </article>

      </div>
    </div>
  </section>
</template>