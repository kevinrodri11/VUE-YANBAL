<template>
  <VaCarousel :items="imageUrls" stateful autoscroll infinite>
    <template #default="{ index }">
      <img :src="imageUrls[index]" alt="Slide" class="carousel-image" />
    </template>
  </VaCarousel>
</template>

<script>
export default {
  data() {
    return {
      imageNames: ['cyc_yanbal.jpg', 'JoyeriaYanbal.jpg', 'yanbal_foto.jpg', 'perfm_yanbal.jpg', 'yanbal_prodct.jpg'],
    }
  },
  computed: {
    imageUrls() {
      return this.imageNames.map((name) => `/public/${name}`)
    },
  },
}
</script>

<style lang="scss">
.va-carousel__slide {
  .carousel-image {
    width: 400px; /* O ajusta el tamaño según tus necesidades */
    height: 250px; /* Esto mantiene la proporción de la imagen */
    object-fit: cover; /* Ajusta la imagen para cubrir el contenedor */
  }
}
</style>
