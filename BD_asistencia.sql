-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para asistencia
CREATE DATABASE IF NOT EXISTS `asistencia` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `asistencia`;

-- Volcando estructura para tabla asistencia.asistencia
CREATE TABLE IF NOT EXISTS `asistencia` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sesion_id` int(11) unsigned NOT NULL,
  `estudiante_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_asistencia_sesion` (`sesion_id`),
  KEY `FK_asistencia_estudiante` (`estudiante_id`),
  CONSTRAINT `FK_asistencia_estudiante` FOREIGN KEY (`estudiante_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `FK_asistencia_sesion` FOREIGN KEY (`sesion_id`) REFERENCES `sesion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia.asistencia: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `asistencia` DISABLE KEYS */;
INSERT INTO `asistencia` (`id`, `sesion_id`, `estudiante_id`) VALUES
	(1, 2, 1),
	(2, 2, 6),
	(5, 1, 3),
	(6, 1, 4);
/*!40000 ALTER TABLE `asistencia` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia.curso
CREATE TABLE IF NOT EXISTS `curso` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia.curso: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
INSERT INTO `curso` (`id`, `nombre`) VALUES
	(1, 'Desarrollo de software'),
	(2, 'Ingenieria De Sistemas'),
	(3, 'Obras Civiles'),
	(4, 'Ingenieria Civil');
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia.espacio_academico
CREATE TABLE IF NOT EXISTS `espacio_academico` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8 NOT NULL,
  `semestre` varchar(50) CHARACTER SET utf8 NOT NULL,
  `curso_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `FK_espacio_curso` (`curso_id`),
  CONSTRAINT `FK_espacio_curso` FOREIGN KEY (`curso_id`) REFERENCES `curso` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia.espacio_academico: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `espacio_academico` DISABLE KEYS */;
INSERT INTO `espacio_academico` (`id`, `nombre`, `semestre`, `curso_id`) VALUES
	(1, 'Ingles', '2', 1),
	(2, 'Lenguaje de cuarta', '5', 1),
	(4, 'Base De Datos 2', '5', 1),
	(5, 'Ingeniería de software II', '7', 2),
	(9, 'Quimica General', '1', 3);
/*!40000 ALTER TABLE `espacio_academico` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia.rol: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` (`id`, `Nombre`) VALUES
	(2, 'Docente'),
	(1, 'Estudiante');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia.sesion
CREATE TABLE IF NOT EXISTS `sesion` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `docente_id` int(11) unsigned NOT NULL,
  `espacioac_id` int(11) unsigned NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `hora_inicial` varchar(50) NOT NULL,
  `hora_final` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_sesion_docente` (`docente_id`),
  KEY `FK_sesion_espacioac` (`espacioac_id`),
  CONSTRAINT `FK_sesion_docente` FOREIGN KEY (`docente_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `FK_sesion_espacioac` FOREIGN KEY (`espacioac_id`) REFERENCES `espacio_academico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia.sesion: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `sesion` DISABLE KEYS */;
INSERT INTO `sesion` (`id`, `docente_id`, `espacioac_id`, `fecha`, `hora_inicial`, `hora_final`) VALUES
	(1, 2, 4, '2021-03-15', '06:00:00', '08:00:00'),
	(2, 7, 2, '2021-03-11', '08:00:00', '10:00:00');
/*!40000 ALTER TABLE `sesion` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `rol_id` int(11) unsigned NOT NULL,
  `identificacion` int(11) unsigned NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8 NOT NULL,
  `apellido` varchar(50) CHARACTER SET utf8 NOT NULL,
  `email` varchar(50) CHARACTER SET utf8 NOT NULL,
  `semestre` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `periodo` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `email` (`email`),
  KEY `FK_usuario_rol` (`rol_id`),
  CONSTRAINT `FK_usuario_rol` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia.usuario: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`id`, `rol_id`, `identificacion`, `nombre`, `apellido`, `email`, `semestre`, `periodo`) VALUES
	(1, 1, 1007, 'Camilo', 'Perez', 'camilo@gmail.com', '4', '2021-01'),
	(2, 2, 1, 'Jeyson', 'Calvache', 'jeyson@gmail.com', '', '2021-01'),
	(3, 1, 1002, 'David', 'Lopez', 'david@gmail.com', '1', '2021-01'),
	(4, 1, 1004, 'Zuly', 'Rosero', 'Zuly@gmail.com', '4', '2021-01'),
	(5, 1, 1005, 'Carlos', 'Chacon', 'carlos@gmail.com', '1', '2021-01'),
	(6, 1, 1003, 'Salome', 'Ortega', 'salome@gmail.com', '5', '2021-01'),
	(7, 2, 2, 'Santiago', 'Possos', 'santiago@gmail.com', '', '2021-01'),
	(8, 1, 1006, 'Fredy', 'Burgos', 'fredy@gmail.com', '4', '2021-01');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
