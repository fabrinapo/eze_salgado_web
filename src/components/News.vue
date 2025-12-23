<script setup lang="ts">
import { ref, onMounted } from 'vue';

// LINK DE GOOGLE SHEET (Pestaña Noticias)
const CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQwOwdKKiQ1WaLS9VhnqVTvWk3LcvcwzihY_Vd4-Is6_yz_TlcIBSxJUzsMKEY0Bp0VGeVhfaAT_yZV/pub?gid=380682145&single=true&output=csv';

// INTERFAZ ESTRICTA
interface NewsItem {
  date: string;
  originalLink: string;
  title: string;
  description: string;
  image: string;
  publisher: string;
  loading: boolean;
}

const news = ref<NewsItem[]>([]);
const mainLoading = ref(true);

const parseCSV = (text: string): NewsItem[] => {
  const rows = text.split('\n').slice(1);
  const mappedRows = rows.map((row) => {
    // Parser que respeta comas dentro de comillas
    const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/).map(c => c.replace(/^"|"$/g, '').trim());
    
    if (!cols[1] || !cols[1].startsWith('http')) return null;

    return {
      date: cols[0] || 'Reciente',
      originalLink: cols[1],
      title: '',             
      description: '',       
      publisher: '',        
      loading: true, // Nace cargando
      image: '/img/eze_salgado_bio.webp' // Placeholder inicial
    };
  });
  return mappedRows.filter((n): n is NewsItem => n !== null);
};

const fetchMetadata = async (item: NewsItem) => {
  try {
    // Usamos Microlink para obtener foto y título
    const apiUrl = `https://api.microlink.io?url=${encodeURIComponent(item.originalLink)}`;
    const res = await fetch(apiUrl);
    const json = await res.json();
    
    if (json.status === 'success') {
      const data = json.data;
      item.title = data.title || 'Nueva Publicación';
      item.description = data.description || '';
      // Si el link trae imagen, la usamos. Si no, dejamos la del músico.
      item.image = data.image?.url || item.image; 
      item.publisher = data.publisher || '';
    } else {
      item.title = 'Leer Noticia';
      item.description = 'Haz clic para ver el contenido completo.';
    }
  } catch (e) {
    console.error('Error fetching preview:', e);
    item.title = 'Nota de Prensa';
  } finally {
    // ¡AQUÍ ESTÁ LA CLAVE! Al poner esto en false, Vue quita el esqueleto y muestra el texto.
    item.loading = false; 
  }
};

onMounted(async () => {
  try {
    const res = await fetch(CSV_URL);
    const text = await res.text();
    
    // 1. Guardamos los datos en la variable reactiva
    news.value = parseCSV(text);
    
    // 2. CORRECCIÓN: Iteramos sobre 'news.value' (la versión reactiva) 
    // para que Vue detecte los cambios cuando llegue la info de Microlink.
    news.value.forEach(item => fetchMetadata(item));
    
  } catch (e) { 
    console.error(e); 
  } finally { 
    mainLoading.value = false; 
  }
});
</script>

<template>
  <section id="news" class="py-24 bg-surface relative overflow-hidden">
    <div class="container mx-auto px-6 max-w-6xl">

      <div class="flex items-end justify-between mb-12 border-b border-white/5 pb-6">
        <div>
          <span class="text-clay font-bold tracking-widest uppercase text-sm block mb-2">Prensa & Blog</span>
          <h2 class="font-western text-4xl md:text-6xl text-mist">Últimas Novedades</h2>
        </div>
      </div>

      <div v-if="mainLoading" class="text-center text-brass font-western">Buscando enlaces...</div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article 
          v-for="(item, i) in news" 
          :key="i"
          class="group bg-patagonia rounded-sm border border-transparent hover:border-brass/30 transition-all flex flex-col h-full overflow-hidden hover:-translate-y-1 duration-500 shadow-lg"
        >
          <div class="h-48 overflow-hidden relative bg-black">
            
            <div v-if="item.loading" class="absolute inset-0 bg-white/10 animate-pulse z-20"></div>
            
            <img 
              :src="item.image" 
              :alt="item.title" 
              class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 opacity-90 group-hover:opacity-100"
              :class="{ 'opacity-0': item.loading }" 
            >
            
            <div class="absolute top-0 right-0 bg-clay text-patagonia text-xs font-bold px-3 py-1 font-mono z-30">
              {{ item.date }}
            </div>
          </div>

          <div class="p-6 flex flex-col flex-grow relative">
            
            <span v-if="!item.loading && item.publisher" class="text-brass/60 text-[10px] uppercase tracking-widest mb-2 font-bold block">
              {{ item.publisher }}
            </span>
            
            <div v-if="item.loading" class="space-y-3 mb-4">
               <div class="h-4 bg-white/10 rounded w-3/4 animate-pulse"></div>
               <div class="h-3 bg-white/5 rounded w-full animate-pulse"></div>
               <div class="h-3 bg-white/5 rounded w-2/3 animate-pulse"></div>
            </div>
            
            <div v-else>
              <h3 class="font-western text-xl text-mist mb-3 leading-tight group-hover:text-clay transition-colors line-clamp-2">
                {{ item.title }}
              </h3>
              <p class="font-sans text-sm text-gray-400 mb-6 line-clamp-3 font-light leading-relaxed">
                {{ item.description }}
              </p>
            </div>
            
            <div class="mt-auto pt-4 border-t border-white/5">
              <a :href="item.originalLink" target="_blank" class="flex items-center text-xs font-bold text-mist hover:text-white uppercase tracking-widest transition-colors">
                Leer Nota
                <span class="ml-2 group-hover:translate-x-1 transition-transform">→</span>
              </a>
            </div>
          </div>
        </article>
      </div>

    </div>
  </section>
</template>