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
  `id_department` int NOT NULL,
  `name_department` varchar(45) DEFAULT NULL,
  `floor` int DEFAULT NULL,
  `head` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `passport_data` double DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `specialization` varchar(45) DEFAULT NULL,
  `date_startwork` date DEFAULT NULL,
  `date_layoff` date DEFAULT NULL,
  `id_department` int DEFAULT NULL,
  `doctor_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_doctor`),
  KEY `id_department_idx` (`id_department`),
  CONSTRAINT `id_department` FOREIGN KEY (`id_department`) REFERENCES `department` (`id_department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,8497033505,'108777, Ленинградская область, город Озёры, въезд Бухарестская, 12','1973-04-23','физиотерапевт','1999-11-19','2019-03-23',3,'Соколова'),(2,3054466812,'462624, Новгородская область, город Павловский Посад, пр. 1905 года, 55','1968-05-06','врач-рентгенолог','2008-07-27','2018-08-04',4,'Галкин'),(3,3955665746,'885547, Ярославская область, город Серпухов, пл. Ломоносова, 99','1972-04-20','неврология','2018-10-11',NULL,2,'Мельникова'),(4,8952487959,'911964, Амурская область, город Люберцы, пл. Космонавтов, 68','1977-02-06','массажист','2015-08-11',NULL,3,'Вешнякова'),(5,1869169490,'669452, Кировская область, город Егорьевск, наб. Бухарестская, 29','1977-02-02','врач-терапевт','2005-05-29',NULL,1,'Агафонова'),(6,2129791421,'306289, Кировская область, город Красногорск, пер. Чехова, 49','1972-09-06','лаборант дневной смены','2014-11-03',NULL,8,'Никонова'),(7,8381861397,'361823, Магаданская область, город Зарайск, шоссе Ленина, 80','1991-09-24','стоматолог-терапевт','2009-06-19',NULL,7,'Васильева'),(8,5668374899,'637915, Сахалинская область, город Серпухов, пр. Космонавтов, 75','1967-01-30','врач-рентгенолог','1999-11-19',NULL,4,'Кузнецова'),(9,2927382493,'678613, Нижегородская область, город Серпухов, пр. Домодедовская, 73','1979-03-23','стоматолог-хирург','2009-12-06','2011-12-02',7,'Ковалева'),(10,1672799206,'379218, Курганская область, город Коломна, спуск Сталина, 98','1996-10-06','медицинская сестра','2007-03-22',NULL,1,'Троицкая');
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
  CONSTRAINT `id_department_office` FOREIGN KEY (`id_department`) REFERENCES `department` (`id_department`)
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
-- Table structure for table `shedule`
--

DROP TABLE IF EXISTS `shedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shedule` (
  `id_shedule` int NOT NULL,
  `id_office` int DEFAULT NULL,
  `rec_date` date DEFAULT NULL,
  `rec_time` time DEFAULT NULL,
  `id_visit_card` int DEFAULT NULL,
  `app_mark` tinyint DEFAULT NULL,
  `id_doctor` int DEFAULT NULL,
  PRIMARY KEY (`id_shedule`),
  KEY `id_office_idx` (`id_office`),
  KEY `id_visit_card_idx` (`id_visit_card`),
  KEY `id_docotr_idx` (`id_doctor`) /*!80000 INVISIBLE */,
  CONSTRAINT `id_docotr` FOREIGN KEY (`id_doctor`) REFERENCES `doctor` (`id_doctor`),
  CONSTRAINT `id_office` FOREIGN KEY (`id_office`) REFERENCES `office` (`id_office`),
  CONSTRAINT `id_visit_card` FOREIGN KEY (`id_visit_card`) REFERENCES `visit_card` (`id_visit_card`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shedule`
--

LOCK TABLES `shedule` WRITE;
/*!40000 ALTER TABLE `shedule` DISABLE KEYS */;
INSERT INTO `shedule` VALUES (1,9,'2022-10-24','10:38:00',2,1,3),(2,3,'2022-06-21','17:24:00',10,1,3),(3,2,'2019-11-22','13:39:00',2,1,5),(4,8,'2020-12-31','13:21:00',10,1,3),(5,2,'2023-05-03','16:51:00',2,1,5),(6,10,'2024-11-20','20:46:00',7,0,6),(7,10,'2024-11-20','20:40:00',3,0,6),(8,10,'2024-11-20','20:41:00',2,0,6),(9,5,'2020-10-31','11:00:00',10,1,10),(10,6,'2024-11-20','10:54:00',4,1,8),(11,4,'2022-03-13','14:46:00',1,0,4),(12,3,'2022-03-02','14:46:00',5,0,5),(13,2,'2024-12-22','14:46:00',8,0,5),(14,2,'2024-12-22','14:46:00',NULL,NULL,5),(15,2,'2024-12-22','14:30:00',NULL,NULL,5),(16,2,'2024-12-20','14:30:00',2,NULL,5),(17,2,'2024-12-20','14:00:00',2,NULL,5);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'123','abc','doctor',6),(2,'2','v','register',1);
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
  KEY `id_visit_ca_idx` (`id_visit_card`),
  CONSTRAINT `id_doctor_visit` FOREIGN KEY (`id_doctor`) REFERENCES `doctor` (`id_doctor`),
  CONSTRAINT `id_visit_ca` FOREIGN KEY (`id_visit_card`) REFERENCES `visit_card` (`id_visit_card`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit`
--

LOCK TABLES `visit` WRITE;
/*!40000 ALTER TABLE `visit` DISABLE KEYS */;
INSERT INTO `visit` VALUES (1,'2021-10-06','острая недостаточность сна','усталость','прописан в рецепте',2,6),(2,'2020-12-31','грипп','усталость','прописан в рецепте',10,3),(3,'2020-10-31','зубная боль','усталость','прописан в рецепте',10,10),(4,'2019-12-21','простуда','усталость','прописан в рецепте',3,6),(5,'2023-05-03','пневмония','усталость','прописан в рецепте',2,5),(6,'2019-11-22','грипп','усталость','прописан в рецепте',2,5),(7,'2022-01-13','острая недостаточность котов','усталость','прописан в рецепте',4,8),(8,'2022-10-24','острая недостаточность витамина D','усталость','прописан в рецепте',2,3),(9,'2022-06-21','перелом ребер','усталость','прописан в рецепте',10,3),(10,'2020-04-26','ушиб ноги','усталость','прописан в рецепте',7,6),(11,'2024-11-19','11','1','1',7,6);
/*!40000 ALTER TABLE `visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit_card`
--

DROP TABLE IF EXISTS `visit_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit_card` (
  `id_visit_card` int NOT NULL,
  `passport_data` double DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `date_create` date DEFAULT NULL,
  `name_patient` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_visit_card`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit_card`
--

LOCK TABLES `visit_card` WRITE;
/*!40000 ALTER TABLE `visit_card` DISABLE KEYS */;
INSERT INTO `visit_card` VALUES (1,7831563830,'907214, Костромская область, город Павловский Посад, пер. Гоголя, 05','1978-06-28','2020-03-21','Назаров'),(2,4893455526,'294371, Оренбургская область, город Мытищи, пер. Будапештсткая, 69','1993-12-11','2020-03-19','Лаврентьев'),(3,9844133849,'449883, Самарская область, город Люберцы, ул. Космонавтов, 96','1995-04-02','2020-01-31','Тихонов'),(4,7463236436,'255747, Липецкая область, город Серебряные Пруды, пр. Гоголя, 94','1992-12-14','2020-01-27','Беляев'),(5,1175355076,'451544, Сахалинская область, город Чехов, пер. Домодедовская, 08','1976-12-17','2020-05-12','Петрова'),(6,8252878530,'961889, Архангельская область, город Дмитров, проезд Косиора, 65','1981-11-12','2020-02-19','Соболев'),(7,9180189001,'371130, Белгородская область, город Орехово-Зуево, шоссе Сталина, 07','1982-02-01','2020-02-12','Овчинникова'),(8,5728854553,'232060, Тверская область, город Видное, пр. Балканская, 99','1965-11-09','2020-07-01','Емельянова'),(9,6796203413,'171999, Кировская область, город Орехово-Зуево, пер. Косиора, 79','1979-12-19','2020-02-26','Давыдов'),(10,9784122200,'370219, Самарская область, город Сергиев Посад, проезд Ломоносова, 28','1967-09-12','2020-09-05','Федотов'),(11,7831563831,'570858, Челябинская область, город Люберцы, шоссе Космонавтов, 34','1995-04-02','2024-03-19','Сергеева'),(12,7831563832,'728089, Мурманская область, город Шатура, бульвар Ладыгина, 50','1995-04-02','2024-03-18','Гаврилов'),(13,7831563833,'290490, Омская область, город Зарайск, пл. 1905 года, 53','1995-04-02','2024-03-18','Осипов'),(14,7831563834,'782858, Волгоградская область, город Мытищи, наб. Космонавтов, 95','1995-04-02','2024-03-19','Устинов');
/*!40000 ALTER TABLE `visit_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'new_schema'
--

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

-- Dump completed on 2024-11-21 13:25:47
