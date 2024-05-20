<template>
  <form @submit.prevent="submit">
    <h1 class="font-semibold text-4xl mb-4">Iniciar sesión</h1>
    <div class="mb-4">
      <label for="usuario">Usuario</label>
      <input
        id="usuario"
        v-model="formData.usuario"
        type="text"
        required
        class="mb-4"
      />
    </div>
    <div class="mb-4">
      <label for="clave">Contraseña</label>
      <input
        id="clave"
        v-model="formData.clave"
        type="password"
        required
        class="mb-4"
      />
    </div>
    <div class="flex justify-center mt-4">
      <button type="submit" class="w-full">Iniciar sesión</button>
    </div>
  </form>
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
