-- Active: 1734576763649@@127.0.0.1@3306@datag3
-- CREAR UNA TABLA
CREATE TABLE alumno(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(10) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100)
 );

 --- MODIFICAR TABLA

 ALTER TABLE alumno
 ADD COLUMN nota INT DEFAULT 0;

 -- elimnar tabla

 DROP Table alumno;

 