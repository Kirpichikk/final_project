-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: new_schema
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id_department` int NOT NULL AUTO_INCREMENT,
  `name_department` varchar(45) DEFAULT NULL,
  `floor` int DEFAULT NULL,
  `head` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_department`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Терaпевтическое',5,'Демин'),(2,'Педиaтрическое',4,'Волков'),(3,'Кaбинет физиотерaпии',2,'Морозова'),(4,'Отделение лучевой диaгностики',5,'Федорова'),(5,'Дневной стaционaр',2,'Никитина'),(6,'Женскaя консультaция',4,'Шилов'),(7,'Стомaтологическое отделение',1,'Родина'),(8,'Лaборaтория',1,'Михеев');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `id_doctor` int NOT NULL,
  `passport_data` double NOT NULL,
  `address` varchar(100) NOT NULL,
  `birthday` date NOT NULL,
  `specialization` varchar(45) NOT NULL,
  `date_startwork` date NOT NULL,
  `date_layoff` date DEFAULT NULL,
  `id_department` int NOT NULL,
  `doctor_name` varchar(45) NOT NULL,
  `docotr_surname` varchar(45) NOT NULL,
  `doctor_patronymic` varchar(45) NOT NULL,
  PRIMARY KEY (`id_doctor`),
  KEY `id_idx` (`id_department`),
  CONSTRAINT `id_department` FOREIGN KEY (`id_department`) REFERENCES `department` (`id_department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,8497033505,'108777, Ленинградская область, город Озёры, въезд Бухарестская, 12','1973-04-23','физиотерапевт','1999-11-19','2019-03-23',3,'Соколова','',''),(2,3054466812,'462624, Новгородская область, город Павловский Посад, пр. 1905 года, 55','1968-05-06','врач-рентгенолог','2008-07-27','2019-03-04',4,'Галкин','',''),(3,3955665746,'885547, Ярославская область, город Серпухов, пл. Ломоносова, 99','1972-04-20','неврология','2018-10-11',NULL,2,'Мельникова','',''),(4,8952487959,'911964, Амурская область, город Люберцы, пл. Космонавтов, 68','1977-02-06','массажист','2015-08-11',NULL,3,'Вешнякова','',''),(5,1869169490,'669452, Кировская область, город Егорьевск, наб. Бухарестская, 29','1977-02-02','врач-терапевт','2005-05-29',NULL,1,'Агафонова','',''),(6,2129791421,'306289, Кировская область, город Красногорск, пер. Чехова, 49','1972-09-06','лаборант дневной смены','2014-11-03',NULL,8,'Никонова','',''),(7,8381861397,'361823, Магаданская область, город Зарайск, шоссе Ленина, 80','1991-09-24','стоматолог-терапевт','2009-06-19',NULL,7,'Васильева','',''),(8,5668374899,'637915, Сахалинская область, город Серпухов, пр. Космонавтов, 75','1967-01-30','врач-рентгенолог','1999-11-19',NULL,4,'Кузнецова','',''),(9,2927382493,'678613, Нижегородская область, город Серпухов, пр. Домодедовская, 73','1979-03-23','стоматолог-хирург','2009-12-06','2019-03-02',7,'Ковалева','',''),(10,1672799206,'379218, Курганская область, город Коломна, спуск Сталина, 98','1996-10-06','медицинская сестра','2007-03-22',NULL,1,'Троицкая','','');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `external_users`
--

DROP TABLE IF EXISTS `external_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `external_users` (
  `id_external_users` int NOT NULL AUTO_INCREMENT,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `id_inside` int DEFAULT NULL,
  `db_config` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_external_users`),
  UNIQUE KEY `iid_dexternal_users_UNIQUE` (`id_external_users`),
  UNIQUE KEY `id_inside_UNIQUE` (`id_inside`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `external_users`
--

LOCK TABLES `external_users` WRITE;
/*!40000 ALTER TABLE `external_users` DISABLE KEYS */;
INSERT INTO `external_users` VALUES (1,'123','abv',2,'123abc');
/*!40000 ALTER TABLE `external_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `new_view`
--

DROP TABLE IF EXISTS `new_view`;
/*!50001 DROP VIEW IF EXISTS `new_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `new_view` AS SELECT 
 1 AS `id_doctor`,
 1 AS `COUNT(*)`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `office`
--

DROP TABLE IF EXISTS `office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `office` (
  `id_office` int NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `square` int DEFAULT NULL,
  `id_department` int DEFAULT NULL,
  `number` int DEFAULT NULL,
  PRIMARY KEY (`id_office`),
  KEY `id_department_idx` (`id_department`),
  KEY `department_idx` (`id_department`),
  CONSTRAINT `department` FOREIGN KEY (`id_department`) REFERENCES `department` (`id_department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `office`
--

LOCK TABLES `office` WRITE;
/*!40000 ALTER TABLE `office` DISABLE KEYS */;
INSERT INTO `office` VALUES (1,'процедурный',7,8,101),(2,'физиотерапевтический',22,1,501),(3,'процедурный',14,2,401),(4,'процедурный',22,8,102),(5,'обычный',5,1,502),(6,'физиотерапевтический',2,4,404),(7,'процедурный',8,1,503),(8,'обычный',27,2,402),(9,'физиотерапевтический',13,2,403),(10,'обычный',7,8,103);
/*!40000 ALTER TABLE `office` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_count_new_patient`
--

DROP TABLE IF EXISTS `report_count_new_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_count_new_patient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `month` int NOT NULL,
  `count_patient` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_count_new_patient`
--

LOCK TABLES `report_count_new_patient` WRITE;
/*!40000 ALTER TABLE `report_count_new_patient` DISABLE KEYS */;
INSERT INTO `report_count_new_patient` VALUES (1,2024,1,2),(2,2024,2,3),(3,2024,3,6),(4,2024,5,1),(5,2024,7,1),(6,2024,9,1);
/*!40000 ALTER TABLE `report_count_new_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_ended_visits`
--

DROP TABLE IF EXISTS `report_ended_visits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_ended_visits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `month` int NOT NULL,
  `count` int NOT NULL,
  `doctor_name` varchar(45) NOT NULL,
  `specialization` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_ended_visits`
--

LOCK TABLES `report_ended_visits` WRITE;
/*!40000 ALTER TABLE `report_ended_visits` DISABLE KEYS */;
INSERT INTO `report_ended_visits` VALUES (1,2022,3,3,'Агафонова','врач-терапевт'),(2,2022,3,1,'Мельникова','неврология'),(3,2022,3,1,'Никонова','лаборант дневной смены'),(4,2022,3,1,'Троицкая','медицинская сестра'),(5,2022,3,1,'Кузнецова','врач-рентгенолог'),(6,2022,3,1,'Вешнякова','массажист'),(7,2022,6,1,'Мельникова','неврология');
/*!40000 ALTER TABLE `report_ended_visits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_layoff_doctor`
--

DROP TABLE IF EXISTS `report_layoff_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_layoff_doctor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `month` int NOT NULL,
  `count_doctors` int NOT NULL,
  `department` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_layoff_doctor`
--

LOCK TABLES `report_layoff_doctor` WRITE;
/*!40000 ALTER TABLE `report_layoff_doctor` DISABLE KEYS */;
INSERT INTO `report_layoff_doctor` VALUES (1,2019,3,1,'Кaбинет физиотерaпии'),(2,2019,3,1,'Отделение лучевой диaгностики'),(3,2019,3,1,'Стомaтологическое отделение');
/*!40000 ALTER TABLE `report_layoff_doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shedule`
--

DROP TABLE IF EXISTS `shedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shedule` (
  `id_shedule` int NOT NULL AUTO_INCREMENT,
  `id_office` int DEFAULT NULL,
  `rec_date` date DEFAULT NULL,
  `rec_time` time DEFAULT NULL,
  `id_visit_card` int DEFAULT NULL,
  `app_mark` tinyint DEFAULT '0',
  `id_doctor` int DEFAULT NULL,
  PRIMARY KEY (`id_shedule`),
  KEY `id_office_idx` (`id_office`),
  KEY `id_visit_card_idx` (`id_visit_card`),
  KEY `id_docotr_idx` (`id_doctor`) /*!80000 INVISIBLE */,
  CONSTRAINT `id_docotr` FOREIGN KEY (`id_doctor`) REFERENCES `doctor` (`id_doctor`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shedule`
--

LOCK TABLES `shedule` WRITE;
/*!40000 ALTER TABLE `shedule` DISABLE KEYS */;
INSERT INTO `shedule` VALUES (1,9,'2022-10-24','10:38:00',2,1,3),(2,3,'2022-06-21','17:24:00',10,1,3),(3,2,'2022-03-02','13:39:00',2,1,5),(4,8,'2022-03-02','13:21:00',10,1,3),(5,2,'2022-03-02','16:51:00',2,1,5),(6,10,'2024-11-24','20:46:00',7,0,6),(7,10,'2024-11-24','20:40:00',3,1,6),(8,10,'2022-03-02','20:41:00',2,1,6),(9,5,'2022-03-02','11:00:00',10,1,10),(10,6,'2022-03-02','10:54:00',4,1,8),(11,4,'2022-03-13','14:46:00',1,1,4),(12,3,'2022-03-02','14:46:00',2,1,5),(13,2,'2024-12-22','14:46:00',NULL,0,5),(14,2,'2024-12-22','14:46:00',NULL,0,5),(15,2,'2024-12-22','14:30:00',NULL,0,5),(16,2,'2024-12-20','14:30:00',NULL,0,5),(17,2,'2024-12-20','14:00:00',NULL,0,5);
/*!40000 ALTER TABLE `shedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  `id_inside` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `login_UNIQUE` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'123','abc','doctor',6),(2,'2','v','register',1),(3,'god','god','supremedoctor',5),(4,'admin','admin','admin',4);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit`
--

DROP TABLE IF EXISTS `visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit` (
  `id_visit` int NOT NULL AUTO_INCREMENT,
  `appoint_date` date DEFAULT NULL,
  `diagnosis` varchar(45) DEFAULT NULL,
  `complains` varchar(45) DEFAULT NULL,
  `appointments` varchar(45) DEFAULT NULL,
  `id_visit_card` int DEFAULT NULL,
  `id_doctor` int DEFAULT NULL,
  PRIMARY KEY (`id_visit`),
  KEY `id_doctor_visit_idx` (`id_doctor`),
  KEY `id_visit_card_idx` (`id_visit_card`),
  CONSTRAINT `id_doctor_visit` FOREIGN KEY (`id_doctor`) REFERENCES `doctor` (`id_doctor`),
  CONSTRAINT `id_visit_card` FOREIGN KEY (`id_visit_card`) REFERENCES `visit_card` (`id_visit_card`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit`
--

LOCK TABLES `visit` WRITE;
/*!40000 ALTER TABLE `visit` DISABLE KEYS */;
INSERT INTO `visit` VALUES (1,'2021-10-06','острая недостаточность сна','усталость','прописан в рецепте',2,6),(2,'2020-12-31','грипп','усталость','прописан в рецепте',10,3),(3,'2020-10-31','зубная боль','усталость','прописан в рецепте',10,10),(4,'2019-12-21','простуда','усталость','прописан в рецепте',3,6),(5,'2023-05-03','пневмония','усталость','прописан в рецепте',2,5),(6,'2019-11-22','грипп','усталость','прописан в рецепте',2,5),(7,'2022-01-13','острая недостаточность котов','усталость','прописан в рецепте',4,8),(8,'2022-10-24','острая недостаточность витамина D','усталость','прописан в рецепте',2,3),(9,'2022-06-21','перелом ребер','усталость','прописан в рецепте',10,3),(10,'2020-04-26','ушиб ноги','усталость','прописан в рецепте',7,6),(11,'2024-11-19','11','1','1',7,6),(12,'2024-11-24','1','1','1',3,6);
/*!40000 ALTER TABLE `visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit_card`
--

DROP TABLE IF EXISTS `visit_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit_card` (
  `id_visit_card` int NOT NULL AUTO_INCREMENT,
  `passport_data` double DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `date_create` date DEFAULT NULL,
  `name_patient` varchar(45) DEFAULT NULL,
  `surname_patient` varchar(45) DEFAULT NULL,
  `patronymic_patient` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_visit_card`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit_card`
--

LOCK TABLES `visit_card` WRITE;
/*!40000 ALTER TABLE `visit_card` DISABLE KEYS */;
INSERT INTO `visit_card` VALUES (1,7831563830,'907214, Костромская область, город Павловский Посад, пер. Гоголя, 05','1978-06-28','2024-03-21','Назаров',NULL,NULL,NULL),(2,4893455526,'294371, Оренбургская область, город Мытищи, пер. Будапештсткая, 69','1993-12-11','2024-03-19','Лаврентьев',NULL,NULL,NULL),(3,9844133849,'449883, Самарская область, город Люберцы, ул. Космонавтов, 96','1995-04-02','2024-01-31','Тихонов',NULL,NULL,NULL),(4,7463236436,'255747, Липецкая область, город Серебряные Пруды, пр. Гоголя, 94','1992-12-14','2024-01-27','Беляев',NULL,NULL,NULL),(5,1175355076,'451544, Сахалинская область, город Чехов, пер. Домодедовская, 08','1976-12-17','2024-05-12','Петрова',NULL,NULL,NULL),(6,8252878530,'961889, Архангельская область, город Дмитров, проезд Косиора, 65','1981-11-12','2024-02-19','Соболев',NULL,NULL,NULL),(7,9180189001,'371130, Белгородская область, город Орехово-Зуево, шоссе Сталина, 07','1982-02-01','2024-02-12','Овчинникова',NULL,NULL,NULL),(8,5728854553,'232060, Тверская область, город Видное, пр. Балканская, 99','1965-11-09','2024-07-01','Емельянова',NULL,NULL,NULL),(9,6796203413,'171999, Кировская область, город Орехово-Зуево, пер. Косиора, 79','1979-12-19','2024-02-26','Давыдов',NULL,NULL,NULL),(10,9784122200,'370219, Самарская область, город Сергиев Посад, проезд Ломоносова, 28','1967-09-12','2024-09-05','Федотов',NULL,NULL,NULL),(11,7831563831,'570858, Челябинская область, город Люберцы, шоссе Космонавтов, 34','1995-04-02','2024-03-19','Сергеева',NULL,NULL,NULL),(12,7831563832,'728089, Мурманская область, город Шатура, бульвар Ладыгина, 50','1995-04-02','2024-03-18','Гаврилов',NULL,NULL,NULL),(13,7831563833,'290490, Омская область, город Зарайск, пл. 1905 года, 53','1995-04-02','2024-03-18','Осипов',NULL,NULL,NULL),(14,7831563834,'782858, Волгоградская область, город Мытищи, наб. Космонавтов, 95','1995-04-02','2024-03-19','Устинов',NULL,NULL,NULL);
/*!40000 ALTER TABLE `visit_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'new_schema'
--
/*!50003 DROP PROCEDURE IF EXISTS `report_1` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `report_1`(yyear int)
BEGIN
declare monthh int;
declare count int;
declare done int default 0;
declare cur cursor for
	SELECT 
		yyear, 
		MONTH(date_create) AS mmonth, 
		COUNT(date_create) AS ccount
	FROM 
		visit_card
	WHERE 
		YEAR(date_create) = yyear
	GROUP BY 
		YEAR(date_create), MONTH(date_create)
	ORDER BY 
		MONTH(date_create);
declare exit handler for not found set done = 1;

If (select count(*) from new_schema.report_count_new_patient where `year`= yyear) = 0 then
	open cur;
		while done = 0 do
			fetch cur into yyear, monthh, count;
			insert into report_count_new_patient(year, month, count_patient) values (yyear, monthh, count);
		end while;
	close cur;
end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `report_2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `report_2`(yyear int, mmonth int)
BEGIN
declare count int;
declare name_doctor varchar(15);
declare spec_doctor varchar(45);
declare done int default 0;
declare cur cursor for
SELECT 
    yyear,
    mmonth,
    COUNT(rec_date) AS appointment_count,
    doctor_name,
    specialization
FROM
    shedule
        JOIN
    doctor ON doctor.id_doctor = shedule.id_doctor
WHERE
    YEAR(rec_date) = yyear
        AND MONTH(rec_date) = mmonth
        AND app_mark = 1
GROUP BY  yyear , mmonth , doctor_name, specialization
ORDER BY  yyear, mmonth;
declare exit handler for not found set done = 1;

if (SELECT COUNT(*) FROM report_ended_visits WHERE `month` = mmonth AND `year` = yyear) = 0 then
	open cur;
		while done = 0 do
			fetch cur into yyear, mmonth, count, name_doctor, spec_doctor;    
            insert into report_ended_visits(`year`, `month`, count, doctor_name, specialization)
      values (yyear, mmonth, count, name_doctor, spec_doctor);
        end while;
    close cur;
end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `report_3` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `report_3`(yyear int, mmonth int)
BEGIN
declare count int;
declare dep varchar(45);
declare done int default 0;
declare cur cursor for
SELECT 
    yyear,
    mmonth,
    COUNT(*),
    name_department
FROM
    doctor
        JOIN
    department ON doctor.id_department = department.id_department
WHERE
    date_layoff IS NOT NULL
        AND YEAR(date_layoff) = yyear
        AND MONTH(date_layoff) = mmonth
GROUP BY yyear , mmonth, name_department
ORDER BY name_department;
declare exit handler for not found set done = 1;

If (SELECT COUNT(*) FROM report_layoff_doctor WHERE `month` = mmonth AND `year` = yyear) = 0 THEN
	open cur;
		while done = 0 do
			fetch cur into yyear, mmonth, count, dep;    
            insert into report_layoff_doctor(`year`, `month`, count_doctors, department)
      values (yyear, mmonth, count, dep);
        end while;
    close cur;
end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `new_view`
--

/*!50001 DROP VIEW IF EXISTS `new_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `new_view` AS select `visit`.`id_doctor` AS `id_doctor`,count(0) AS `COUNT(*)` from `visit` where (year(`visit`.`appoint_date`) = 2020) group by `visit`.`id_doctor` order by count(0) desc limit 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-25 10:54:03
