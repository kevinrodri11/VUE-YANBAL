export const sleep = (ms = 0) => {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

/** Validation */
export const validators = {
  email: (v: string) => {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return pattern.test(v) || 'Por favor ingrese un correo válido'
  },
  user: (v: string) => {
    // Validación de usuario (ejemplo: al menos 4 caracteres)
    return (v && v.length >= 4) || 'Por favor ingrese un usuario válido'
  },
  required: (v: any) => !!v || 'Este campo es requerido',
}
