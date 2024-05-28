<template>
  <div>
    <h1 class="page-title">Resultado de tu búsqueda...</h1>
    <section class="volver-section">
      <button class="volver" @click="goBack">Volver a consultar</button>
    </section>
    <div class="filter-container">
      <input v-model="filterText" type="text" placeholder="Buscar en la tabla" class="filter-input" />
    </div>
    <div class="table-container" v-if="project && project.length > 0">
      <table class="table">
        <thead>
          <tr>
            <th>Fecha de Gestión</th>
            <th>Nombre de la Consultora</th>
            <th>Factura en Mora</th>
            <th>Saldo en Mora</th>
            <th>Días en Mora</th>
            <th>Tipificación</th>
            <th>Fecha de acuerdo</th>
            <th>Valor de acuerdo</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in filteredItems" :key="index">
            <td>{{ item.fecha_gestion }}</td>
            <td>{{ item.nombre }}</td>
            <td>{{ item.factura }}</td>
            <td>{{ item.valor_total_al_dia }}</td>
            <td>{{ item.dias_mora_inicial }}</td>
            <td>{{ item.perfil }}</td>
            <td>{{ item.fecha_promesa }}</td>
            <td>{{ item.valor_promesa }}</td>
            <td>{{ item.descripcion }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="selectedClient" class="client-details">
      <div class="client-details-content">
        <h4><b>TIPIFICACION:</b></h4>
        <br />
        <p><strong>Fecha de Gestión:</strong> {{ selectedClient.fecha_gestion }}</p>
        <p><strong>Nombre de la Consultora:</strong> {{ selectedClient.nombre_consultora }}</p>
        <p><strong>Factura en Mora:</strong> {{ selectedClient.factura_en_mora }}</p>
        <p><strong>Saldo en Mora:</strong> {{ selectedClient.saldo_en_mora }}</p>
        <p><strong>Días en Mora:</strong> {{ selectedClient.dias_en_mora }}</p>
        <button class="close-button" @click="hideClientDetails">Cerrar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const project = ref(null)

const fetchProjectDetails = async (id) => {
  try {
    const response = await fetch(`http://localhost:3000/api/projects/${id}`)
    const data = await response.json()
    project.value = data
    console.log(project)
  } catch (error) {
    console.error('Error al obtener detalles del proyecto:', error)
  }
}

const selectedClient = ref(null)

const hideClientDetails = () => {
  selectedClient.value = null
}

const goBack = () => {
  router.push('/dashboard')
}

const filterText = ref('')
const filteredItems = computed(() => {
  return project.value.filter((item) =>
    Object.values(item).some((field) => field.toString().toLowerCase().includes(filterText.value.toLowerCase())),
  )
})

onMounted(() => {
  const projectId = route.params.id
  if (projectId) {
    fetchProjectDetails(projectId)
  }
})
</script>

<style>
.volver-section {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  padding: 20px;
}
.volver {
  height: 47px;
  padding: 10px 20px;
  background-color: #ffa05c;
  color: #fff;
  cursor: pointer;
  text-align: center;
  border-radius: 5px;
}
/* Estilos para el filtro */
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
.button {
  padding: 5px 10px;
  background-color: #ffa05c;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}
h4 {
  color: black;
  text-align: center;
  font-size: large;
}
.client-details {
  width: 600px;
  height: 270px;
  position: fixed;
  top: 35%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  border: 2px solid #ccc;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
}
.client-details-content {
  text-align: left;
  padding: 7%;
}
.close-button {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #ffa05c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
