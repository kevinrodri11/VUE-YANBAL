<template>
  <VaSidebar v-model="writableVisible" :width="sidebarWidth" :color="color" minimized-width="0">
    <VaAccordion v-model="value" multiple>
      <VaCollapse v-for="(route, index) in navigationRoutes.routes" :key="index">
        <template #header="{}">
          <VaSidebarItem
            :to="route.children ? undefined : { name: route.name }"
            :active="routeHasActiveChild(route)"
            :active-color="activeColor"
            :text-color="textColor(route)"
            :aria-label="`${route.children ? 'Open category ' : 'Visit'} ${t(route.displayName)}`"
            role="button"
            hover-opacity="0.10"
            @click="route.name === 'login' ? logout() : null"
          >
            <VaSidebarItemContent class="py-3 pr-2 pl-4">
              <VaIcon
                v-if="route.meta.icon"
                aria-hidden="true"
                :name="route.meta.icon"
                size="25px"
                :color="iconColor(route)"
              />
              <VaSidebarItemTitle class="flex justify-between items-center leading-5 font-semibold">
                {{ t(route.displayName) }}
              </VaSidebarItemTitle>
            </VaSidebarItemContent>
          </VaSidebarItem>
        </template>
      </VaCollapse>
    </VaAccordion>
  </VaSidebar>
</template>

<script lang="ts">
import { defineComponent, watch, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router' // Importar useRouter
import { useI18n } from 'vue-i18n'
import { useColors } from 'vuestic-ui'

import navigationRoutes, { type INavigationRoute } from './NavigationRoutes'

export default defineComponent({
  name: 'Sidebar',
  props: {
    visible: { type: Boolean, default: true },
    mobile: { type: Boolean, default: false },
  },
  emits: ['update:visible'],

  setup: (props, { emit }) => {
    const { getColor, colorToRgba } = useColors()
    const route = useRoute()
    const router = useRouter() // Definir router
    const { t } = useI18n()

    const value = ref<boolean[]>([])

    const writableVisible = computed({
      get: () => props.visible,
      set: (v: boolean) => emit('update:visible', v),
    })

    const isActiveChildRoute = (child: INavigationRoute) => route.name === child.name

    const routeHasActiveChild = (section: INavigationRoute) => {
      if (!section.children) {
        return route.path.endsWith(`${section.name}`)
      }

      return section.children.some(({ name }) => route.path.endsWith(`${name}`))
    }

    const setActiveExpand = () =>
      (value.value = navigationRoutes.routes.map((route: INavigationRoute) => routeHasActiveChild(route)))

    const sidebarWidth = computed(() => (props.mobile ? '100vw' : '230px'))
    const color = computed(() => '#212121')
    const activeColor = computed(() => colorToRgba(getColor('#FFA05C'), 8))

    const iconColor = (route: INavigationRoute) => (routeHasActiveChild(route) ? '#FFFFFF' : '#B3C4C9')
    const textColor = (route: INavigationRoute) => (routeHasActiveChild(route) ? '#FFFFFF' : '#B3C4C9')
    const arrowDirection = (state: boolean) => (state ? 'va-arrow-up' : 'va-arrow-down')

    watch(() => route.fullPath, setActiveExpand, { immediate: true })

    // Método para manejar el evento de salir
    const logout = () => {
      localStorage.removeItem('nombreUsuario');
      localStorage.removeItem('usuarioUsuario');
      router.push({ name: 'login' }); // Redirigir al usuario a la página de inicio de sesión
    };

    return {
      writableVisible,
      sidebarWidth,
      value,
      color,
      activeColor,
      navigationRoutes,
      routeHasActiveChild,
      isActiveChildRoute,
      t,
      iconColor,
      textColor,
      arrowDirection,
      logout, // Exponer el método logout
    };
  },
})
</script>

<style>
/* Agrega aquí tus estilos */
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

.pagination {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.pagination button {
  padding: 5px 10px;
  background-color: #ffa05c;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}

.pagination button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

.logout-button {
  padding: 8px 16px;
  background-color: #ff6b6b;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

.logout-button:hover {
  background-color: #ff4d4d;
}
</style>
