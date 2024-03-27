const express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000; // Puedes cambiar el puerto si lo necesitas

// Configuración de la conexión a la base de datos
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'yanbal'
});

connection.connect((err) => {
  if (err) {
    console.error('Error de conexión a la base de datos: ', err);
    return;
  }
  console.log('Conexión exitosa a la base de datos');
});

// Ejemplo de ruta para obtener datos de la base de datos
app.get('/datos', (req, res) => {
  connection.query('SELECT * FROM consultoras', (error, results) => {
    if (error) {
      console.error('Error al ejecutar la consulta: ', error);
      res.status(500).json({ error: 'Error interno del servidor' });
      return;
    }
    res.json(results);
  });
});

// Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor Express escuchando en el puerto ${port}`);
});
