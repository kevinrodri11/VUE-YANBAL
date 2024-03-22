<template>
  <VaCarousel :items="items" stateful autoscroll infinite>
    <template #default="{ index }">
      {{ index + 1 }}
    </template>
  </VaCarousel>
</template>

<script>
export default {
  data() {
    return {
      value: 0,
      items: ['1', '2', '3', '4', '5'],
    }
  },
}
</script>
<style lang="scss">
.va-carousel__slide {
  font-size: 40px;
}
</style>
