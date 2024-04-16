// test.js

const db = require('./db');

db.query('SELECT 1 + 1 AS solution', (error, results) => {
    if (error) {
        console.error('Error de prueba de conexión:', error);
        return;
    }
    console.log('La conexión a la base de datos funciona correctamente. Resultado:', results[0].solution);
});