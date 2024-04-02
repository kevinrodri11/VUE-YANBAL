<script lang="ts" setup>
import Carrusel from './cards/Carrusel.vue'
import Tablainicial from './cards/Tablaini.vue'
</script>

<template>
  <section class="flex flex-col gap-4">
    <div class="flex flex-col sm:flex-row gap-4">
      <Carrusel />
    </div>
    <h1 class="page-title font-bold">Bienvenid@ {name_user}</h1>
    <DataSection />
    <div>
      <Tablainicial />
    </div>
  </section>
</template>
