<template>
  <h1 class="page-title">Estado de cartera</h1>
  <div class="card">
    <div class="card-body">
      <img src="../../../public/yanbal.jpg" alt="Imagen tarjeta izquierda" class="img-fluid" />
    </div>

    <form class="formulario" @submit.prevent="generarInforme">
      <h2 class="page-title">Ingrese el codigo de la directora</h2>
      <input id="codigo" v-model="formData.codigo" type="number" placeholder="Codigo directora" />
      <button type="submit">generar informe</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'

const formData = reactive({
  codigo: '',
})

const generarInforme = async () => {
  try {
    const response = await fetch('http://localhost:3000/api/generar-informe', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.message)
    } else if (response.status === 200) {
      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.style.display = 'none'
      a.href = url
      a.download = 'informe.pdf'
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
    }
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped>
.card {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: flex-end;
}
.card-body {
  width: 55%;
  float: none;
  margin: 0;
  padding: 10px;
  border: 2px solid #ddd;
  border-radius: 9px;
  background-color: #fff;
}
.formulario {
  width: 600px;
  height: 440px;
  margin-right: 100px;
  padding: 50px;
  border: 1px solid #ddd;
  border-radius: 9px;
  background-color: #fff;
}
h2 {
  text-align: center;
  margin-bottom: 30px;
}
input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 20px;
}
button {
  height: 47px;
  padding: 10px 20px;
  border: 1px solid;
  border-radius: 5px;
  background-color: #ffa05c;
  color: #fff;
  cursor: pointer;
}
@media (max-width: 768px) {
  .contenedor,
  .imagen-formulario,
  .formulario {
    width: 100%;
    float: none;
    margin: 0 auto;
  }
}
</style>
