-- MySQL dump 10.13  Distrib 5.6.20, for Win64 (x86_64)
--
-- Host: localhost    Database: test_db
-- ------------------------------------------------------
-- Server version	5.6.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data_validation`
--

DROP TABLE IF EXISTS `data_validation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_validation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(255) DEFAULT NULL,
  `raw_table_name` varchar(255) DEFAULT NULL,
  `table_column` varchar(255) DEFAULT NULL,
  `data_types` varchar(100) DEFAULT NULL,
  `raw_column_field` varchar(200) DEFAULT NULL,
  `column_order` int(11) DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_validation`
--

LOCK TABLES `data_validation` WRITE;
/*!40000 ALTER TABLE `data_validation` DISABLE KEYS */;
INSERT INTO `data_validation` VALUES (1,'Teletech','zzz_teletech_candidate_raw','teletech_candidate_raw_id','','',1,'2015-09-14'),(2,'Teletech','zzz_teletech_candidate_raw','id','int','',2,'2015-09-14'),(3,'Teletech','zzz_teletech_candidate_raw','id_date','datetime','ID_Date',3,'2015-09-14'),(4,'Teletech','zzz_teletech_candidate_raw','auto_req_id','varchar','Requisition NO',4,'2015-09-14'),(5,'Teletech','zzz_teletech_candidate_raw','candidate_ref_num','int','Candidate ID',5,'2015-09-14'),(6,'Teletech','zzz_teletech_candidate_raw','candidate_f_name','varchar','Candidate First Name',6,'2015-09-14'),(7,'Teletech','zzz_teletech_candidate_raw','candidate_l_name','varchar','Candidate Last Name',7,'2015-09-14'),(8,'Teletech','zzz_teletech_candidate_raw','candidate_email','varchar','Candidate Email',8,'2015-09-14'),(9,'Teletech','zzz_teletech_candidate_raw','internal_external','varchar','Application is Internal',9,'2015-09-14'),(10,'Teletech','zzz_teletech_candidate_raw','ip_address','varchar','Application E-Signature IP Address',10,'2015-09-14'),(11,'Teletech','zzz_teletech_candidate_raw','candidate_status','varchar','Application Current CSW Step & Status',11,'2015-09-14'),(13,'Teletech','zzz_teletech_candidate_raw','candidate_start_date','datetime','Application Current CSW Start Date',13,'2015-09-14'),(14,'Teletech','zzz_teletech_candidate_raw','gender','varchar','Candidate Gender',14,'2015-09-14'),(15,'Teletech','zzz_teletech_candidate_raw','ethnicity_eeo2','varchar','Candidate Ethnicity (EEO2)',15,'2015-09-14'),(16,'Teletech','zzz_teletech_candidate_raw','ethnicity','varchar','Candidate Ethnicity',16,'2015-09-14'),(17,'Teletech','zzz_teletech_candidate_raw','source_id','int','Application Source ID (AWT)',17,'2015-09-14'),(18,'Teletech','zzz_teletech_candidate_raw','source_code','varchar','Application Source (ML)',18,'2015-09-14'),(19,'Teletech','zzz_teletech_candidate_raw','source_code_description','varchar','Application Source Type (Administration)',19,'2015-09-14'),(20,'Teletech','zzz_teletech_candidate_raw','candidate_csw_workflow_name','varchar','Req. CSW Workflow Name',20,'2015-09-14'),(21,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Offshore0912CALLSIM','datetime','ApplicantPool-Offshore 0912CALLSIM',21,'2015-09-14'),(22,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Offshore0912CLIENTVAL','datetime','ApplicantPool-Offshore 0912CLIENTVAL',22,'2015-09-14'),(23,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Offshore0912MP','datetime','ApplicantPool-Offshore 0912MP',23,'2015-09-14'),(24,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Offshore0912NEW','datetime','ApplicantPool-Offshore 0912NEW',24,'2015-09-14'),(25,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Offshore0912PREGTASOFF','datetime','ApplicantPool-Offshore 0912PREGTASOFF',25,'2015-09-14'),(26,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Offshore0912PREONSITE','datetime','ApplicantPool-Offshore 0912PREONSITE',26,'2015-09-14'),(27,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Onshore0314INTERVIEW','datetime','ApplicantPool-Onshore 0314INTERVIEW',27,'2015-09-14'),(28,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Onshore0513ASSESS','datetime','ApplicantPool-Onshore 0513ASSESS',28,'2015-09-14'),(29,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Onshore0912ACEREV','datetime','ApplicantPool-Onshore 0912ACEREV',29,'2015-09-14'),(30,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Onshore0912MP','datetime','ApplicantPool-Onshore 0912MP',20,'2015-09-14'),(31,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Onshore0912SCHED','datetime','ApplicantPool-Onshore 0912SCHED',1,'2015-09-14'),(32,'Teletech','zzz_teletech_candidate_raw','ApplicantPool_Onshorez0912INT','datetime','ApplicantPool-Onshore z0912INT',32,'2015-09-14'),(33,'Teletech','zzz_teletech_candidate_raw','ClassOnshoreandOffshore00HIRE','datetime','Class Onshore and Offshore 00HIRE',33,'2015-09-14'),(34,'Teletech','zzz_teletech_candidate_raw','ClassOnshoreandOffshore0912BCONOFF','datetime','Class Onshore and Offshore 0912BCONOFF',34,'2015-09-14'),(35,'Teletech','zzz_teletech_candidate_raw','ClassOnshoreandOffshoreRSOFFER','datetime','Class Onshore and Offshore RSOFFER',35,'2015-09-14');
/*!40000 ALTER TABLE `data_validation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-06 11:19:03
