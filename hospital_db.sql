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
AUTO_INCREMENT = 4
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
  `monday` BIT(1) NULL DEFAULT NULL,
  `tuesday` BIT(1) NULL DEFAULT NULL,
  `wednesday` BIT(1) NULL DEFAULT NULL,
  `thursday` BIT(1) NULL DEFAULT NULL,
  `friday` BIT(1) NULL DEFAULT NULL,
  `saturday` BIT(1) NULL DEFAULT NULL,
  `sunday` BIT(1) NULL DEFAULT NULL,
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
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `test` ;

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
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getContactUsMessages`()
BEGIN
SELECT * from test.contact_us_messages;
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
-- procedure sp_getAppointments
-- -----------------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getAppointments`(IN userID INT)
BEGIN
	SELECT appointment.appointment_date, appointment.description, user.first_name, user.last_name
	FROM appointment
	INNER JOIN user ON appointment.idphysician = user.iduser
    where appointment.idpatient=userID;
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
-- procedure sp_assignBed
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
-- procedure sp_getUser
-- -----------------------------------------------------
DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getUser`(IN p_userid INT)
BEGIN
SELECT first_name,last_name,street, city, state,zip,phone,date_of_birth ,sex, email from user where iduser=p_userid;
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


insert into admin(`idpadmin`, `idDepartment`)
values(1, 1);
insert into user(`username`,`password`,`first_name`,`last_name`,`street`,`city`,`state`,`zip`,`phone`,
            `date_of_birth`,`sex`,`email`, `type`)
values('admin','admin','admin','admin','admin','admin','admin','admin','admin','admin','admin', 'admin', 'admin');

-- -----------------------------------------------------
-- procedure sp_createAdmin
-- --------- --------------------------------------------

DELIMITER $$
USE `test`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createAdmin`(
	IN p_username VARCHAR(45),IN p_password VARCHAR(103),IN p_FN VARCHAR(45),
    IN p_LN VARCHAR(45),IN p_street VARCHAR(45),IN p_city VARCHAR(45),
    IN p_state VARCHAR(45),IN p_zip VARCHAR(45),IN p_phone VARCHAR(45),
    IN p_dob VARCHAR(45),IN p_sex VARCHAR(45),IN p_email VARCHAR(45), IN p_type VARCHAR(45), IN p_deptId INT
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
            p_dob ,p_sex,p_email, p_type
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

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;