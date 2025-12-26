<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface NewsItem {
  id: number;
  date: string;
  link: string;
  title: string;
  source: string;
  image: string;
  loading: boolean;
}

const newsList = ref<NewsItem[]>([]);
const isLoadingInitial = ref(true);

// TU LINK DE GOOGLE SHEET (Formato CSV)
const SHEET_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQwOwdKKiQ1WaLS9VhnqVTvWk3LcvcwzihY_Vd4-Is6_yz_TlcIBSxJUzsMKEY0Bp0VGeVhfaAT_yZV/pub?gid=380682145&single=true&output=csv';

// 1. FUNCIÓN DE OPTIMIZACIÓN (Mantiene el SEO alto)
const optimizeImage = (url: string) => {
  if (!url) return 'https://placehold.co/600x400/1a1a1a/CD5D36?text=Cargando...';
  if (url.startsWith('/') || url.includes('ezesalgado.com')) return url;
  return `https://wsrv.nl/?url=${encodeURIComponent(url)}&w=600&q=80&output=webp`;
};

// 2. PARSEADOR ADAPTADO A TU EXCEL (2 Columnas: Fecha, Link)
const parseCSV = (csvText: string) => {
  const lines = csvText.split('\n');
  const items: NewsItem[] = [];
  
  // Saltamos la fila 0 (encabezados)
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;

    // Separamos por comas. 
    // Columna A (0) = Fecha
    // Columna B (1) = Link
    const cols = line.split(',').map(c => c.trim());

    if (cols.length >= 2) {
      items.push({
        id: i,
        date: cols[0] || '',       
        link: cols[1] || '#',
        // Datos temporales mientras cargamos la info real
        title: 'Cargando noticia...',
        source: '...',
        image: '', 
        loading: true
      });
    }
  }
  return items;
};

// 3. RECUPERAR METADATOS (Magia automática)
const fetchMetadata = async (item: NewsItem) => {
  try {
    // Usamos Microlink para "leer" la noticia y sacar foto/título
    const response = await fetch(`https://api.microlink.io/?url=${encodeURIComponent(item.link)}`);
    const data = await response.json();

    if (data.status === 'success') {
      item.title = data.data.title || 'Noticia sin título';
      item.source = data.data.publisher || new URL(item.link).hostname.replace('www.', '');
      // Si Microlink encuentra foto, la usamos. Si no, una genérica.
      item.image = data.data.image?.url || 'https://placehold.co/600x400/101010/CD5D36?text=News';
    }
  } catch (e) {
    console.error('Error al leer metadatos:', e);
    item.title = 'Ver Noticia';
  } finally {
    item.loading = false;
  }
};

// 4. CARGA DE DATOS
onMounted(async () => {
  try {
    const response = await fetch(SHEET_URL);
    const text = await response.text();
    const items = parseCSV(text);
    newsList.value = items;
    isLoadingInitial.value = false;

    // Disparamos la búsqueda de info para cada noticia en segundo plano
    items.forEach(item => fetchMetadata(item));

  } catch (error) {
    console.error('Error cargando sheet:', error);
    isLoadingInitial.value = false;
  }
});
</script>

<template>
  <section id="videos" class="py-24 bg-patagonia relative border-t border-white/5">
    
    <div class="container mx-auto px-6 max-w-7xl">
      
      <div class="mb-16 text-center">
        <h2 class="font-western text-4xl md:text-6xl text-mist mb-4">Prensa & Novedades</h2>
        <p class="text-brass font-sans uppercase tracking-[0.3em] text-xs font-bold">Últimas Noticias</p>
        <div class="h-px w-24 bg-brass/30 mx-auto mt-6"></div>
      </div>

      <div v-if="isLoadingInitial" class="text-center py-12">
        <div class="inline-block w-8 h-8 border-2 border-brass border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <article 
          v-for="item in newsList" 
          :key="item.id" 
          class="group bg-surface/30 border border-white/5 hover:border-brass/30 transition-all duration-300 flex flex-col h-full rounded-sm overflow-hidden"
        >
          
          <div class="relative h-60 overflow-hidden bg-black">
            <a :href="item.link" target="_blank" class="block w-full h-full cursor-pointer">
              
              <div v-if="item.loading" class="w-full h-full bg-white/5 animate-pulse"></div>

              <img 
                v-else
                :src="optimizeImage(item.image)" 
                :alt="item.title"
                loading="lazy"
                class="w-full h-full object-cover transform transition-transform duration-700 group-hover:scale-110 filter grayscale-[30%] group-hover:grayscale-0"
              />
              
              <div class="absolute inset-0 bg-clay/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300 mix-blend-overlay"></div>
            </a>
          </div>

          <div class="p-6 flex flex-col flex-grow relative">
            
            <div class="flex justify-between items-center mb-3">
              <span class="text-brass text-[10px] font-bold uppercase tracking-widest">{{ item.date }}</span>
              <span class="text-gray-500 text-[10px] uppercase tracking-widest truncate max-w-[120px]">
                {{ item.loading ? '...' : item.source }}
              </span>
            </div>

            <h3 class="font-western text-xl text-mist mb-4 leading-tight group-hover:text-clay transition-colors min-h-[3rem]">
              <a :href="item.link" target="_blank">
                <span v-if="item.loading" class="block h-6 w-3/4 bg-white/10 animate-pulse rounded"></span>
                <span v-else>{{ item.title }}</span>
              </a>
            </h3>

            <div class="mt-auto pt-4 border-t border-white/5">
              <a 
                :href="item.link" 
                target="_blank"
                class="inline-flex items-center text-[10px] font-bold text-gray-500 hover:text-white transition-colors uppercase tracking-widest"
              >
                Leer Nota
                <span class="ml-2">→</span>
              </a>
            </div>
          </div>

        </article>

      </div>

    </div>
  </section>
</template>