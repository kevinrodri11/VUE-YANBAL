const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const conexion = require('./conexion');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Ruta para la autenticación de usuarios
app.post('/auth/login-test', (req, res) => {
  const { usuario, clave } = req.body;

  const query = `SELECT nombre, usuario FROM consultoras WHERE usuario = ? AND clave = ?`;
  conexion.query(query, [usuario, clave], (err, results) => {
    if (err) {
      console.error('Error al consultar la base de datos:', err);
      res.status(500).json({ message: 'Error interno del servidor' });
      return;
    }
    if (results.length === 1) {
      // Usuario autenticado correctamente
      const nombreUsuario = results[0].nombre;
      const usuarioUsuario = results[0].usuario;
      res.json({ message: 'Has iniciado sesión correctamente', nombre: nombreUsuario, usuario: usuarioUsuario });
    } else {
      // Usuario o contraseña incorrectos
      res.status(401).json({ message: 'Usuario o contraseña incorrectos' });
    }
  });
});

app.get('/api/dashboard-data', (req, res) => {
  const usuario = req.query.usuario;
  console.log(usuario)
  const query = `SELECT codigo, nombre FROM reparto WHERE directora = ?;`
  conexion.query(query, [usuario], (err, results) => {
    if (err) {
      console.error('Error al consultar la base de datos:', err);
      res.status(500).json({ message: 'Error interno del servidor' });
      return;
    }
    res.json(results);
  });
});

app.get('/api/projects/:id', (req, res) => {
  const projectId = req.params.id;
  console.log('Project ID:', projectId);  // Verificar que el ID se pasa correctamente
  const query = `
  SELECT 
  fecha_gestion,
  repart.nombre,
  factura,
  valor_total_al_dia,
  dias_mora_inicial,
  perfil,
  gestion,
  fecha_promesa,
  valor_promesa,
  descripcion 
FROM 
  historico_gestion AS history
  INNER JOIN reparto AS repart ON repart.cedula = history.identificacion
  INNER JOIN perfil AS perfill ON perfill.id = history.id_perfil
  INNER JOIN accion AS action ON action.codigo = history.id_accion
  INNER JOIN consultoras AS consult ON consult.usuario = repart.directora
WHERE  
  repart.codigo = ? 
ORDER BY 
  fecha_gestion DESC;
`;

  conexion.query(query, [projectId], (err, results) => {
    if (err) {
      console.error('Error al consultar la base de datos:', err);
      res.status(500).json({ message: 'Error interno del servidor' });
      return;
    }
    console.log('resultado:', results);  
    res.json(results); // Suponiendo que solo haya un resultado
  });
});


app.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000');
});