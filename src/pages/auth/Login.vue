<template>
  <VaForm ref="form" @submit.prevent="submit">
    <h1 class="font-semibold text-4xl mb-4">Iniciar sesión</h1>
    <VaInput
      v-model="formData.usuario"
      :rules="[validators.required]"
      class="mb-4"
      label="Usuario"
      type="text"
    />
    <VaValue v-slot="isPasswordVisible" :default-value="false">
      <VaInput
        v-model="formData.clave"
        :rules="[validators.required]"
        :type="isPasswordVisible.value ? 'text' : 'password'"
        class="mb-4"
        label="Contraseña"
        @clickAppendInner.stop="isPasswordVisible.value = !isPasswordVisible.value"
      >
        <template #appendInner>
          <VaIcon
            :name="isPasswordVisible.value ? 'mso-visibility_off' : 'mso-visibility'"
            class="cursor-pointer"
            color="secondary"
          />
        </template>
      </VaInput>
    </VaValue>
    <div class="flex justify-center mt-4">
      <VaButton class="w-full" type="submit">Iniciar sesión</VaButton>
    </div>
  </VaForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useForm, useToast } from 'vuestic-ui'
import { validators } from '../../services/utils'
import axios from 'axios'

const { push } = useRouter()
const { init } = useToast()

const formData = reactive({
  usuario: '',
  clave: '',
})

const submit = async () => {
  try {
    const response = await axios.post('/login', {
      usuario: formData.usuario,
      clave: formData.clave,
    })

    if (response.data.success) {
      init({ message: 'Has iniciado sesión correctamente', color: 'success' })
      push({ name: 'dashboard' }) // Redirecciona al usuario a la página de dashboard
    } else {
      init({ message: 'Credenciales inválidas', color: 'error' })
    }
  } catch (error) {
    console.error('Error al iniciar sesión:', error)
    init({ message: 'Error al iniciar sesión', color: 'error' })
  }
}
</script>