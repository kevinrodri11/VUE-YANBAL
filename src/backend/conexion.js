const mysql = require('mysql');

const conexion = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'yanbal'
});

conexion.connect((err) => {
  if (err) {
    console.error('No se pudo establecer la conexión a la base de datos:', err);
    return;
  }
  console.log('Conexión a la base de datos establecida correctamente.'); 
});

module.exports = conexion;
