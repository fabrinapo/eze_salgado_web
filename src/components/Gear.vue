<script setup lang="ts">
import { ref, reactive, onMounted, onUnmounted } from 'vue';

// DEFINICIÓN DE TIPOS (Para que TypeScript no se queje)
interface GearItem {
  id: number;
  title: string;
  subtitle: string;
  desc: string;
  img: string;        // Imagen principal (thumbnail por defecto)
  gallery?: string[]; // OPCIONAL: Array de imágenes para carrusel
  logo?: string;
  link?: string;
  isSponsor: boolean;
}

const gearItems = ref<GearItem[]>([
  {
    id: 1,
    title: 'Kongsheng Harmonicas',
    subtitle: 'Official Endorser | Since 2022',
    desc: 'Desde 2022 soy endorser de esta innovadora marca. Buscando velocidad y fluidez, desarrollé mi set actual con los modelos Ting Harp, Solist y Lyra.',
    img: '/img/equipacion_armonicas.jpg',
    logo: '/img/logo_kongsheng.png', 
    link: 'https://kongsheng.com',
    isSponsor: true
  },
  {
    id: 2,
    title: 'Amplificación',
    subtitle: 'Fender • Vintage Electric • Marshall',
    desc: 'Armónica: Fender Hot Rod Deluxe o Vintage Ñu Twin/Superlead para un clean absoluto y gain ideal. Guitarra: El mítico Marshall JCM 900 + Caja 1960b con Celestion GB12.',
    img: '/img/equipacion_amplificadores.webp',
    isSponsor: false
  },
  {
    id: 3,
    title: 'Pedalboard & FX',
    subtitle: 'Tono Carlos del Junco Style',
    desc: 'Búsqueda de claridad evitando feedbacks. Proceso digital con Line 6 sumado a ganancia valvular, compresores y Tubescreamer para un sonido potente y moderno.',
    img: 'https://foundsound.com.au/cdn/shop/files/Line_6_POD_XT_LIVE_sku_30068_MPN_3_2048x.jpg?v=1699158846', 
    isSponsor: false
  },
  {
    id: 4,
    title: 'Micrófonos',
    subtitle: 'Vocal & Bullet High-Z',
    desc: 'Voz: Samson Q7. Armónica: El clásico bullet Astatic JT 30 y Shure SM57 para pedales. Alterno con sistemas inalámbricos según la exigencia del show.',
    img: 'https://i.ibb.co/HD0tzps0/unnamed.jpg', 
    isSponsor: false
  },
  {
    id: 5,
    title: 'Guitarras', // Título actualizado
    subtitle: 'Gibson • Fender • Epiphone',
    desc: 'Para la gira junto a Black Cadillacs trio, se usan Stratocaster y Les Paul , para las giras sesionistas de blues podemos encontrar 335 semihollow o Epiphone acústica',
    img: 'https://scontent.fmdq6-1.fna.fbcdn.net/v/t39.30808-6/505374598_10231416287164181_6718101116765171232_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=FK2c832Bgg0Q7kNvwF3a0Mk&_nc_oc=AdkC3qndZxT7Xs_-42D6hVm-GkSGCM44hl9FU_VR5xJFEuGDwokVv8bLHuQBalnttmU&_nc_zt=23&_nc_ht=scontent.fmdq6-1.fna&_nc_gid=qxV1huUly5zwz_0vBhTzdA&oh=00_AfmDG0otWSy-_ATfVb1LyLIrRxnj1g0fB9GknTcFl702EQ&oe=695241D6', // Imagen por defecto si falla el carrusel
    // AQUÍ AGREGAS TUS FOTOS REALES 👇
    gallery: [
      'https://scontent.fmdq6-1.fna.fbcdn.net/v/t39.30808-6/505374598_10231416287164181_6718101116765171232_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=FK2c832Bgg0Q7kNvwF3a0Mk&_nc_oc=AdkC3qndZxT7Xs_-42D6hVm-GkSGCM44hl9FU_VR5xJFEuGDwokVv8bLHuQBalnttmU&_nc_zt=23&_nc_ht=scontent.fmdq6-1.fna&_nc_gid=qxV1huUly5zwz_0vBhTzdA&oh=00_AfmDG0otWSy-_ATfVb1LyLIrRxnj1g0fB9GknTcFl702EQ&oe=695241D6', // Foto 1 (Gibson)
      'https://scontent.fmdq7-1.fna.fbcdn.net/v/t39.30808-6/570418251_10233048668732700_3100859797557091768_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=833d8c&_nc_ohc=qplZ769iBo0Q7kNvwHsJJ7R&_nc_oc=AdlgA_jkNuDgRNmFg4EtMX30mXdWm18lkz-t8fD_Miq1LjIculFnOC2DL-Z0Koyxdeg&_nc_zt=23&_nc_ht=scontent.fmdq7-1.fna&_nc_gid=U70SbzE-zhRDSpPeo3ELcw&oh=00_AfkMhNSH3YtdT-9auDt1R7xo9k79dfuJrqmDms90SF-ung&oe=69524FA3', // Foto 2 (Fender) - REEMPLAZAR
      'https://scontent.fmdq6-1.fna.fbcdn.net/v/t39.30808-6/495577045_10231063881474259_64145070171670476_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=4V9vrksaFIYQ7kNvwFiHWHJ&_nc_oc=AdlD0qSbA0NiT1u8EmTAks1IirniyDkqjxpqvbhOu3tFLKDdP0S8WeMyASEe24Rn7Fo&_nc_zt=23&_nc_ht=scontent.fmdq6-1.fna&_nc_gid=HXv3Qu-3AQ91yqiNzSYnVQ&oh=00_AfnE0PoYiBCYzGz0IO6jQcWYWewNtfW0RSvwtIr6Y57oDg&oe=69522254'             // Foto 3 (Acústica) - REEMPLAZAR
    ],
    isSponsor: false
  }
]);

// --- LÓGICA DEL CARRUSEL ---

// Almacena el índice de la foto activa para cada tarjeta que tenga galería.
// Formato: { id_del_item: indice_foto_actual } -> Ej: { 5: 0 }
const activeIndexes = reactive<Record<number, number>>({});
let intervalId: any;

onMounted(() => {
  // Inicializamos los índices en 0 para los ítems con galería
  gearItems.value.forEach(item => {
    if (item.gallery && item.gallery.length > 1) {
      activeIndexes[item.id] = 0;
    }
  });

  // Iniciamos un temporizador único que actualiza todos los carruseles a la vez
  intervalId = setInterval(() => {
    gearItems.value.forEach(item => {
      if (item.gallery && item.gallery.length > 1) {
        // Avanza al siguiente índice de forma cíclica (0 -> 1 -> 2 -> 0...)
        activeIndexes[item.id] = (activeIndexes[item.id] + 1) % item.gallery.length;
      }
    });
  }, 3500); // Cambia la foto cada 3.5 segundos
});

// Limpiamos el temporizador cuando se desmonta el componente para evitar fugas de memoria
onUnmounted(() => {
  if (intervalId) clearInterval(intervalId);
});
</script>

<template>
  <section id="gear" class="py-24 bg-patagonia relative border-t border-white/5">
    <div class="container mx-auto px-6 max-w-7xl">
      
      <div class="mb-16 text-center">
        <h2 class="font-western text-4xl md:text-6xl text-mist mb-4">Sonido & Equipamiento</h2>
        <p class="text-brass font-sans uppercase tracking-[0.3em] text-xs font-bold">Catálogo Técnico 2024</p>
        <div class="h-px w-24 bg-brass/30 mx-auto mt-6"></div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <article 
          v-for="item in gearItems" 
          :key="item.id" 
          class="group bg-surface/30 border border-white/5 hover:border-brass/30 transition-all duration-300 rounded-sm overflow-hidden flex flex-col h-full"
        >
          
          <div class="relative h-64 overflow-hidden bg-black w-full">
             
             <div class="absolute inset-0 bg-clay/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 z-20 mix-blend-overlay pointer-events-none"></div>
            
            <div v-if="item.isSponsor" class="absolute top-0 left-0 bg-clay text-patagonia text-[10px] font-bold px-3 py-1 uppercase tracking-widest z-30 shadow-md">
              Official Partner
            </div>

            <img 
              v-if="!item.gallery || item.gallery.length === 0"
              :src="item.img" 
              :alt="item.title"
              class="absolute inset-0 w-full h-full object-cover transform transition-transform duration-700 group-hover:scale-110 filter grayscale-[30%] contrast-110 group-hover:grayscale-0 z-0"
            />

            <template v-else>
              <img 
                v-for="(photoUrl, index) in item.gallery"
                :key="photoUrl"
                :src="photoUrl" 
                :alt="item.title + ' ' + index"
                class="absolute inset-0 w-full h-full object-cover transform transition-all duration-[1500ms] ease-in-out group-hover:scale-110 filter grayscale-[30%] contrast-110 group-hover:grayscale-0 will-change-transform will-change-opacity"
                :class="{ 
                  'opacity-100 z-10': activeIndexes[item.id] === index, // Foto activa visible
                  'opacity-0 z-0': activeIndexes[item.id] !== index     // Las demás transparentes
                }"
              />
            </template>

          </div>

          <div class="p-8 flex flex-col flex-grow relative z-30 bg-surface/95">
            
            <div class="flex items-center gap-3 mb-3 h-6">
              <img v-if="item.logo" :src="item.logo" :alt="item.title" class="h-full w-auto object-contain opacity-80 filter brightness-0 invert" />
              <div v-if="item.logo" class="h-3 w-px bg-white/20"></div> 
              <span class="text-clay text-[10px] font-bold uppercase tracking-widest truncate">{{ item.subtitle }}</span>
            </div>

            <h3 class="font-western text-2xl md:text-3xl text-mist mb-4 group-hover:text-brass transition-colors leading-none">
              {{ item.title }}
            </h3>

            <p class="font-sans text-sm text-mist/70 font-light leading-relaxed mb-6 flex-grow border-l border-white/10 pl-4">
              {{ item.desc }}
            </p>

            <div v-if="item.link" class="mt-auto pt-4 border-t border-white/5">
               <a 
                 :href="item.link" 
                 target="_blank" 
                 class="inline-flex items-center text-[10px] font-bold text-brass hover:text-white transition-colors uppercase tracking-widest"
               >
                 Ver Marca
                 <span class="ml-2">→</span>
               </a>
            </div>

          </div>

        </article>

      </div>

    </div>
  </section>
</template>