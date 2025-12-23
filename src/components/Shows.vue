<script setup lang="ts">
import { ref, onMounted } from 'vue';

// TU LINK DE GOOGLE SHEETS
const CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQwOwdKKiQ1WaLS9VhnqVTvWk3LcvcwzihY_Vd4-Is6_yz_TlcIBSxJUzsMKEY0Bp0VGeVhfaAT_yZV/pub?gid=0&single=true&output=csv';

// DEFINICIÓN DE TIPOS (Simplificada para evitar errores)
// Quitamos los '?' porque siempre devolveremos un string, aunque sea vacío.
interface Show {
  fecha: string;
  lugar: string;
  ciudad: string;
  link: string;
  estado: string;
}

const shows = ref<Show[]>([]);
const loading = ref(true);
const error = ref(false);

// Función de parseo con Tipado Estricto
const parseCSV = (text: string): Show[] => {
  const rows = text.split('\n').slice(1); // Quitamos encabezado
  
  const parsedRows = rows.map((row) => {
    if (!row.trim()) return null; // Ignorar filas vacías

    // Regex para separar por comas respetando comillas
    const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
    
    // Limpieza de datos
    const cleanCols = cols.map(col => col.replace(/^"|"$/g, '').trim());

    // Creamos el objeto Show asegurando que todo sea string
    return {
      fecha: cleanCols[0] || 'TBA',
      lugar: cleanCols[1] || 'Por confirmar',
      ciudad: cleanCols[2] || '',
      link: cleanCols[3] || '',
      estado: cleanCols[4] || '' 
    };
  });

  // Filtramos los nulos y aseguramos a TS que el resultado es Show[]
  return parsedRows.filter((show): show is Show => show !== null && show.fecha !== 'TBA');
};

onMounted(async () => {
  try {
    const response = await fetch(CSV_URL);
    if (!response.ok) throw new Error('Error al conectar con Google Sheets');
    
    const text = await response.text();
    shows.value = parseCSV(text);
  } catch (e) {
    console.error('Error cargando shows:', e);
    error.value = true;
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <section id="shows" class="py-24 bg-patagonia relative border-t border-white/5 overflow-hidden">
    
    <div class="absolute top-0 right-0 p-4 opacity-[0.03] pointer-events-none select-none">
       <span class="font-western text-[8rem] md:text-[15rem] text-white leading-none">TOUR</span>
    </div>

    <div class="container mx-auto px-6 max-w-5xl relative z-10">
      
      <div class="flex flex-col md:flex-row items-end justify-between mb-16 gap-6 border-b border-brass/30 pb-6">
        <div>
          <span class="text-clay font-bold tracking-[0.2em] uppercase text-sm block mb-2">On The Road</span>
          <h2 class="font-western text-5xl md:text-7xl text-mist">Próximas Fechas</h2>
        </div>
        
        <div class="border border-mist/20 px-4 py-2 rounded-sm bg-surface backdrop-blur-sm">
           <span class="font-mono text-xs text-brass uppercase">Season 2025 / 2026</span>
        </div>
      </div>

      <div v-if="loading" class="text-center py-20">
        <span class="text-brass animate-pulse font-western text-xl">Cargando fechas...</span>
      </div>

      <div v-else-if="error" class="text-center py-10 border border-red-900/50 bg-red-900/10 rounded">
        <p class="text-red-400 font-sans">No se pudieron cargar los shows.</p>
        <p class="text-sm text-red-300/50 mt-2">Verifica la conexión.</p>
      </div>

      <div v-else class="flex flex-col">
        
        <div 
          v-for="(show, index) in shows" 
          :key="index"
          class="group flex flex-col md:flex-row md:items-center py-8 border-b border-white/10 hover:border-clay/50 hover:bg-white/[0.02] transition-all duration-300"
        >
          
          <div class="w-full md:w-1/4 mb-4 md:mb-0">
            <span class="font-western text-4xl text-mist group-hover:text-clay transition-colors block">
              {{ show.fecha }}
            </span>
          </div>

          <div class="w-full md:w-2/4 mb-6 md:mb-0">
            <h3 class="font-sans text-xl font-bold text-mist mb-1 group-hover:text-white transition-colors">
              {{ show.lugar }}
            </h3>
            <div class="flex items-center gap-2">
               <span class="text-clay text-lg">📍</span>
               <span class="text-gray-400 font-light font-sans">{{ show.ciudad }}</span>
            </div>
          </div>

          <div class="w-full md:w-1/4 flex items-center justify-start md:justify-end gap-4">
            
            <span v-if="show.estado" class="font-mono text-[10px] uppercase text-gray-500 border border-white/10 px-2 py-1 rounded-sm">
              {{ show.estado }}
            </span>

            <a 
              v-if="show.link && show.link.startsWith('http')"
              :href="show.link" 
              target="_blank"
              class="bg-brass text-patagonia hover:bg-clay hover:text-white font-bold uppercase text-xs px-6 py-3 transition-colors tracking-widest clip-path-ticket shadow-lg shadow-brass/10"
            >
              Tickets
            </a>
            
            <span v-else class="text-xs text-gray-600 font-bold uppercase tracking-widest cursor-default">
              En Puerta
            </span>
          </div>

        </div>

        <div v-if="shows.length === 0" class="text-center py-16 border border-dashed border-white/10 mt-8 rounded-lg bg-white/5">
          <p class="text-gray-400 font-western text-2xl opacity-50">No hay fechas confirmadas</p>
          <p class="text-sm text-gray-600 mt-2 font-sans">Pronto anunciaremos nuevas fechas.</p>
        </div>

      </div>

    </div>
  </section>
</template>

<style scoped>
.clip-path-ticket {
  clip-path: polygon(5% 0, 100% 0, 100% 100%, 0 100%, 0 20%);
}
</style>