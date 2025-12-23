<script setup lang="ts">
// Bio actualizada con datos del dossier
</script>

<template>
  <section id="bio" class="py-20 md:py-32 bg-patagonia overflow-hidden">
    <div class="container mx-auto px-6">
      
      <div class="flex flex-col md:flex-row items-center gap-12 lg:gap-20">
        
        <div class="w-full md:w-1/2 relative group">
          <div class="absolute top-4 -left-4 w-full h-full border-2 border-brass/30 rounded-sm -z-0 transition-transform duration-500 group-hover:translate-x-2 group-hover:-translate-y-2"></div>
          <img 
            src="/img/eze_salgado_bio2.webp" 
            alt="Ezequiel Salgado" 
            class="relative z-10 w-full h-auto rounded-sm shadow-2xl grayscale group-hover:grayscale-0 transition-all duration-700 object-cover aspect-[4/5]"
          />
        </div>

        <div class="w-full md:w-1/2">
          <span class="text-brass font-sans tracking-[0.2em] text-sm uppercase mb-4 block">Biografía & Trayectoria</span>
          
          <h2 class="font-serif text-4xl md:text-5xl text-moonlight mb-8 leading-tight">
            Del Valle de Río Negro <br/>
            <span class="text-copper italic">a los grandes escenarios.</span>
          </h2>

          <div class="space-y-6 text-moonlight/80 font-sans font-light text-lg leading-relaxed">
            <p>
              Considerado un referente de la armónica a nivel nacional, Ezequiel Salgado ha llevado su sonido desde la Patagonia hasta los festivales más importantes del país.
            </p>
            <p>
              Su versatilidad le ha permitido compartir escenario con leyendas del rock y blues como 
              <strong class="text-white">Ciro y Los Persas, La Mississippi, Vox Dei</strong> y figuras internacionales de Chicago como 
              <strong class="text-white">Tail Dragger y Jimmy Burns</strong>.
            </p>
            <p class="text-sm border-l-2 border-brass pl-4 italic text-gray-400">
              "Precursor en el sur argentino en la armónica diatónica y cromática."
            </p>
          </div>
          
          <div class="mt-10 pt-8 border-t border-surface flex items-center gap-4">
             <span class="font-serif text-2xl text-brass italic">Ezequiel Salgado</span>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>