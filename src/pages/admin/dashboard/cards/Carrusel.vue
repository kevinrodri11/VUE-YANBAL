<template>
  <div class="carousel-container">
    <div class="image-container">
      <img :src="images[currentImageIndex]" alt="Imagen de carrusel" class="carousel-image" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const images = ref([
  '/public/cyc_yanbal.jpg',
  '/public/JoyeriaYanbal.jpg',
  '/public/yanbal_foto.jpg',
  '/public/perfm_yanbal.jpg',
  '/public/yanbal_prodct.jpg',
])

const currentImageIndex = ref(0)

const nextImage = () => {
  currentImageIndex.value = (currentImageIndex.value + 1) % images.value.length
}

let intervalId = null

onMounted(() => {
  intervalId = setInterval(nextImage, 5000)
})

onUnmounted(() => {
  clearInterval(intervalId)
})
</script>

<style>
.carousel-container {
  max-width: 600px; /* Ajusta este valor según tus necesidades */
  margin: auto;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.image-container {
  width: 100%;
  height: 400px; /* Ajusta este valor según tus necesidades */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.carousel-image {
  width: 100%; /* Hace que la imagen se extienda para cubrir el ancho del contenedor */
  height: 100%; /* Hace que la imagen se extienda para cubrir el alto del contenedor */
  object-fit: cover; /* Asegura que la imagen se ajuste de forma atractiva dentro del contenedor sin deformarse */
}
</style>
