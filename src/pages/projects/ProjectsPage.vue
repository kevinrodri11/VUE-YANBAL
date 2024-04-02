<template>
  <div>
    <h1 class="page-title">Resultado de tu búsqueda...</h1>
    <section class="volver-section">
      <button class="volver" @click="goBack">Volver a consultar</button>
    </section>
    <div class="filter-container">
      <input v-model="filterText" type="text" placeholder="Buscar en la tabla" class="filter-input" />
    </div>
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th>Fecha de Gestión</th>
            <th>Nombre de la Consultora</th>
            <th>Factura en Mora</th>
            <th>Saldo en Mora</th>
            <th>Días en Mora</th>
            <th>Tipificacion</th>
            <th>Fecha de acuerdo</th>
            <th>Valor de acuerdo</th>
            <th>Accion</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in filteredItems" :key="index">
            <td>{{ item.fecha_gestion }}</td>
            <td>{{ item.nombre_consultora }}</td>
            <td>{{ item.factura_en_mora }}</td>
            <td>{{ item.saldo_en_mora }}</td>
            <td>{{ item.dias_en_mora }}</td>
            <td><button class="button" @click="showClientDetails(item)">Ver+</button></td>
            <td>{{ item.fecha_acuerdo }}</td>
            <td>{{ item.valor_acuerdo }}</td>
            <td>{{ item.accion }}</td>
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
import { ref, computed } from 'vue'

const items = ref([
  {
    fecha_gestion: '12/12/12',
    nombre_consultora: 'Brety Consultores S.L.',
    factura_en_mora: '15151518',
    saldo_en_mora: '1.900.000',
    dias_en_mora: '5 días',
    tipificacion: 'ver+',
    fecha_acuerdo: '12/12/12',
    valor_acuerdo: '8.000.000',
    accion: '-',
  },
  {
    fecha_gestion: '10/06/23',
    nombre_consultora: 'Soluciones Financieras S.A.S.',
    factura_en_mora: '12345678',
    saldo_en_mora: '4.500.000',
    dias_en_mora: '7 días',
    tipificacion: 'ver+',
    fecha_acuerdo: '15/06/23',
    valor_acuerdo: '4.800.000',
    accion: 'Reestructuración de deuda',
  },
  {
    fecha_gestion: '01/04/23',
    nombre_consultora: 'Gestiones Integrales S.A.',
    factura_en_mora: '20232401',
    saldo_en_mora: '3.500.000',
    dias_en_mora: '10 días',
    tipificacion: 'ver+',
    fecha_acuerdo: '05/04/23',
    valor_acuerdo: '3.700.000',
    accion: 'Negociación de pago',
  },
  {
    fecha_gestion: '15/05/23',
    nombre_consultora: 'Asesorías Empresariales S.L.',
    factura_en_mora: '98765432',
    saldo_en_mora: '2.000.000',
    dias_en_mora: '15 días',
    tipificacion: 'ver+',
    fecha_acuerdo: '20/05/23',
    valor_acuerdo: '2.100.000',
    accion: 'Compromiso de pago',
  },
])

const selectedClient = ref(null)

const showClientDetails = (client) => {
  selectedClient.value = client
}

const hideClientDetails = () => {
  selectedClient.value = null
}
const goBack = () => {
  window.location.href = '/'
}
const filterText = ref('')
const filteredItems = computed(() => {
  // Filtrar elementos en base al texto de búsqueda en todos los campos
  return items.value.filter((item) =>
    Object.values(item).some((field) => field.toString().toLowerCase().includes(filterText.value.toLowerCase())),
  )
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
