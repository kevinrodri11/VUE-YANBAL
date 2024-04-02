<template>
  <div>
    <div class="filter-container">
      <input v-model="filterText" type="text" placeholder="Buscar en la tabla" class="filter-input" />
    </div>
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th>Codigo</th>
            <th>Nombre</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in paginatedItems" :key="index">
            <td>
              <a :href="'/projects/'">{{ item.codigo }}</a>
            </td>
            <td>
              <a :href="'/projects/'">{{ item.nombre }}</a>
            </td>
            <!-- + item.codigo -->
          </tr>
        </tbody>
      </table>
    </div>
    <div class="pagination">
      <button :disabled="currentPage === 1" @click="prevPage">Anterior</button>
      <span>Página {{ currentPage }} de {{ totalPages }}</span>
      <button :disabled="currentPage === totalPages" @click="nextPage">Siguiente</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const itemsPerPage = 5
const currentPage = ref(1)
const filterText = ref('')

const items = ref([
  {
    codigo: '1215561',
    nombre: 'Brety Consultores S.L.',
  },
  {
    codigo: '963',
    nombre: 'Kirk Hayden',
  },
  {
    codigo: '852',
    nombre: 'Greg Cline',
  },
  {
    codigo: '741',
    nombre: 'Melvin Friedman',
  },
  {
    codigo: '951',
    nombre: 'Genaro Waters',
  },
  {
    codigo: '753',
    nombre: 'Wallace Mccullough',
  },
  {
    codigo: '654',
    nombre: 'Alexis Roberson',
  },
  {
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },
  {
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'Salvador Ortiz',
  },{
    codigo: '00000',
    nombre: 'esneider peña',
  },{
    codigo: '00000',
    nombre: 'kevin esne rodriguez',
  },
])
const filteredItems = computed(() => {
  return items.value.filter((item) =>
    Object.values(item).some((field) => field.toString().toLowerCase().includes(filterText.value.toLowerCase())),
  )
})

const totalPages = computed(() => {
  return Math.ceil(filteredItems.value.length / itemsPerPage)
})

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredItems.value.slice(start, end)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}
</script>

<style>
.filter-container {
  margin-bottom: 2px;
}

.filter-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  background-color: #f2f2f2;
}
.table-container {
  max-height: 400px;
  overflow-y: auto;
}
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th,
.table td {
  border: 1px solid #ddd;
  padding: 8px;
}
.table th {
  background-color: #f2f2f2;
  font-weight: bold;
  text-align: left;
}

/* Agrega tus estilos aquí */
.pagination {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.pagination button {
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  background-color: #f2f2f2;
  border: 1px solid #ddd;
}

.pagination button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
