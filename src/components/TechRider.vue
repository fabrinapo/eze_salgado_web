<script setup lang="ts">
import { ref } from 'vue';

// Estado para controlar la visibilidad
const isOpen = ref(false);

const toggleRider = () => {
  isOpen.value = !isOpen.value;
};

// Datos del Rider (Input List)
const inputList = [
  { ch: 1, instrument: 'Voz Principal', mic: 'Shure SM58 / Beta 58', stand: 'Boom Stand' },
  { ch: 2, instrument: 'Armónica (Amp Mic)', mic: 'Shure SM57 / Sennheiser e609', stand: 'Short Boom' },
  { ch: 3, instrument: 'Armónica (Línea)', mic: 'XLR Direct Out (Desde Pedalera)', stand: '-' },
];

const monitors = [
  "Mezcla independiente para armónica.",
  "Necesito escuchar mi señal con efecto (Wet) en monitores.",
  "Buen nivel de Guitarra y Voz principal en mi mezcla."
];
</script>

<template>
  <section id="rider" class="py-24 bg-patagonia border-t border-white/5 relative overflow-hidden">
    
    <div class="container mx-auto px-6 max-w-4xl relative z-10">
      
      <div class="text-center">
        <span class="text-clay font-bold tracking-[0.2em] uppercase text-xs block mb-4">Solo para Sonidistas</span>
        <h2 class="font-western text-4xl md:text-6xl text-mist mb-8">Rider Técnico</h2>
        
        <button 
          @click="toggleRider"
          class="group inline-flex items-center gap-4 px-8 py-4 bg-transparent border border-brass text-brass hover:bg-brass hover:text-patagonia transition-all duration-300 uppercase tracking-widest font-bold text-xs md:text-sm rounded-sm"
        >
          <span>{{ isOpen ? 'Ocultar Especificaciones' : 'Ver Especificaciones Técnicas' }}</span>
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke-width="2" 
            stroke="currentColor" 
            class="w-4 h-4 transition-transform duration-300"
            :class="{ 'rotate-180': isOpen }"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
          </svg>
        </button>
      </div>

      <transition 
        enter-active-class="transition-all duration-500 ease-out overflow-hidden"
        leave-active-class="transition-all duration-300 ease-in overflow-hidden"
        enter-from-class="max-h-0 opacity-0 translate-y-4"
        enter-to-class="max-h-[1000px] opacity-100 translate-y-0"
        leave-from-class="max-h-[1000px] opacity-100 translate-y-0"
        leave-to-class="max-h-0 opacity-0 translate-y-4"
      >
        <div v-show="isOpen" class="mt-16 text-left border-t border-white/10 pt-12">
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
            
            <div>
              <h3 class="font-western text-2xl text-mist mb-6 border-l-4 border-clay pl-4">Input List</h3>
              <div class="overflow-x-auto">
                <table class="w-full text-left text-sm font-sans text-gray-400">
                  <thead class="text-brass uppercase text-[10px] tracking-widest border-b border-white/10">
                    <tr>
                      <th class="py-2 pr-4">CH</th>
                      <th class="py-2 px-2">Instrumento</th>
                      <th class="py-2 px-2">Mic Sugerido</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-white/5">
                    <tr v-for="item in inputList" :key="item.ch" class="hover:bg-white/5 transition-colors">
                      <td class="py-3 pr-4 font-mono text-clay">{{ item.ch }}</td>
                      <td class="py-3 px-2 font-bold text-mist">{{ item.instrument }}</td>
                      <td class="py-3 px-2">{{ item.mic }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div>
              <h3 class="font-western text-2xl text-mist mb-6 border-l-4 border-clay pl-4">Monitoreo & Stage</h3>
              <ul class="space-y-4">
                <li v-for="(req, i) in monitors" :key="i" class="flex items-start gap-3 text-gray-400 text-sm leading-relaxed">
                  <span class="text-brass mt-1">➤</span>
                  <span>{{ req }}</span>
                </li>
              </ul>

              <div class="mt-8 p-4 border border-brass/20 bg-brass/5 rounded-sm">
                <p class="text-brass text-xs font-bold uppercase tracking-widest mb-2">⚡ Energía</p>
                <p class="text-gray-400 text-xs">
                  Se requiere 1 tomacorriente (220v) al pie del amplificador con toma a tierra verificada.
                </p>
              </div>
            </div>

          </div>

          <div class="mt-12 text-center pt-8 border-t border-white/5">
             <a href="#" class="inline-block text-xs font-bold text-gray-500 hover:text-white border-b border-transparent hover:border-white transition-all uppercase tracking-widest">
               Descargar Rider en PDF
             </a>
          </div>

        </div>
      </transition>

    </div>
  </section>
</template>