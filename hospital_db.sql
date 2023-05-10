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
-- Table `test`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`admin` (
  `idpadmin` INT NOT NULL,
  `idDepartment` INT NOT NULL,
  PRIMARY KEY (`idpadmin`),
  UNIQUE INDEX `idpadmin` (`idpadmin` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`insurance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`insurance` (
  `insuranceID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  discount FLOAT NOT NULL,
  copay INT NOT NULL,
  PRIMARY KEY (`insuranceID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

insert into insurance values (1, 'united', .20, 10);
insert into insurance values (2, 'bcbs', .10, 20);

-- -----------------------------------------------------
-- Table `test`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`appointment` (
  `idappointment` INT NOT NULL AUTO_INCREMENT,
  `appointment_date` DATETIME NOT NULL,
  `idpatient` INT NOT NULL,
  `idphysician` INT NOT NULL,
  `description` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`idappointment`),
  UNIQUE INDEX `idappointment` (`idappointment` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`afterVisit` (
 `id` INT NOT NULL AUTO_INCREMENT,
  `idappointment` INT NOT NULL ,
  `summary` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id` (`id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`bed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`bed` (
  `idbed` INT NOT NULL AUTO_INCREMENT,
  `idclinic` INT NULL DEFAULT NULL,
  `room_number` VARCHAR(45) NOT NULL,
  `occupancy_status` VARCHAR(45) NOT NULL,
  `idpatient` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idbed`),
  UNIQUE INDEX `idbed` (`idbed` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`clinic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`clinic` (
  `idclinic` INT NOT NULL AUTO_INCREMENT,
  `clinic_name` VARCHAR(45) NOT NULL,
  `location` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idclinic`),
  UNIQUE INDEX `idclinic` (`idclinic` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`contact_us_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`contact_us_messages` (
  `messageID` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `message` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`messageID`),
  UNIQUE INDEX `messageID` (`messageID` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`invoice` (
  `idinvoice` INT NOT NULL AUTO_INCREMENT,
  `idstatement` INT NOT NULL,
  `date` VARCHAR(45) NOT NULL,
  `charge` VARCHAR(45) NOT NULL,
  `insurance` INT NOT NULL,
  `total` INT NOT NULL,
  `description` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`idinvoice`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`nurse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`nurse` (
  `idnurse` INT NOT NULL,
  `Classification` VARCHAR(45) NOT NULL,
  `DepartmentID` VARCHAR(45) NOT NULL,
  `ClinicID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idnurse`),
  UNIQUE INDEX `idnurse` (`idnurse` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`patient` (
  `idpatient` INT NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`idpatient`),
  UNIQUE INDEX `idpatient` (`idpatient` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`physician`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`physician` (
  `idphysician` INT NOT NULL,
  `Specialization` VARCHAR(45) NOT NULL,
  `DepartmentID` VARCHAR(45) NOT NULL,
  `ClinicID` VARCHAR(45) NOT NULL,
  `Rank` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idphysician`),
  UNIQUE INDEX `idphysician` (`idphysician` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`schedule` (
  `idphysician` INT NOT NULL,
  `monTL` VARCHAR(100) NULL DEFAULT NULL,
  `tueTL` VARCHAR(100) NULL DEFAULT NULL,
  `wedTL` VARCHAR(100) NULL DEFAULT NULL,
  `thursTL` VARCHAR(100) NULL DEFAULT NULL,
  `friTL` VARCHAR(100) NULL DEFAULT NULL,
  `satTL` VARCHAR(100) NULL DEFAULT NULL,
  `sunTL` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`idphysician`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`statement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`statement` (
  `idstatement` INT NOT NULL AUTO_INCREMENT,
  `idpatient` VARCHAR(45) NOT NULL,
  `balance_due` INT NOT NULL,
  `due_date` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idstatement`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(103) NOT NULL,
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
  `type` VARCHAR(45) NOT NULL,
  `insurance` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `test` ;

---------
-- default admin user
---------
INSERT INTO `test`.`user` (`username`, `password`, `first_name`, `last_name`, `street`, `city`, `state`, `zip`, `phone`, `date_of_birth`, `sex`, `email`, `type`) VALUES ('admin', 'admin', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'admin');


-- -----------------------------------------------------
-- Table `test`.`billRates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`billRates` (
  `rateID` INT NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  `charge` INT NOT NULL,
  PRIMARY KEY (`rateID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

insert into billRates values (1, "Office Visit", 50);
insert into billRates values (2, "General Surgery", 3000);
insert into billRates values (3, "X-Ray", 100);
insert into billRates values (4, "Medication Refill", 30);
insert into billRates values (5, "Room Charge", 4000);
insert into billRates values (6, "Physical Therapy", 200);
insert into billRates values (7, "Labs", 100);

-- -----------------------------------------------------
-- procedure sp_addBeds
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addBeds`(idbed INT,idclinic INT,room_number varchar(45),occupancy_status varchar(45),idpatient INT)
BEGIN
insert into bed(idbed,idclinic,room_number,occupancy_status,idpatient)
values(idbed,idclinic,room_number,occupancy_status,idpatient);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_addContactUsMessage
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addContactUsMessage`(
    IN first_name VARCHAR(45),
    IN last_name VARCHAR(45),
    IN email VARCHAR(45),
    IN message MEDIUMTEXT
)
BEGIN
	INSERT INTO contact_us_messages
    (first_name, last_name, email, message)
    VALUES
    (first_name, last_name, email, message);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_addSummary
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addSummary`(p_idappointment INT,p_summary MEDIUMTEXT)
BEGIN
insert into bed(idappointment,summary )
values(p_idappointment, p_summary);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_changePassword
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_changePassword`(IN userID VARCHAR(45), IN `new_password` VARCHAR(103))
BEGIN
	UPDATE `user`
    SET `password` = new_password
    WHERE iduser = userID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createAdmin
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createAdmin`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45), IN p_deptId INT
)
BEGIN
    if ( select exists (select 1 from `user` where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into `user`
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`, `type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email, "admin"
		);
        insert into `admin`
        (
			`idpadmin`,`idDepartment`
		)
        values
        (
			LAST_INSERT_ID(), p_deptId
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createAppointment
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createAppointment`(
	IN `date` DATETIME,
    IN physician_id INT,
    IN patient_id INT,
    IN reason TEXT
)
BEGIN
	INSERT INTO appointment
    (appointment_date, idpatient, idphysician, `description`)
    VALUES
    (`date`, patient_id, physician_id, reason);
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createInvoice
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createInvoice`(
	IN statement INT,
    IN charge INT,
    IN insurance INT,
    IN total INT,
    IN `description` MEDIUMTEXT
)
BEGIN
	INSERT INTO invoice
    (idstatement, `date`, charge, insurance, total, `description`)
    VALUES (statement, current_date, charge, insurance, total, `description`);

    UPDATE statement
    SET `balance_due` = `balance_due` + total
    WHERE idstatement = statement;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- procedure sp_deleteInvoice
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteInvoice`(IN inID INT)
BEGIN
	DELETE FROM invoice
    WHERE idinvoice = inID;
END$$

DELIMITER ;



-- -----------------------------------------------------
-- procedure sp_getStatementByDescr
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getStatementByDescr`(IN d date)
BEGIN
	select idstatement from statement where date = d;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createNurse
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createNurse`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45),IN p_classification VARCHAR(45),IN p_deptId VARCHAR(45),
    IN p_clinicId VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from `user` where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into `user`
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`,`type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,"nurse"
		);
        insert into `nurse`
        (
			idnurse,`Classification`,`DepartmentID`,`ClinicID`
		)
        values
        (
			LAST_INSERT_ID(), p_classification, p_deptId, p_clinicId
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createPhysician
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createPhysician`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45),
    IN p_specialization VARCHAR(45),IN p_deptId VARCHAR(45),
    IN p_clinicId VARCHAR(45), IN p_rank VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from `user` where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into `user`
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`,`type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,"phys"
		);
        insert into `physician`
        (
			idphysician,`Specialization`,`DepartmentID`,`ClinicID`,`Rank`
		)
        values
        (
			LAST_INSERT_ID(),p_specialization, p_deptId, p_clinicId,p_rank
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createStatement
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createStatement`(
	IN patientid INT,
    IN balance INT,
    IN due_date VARCHAR(45)
)
BEGIN
	INSERT INTO statement
    (idpatient, balance_due, due_date)
    VALUES (patientid, balance, due_date);
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteStatement
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteStatement`(IN sID INT, IN pID VARCHAR(45))
BEGIN
	DELETE FROM statement
    WHERE idstatement = sID and idpatient = pID;
END$$

DELIMITER ;
-- -----------------------------------------------------
-- procedure sp_createUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
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
            `date_of_birth`,`sex`,`email`,`type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,"user"
		);
	END IF;
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteAppointment
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteAppointment`(
    IN appointmentID INT
)
BEGIN
    DELETE FROM appointment WHERE idappointment = appointmentID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteBeds
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteBeds`(p_idbed INT)
BEGIN
DELETE FROM bed where idbed=p_idbed;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteSchedule
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteSchedule`(pid INT)
BEGIN
DELETE FROM schedule where idphysician=pid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteUser`(p_username VARCHAR(45))
BEGIN
DELETE FROM user where username=p_username;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_findOwnPatient
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_findOwnPatient`(
    IN p_physicianid INT
    
)
BEGIN
	SELECT idpatient from appointment where idphysician=p_physicianid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getAppointments`(IN userID INT)
BEGIN
	SELECT * from appointment
    WHERE idpatient = userID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getBeds
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getBeds`()
BEGIN
select * from bed;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getContactUsMessages
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getContactUsMessages`()
BEGIN
SELECT * from test.contact_us_messages;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getInvoices`(IN statement INT)
BEGIN
	SELECT * FROM invoice
    WHERE idstatement = statement;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianAppointments`(IN userID INT)
BEGIN
	SELECT appointment.appointment_date, appointment.description,appointment.idpatient,user.first_name, user.last_name
	FROM appointment
	INNER JOIN user ON appointment.idpatient = user.iduser
    where appointment.idphysician=userID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPatientsFromAppt
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPatientsFromAppt`()
BEGIN
	SELECT user.iduser, user.first_name, user.last_name FROM appointment INNER JOIN user  on appointment.idpatient = user.iduser where appointment.appointment_date < now();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_assignBedAdmin
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_assignBedAdnin`(In p_idbed INT, IN p_idpatient INT)
BEGIN
      UPDATE bed SET `idpatient`=p_idpatient WHERE idbed = p_idbed AND EXISTS (select idpatient from user where iduser=p_idpatient);
    
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_dischargePatient
-- -----------------------------------------------------


DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_dischargePatient`(IN patient_id INT, IN physician_id INT,IN p_summary MEDIUMTEXT)
BEGIN
    DECLARE patient_exists INT DEFAULT 0;
    DECLARE appointment_exists INT DEFAULT 0;
    DECLARE appointment_id INT DEFAULT 0;
    
	
    
    -- check if patient exists in beds table
    SELECT COUNT(*) INTO patient_exists FROM bed WHERE idpatient = patient_id;
    
    IF patient_exists > 0 THEN
        -- check if patient exists in appointments table for the given physician
        SELECT COUNT(*) INTO appointment_exists FROM appointment WHERE idpatient = patient_id AND idphysician = physician_id;
        
        IF appointment_exists > 0 THEN
            -- update idbed to 0 for the given patient
            UPDATE bed SET idpatient = 0 WHERE idpatient = patient_id;
            select idappointment into appointment_id from appointment where idpatient=patient_id AND idphysician=physician_id;
            insert into afterVisit(idappointment,summary ) values(appointment_id, p_summary);
            SELECT CONCAT('Bed updated for patient with id ', patient_id) AS message;
        ELSE
            SELECT CONCAT('Patient with id ', patient_id, ' does not have an appointment with physician with id ', physician_id) AS message;
        END IF;
    ELSE
        SELECT CONCAT('Patient with id ', patient_id, ' does not exist in beds table.') AS message;
    END IF;
END$$

DELIMITER ;
-- -----------------------------------------------------
-- procedure sp_modifyBedLocation
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_modifyBedLocation`(In p_idbed INT,  IN p_room_number VARCHAR(45))
BEGIN
   UPDATE bed SET `room_number`=p_room_number WHERE idbed = p_idbed;
    
END$$

DELIMITER ;


-- -----------------------------------------------------
-- procedure sp_getPhysicianNameByID
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianNameByID`(IN physID INT)
BEGIN
	SELECT first_name, last_name FROM `user` WHERE iduser = physID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianSchedules
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianSchedules`()
BEGIN
SELECT * from test.schedule ;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianSchedulesById
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianSchedulesById`(IN p_userid INT)
BEGIN
SELECT * from test.schedule where idphysician=p_userid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysiciansByNameAndId
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysiciansByNameAndId`()
BEGIN
SELECT a.first_name, a.last_name, b.idphysician FROM test.user a JOIN test.physician b where a.iduser = b.idphysician;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getStatements
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getStatements`(
	IN patientid INT
)
BEGIN
	SELECT * FROM statement
    WHERE idpatient = patientid;
END$$

DELIMITER ;-- MySQL Workbench Forward Engineering

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
-- Table `test`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`admin` (
  `idpadmin` INT NOT NULL,
  `idDepartment` INT NOT NULL,
  PRIMARY KEY (`idpadmin`),
  UNIQUE INDEX `idpadmin` (`idpadmin` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`insurance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`insurance` (
  `insuranceID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  discount FLOAT NOT NULL,
  copay INT NOT NULL,
  PRIMARY KEY (`insuranceID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

insert into insurance values (1, 'united', .20, 10);
insert into insurance values (2, 'bcbs', .10, 20);

-- -----------------------------------------------------
-- Table `test`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`appointment` (
  `idappointment` INT NOT NULL AUTO_INCREMENT,
  `appointment_date` DATETIME NOT NULL,
  `idpatient` INT NOT NULL,
  `idphysician` INT NOT NULL,
  `description` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`idappointment`),
  UNIQUE INDEX `idappointment` (`idappointment` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`afterVisit` (
 `id` INT NOT NULL AUTO_INCREMENT,
  `idappointment` INT NOT NULL ,
  `summary` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id` (`id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `test`.`bed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`bed` (
  `idbed` INT NOT NULL AUTO_INCREMENT,
  `idclinic` INT NULL DEFAULT NULL,
  `room_number` VARCHAR(45) NOT NULL,
  `occupancy_status` VARCHAR(45) NOT NULL,
  `idpatient` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idbed`),
  UNIQUE INDEX `idbed` (`idbed` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`clinic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`clinic` (
  `idclinic` INT NOT NULL AUTO_INCREMENT,
  `clinic_name` VARCHAR(45) NOT NULL,
  `location` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idclinic`),
  UNIQUE INDEX `idclinic` (`idclinic` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`contact_us_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`contact_us_messages` (
  `messageID` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `message` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`messageID`),
  UNIQUE INDEX `messageID` (`messageID` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`invoice` (
  `idinvoice` INT NOT NULL AUTO_INCREMENT,
  `idstatement` INT NOT NULL,
  `date` VARCHAR(45) NOT NULL,
  `charge` VARCHAR(45) NOT NULL,
  `insurance` INT NOT NULL,
  `total` INT NOT NULL,
  `description` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`idinvoice`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`nurse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`nurse` (
  `idnurse` INT NOT NULL,
  `Classification` VARCHAR(45) NOT NULL,
  `DepartmentID` VARCHAR(45) NOT NULL,
  `ClinicID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idnurse`),
  UNIQUE INDEX `idnurse` (`idnurse` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`patient` (
  `idpatient` INT NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`idpatient`),
  UNIQUE INDEX `idpatient` (`idpatient` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`physician`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`physician` (
  `idphysician` INT NOT NULL,
  `Specialization` VARCHAR(45) NOT NULL,
  `DepartmentID` VARCHAR(45) NOT NULL,
  `ClinicID` VARCHAR(45) NOT NULL,
  `Rank` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idphysician`),
  UNIQUE INDEX `idphysician` (`idphysician` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`schedule` (
  `idphysician` INT NOT NULL,
  `monTL` VARCHAR(100) NULL DEFAULT NULL,
  `tueTL` VARCHAR(100) NULL DEFAULT NULL,
  `wedTL` VARCHAR(100) NULL DEFAULT NULL,
  `thursTL` VARCHAR(100) NULL DEFAULT NULL,
  `friTL` VARCHAR(100) NULL DEFAULT NULL,
  `satTL` VARCHAR(100) NULL DEFAULT NULL,
  `sunTL` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`idphysician`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`statement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`statement` (
  `idstatement` INT NOT NULL AUTO_INCREMENT,
  `idpatient` VARCHAR(45) NOT NULL,
  `balance_due` INT NOT NULL,
  `due_date` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idstatement`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(103) NOT NULL,
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
  `type` VARCHAR(45) NOT NULL,
  `insurance` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `test` ;

---------
-- default admin user
---------
INSERT INTO `test`.`user` (`username`, `password`, `first_name`, `last_name`, `street`, `city`, `state`, `zip`, `phone`, `date_of_birth`, `sex`, `email`, `type`) VALUES ('admin', 'admin', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'admin');


-- -----------------------------------------------------
-- Table `test`.`billRates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`billRates` (
  `rateID` INT NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  `charge` INT NOT NULL,
  PRIMARY KEY (`rateID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

insert into billRates values (1, "Office Visit", 50);
insert into billRates values (2, "General Surgery", 3000);
insert into billRates values (3, "X-Ray", 100);
insert into billRates values (4, "Medication Refill", 30);
insert into billRates values (5, "Room Charge", 4000);
insert into billRates values (6, "Physical Therapy", 200);
insert into billRates values (7, "Labs", 100);

-- -----------------------------------------------------
-- procedure sp_Identify_UserType
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Identify_UserType`(username varchar(45), password varchar(45))
BEGIN
SELECT CASE
         WHEN EXISTS (SELECT * FROM physician WHERE physician.username =username) THEN 'Physician'
         WHEN EXISTS (SELECT * FROM nurse WHERE nurse.username =username) THEN 'Nurse'
         WHEN EXISTS (SELECT * FROM user WHERE user.username =username) THEN 'User'
       END;

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_addBeds
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addBeds`(idbed INT,idclinic INT,room_number varchar(45),occupancy_status varchar(45),idpatient INT)
BEGIN
insert into bed(idbed,idclinic,room_number,occupancy_status,idpatient)
values(idbed,idclinic,room_number,occupancy_status,idpatient);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_addContactUsMessage
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addContactUsMessage`(
    IN first_name VARCHAR(45),
    IN last_name VARCHAR(45),
    IN email VARCHAR(45),
    IN message MEDIUMTEXT
)
BEGIN
	INSERT INTO contact_us_messages
    (first_name, last_name, email, message)
    VALUES
    (first_name, last_name, email, message);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_addSummary
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addSummary`(p_idappointment INT,p_summary MEDIUMTEXT)
BEGIN
insert into bed(idappointment,summary )
values(p_idappointment, p_summary);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getContactUsMessages
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_assignBed`(In p_idbed INT, IN p_idpatient INT)
BEGIN
   UPDATE bed SET `idpatient`=p_idpatient WHERE idbed = p_idbed;

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_changePassword
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_changePassword`(IN userID VARCHAR(45), IN `new_password` VARCHAR(103))
BEGIN
	UPDATE `user`
    SET `password` = new_password
    WHERE iduser = userID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createAdmin
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createAdmin`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45), IN p_deptId INT
)
BEGIN
    if ( select exists (select 1 from `user` where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into `user`
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`, `type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email, "admin"
		);
        insert into `admin`
        (
			`idpadmin`,`idDepartment`
		)
        values
        (
			LAST_INSERT_ID(), p_deptId
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createAppointment
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createAppointment`(
	IN `date` DATETIME,
    IN physician_id INT,
    IN patient_id INT,
    IN reason TEXT
)
BEGIN
	INSERT INTO appointment
    (appointment_date, idpatient, idphysician, `description`)
    VALUES
    (`date`, patient_id, physician_id, reason);
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createInvoice
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createInvoice`(
	IN statement INT,
    IN charge INT,
    IN insurance INT,
    IN total INT,
    IN `description` MEDIUMTEXT
)
BEGIN
	INSERT INTO invoice
    (idstatement, `date`, charge, insurance, total, `description`)
    VALUES (statement, current_date, charge, insurance, total, `description`);

    UPDATE statement
    SET `balance_due` = `balance_due` + total
    WHERE idstatement = statement;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- procedure sp_deleteInvoice
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteInvoice`(IN inID INT)
BEGIN
	DELETE FROM invoice
    WHERE idinvoice = inID;
END$$

DELIMITER ;



-- -----------------------------------------------------
-- procedure sp_getStatementByDescr
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getStatementByDescr`(IN d date)
BEGIN
	select idstatement from statement where date = d;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createNurse
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createNurse`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45),IN p_classification VARCHAR(45),IN p_deptId VARCHAR(45),
    IN p_clinicId VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from `user` where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into `user`
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`,`type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,"nurse"
		);
        insert into `nurse`
        (
			idnurse,`Classification`,`DepartmentID`,`ClinicID`
		)
        values
        (
			LAST_INSERT_ID(), p_classification, p_deptId, p_clinicId
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createPhysician
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createPhysician`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45),
    IN p_specialization VARCHAR(45),IN p_deptId VARCHAR(45),
    IN p_clinicId VARCHAR(45), IN p_rank VARCHAR(45)
)
BEGIN
	if ( select exists (select 1 from `user` where username = p_username) ) THEN
		select 'Username exists!!';
	else

        insert into `user`
        (
			`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`,`type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,"phys"
		);
        insert into `physician`
        (
			idphysician,`Specialization`,`DepartmentID`,`ClinicID`,`Rank`
		)
        values
        (
			LAST_INSERT_ID(),p_specialization, p_deptId, p_clinicId,p_rank
		);
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_createStatement
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createStatement`(
	IN patientid INT,
    IN balance INT,
    IN due_date VARCHAR(45)
)
BEGIN
	INSERT INTO statement
    (idpatient, balance_due, due_date)
    VALUES (patientid, balance, due_date);
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteStatement
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteStatement`(IN sID INT, IN pID VARCHAR(45))
BEGIN
	DELETE FROM statement
    WHERE idstatement = sID and idpatient = pID;
END$$

DELIMITER ;
-- -----------------------------------------------------
-- procedure sp_createUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
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
            `date_of_birth`,`sex`,`email`,`type`
		)
        values
        (
			p_username,p_password,p_FN ,p_LN,p_street,p_city,p_state,p_zip,p_phone,
            p_dob ,p_sex,p_email,"user"
		);
	END IF;
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteAppointment
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteAppointment`(
    IN appointmentID INT
)
BEGIN
    DELETE FROM appointment WHERE idappointment = appointmentID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteBeds
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteBeds`(p_idbed INT)
BEGIN
DELETE FROM bed where idbed=p_idbed;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteSchedule
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteSchedule`(pid INT)
BEGIN
DELETE FROM schedule where idphysician=pid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteUser`(p_username VARCHAR(45))
BEGIN
DELETE FROM user where username=p_username;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_findOwnPatient
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_findOwnPatient`(
    IN p_physicianid INT

)
BEGIN
	SELECT idpatient from appointment where idphysician=p_physicianid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getAppointments`(IN userID INT)
BEGIN
	SELECT * from appointment
    WHERE idpatient = userID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getBeds
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getBeds`()
BEGIN
select * from bed;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getContactUsMessages
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getContactUsMessages`()
BEGIN
SELECT * from test.contact_us_messages;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getInvoices`(IN statement INT)
BEGIN
	SELECT * FROM invoice
    WHERE idstatement = statement;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianAppointments`(IN userID INT)
BEGIN
	SELECT appointment.appointment_date, appointment.description,appointment.idpatient,user.first_name, user.last_name
	FROM appointment
	INNER JOIN user ON appointment.idpatient = user.iduser
    where appointment.idphysician=userID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPatientsFromAppt
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_assignBed`(In p_idbed INT, IN p_idpatient INT,IN p_idphysician INT)
BEGIN
      UPDATE bed SET `idpatient`=p_idpatient WHERE idbed = p_idbed AND EXISTS (select idpatient,idphysician from appointment where p_idpatient=idpatient AND p_idphysician=idphysician);

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_assignBedAdmin
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_assignBedAdnin`(In p_idbed INT, IN p_idpatient INT)
BEGIN
      UPDATE bed SET `idpatient`=p_idpatient WHERE idbed = p_idbed AND EXISTS (select idpatient from user where iduser=p_idpatient);

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_dischargePatient
-- -----------------------------------------------------


DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_dischargePatient`(IN patient_id INT, IN physician_id INT,IN p_summary MEDIUMTEXT)
BEGIN
    DECLARE patient_exists INT DEFAULT 0;
    DECLARE appointment_exists INT DEFAULT 0;
    DECLARE appointment_id INT DEFAULT 0;



    -- check if patient exists in beds table
    SELECT COUNT(*) INTO patient_exists FROM bed WHERE idpatient = patient_id;

    IF patient_exists > 0 THEN
        -- check if patient exists in appointments table for the given physician
        SELECT COUNT(*) INTO appointment_exists FROM appointment WHERE idpatient = patient_id AND idphysician = physician_id;

        IF appointment_exists > 0 THEN
            -- update idbed to 0 for the given patient
            UPDATE bed SET idpatient = 0 WHERE idpatient = patient_id;
            select idappointment into appointment_id from appointment where idpatient=patient_id AND idphysician=physician_id;
            insert into afterVisit(idappointment,summary ) values(appointment_id, p_summary);
            SELECT CONCAT('Bed updated for patient with id ', patient_id) AS message;
        ELSE
            SELECT CONCAT('Patient with id ', patient_id, ' does not have an appointment with physician with id ', physician_id) AS message;
        END IF;
    ELSE
        SELECT CONCAT('Patient with id ', patient_id, ' does not exist in beds table.') AS message;
    END IF;
END$$

DELIMITER ;
-- -----------------------------------------------------
-- procedure sp_modifyBedLocation
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_modifyBedLocation`(In p_idbed INT,  IN p_room_number VARCHAR(45))
BEGIN
   UPDATE bed SET `room_number`=p_room_number WHERE idbed = p_idbed;

END$$

DELIMITER ;


-- -----------------------------------------------------
-- procedure sp_getPhysicianNameByID
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianNameByID`(IN physID INT)
BEGIN
	SELECT first_name, last_name FROM `user` WHERE iduser = physID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianSchedules
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianSchedules`()
BEGIN
SELECT * from test.schedule ;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysicianSchedulesById
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysicianSchedulesById`(IN p_userid INT)
BEGIN
SELECT * from test.schedule where idphysician=p_userid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPhysiciansByNameAndId
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPhysiciansByNameAndId`()
BEGIN
SELECT a.first_name, a.last_name, b.idphysician FROM test.user a JOIN test.physician b where a.iduser = b.idphysician;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getStatements
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getStatements`(
	IN patientid INT
)
BEGIN
	SELECT * FROM statement
    WHERE idpatient = patientid;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- procedure sp_updateStatementBalance
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateStatementBalance`(
	IN patientid VARCHAR(45), IN amount INT, IN statementid INT
)
BEGIN
	update statement
	set balance_due = balance_due - amount
    WHERE idpatient = patientid and idstatement=statementid;
END$$
DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_changeInsurance
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_changeInsurance`(IN userID INT, IN insurance_type VARCHAR(45))
BEGIN
	UPDATE `user`
    SET insurance = insurance_type
    WHERE iduser = userID;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- Table `test`.`paymentHistory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`paymentHistory` (
    phid INT NOT NULL AUTO_INCREMENT,
  `date` datetime not null,
  `amount` INT NOT NULL,
  `userID` varchar(45) NOT NULL,
  `statementID` int not null,
  PRIMARY KEY (`phid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- procedure sp_paymentHistory
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_paymentHistory`(IN p_userid INT, IN sID INT)
BEGIN
SELECT * from paymentHistory where userID=p_userid and statementID=sID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deletePaymentHistory
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deletePaymentHistory`(IN p_userID VARCHAR(45), IN p_statementID INT )
BEGIN
	DELETE FROM paymentHistory
    WHERE userID = p_userID and statementID = p_statementID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getUser`(IN p_userid INT)
BEGIN
SELECT username,first_name,last_name,street,city,state,zip,phone,date_of_birth,sex,email from user where iduser=p_userid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_modifyAppointment
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_modifyAppointment`(
	IN _appointmentID INT, IN _date DATETIME, IN _physID INT, IN reason MEDIUMTEXT
)
BEGIN
	UPDATE appointment
    SET appointment_date = _date, idphysician = _physID, `description` = reason
    WHERE idappointment = _appointmentID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_setHours
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_setHours`(
	IN `p_idphysician` INT,
    IN  `p_monTL` VARCHAR(100),
    IN  `p_tueTL` VARCHAR(100),
    IN  `p_wedTL` VARCHAR(100),
    IN  `p_thursTL` VARCHAR(100),
    IN  `p_friTL` VARCHAR(100),
    IN  `p_satTL` VARCHAR(100),
    IN  `p_sunTL` VARCHAR(100)


)
BEGIN
    if (select exists (select 1 from schedule where idphysician = p_idphysician))  then
        update schedule set monTL = p_monTL, tueTL = p_tueTL,
           wedTL = p_wedTL, thursTL = p_thursTL, friTL = p_friTL, satTL = p_satTL, sunTL = p_sunTL where idphysician = p_idphysician;
    else
        insert into schedule (idphysician, monTL, tueTL, wedTL, thursTL, friTL, satTL, sunTL)
        values (p_idphysician, p_monTL, p_tueTL, p_wedTL, p_thursTL, p_friTL, p_satTL, p_sunTL);
    end if;

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_validateLogin
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(
IN p_username VARCHAR(20)
)
BEGIN
    SELECT * FROM `user`
    WHERE `user`.username = p_username;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPatientEmail
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPatientEmail`(IN p_idpatient INT, IN p_idphysician INT)
BEGIN
    SELECT email FROM `user` WHERE `user`.iduser = p_idpatient AND
    EXISTS (select idpatient,idphysician from appointment where p_idpatient=idpatient
        AND p_idphysician=idphysician);
END$$

DELIMITER ;

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteCUMessage
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteCUMessage`(
	IN mID int
)
BEGIN
	delete from contact_us_messages where messageID=mID;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- trigger to insert into paymenthistory
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER= root@localhost TRIGGER create_payment_history_on_balance_update
AFTER UPDATE on statement
FOR EACH ROW
BEGIN
INSERT INTO paymentHistory (date, amount, userID, statementID) VALUES (now(), (old.balance_due - new.balance_due), old.idpatient, old.idstatement);
END $$
DELIMITER ;

-- -----------------------------------------------------
-- Table `test`.`insurance`
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE TABLE IF NOT EXISTS `test`.`insurance` (
  `insuranceID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `discount` FLOAT NOT NULL,
  `copay` INT NOT NULL,
  PRIMARY KEY (`insuranceID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

insert into insurance values (1, 'united', .10,  10);
insert into insurance values (2, 'bcbs', .15,  20);

-- -----------------------------------------------------
-- procedure sp_getPatientInsuranceInfo
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPatientInsuranceInfo`(IN pid INT)
BEGIN
	select insurance.name, insurance.discount, insurance.copay from user inner join insurance where user.iduser = pid and user.insurance = insurance.name;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getBillRates
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getBillRates`()
BEGIN
	select description, charge from billRates;
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- procedure sp_updateStatementBalance
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateStatementBalance`(
	IN patientid VARCHAR(45), IN amount INT, IN statementid INT
)
BEGIN
	update statement
	set balance_due = balance_due - amount
    WHERE idpatient = patientid and idstatement=statementid;
END$$
DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_changeInsurance
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_changeInsurance`(IN userID INT, IN insurance_type VARCHAR(45))
BEGIN
	UPDATE `user`
    SET insurance = insurance_type
    WHERE iduser = userID;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- Table `test`.`paymentHistory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`paymentHistory` (
    phid INT NOT NULL AUTO_INCREMENT,
  `date` datetime not null,
  `amount` INT NOT NULL,
  `userID` varchar(45) NOT NULL,
  `statementID` int not null,
  PRIMARY KEY (`phid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- procedure sp_paymentHistory
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_paymentHistory`(IN p_userid INT, IN sID INT)
BEGIN
SELECT * from paymentHistory where userID=p_userid and statementID=sID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deletePaymentHistory
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deletePaymentHistory`(IN p_userID VARCHAR(45), IN p_statementID INT )
BEGIN
	DELETE FROM paymentHistory
    WHERE userID = p_userID and statementID = p_statementID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getUser
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getUser`(IN p_userid INT)
BEGIN
SELECT username,first_name,last_name,street,city,state,zip,phone,date_of_birth,sex,email from user where iduser=p_userid;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_modifyAppointment
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_modifyAppointment`(
	IN _appointmentID INT, IN _date DATETIME, IN _physID INT, IN reason MEDIUMTEXT
)
BEGIN
	UPDATE appointment
    SET appointment_date = _date, idphysician = _physID, `description` = reason
    WHERE idappointment = _appointmentID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_setHours
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_setHours`(
	IN `p_idphysician` INT,
    IN  `p_monTL` VARCHAR(100),
    IN  `p_tueTL` VARCHAR(100),
    IN  `p_wedTL` VARCHAR(100),
    IN  `p_thursTL` VARCHAR(100),
    IN  `p_friTL` VARCHAR(100),
    IN  `p_satTL` VARCHAR(100),
    IN  `p_sunTL` VARCHAR(100)


)
BEGIN
    if (select exists (select 1 from schedule where idphysician = p_idphysician))  then
        update schedule set monTL = p_monTL, tueTL = p_tueTL,
           wedTL = p_wedTL, thursTL = p_thursTL, friTL = p_friTL, satTL = p_satTL, sunTL = p_sunTL where idphysician = p_idphysician;
    else
        insert into schedule (idphysician, monTL, tueTL, wedTL, thursTL, friTL, satTL, sunTL)
        values (p_idphysician, p_monTL, p_tueTL, p_wedTL, p_thursTL, p_friTL, p_satTL, p_sunTL);
    end if;

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_validateLogin
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(
IN p_username VARCHAR(20)
)
BEGIN
    SELECT * FROM `user`
    WHERE `user`.username = p_username;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getPatientEmail
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPatientEmail`(IN p_idpatient INT, IN p_idphysician INT)
BEGIN
    SELECT email FROM `user` WHERE `user`.iduser = p_idpatient AND
    EXISTS (select idpatient,idphysician from appointment where p_idpatient=idpatient 
        AND p_idphysician=idphysician);
END$$

DELIMITER ;

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_deleteCUMessage
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteCUMessage`(
	IN mID int
)
BEGIN
	delete from contact_us_messages where messageID=mID;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getCUMessageID
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getCUMessageID`(
	IN fname VARCHAR(45), IN lname VARCHAR(45), IN email VARCHAR(45), IN message MEDIUMTEXT
)
BEGIN
	select messageID from contact_us_messages where first_name=fname and last_name=lname and email=email and message= message;
END$$

DELIMITER ;


-- -----------------------------------------------------
-- trigger to insert into paymenthistory
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER= root@localhost TRIGGER create_payment_history_on_balance_update
AFTER UPDATE on statement
FOR EACH ROW
BEGIN
INSERT INTO paymentHistory (date, amount, userID, statementID) VALUES (now(), (old.balance_due - new.balance_due), old.idpatient, old.idstatement);
END $$
DELIMITER ;

-- -----------------------------------------------------
-- Table `test`.`insurance`
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE TABLE IF NOT EXISTS `test`.`insurance` (
  `insuranceID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `discount` FLOAT NOT NULL,
  `copay` INT NOT NULL,
  PRIMARY KEY (`insuranceID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

insert into insurance values (1, 'united', .10,  10);
insert into insurance values (2, 'bcbs', .15,  20);

-- -----------------------------------------------------
-- procedure sp_getPatientInsuranceInfo
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPatientInsuranceInfo`(IN pid INT)
BEGIN
	select insurance.name, insurance.discount, insurance.copay from user inner join insurance where user.iduser = pid and user.insurance = insurance.name;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure sp_getBillRates
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getBillRates`()
BEGIN
	select description, charge from billRates;
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;