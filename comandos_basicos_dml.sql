/*Seleccionar todos los registros de una tabla, se puede utilizar el where dentro*/
/*SELECT * FROM movement WHERE quantity<0;*/
/*Seleccionar algunos campos de una tabla de datos*/
/*SELECT concept, quantity FROM movement;*/
/* Insertar nuevos registros en la tabla movement */
/*INSERT INTO movement(date, concept, quantity) VALUES("2025-09-05", "Mercado", -250);
/*Comando para actualizar registros de la tabla movement*/
/*UPDATE movement SET concept = "Almuerzo", quantity = -50 WHERE id=2;*/
/*INSERT INTO movement(date, concept, quantity) VALUES("2025-09-08", "Tarde", -35);*/
SELECT * FROM movement;
/*Borrado de registros, importante utilizar el where siempre que se quiera borrar un registro específico */
/*DELETE FROM movement WHERE id=3;*/
SELECT * FROM movement ORDER BY id ASC;