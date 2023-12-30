-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: work1
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Temporary view structure for view `team_league_player_view`
--

DROP TABLE IF EXISTS `team_league_player_view`;
/*!50001 DROP VIEW IF EXISTS `team_league_player_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `team_league_player_view` AS SELECT 
 1 AS `teamname`,
 1 AS `scores`,
 1 AS `fame`,
 1 AS `homecount`,
 1 AS `profit`,
 1 AS `ranking`,
 1 AS `leaguename`,
 1 AS `level`,
 1 AS `nation`,
 1 AS `playername`,
 1 AS `playnumber`,
 1 AS `status`,
 1 AS `age`,
 1 AS `usedfoot`,
 1 AS `height`,
 1 AS `weight`,
 1 AS `goals`,
 1 AS `assists`,
 1 AS `appearances`,
 1 AS `startings`,
 1 AS `nogoaltimes`,
 1 AS `averagecomments`,
 1 AS `playposition`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `team_league_player_view`
--

/*!50001 DROP VIEW IF EXISTS `team_league_player_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `team_league_player_view` AS select `t`.`teamname` AS `teamname`,`t`.`scores` AS `scores`,`t`.`fame` AS `fame`,`t`.`homecount` AS `homecount`,`t`.`profit` AS `profit`,`t`.`ranking` AS `ranking`,`l`.`leaguename` AS `leaguename`,`l`.`level` AS `level`,`l`.`nation` AS `nation`,`p`.`playername` AS `playername`,`p`.`playnumber` AS `playnumber`,`p`.`status` AS `status`,`p`.`age` AS `age`,`p`.`usedfoot` AS `usedfoot`,`p`.`height` AS `height`,`p`.`weight` AS `weight`,`p`.`goals` AS `goals`,`p`.`assists` AS `assists`,`p`.`appearances` AS `appearances`,`p`.`startings` AS `startings`,`p`.`nogoaltimes` AS `nogoaltimes`,`p`.`averagecomments` AS `averagecomments`,`p`.`playposition` AS `playposition` from ((`team` `t` join `league` `l` on((`t`.`leaguename` = `l`.`leaguename`))) join `player` `p` on((`t`.`teamname` = `p`.`teamname`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping events for database 'work1'
--

--
-- Dumping routines for database 'work1'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-01 22:25:37
