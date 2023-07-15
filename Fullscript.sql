-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
drop database mydb;
-----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`admin` (
  `Employee_ID` DOUBLE NOT NULL,
  `Name` VARCHAR(45) NULL DEFAULT NULL,
  `Emp_email` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Employee_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car` (
  `number` VARCHAR(45) NOT NULL,
  `Con` DOUBLE NULL DEFAULT NULL,
  `category` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cities` (
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`drivers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`drivers` (
  `D_Phone_number` DOUBLE NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `rating` DOUBLE NULL DEFAULT NULL,
  `Revenue` DOUBLE NULL DEFAULT NULL,
  `Cities_Name` VARCHAR(45) NOT NULL,
  `Car_number` VARCHAR(45) NOT NULL,
  `Admin_Employee_ID` DOUBLE NOT NULL,
  PRIMARY KEY (`D_Phone_number`, `Cities_Name`, `Car_number`, `Admin_Employee_ID`),
  INDEX `fk_Drivers_Cities1_idx` (`Cities_Name` ASC) VISIBLE,
  INDEX `fk_Drivers_Car1_idx` (`Car_number` ASC) VISIBLE,
  INDEX `fk_Drivers_Admin1_idx` (`Admin_Employee_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Drivers_Admin1`
    FOREIGN KEY (`Admin_Employee_ID`)
    REFERENCES `mydb`.`admin` (`Employee_ID`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_Drivers_Car1`
    FOREIGN KEY (`Car_number`)
    REFERENCES `mydb`.`car` (`number`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_Drivers_Cities1`
    FOREIGN KEY (`Cities_Name`)
    REFERENCES `mydb`.`cities` (`Name`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`trips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`trips` (
  `Trip_ID` DOUBLE NOT NULL,
  `Cost` DOUBLE NOT NULL,
  `StartTime` VARCHAR(45) NULL DEFAULT NULL,
  `Duration` TIME NULL DEFAULT NULL,
  `PickUpLocation` VARCHAR(45) NOT NULL,
  `DropLocation` VARCHAR(45) NOT NULL,
  `Drivers_D_Phone_number` DOUBLE NOT NULL,
  PRIMARY KEY (`Trip_ID`, `Drivers_D_Phone_number`),
  INDEX `fk_Trips_Drivers1_idx` (`Drivers_D_Phone_number` ASC) VISIBLE,
  CONSTRAINT `fk_Trips_Drivers1`
    FOREIGN KEY (`Drivers_D_Phone_number`)
    REFERENCES `mydb`.`drivers` (`D_Phone_number`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer` (
  `C_Phone_Number` DOUBLE NOT NULL,
  `C_email_ID` VARCHAR(45) NOT NULL,
  `C_Name` VARCHAR(45) NOT NULL,
  `Wallet` DOUBLE NOT NULL,
  `rating` DOUBLE NULL DEFAULT NULL,
  `Trips_Trip_ID` DOUBLE ,
  `Drivers_D_Phone_number` DOUBLE ,
  `Drivers_D_Phone_number1` DOUBLE ,
  `Car_number` VARCHAR(45) ,
  PRIMARY KEY (`C_Phone_Number`, `C_email_ID`, `Trips_Trip_ID`, `Drivers_D_Phone_number`, `Drivers_D_Phone_number1`, `Car_number`),
  INDEX `Phone Number_UNIQUE` (`C_Phone_Number` ASC) VISIBLE,
  INDEX `email number_UNIQUE` (`C_email_ID` ASC) VISIBLE,
  INDEX `fk_Customer_Trips1_idx` (`Trips_Trip_ID` ASC) VISIBLE,
  INDEX `fk_Customer_Drivers1_idx` (`Drivers_D_Phone_number` ASC) VISIBLE,
  INDEX `fk_Customer_Drivers2_idx` (`Drivers_D_Phone_number1` ASC) VISIBLE,
  INDEX `fk_Customer_Car1_idx` (`Car_number` ASC) VISIBLE,
  CONSTRAINT `fk_Customer_Car1`
    FOREIGN KEY (`Car_number`)
    REFERENCES `mydb`.`car` (`number`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_Customer_Drivers1`
    FOREIGN KEY (`Drivers_D_Phone_number`)
    REFERENCES `mydb`.`drivers` (`D_Phone_number`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_Customer_Drivers2`
    FOREIGN KEY (`Drivers_D_Phone_number1`)
    REFERENCES `mydb`.`drivers` (`D_Phone_number`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_Customer_Trips1`
    FOREIGN KEY (`Trips_Trip_ID`)
    REFERENCES `mydb`.`trips` (`Trip_ID`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`locations` (
  `Address` VARCHAR(145) NOT NULL,
  `Name` VARCHAR(45) NULL DEFAULT NULL,
  `Frequency` DOUBLE NULL DEFAULT NULL,
  `Last_Trip` VARCHAR(45) NULL DEFAULT NULL,
  `Customer_C_Phone_Number` DOUBLE NOT NULL,
  `Customer_C_email_ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Address`, `Customer_C_Phone_Number`, `Customer_C_email_ID`),
  INDEX `fk_Locations_Customer_idx` (`Customer_C_Phone_Number` ASC, `Customer_C_email_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Locations_Customer`
    FOREIGN KEY (`Customer_C_Phone_Number` , `Customer_C_email_ID`)
    REFERENCES `mydb`.`customer` (`C_Phone_Number` , `C_email_ID`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
