const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const conexion = require('./conexion'); // Importa la conexión a la base de datos

const app = express();
app.use(cors()); // Habilita CORS para todas las rutas
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
  const query = `SELECT codigo, nombre FROM reparto WHERE directora = ?;` // Modifica esto según tus necesidades
  conexion.query(query,[usuario],(err, results) => {
    if (err) {
      console.error('Error al consultar la base de datos:', err);
      res.status(500).json({ message: 'Error interno del servidor' });
      return;
    }
    res.json(results);
  });
});


app.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000');
});

