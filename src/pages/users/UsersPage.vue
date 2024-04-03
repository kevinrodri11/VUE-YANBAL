<template>
  <h1 class="page-title">Estado de cartera</h1>
  <div class="card">
    <div class="card-body">
      <img src="../../../public/cyc_yanbal.jpg" alt="Imagen tarjeta izquierda" class="img-fluid" />
    </div>

    <form class="formulario">
      <h2 class="page-title">Ingrese el codigo de la directora</h2>
      <input type="number" placeholder="Codigo directora" name="" />
      <button>generar informe</button>
    </form>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.card {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: flex-end; /* Alinea el formulario a la derecha */
}
.card-body {
  width: 35%;
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
  /* Mismo estilo para pantallas pequeñas */
  .contenedor,
  .imagen-formulario,
  .formulario {
    width: 100%;
    float: none;
    margin: 0 auto;
  }
}
</style>
