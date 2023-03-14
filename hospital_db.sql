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
DROP DATABASE IF EXISTS `test`;

CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `test` ;



-- -----------------------------------------------------
-- Table `test`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`appointment` (
  `idappointment` INT NOT NULL AUTO_INCREMENT UNIQUE,
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
  `username` VARCHAR(45) NOT NULL UNIQUE,
  `password` VARCHAR(45) NOT NULL,
  `idnurse` INT NOT NULL AUTO_INCREMENT UNIQUE,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `street` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `date_of_birth` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `Classification` VARCHAR(45) NOT NULL,
  `DepartmentID` VARCHAR(45) NOT NULL,
  `ClinicID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idnurse`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`patient` (
  `idpatient` INT NOT NULL AUTO_INCREMENT UNIQUE,
 `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `street` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `date_of_birth` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idpatient`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`physician`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`physician` (
  `username` VARCHAR(45) NOT NULL UNIQUE,
  `password` VARCHAR(45) NOT NULL,
  `idphysician` INT NOT NULL AUTO_INCREMENT UNIQUE,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `street` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `date_of_birth` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Specialization` VARCHAR(45) NOT NULL,
  `DepartmentID` VARCHAR(45) NOT NULL,
  `ClinicID` VARCHAR(45) NOT NULL,
  

  
  PRIMARY KEY (`idphysician`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`schedule` (
  `idphysician` INT NOT NULL,
  `monday` BIT,
  `tuesday` BIT,
  `wednesday` BIT,
  `thursday` BIT,
  `friday` BIT,
  `saturday` BIT,
  `sunday` BIT,
  `monTL` VARCHAR(100),
  `tueTL` VARCHAR(100),
  `wedTL` VARCHAR(100),
  `thursTL` VARCHAR(100),
  `friTL` VARCHAR(100),
  `satTL` VARCHAR(100),
  `sunTL` VARCHAR(100),
  PRIMARY KEY (`idphysician`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user` (
  `username` VARCHAR(45) NOT NULL UNIQUE,
  `password` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `street` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `date_of_birth` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`username`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `test` ;

-- -----------------------------------------------------
-- procedure sp_setHours
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_setHours`(
	IN `p_idphysician` INT,
    IN  `p_monday` BIT,
    IN  `p_tuesday` BIT,
    IN  `p_wednesday` BIT,
    IN  `p_thursday` BIT,
    IN  `p_friday` BIT,
    IN  `p_saturday` BIT,
    IN  `p_sunday` BIT,
    IN  `p_monTL` VARCHAR(100),
    IN  `p_tueTL` VARCHAR(100),
    IN  `p_wedTL` VARCHAR(100),
    IN  `p_thursTL` VARCHAR(100),
    IN  `p_friTL` VARCHAR(100),
    IN  `p_satTL` VARCHAR(100),
    IN  `p_sunTL` VARCHAR(100)


)
BEGIN
    if (select exists (select 1 from schedule where idphysician = p_idphysician) ) then
        update schedule set monday = p_monday and tuesday = p_tuesday and wednesday = p_wednesday
         and thursday = p_thursday and friday = p_friday and saturday = p_saturday and
          sunday = p_sunday and monTL = p_monTL and tueTL = p_tueTL and
           wedTL = p_wedTL and thursTL = p_thursTL and friTL = p_friTL and satTL = p_satTL
            and sunTL = p_sunTL where idphysician = p_idphysician;
    else
        insert into schedule (idphysician, monday, tuesday, wednesday, thursday, friday, saturday, sunday, monTL, tueTL, wedTL, thursTL, friTL, satTL, sunTL)
        values (p_idphysician, p_monday, p_tuesday, p_wednesday, p_thursday, p_friday, p_saturday, p_sunday, p_monTL, p_tueTL, p_wedTL, p_thursTL, p_friTL, p_satTL, p_sunTL);
    end if;

END$$

DELIMITER ;


-- -----------------------------------------------------
-- procedure sp_createUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(45),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from user where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into user
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email
		);
	END IF;
END$$

DELIMITER ;
-- -----------------------------------------------------
-- procedure user_login
-- -----------------------------------------------------
USE `test`;
DROP procedure IF EXISTS `sp_validateLogin`;

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(username varchar(45), password varchar(45))
BEGIN
select * from user where ( user.username = username) and (user.password = password);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createPhysician
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createPhysician`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(45),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45),
    IN p_type VARCHAR(45),IN p_specialization VARCHAR(45),IN p_deptId VARCHAR(45),
    IN p_clinicId VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from physician where username = p_username) ) THEN
		select 'Username exists!!';
	else
      insert into user
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email
		);
		
        insert into physician
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`,`Type`,`Specialization`,`DepartmentID`,`ClinicID`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,p_type,p_specialization,p_deptId,p_clinicId
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createNurse
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createNurse`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(45),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45),
    IN p_type VARCHAR(45),IN p_Classification VARCHAR(45),IN p_deptId VARCHAR(45),
    IN p_clinicId VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from nurse where username = p_username) ) THEN
		select 'Username exists!!';
	else
		
        insert into nurse
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`,`Classification`,`DepartmentID`,`ClinicID`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,p_Classification,p_deptId,p_clinicId
		);
	END IF;
END$$

DELIMITER ;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
