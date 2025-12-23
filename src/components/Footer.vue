<script setup lang="ts">
const currentYear = new Date().getFullYear();
</script>

<template>
  <footer id="contact" class="bg-patagonia border-t border-brass/20 text-mist pt-20 pb-10 relative overflow-hidden">
    
    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent pointer-events-none"></div>

    <div class="container mx-auto px-6 max-w-4xl relative z-10 text-center">
      
      <div class="mb-12">
        <span class="text-clay font-bold tracking-[0.3em] uppercase text-xs block mb-4">Booking & Management</span>
        <h2 class="font-western text-5xl md:text-7xl mb-6">Hablemos de Música</h2>
        <p class="font-sans text-xl text-mist/70 font-light max-w-2xl mx-auto leading-relaxed">
          ¿Buscas clases de armónica, contratar un show o consultoría de equipamiento?
          Estoy disponible para proyectos que tengan alma.
        </p>
      </div>

      <div class="flex flex-col md:flex-row justify-center items-center gap-6 mb-16">
        
        <a 
          href="mailto:ezesalgadook@gmail.com" 
          class="group relative px-10 py-5 bg-brass hover:bg-clay transition-colors duration-300 min-w-[280px]"
        >
          <div class="absolute inset-0 border border-white/20 m-1 pointer-events-none"></div>
          <span class="font-western text-patagonia text-2xl uppercase tracking-widest font-bold group-hover:text-white transition-colors">
            Enviar Correo
          </span>
        </a>

        <a 
          href="#" 
          class="group relative px-10 py-5 bg-transparent border-2 border-mist/20 hover:border-green-500 transition-colors duration-300 min-w-[280px] cursor-pointer"
          onclick="return false;" 
        >
           <span class="font-western text-mist text-2xl uppercase tracking-widest font-bold group-hover:text-green-400 transition-colors">
            WhatsApp
          </span>
        </a>

      </div>

      <div class="border-t border-white/10 pt-12 pb-8">
        <h3 class="text-brass font-sans text-xs font-bold uppercase tracking-[0.2em] mb-8">Sígueme en redes</h3>
        
        <div class="flex flex-wrap justify-center gap-8 md:gap-12 items-center">
          
          <a href="https://www.instagram.com/eze_salgado/" target="_blank" class="flex flex-col items-center group gap-2">
            <div class="w-12 h-12 flex items-center justify-center rounded-full border border-white/10 group-hover:border-clay group-hover:bg-clay/10 transition-all">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-mist group-hover:text-clay transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5" stroke="currentColor" fill="none"/>
                <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z" stroke="currentColor" fill="none"/>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke="currentColor" stroke-width="2"/>
              </svg>
            </div>
            <span class="text-[10px] uppercase tracking-widest text-gray-500 group-hover:text-clay transition-colors">@eze_salgado</span>
          </a>

          <a href="https://www.instagram.com/anvil.rock/" target="_blank" class="flex flex-col items-center group gap-2">
            <div class="w-12 h-12 flex items-center justify-center rounded-full border border-white/10 group-hover:border-brass group-hover:bg-brass/10 transition-all">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-mist group-hover:text-brass transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                 <rect x="2" y="2" width="20" height="20" rx="5" ry="5" stroke="currentColor" fill="none"/>
                <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z" stroke="currentColor" fill="none"/>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke="currentColor" stroke-width="2"/>
              </svg>
            </div>
            <span class="text-[10px] uppercase tracking-widest text-gray-500 group-hover:text-brass transition-colors">@anvil.rock</span>
          </a>

          <a href="https://www.facebook.com/ezequiel.salgado" target="_blank" class="flex flex-col items-center group gap-2">
            <div class="w-12 h-12 flex items-center justify-center rounded-full border border-white/10 group-hover:border-blue-500 group-hover:bg-blue-500/10 transition-all">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-mist group-hover:text-blue-500 transition-colors" viewBox="0 0 24 24" fill="currentColor">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.791-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
            </div>
            <span class="text-[10px] uppercase tracking-widest text-gray-500 group-hover:text-blue-500 transition-colors">Facebook</span>
          </a>

        </div>
      </div>

      <div class="mt-12 text-center border-t border-white/5 pt-8">
        <p class="font-sans text-xs text-gray-600">
          © {{ currentYear }} Ezequiel Salgado. Todos los derechos reservados.
        </p>
        <p class="font-sans text-[10px] text-gray-700 mt-2">
          Design System: Nocturnal Soul
        </p>
      </div>

    </div>
  </footer>
</template>