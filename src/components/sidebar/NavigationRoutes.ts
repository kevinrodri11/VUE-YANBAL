export interface INavigationRoute {
  name: string
  displayName: string
  meta: { icon: string }
  children?: INavigationRoute[]
}

export default {
  root: {
    name: '/',
    displayName: 'navigationRoutes.home',
  },
  routes: [
    {
      name: 'dashboard',
      displayName: 'Pagina principal',
      meta: {
        icon: 'vuestic-iconset-dashboard',
      },
    },
    {
      name: 'users',
      displayName: 'Estado de cartera',
      meta: {
        icon: 'group',
      },
    },
    {
      name: 'login',
      displayName: 'Salir',
      meta: {
        icon: 'login',
      },
    },
  ] as INavigationRoute[],
}
