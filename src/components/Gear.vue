<script setup lang="ts">
import { ref } from 'vue';

const gearItems = ref([
  {
    id: 1,
    title: 'Kongsheng Harmonicas',
    subtitle: 'Main Sponsor | Official Endorser',
    desc: 'La piedra angular de mi sonido. Modelos Bluebird y Solist. Aleación de bronce fosforado para respuesta hermética.',
    img: '/img/equipacion_armonicas.jpg',
    logo: '/img/logo_kongsheng.png',
    link: 'https://kongsheng.com',
    isSponsor: true
  },
  {
    id: 2,
    title: 'Anvil Rock Amps',
    subtitle: 'Amplificación Valvular',
    desc: 'Cabezales 100% valvulares hechos a mano. Configuración clásica con parlantes de 12" para mover el aire necesario.',
    img: '/img/equipacion_amplificadores.jpg',
    logo: '/img/logo_anvil.png',
    isSponsor: true
  },
  {
    id: 3,
    title: 'Guitarras & Resonators',
    subtitle: 'Delta Blues Textures',
    desc: 'Guitarras con cuerdas de acero y resonadores para buscar ese sonido metálico y percusivo del Mississippi primitivo.',
    img: '/img/equipacion_guitarras.webp',
    isSponsor: false
  },
   {
    id: 4,
    title: 'Micrófonos Vintage',
    subtitle: 'Captación High-Z',
    desc: 'Alterno entre cápsulas de cristal antiguas y dinámicos modernos de alta impedancia para lograr el "breakup" correcto.',
    img: '/img/armonicas1.webp', 
    isSponsor: false
  }
]);
</script>

<template>
  <section class="py-24 bg-patagonia relative border-t border-white/5">
    <div class="container mx-auto px-6 max-w-6xl">
      
      <div class="mb-16 text-center">
        <h2 class="font-western text-4xl md:text-6xl text-mist mb-4">Sonido & Equipamiento</h2>
        <p class="text-brass font-sans uppercase tracking-[0.3em] text-xs font-bold">Catálogo Técnico</p>
        <div class="h-px w-24 bg-brass/30 mx-auto mt-6"></div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">
        
        <article 
          v-for="item in gearItems" 
          :key="item.id" 
          class="group bg-surface/30 border border-white/5 hover:border-brass/30 transition-all duration-300 rounded-sm overflow-hidden flex flex-col"
        >
          
          <div class="relative h-64 overflow-hidden">
             <div class="absolute inset-0 bg-clay/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 z-10 mix-blend-overlay"></div>
             
             <img 
              :src="item.img" 
              :alt="item.title"
              class="w-full h-full object-cover transform transition-transform duration-700 group-hover:scale-110 filter grayscale-[30%] contrast-110 group-hover:grayscale-0"
            />
            
            <div v-if="item.isSponsor" class="absolute top-0 left-0 bg-clay text-patagonia text-[10px] font-bold px-3 py-1 uppercase tracking-widest z-20">
              Partner
            </div>
          </div>

          <div class="p-8 flex flex-col flex-grow">
            
            <div class="flex items-center gap-3 mb-4 h-8">
              <img v-if="item.logo" :src="item.logo" :alt="item.title" class="h-full w-auto object-contain opacity-80 filter brightness-0 invert" />
              <div v-if="item.logo" class="h-4 w-px bg-white/20"></div> 
              <span class="text-clay text-[10px] font-bold uppercase tracking-widest self-center">{{ item.subtitle }}</span>
            </div>

            <h3 class="font-western text-3xl text-mist mb-4 group-hover:text-brass transition-colors">
              {{ item.title }}
            </h3>

            <p class="font-sans text-sm text-mist/70 font-light leading-relaxed mb-6 flex-grow">
              {{ item.desc }}
            </p>

            <div v-if="item.link" class="mt-auto pt-4 border-t border-white/5">
               <a 
                 :href="item.link" 
                 target="_blank" 
                 class="inline-flex items-center text-xs font-bold text-brass hover:text-white transition-colors uppercase tracking-widest"
               >
                 Especificaciones
                 <span class="ml-2">→</span>
               </a>
            </div>

          </div>

        </article>

      </div>

    </div>
  </section>
</template>