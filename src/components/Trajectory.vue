<script setup lang="ts">
// Lineup actualizado con todos los invitados del Dossier
const lineup = [
  // HEADLINERS (Nivel Estadio/Masivo)
  { 
    id: 1, 
    role: 'Telonero de', 
    name: 'CIRO Y LOS PERSAS', 
    size: 'giant' 
  },
  { 
    id: 2, 
    role: 'Invitado de', 
    name: 'LA MISSISSIPPI', 
    size: 'giant' 
  },
  
  // LEGENDS (Nivel Leyenda del Rock)
  { 
    id: 3, 
    role: 'Invitado de', 
    name: 'VOX DEI', 
    size: 'mid' 
  },
  { 
    id: 4, 
    role: 'Invitado de', 
    name: 'WILLY QUIROGA', 
    size: 'mid' 
  },
  
  // BLUES MASTERS (Referentes del género)
  { 
    id: 5, 
    role: 'Invitado de', 
    name: 'LUIS ROBINSON', 
    size: 'mid' 
  },
  { 
    id: 6, 
    role: 'Invitado de', 
    name: 'DANIEL RAFFO', 
    size: 'mid' 
  },

  // FESTIVALES & HITOS
  { 
    id: 7, 
    name: 'FIESTA NACIONAL DE LA MANZANA', 
    size: 'small' 
  },
  { 
    id: 8, 
    name: 'FESTIVAL INT. DE BLUES (CHILE)', 
    size: 'small' 
  },
  { 
    id: 9, 
    name: 'FESTIVAL KONGSHENG', 
    size: 'small' 
  }
];
</script>

<template>
  <section class="py-16 bg-surface border-y border-brass/20 relative overflow-hidden">
    
    <div class="absolute inset-0 opacity-[0.05]" 
         style="background-image: url('https://www.transparenttextures.com/patterns/stardust.png');">
    </div>

    <div class="container mx-auto px-4 relative z-10 text-center">
      
      <div class="mb-12 flex items-center justify-center gap-4 opacity-70">
        <div class="h-px w-8 bg-brass"></div>
        <span class="font-sans text-[10px] md:text-xs uppercase tracking-[0.5em] text-brass">
          Official Line Up History
        </span>
        <div class="h-px w-8 bg-brass"></div>
      </div>

      <div class="flex flex-wrap justify-center items-end gap-x-8 gap-y-6 max-w-6xl mx-auto leading-none">
        
        <div 
          v-for="item in lineup" 
          :key="item.id"
          class="flex flex-col items-center group relative p-2"
        >
          <span 
            v-if="item.role" 
            class="font-sans text-[9px] md:text-[10px] uppercase tracking-widest text-clay mb-2 opacity-80 group-hover:opacity-100 transition-opacity font-bold"
          >
            {{ item.role }}
          </span>

          <span 
            class="font-western text-mist group-hover:text-white transition-all duration-300 text-center drop-shadow-md break-words max-w-[90vw]"
             :class="{
              'text-4xl md:text-6xl lg:text-7xl font-bold tracking-tighter opacity-100 py-2': item.size === 'giant',
              'text-2xl md:text-4xl tracking-tight opacity-90': item.size === 'mid',
              'text-lg md:text-xl tracking-widest opacity-60 font-sans font-bold uppercase': item.size === 'small'
            }"
          >
            {{ item.name }}
          </span>
          
          <div class="w-0 group-hover:w-full h-px bg-clay mt-1 transition-all duration-500 opacity-50"></div>
        </div>

      </div>
      
      <div class="mt-16 opacity-40">
        <p class="font-western text-sm text-mist tracking-widest">
          Patagonia &bull; Blues &bull; Rock Nacional
        </p>
      </div>

    </div>
  </section>
</template>