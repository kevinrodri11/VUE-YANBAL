<template>
  <div class="grid md:grid-cols-2 gap-6 mb-6">
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
</template>

<script setup>
import { ref } from 'vue'

const items = [
  {
    fecha_gestion: '12 / 12 / 12',
    nombre_consultora: 'Brety Consultores S.L.',
    factura_en_mora: '15151518',
    saldo_en_mora: '1.900.000',
    dias_en_mora: '5 días',
    address: {},
    fecha_acuerdo: '12 / 12 / 12',
    valor_acuerdo: '8.000.000',
    accion: '-',
  },
  {
    fecha_gestion: '10/06/23',
    nombre_consultora: 'Soluciones Financieras S.A.S.',
    factura_en_mora: '12345678',
    saldo_en_mora: '4.500.000',
    dias_en_mora: '7 días',
    address: {},
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
    address: {},
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
    address: {},
    fecha_acuerdo: '20/05/23',
    valor_acuerdo: '2.100.000',
    accion: 'Compromiso de pago',
  },
]

const columns = [
  { key: 'fecha_gestion', sortable: true, label: 'Fecha de Gestión' },
  { key: 'nombre_consultora', sortable: true, label: 'Nombre de la Consultora' },
  { key: 'factura_en_mora', sortable: true, label: 'Factura en Mora' },
  { key: 'saldo_en_mora', sortable: true, label: 'Saldo en Mora' },
  { key: 'dias_en_mora', sortable: true, label: 'Días en Mora' },
  { key: 'fecha_acuerdo', sortable: true, label: 'Fecha de Acuerdo' },
  { key: 'valor_acuerdo', sortable: true, label: 'Valor de Acuerdo' },
  { key: 'accion', sortable: false, label: 'Acción' },
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
