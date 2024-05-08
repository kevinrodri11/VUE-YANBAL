<template>
  <VaForm ref="form" @submit.prevent="submit">
    <h1 class="font-semibold text-4xl mb-4">Iniciar sesión</h1>
    <VaInput
      v-model="formData.user"
      :rules="[validators.required, validators.user]"
      class="mb-4"
      label="Usuario"
      type="text"
    />
    <VaValue v-slot="isPasswordVisible" :default-value="false">
      <VaInput
        v-model="formData.password"
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
      <VaButton class="w-full" @click="submit">Iniciar sesión</VaButton>
    </div>
  </VaForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useForm, useToast } from 'vuestic-ui'
import { validators } from '../../services/utils'

const { validate } = useForm('form')
const { push } = useRouter()
const { init } = useToast()

const formData = reactive({
  user: '',
  password: '',
  keepLoggedIn: false,
})

const submit = () => {
  if (validate()) {
    // Simulando verificación de credenciales con datos estáticos
    const validUser = '1920';
    const validPassword = 'Cyc'; 

    if (formData.user === validUser && formData.password === validPassword) {
      init({ message: 'Has iniciado sesión correctamente', color: 'success' })
      push({ name: 'dashboard' })
    } else {
      init({ message: 'Usuario o contraseña incorrectos', color: 'error' })
    }
  }
}
</script>