<script setup lang="ts">
import { ref, onMounted } from 'vue';

// --- CONFIGURACIÓN ---
const SHEET_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQwOwdKKiQ1WaLS9VhnqVTvWk3LcvcwzihY_Vd4-Is6_yz_TlcIBSxJUzsMKEY0Bp0VGeVhfaAT_yZV/pub?gid=380682145&single=true&output=csv';

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

// --- MANEJO DE ERRORES DE IMAGEN (El fix de TypeScript) ---
const handleImageError = (event: Event) => {
  // Le decimos a TS que el target es efectivamente una etiqueta IMG
  const imgElement = event.target as HTMLImageElement;
  if (imgElement) {
    // Ponemos la imagen de respaldo
    imgElement.src = 'https://placehold.co/600x400/101010/CD5D36?text=Ver+Noticia';
  }
};

// --- LÓGICA DE DATOS ---

const fetchMetadata = async (item: NewsItem) => {
  try {
    const response = await fetch(`https://api.microlink.io/?url=${encodeURIComponent(item.link)}`);
    const data = await response.json();

    if (data.status === 'success') {
      const info = data.data;
      item.title = info.title || 'Nueva fecha confirmada';
      item.source = info.publisher || new URL(item.link).hostname.replace('www.', '');

      if (info.image && info.image.url) {
        item.image = info.image.url;
      } else {
        item.image = `https://api.microlink.io/?url=${encodeURIComponent(item.link)}&screenshot=true&meta=false&embed=screenshot.url`;
      }
    }
  } catch (e) {
    console.error('Error obteniendo info de:', item.link);
  } finally {
    item.loading = false;
  }
};

const parseCSV = (csvText: string) => {
  const lines = csvText.split('\n');
  const items: NewsItem[] = [];
  
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;
    const cols = line.split(','); 
    if (cols.length >= 2) {
      const cleanLink = cols[1]?.trim() || '#';
      items.push({
        id: i,
        date: cols[0]?.trim() || '',       
        link: cleanLink,
        title: 'Cargando información...',
        source: 'Prensa',
        image: 'https://placehold.co/600x400/111111/333333?text=Cargando...', 
        loading: true
      });
    }
  }
  return items;
};

onMounted(async () => {
  try {
    const response = await fetch(SHEET_URL);
    const text = await response.text();
    newsList.value = parseCSV(text);
    isLoadingInitial.value = false;
    newsList.value.forEach(item => fetchMetadata(item));
  } catch (error) {
    console.error('Error cargando Sheet:', error);
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
            <a :href="item.link" target="_blank" class="block w-full h-full">
              
              <img 
                :src="item.image" 
                alt="Portada noticia"
                class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110 opacity-90 group-hover:opacity-100"
                loading="lazy"
                @error="handleImageError"
              />
              
              <div class="absolute inset-0 bg-white/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            </a>
          </div>

          <div class="p-6 flex flex-col flex-grow relative bg-[#0a0a0a]">
            
            <div class="flex justify-between items-center mb-3">
              <span class="text-brass text-[10px] font-bold uppercase tracking-widest bg-brass/10 px-2 py-1 rounded">
                {{ item.date }}
              </span>
              <span class="text-gray-500 text-[10px] uppercase tracking-widest truncate max-w-[120px]">
                {{ item.source }}
              </span>
            </div>

            <h3 class="font-western text-xl text-mist mb-4 leading-tight group-hover:text-clay transition-colors min-h-[3rem] line-clamp-3">
              <a :href="item.link" target="_blank">
                <span v-if="item.loading && item.title === 'Cargando información...'" class="animate-pulse text-gray-600">
                  Buscando info...
                </span>
                <span v-else>{{ item.title }}</span>
              </a>
            </h3>

            <div class="mt-auto pt-4 border-t border-white/5">
              <a 
                :href="item.link" 
                target="_blank"
                class="inline-flex items-center text-[10px] font-bold text-gray-500 hover:text-white transition-colors uppercase tracking-widest"
              >
                Leer Nota Completa
                <span class="ml-2 group-hover:translate-x-1 transition-transform">→</span>
              </a>
            </div>
          </div>

        </article>

      </div>

    </div>
  </section>
</template>