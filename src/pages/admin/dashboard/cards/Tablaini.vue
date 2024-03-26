<template>
  <div class="container">
    <div class="">
      <VaInput v-model="filter" placeholder="Buscar" class="w-full" />
    </div>

    <VaDataTable
      :items="items"
      :columns="filteredColumns"
      :filter="filter"
      :filter-method="customFilteringFn"
      @filtered="filteredCount = $event.items.length"
    />

    <VaAlert class="!mt-6" color="info" outline>
      Numero de filas:
      <VaChip>{{ filteredCount }}</VaChip>
    </VaAlert>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = [
  { id: 1, name: 'dayan' },
  { id: 2, name: 'laura valentina mendez arevalo' },
  { id: 3, name: 'karen juliana moreno ' },
]

const columns = [
  { key: 'id', sortable: true, label: 'Codigo' },
  { key: 'name', sortable: true, label: 'Nombre' },
]

const filteredColumns = ref(columns)

const filter = ref('')
const filteredCount = ref(items.length)

const customFilteringFn = (source) => {
  if (!filter.value) {
    return true
  }

  const filterRegex = new RegExp(filter.value, 'i')
  return filterRegex.test(source)
}
</script>

<style>
.container {
  background-color: white;
  padding: 10px;
}
</style>
