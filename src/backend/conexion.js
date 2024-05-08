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
  
  // Consulta para obtener registros de la tabla example_table
  conexion.query('SELECT * FROM consultoras', (error, results) => {
    if (error) {
      console.error('Error al ejecutar la consulta:', error);
      return;
    }
    console.log('Registros obtenidos correctamente:', results);
  });
});

module.exports = conexion;
