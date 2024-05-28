<template>
  <div class="login-container">
    <div class="inner__brand">
      <div class="bg-neutral-900 radius-large space-8">
        <img class="brand__logo radius-large" src="/logo favicon.png" />
      </div>
      <div class="brand__text">
        <span>
          <h3>C&C Services</h3>
        </span>
      </div>
    </div>
    <form class="login-form" @submit.prevent="submit">
      <h1 class="font-semibold text-4xl mb-4">Iniciar sesión</h1>
      <div class="mb-4">
        <label for="usuario">Usuario</label>
        <input id="usuario" v-model="formData.usuario" type="text" required class="input" />
      </div>
      <div class="mb-4">
        <label for="clave">Contraseña</label>
        <input id="clave" v-model="formData.clave" type="password" required class="input" />
      </div>
      <div class="flex justify-center mt-4">
        <button type="submit" class="button">Iniciar sesión</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vuestic-ui'

const { push } = useRouter()
const { init } = useToast()

const formData = reactive({
  usuario: '',
  clave: '',
  keepLoggedIn: false,
})

const submit = async () => {
  console.log('Submit function called'); // Verificar que la función se ejecuta
  console.log('Form data:', formData); // Verificar los datos del formulario

  try {
    const response = await fetch('http://localhost:3000/auth/login-test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });

    const data = await response.json();
    console.log('Response from server:', data); // Verificar la respuesta del servidor

    if (response.ok) {
      localStorage.setItem('nombreUsuario', data.nombre);
      localStorage.setItem('usuarioUsuario', data.usuario);
      init({ message: data.message, color: 'success' });
      push({ name: 'dashboard' });
    } else {
      init({ message: data.message, color: 'error' });
    }
  } catch (error) {
    console.error('Error al iniciar sesión:', error);
    init({ message: 'Error interno del servidor', color: 'error' });
  }
};
</script>

<style>
.input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  background-color: #f2f2f2;
}
.button {
  width: 100%;
  padding: 10px 10px;
  background-color: #ffa05c;
  color: #fff;
  border-radius: 5px;
  text-align: center;
  font-size: 18px;
}
.inner__brand {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-bottom: 40px;
}
.radius-large {
  border-radius: 0.75rem;
}
.space-8 {
  padding: 0.4rem;
}
.brand__logo {
  max-width: 40px;
}
.brand__text h3 {
  font-size: 1.5rem;
  margin: 0; 
}
</style>
