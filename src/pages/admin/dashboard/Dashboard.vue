<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import Carrusel from './cards/Carrusel.vue';
import Tablainicial from './cards/Tablaini.vue';
import { useToast } from 'vuestic-ui';

const datosTabla = ref([]);
const nombreUsuario = ref('');
const { init } = useToast();

onMounted(() => {
  nombreUsuario.value = localStorage.getItem('nombreUsuario') || 'Usuario';
  getTableData();
});

const getTableData = async () => {
  const usuarioUsuario = localStorage.getItem('usuarioUsuario') || 'Usuario';
  try {
    const response = await fetch(`http://localhost:3000/api/dashboard-data?usuario=${usuarioUsuario}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      init({ message: errorData.message, color: 'error' });
      return;
    }

    const data = await response.json();
    console.log('Response from server:', data); // Verificar la respuesta del servidor

    datosTabla.value = data;

  } catch (error) {
    console.error('Error al obtener datos:', error);
    init({ message: 'Error interno del servidor', color: 'error' });
  }
};
</script>

<template>
  <section class="flex flex-col gap-4">
    <div class="flex flex-col sm:flex-row gap-4">
      <Carrusel />
    </div>
    <h1 class="page-title font-bold">Bienvenid@ {{ nombreUsuario }}</h1>
    <DataSection />
    <div>
      <Tablainicial :datos="datosTabla" />
    </div>
  </section>
</template>
