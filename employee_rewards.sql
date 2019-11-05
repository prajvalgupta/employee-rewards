CREATE TABLE IF NOT EXISTS `mydb`.`Employee` (
  `eId` INT NOT NULL,
  `eName` VARCHAR(45) NULL,
  `password` VARCHAR(45) NOT NULL,
  `Admin` TINYINT NULL,
  PRIMARY KEY (`eId`),
  UNIQUE INDEX `userId_UNIQUE` (`eId` ASC) VISIBLE)
ENGINE = InnoDB


CREATE TABLE IF NOT EXISTS `mydb`.`BalancedPoints` (
  `eId` INT NOT NULL,
  `PAmount` INT NULL,
  INDEX `fk_RecievedPoints_User1_idx` (`eId` ASC) VISIBLE,
  CONSTRAINT `fk_RecievedPoints_User10`
    FOREIGN KEY (`eId`)
    REFERENCES `mydb`.`Employee` (`eId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`RecievedPoints` (
  `eId` INT NOT NULL,
  `PAmount` INT NULL,
  INDEX `fk_RecievedPoints_User1_idx` (`eId` ASC) VISIBLE,
  CONSTRAINT `fk_RecievedPoints_User1`
    FOREIGN KEY (`eId`)
    REFERENCES `mydb`.`Employee` (`eId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`PointTrans` (
  `PTransId` INT NOT NULL,
  `PTransDate` DATETIME NOT NULL,
  `pointAmount` INT NOT NULL,
  `received_eId` INT NOT NULL,
  `given_eId` INT NOT NULL,
  PRIMARY KEY (`PTransId`),
  UNIQUE INDEX `TransId_UNIQUE` (`PTransId` ASC) VISIBLE,
  INDEX `fk_PointTrans_User_idx` (`given_eId` ASC) VISIBLE,
  CONSTRAINT `fk_PointTrans_User`
    FOREIGN KEY (`given_eId`)
    REFERENCES `mydb`.`Employee` (`eId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB


CREATE TABLE IF NOT EXISTS `mydb`.`GiftCards` (
  `eId` INT NOT NULL,
  `GAmount` INT NULL,
  CONSTRAINT `fk_GiftCard_User1`
    FOREIGN KEY (`eId`)
    REFERENCES `mydb`.`Employee` (`eId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB


CREATE TABLE IF NOT EXISTS `mydb`.`GiftTrans` (
  `GTransId` INT NOT NULL,
  `GTransDate` DATETIME NOT NULL,
  `giftcardAmount` INT NOT NULL,
  `eId` INT NOT NULL,
  PRIMARY KEY (`GTransId`),
  UNIQUE INDEX `TransId_UNIQUE` (`GTransId` ASC) VISIBLE,
  INDEX `fk_PointTrans_User_idx` (`eId` ASC) VISIBLE,
  CONSTRAINT `fk_PointTrans_User0`
    FOREIGN KEY (`eId`)
    REFERENCES `mydb`.`Employee` (`eId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB