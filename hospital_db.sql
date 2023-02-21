-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `test` ;

-- -----------------------------------------------------
-- Table `test`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`appointment` (
  `idappointment` INT NOT NULL AUTO_INCREMENT,
  `appointment_date` DATETIME NOT NULL,
  `idpatient` INT NOT NULL,
  `idphysician` INT NOT NULL,
  `description` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`idappointment`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`nurse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`nurse` (
  `idnurse` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `iduser` INT NOT NULL,
  PRIMARY KEY (`idnurse`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`patient` (
  `idpatient` INT NOT NULL,
  `idnurse` INT NULL DEFAULT NULL,
  `idphysician` INT NOT NULL,
  `iduser` INT NOT NULL,
  PRIMARY KEY (`idpatient`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`physician`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`physician` (
  `idphysician` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `iduser` INT NOT NULL,
  PRIMARY KEY (`idphysician`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(15) NOT NULL,
  `password` VARCHAR(15) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `phone_no` VARCHAR(15) NOT NULL,
  `status` INT NOT NULL COMMENT '0 - Patient\\n1 - Nurse\\n2 - Physician\\n3 - Admin',
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `test` ;

-- -----------------------------------------------------
-- procedure get_hospitals
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_hospitals`()
BEGIN
	SELECT * FROM hospital;
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
