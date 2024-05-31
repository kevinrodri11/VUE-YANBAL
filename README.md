# ¡Bienvenido a la documentación del proyecto YANBAL!

## Tabla de contenido

- [Acerca](#acerca)
- [Tecnologías](#tecnologías)
- [Funciones](#funciones)
- [Uso](#uso)
 - [Organización del archivo](#organización-del-archivo)






## Acerca

El proyecto yanbal es una página web diseñada por C&C Services S.A.S, para permitir a las directoras de la campaña iniciar sesión,los usuarios pueden navegar por la página utilizando un sidebar que incluye tres secciones: 'Página principal, un carrusel con novedades y la tabla con sus encargados, 'Estado de cartera' campo para ingresar codigo de la directora y asi poderle generar un pdf y 'Salir'.

## Tecnologías

- **Frontend**: VUE, Vuestic-UI, Vite, Pinia y Tailwind CSS.
- **Backend**: JavaScript, express, node.js.
- **Base de datos**: MySQL.

## Funciones

- Sistema de inicio de sesión.
- Sidebar de navegación con enlaces a diferentes secciones.
- Página principal con carrusel de bienvenida personalizado.
- Tabla de encargados con enlaces a detalles específicos.
- Página de detalles con información sobre consultoras y facturas en mora.
- Estado de cartera con imagen y campo para código de directora (en desarrollo).
- Botón de cierre de sesión.
- API backend para autenticación y gestión de datos de usuarios.


## Instalación
### Interfaz:
Requisitos previos:
- git
- Node.js
- npm

1. Clonar el repositorio del proyecto `git clone https://github.com/kevinrodri11/VUE-YANBAL.git`
2. Vaya al directorio del proyecto `cd VUE-YANBAL`
3. Instale las dependencias ejecutando `npm install` 
4. Corralo con `npm run dev`

## Uso

### Interfaz:
1. Vaya al directorio del proyecto `cd .\src\backend\`
2. Ejecute el siguiente comando para iniciar el servidor frontend: `node .\login.js `
3. El servidor frontend se actualizará automáticamente cuando se realicen cambios en el código.
4. Para detener el servidor frontend, presione `Ctrl + C`


#### Organización del archivo:
- El código de interfaz se encuentra en el directorio `/src`
- El punto de entrada principal es el archivo `backend.js`
- El directorio `/public` está organizado según las páginas donde se utilizan las imágenes.
- Los componentes están ubicados en el directorio `/src/components`

#### Estructura del código: