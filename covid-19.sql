CREATE DATABASE `covid-19` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- `covid-19`.world_confirm_date definition

CREATE TABLE `world_confirm_date` (
  `Date` date NOT NULL,
  `Australia` int DEFAULT NULL,
  `Canada` int DEFAULT NULL,
  `China` int DEFAULT NULL,
  `Colombia` int DEFAULT NULL,
  `Egypt` int DEFAULT NULL,
  `France` int DEFAULT NULL,
  `Germany` int DEFAULT NULL,
  `India` int DEFAULT NULL,
  `Iran` int DEFAULT NULL,
  `Italy` int DEFAULT NULL,
  `Japan` int DEFAULT NULL,
  `New Zealand` int DEFAULT NULL,
  `South Africa` int DEFAULT NULL,
  `Thailand` int DEFAULT NULL,
  `United Kingdom` int DEFAULT NULL,
  `sum` int DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- `covid-19`.world_data definition

CREATE TABLE `world_data` (
  `country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `total_confirm` int DEFAULT NULL,
  `total_vaccinated` int DEFAULT NULL,
  `total_death` int DEFAULT NULL,
  PRIMARY KEY (`country`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- `covid-19`.world_date_gender definition

CREATE TABLE `world_date_gender` (
  `country` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `confirm_male` int DEFAULT NULL,
  `confirm_female` int DEFAULT NULL,
  `death_male` int DEFAULT NULL,
  `death_femal` int DEFAULT NULL,
  PRIMARY KEY (`country`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- `covid-19`.world_death_date definition

CREATE TABLE `world_death_date` (
  `Date` date NOT NULL,
  `Australia` int DEFAULT NULL,
  `Canada` int DEFAULT NULL,
  `China` int DEFAULT NULL,
  `Colombia` int DEFAULT NULL,
  `Egypt` int DEFAULT NULL,
  `France` int DEFAULT NULL,
  `Germany` int DEFAULT NULL,
  `India` int DEFAULT NULL,
  `Iran` int DEFAULT NULL,
  `Italy` int DEFAULT NULL,
  `Japan` int DEFAULT NULL,
  `New Zealand` int DEFAULT NULL,
  `South Africa` int DEFAULT NULL,
  `Thailand` int DEFAULT NULL,
  `United Kingdom` int DEFAULT NULL,
  `sum` int DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- `covid-19`.world_vaccinated_date definition

CREATE TABLE `world_vaccinated_date` (
  `Date` date NOT NULL,
  `Australia` int DEFAULT NULL,
  `Canada` int DEFAULT NULL,
  `China` int DEFAULT NULL,
  `Colombia` int DEFAULT NULL,
  `Egypt` int DEFAULT NULL,
  `France` int DEFAULT NULL,
  `Germany` int DEFAULT NULL,
  `India` int DEFAULT NULL,
  `Iran` int DEFAULT NULL,
  `Italy` int DEFAULT NULL,
  `Japan` int DEFAULT NULL,
  `New Zealand` int DEFAULT NULL,
  `South Africa` int DEFAULT NULL,
  `Thailand` int DEFAULT NULL,
  `United Kingdom` int DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- `covid-19`.world_vaccine definition

CREATE TABLE `world_vaccine` (
  `country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `vaccination_type` varchar(50) NOT NULL,
  PRIMARY KEY (`country`,`vaccination_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;