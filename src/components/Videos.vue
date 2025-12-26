<script setup lang="ts">
import { ref, onMounted } from 'vue';

// LINK DE GOOGLE SHEET (Pestaña Videos)
const CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQwOwdKKiQ1WaLS9VhnqVTvWk3LcvcwzihY_Vd4-Is6_yz_TlcIBSxJUzsMKEY0Bp0VGeVhfaAT_yZV/pub?gid=1201720570&single=true&output=csv';

interface Video {
  title: string;
  youtubeId: string;
}

const videos = ref<Video[]>([]);
const loading = ref(true);

const getYouTubeID = (url: string) => {
  if (!url) return null;
  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
  const match = url.match(regExp);
  return (match && match[2].length === 11) ? match[2] : null;
};

const parseCSV = (text: string) => {
  const rows = text.split('\n').slice(1);
  return rows.map(row => {
    const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/).map(c => c.replace(/^"|"$/g, '').trim());
    const title = cols[0] || 'Sin título';
    const link = cols[1] || '';
    const id = getYouTubeID(link);
    if (!id) return null;
    return { title, youtubeId: id };
  }).filter((v): v is Video => v !== null);
};

onMounted(async () => {
  try {
    const res = await fetch(CSV_URL);
    const text = await res.text();
    videos.value = parseCSV(text);
  } catch (e) {
    console.error('Error cargando videos:', e);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <section id="videos" class="py-24 bg-patagonia border-t border-white/5">
    <div class="container mx-auto px-6">
      
      <div class="text-center mb-16">
        <h2 class="font-western text-4xl md:text-6xl text-mist mb-4">Videos & Shows</h2>
        <div class="h-1 w-24 bg-clay mx-auto"></div>
      </div>

      <div v-if="loading" class="text-center text-brass font-western animate-pulse">Cargando videos...</div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article v-for="(video, i) in videos" :key="i" class="group">
          
          <div class="relative aspect-video bg-black rounded-sm overflow-hidden border border-white/10 group-hover:border-clay transition-colors shadow-2xl">
            <iframe 
              class="w-full h-full"
              :src="`https://www.youtube.com/embed/${video.youtubeId}?preload=none`" 
              title="YouTube video player" 
              width="560" 
              height="315"
              loading="lazy"
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen
            ></iframe>
          </div>
          
          <h3 class="mt-4 font-western text-xl text-mist group-hover:text-clay transition-colors text-center">
            {{ video.title }}
          </h3>
          
        </article>
      </div>

    </div>
  </section>
</template>