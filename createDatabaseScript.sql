CREATE DATABASE amazon_bot_db;

USE amazon_bot_db;

CREATE TABLE User (
	UserId int,
    Email varchar(45),
    Password varchar(45),
    HistoryId int,
    PRIMARY KEY(UserId)
);

CREATE TABLE Tracking_Info (
	TrackingId int,
    UserId int,
    ItemId int,
    targetPrice double,
    PRIMARY KEY(TrackingId)
);

CREATE TABLE History (
	HistoryId int,
    UserId int,
    RecentOrderEntryId int,
    CurrentTrackingId int,
    PRIMARY KEY(HistoryId)
);

CREATE TABLE Item (
	ItemId int,
    CurrentPrice double,
    Description varchar(512),
    AmazonLink varchar(512),
    PRIMARY KEY (ItemId)
);

CREATE TABLE RecentOrders (
	RecentOrderEntryId int,
    UserId int,
    ItemId int,
    PRIMARY KEY(RecentOrderEntryId)
);

CREATE TABLE CurrentTrackings (
	CurrentTrackingsId int,
    UserId int,
    ItemId int,
    PRIMARY KEY(CurrentTrackingsId)
);

ALTER TABLE `amazon_bot_db`.`CurrentTrackings` 
ADD INDEX `fk_CurrentTrackings_1_idx` (`ItemId` ASC),
ADD INDEX `fk_CurrentTrackings_2_idx` (`UserId` ASC);
ALTER TABLE `amazon_bot_db`.`CurrentTrackings` 
ADD CONSTRAINT `fk_CurrentTrackings_1`
  FOREIGN KEY (`ItemId`)
  REFERENCES `amazon_bot_db`.`Item` (`ItemId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_CurrentTrackings_2`
  FOREIGN KEY (`UserId`)
  REFERENCES `amazon_bot_db`.`User` (`UserId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  ALTER TABLE `amazon_bot_db`.`History` 
ADD INDEX `fk_History_1_idx` (`UserId` ASC),
ADD INDEX `fk_History_2_idx` (`RecentOrderEntryId` ASC),
ADD INDEX `fk_History_3_idx` (`CurrentTrackingId` ASC);
ALTER TABLE `amazon_bot_db`.`History` 
ADD CONSTRAINT `fk_History_1`
  FOREIGN KEY (`UserId`)
  REFERENCES `amazon_bot_db`.`User` (`UserId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_History_2`
  FOREIGN KEY (`RecentOrderEntryId`)
  REFERENCES `amazon_bot_db`.`RecentOrders` (`RecentOrderEntryId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_History_3`
  FOREIGN KEY (`CurrentTrackingId`)
  REFERENCES `amazon_bot_db`.`Tracking_Info` (`TrackingId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  ALTER TABLE `amazon_bot_db`.`RecentOrders` 
ADD INDEX `fk_RecentOrders_1_idx` (`UserId` ASC),
ADD INDEX `fk_RecentOrders_2_idx` (`ItemId` ASC);
ALTER TABLE `amazon_bot_db`.`RecentOrders` 
ADD CONSTRAINT `fk_RecentOrders_1`
  FOREIGN KEY (`UserId`)
  REFERENCES `amazon_bot_db`.`User` (`UserId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_RecentOrders_2`
  FOREIGN KEY (`ItemId`)
  REFERENCES `amazon_bot_db`.`Item` (`ItemId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `amazon_bot_db`.`Tracking_Info` 
ADD INDEX `fk_Tracking_Info_1_idx` (`UserId` ASC),
ADD INDEX `fk_Tracking_Info_2_idx` (`ItemId` ASC);
ALTER TABLE `amazon_bot_db`.`Tracking_Info` 
ADD CONSTRAINT `fk_Tracking_Info_1`
  FOREIGN KEY (`UserId`)
  REFERENCES `amazon_bot_db`.`User` (`UserId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_Tracking_Info_2`
  FOREIGN KEY (`ItemId`)
  REFERENCES `amazon_bot_db`.`Item` (`ItemId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  ALTER TABLE `amazon_bot_db`.`User` 
ADD INDEX `fk_User_1_idx` (`HistoryId` ASC);
ALTER TABLE `amazon_bot_db`.`User` 
ADD CONSTRAINT `fk_User_1`
  FOREIGN KEY (`HistoryId`)
  REFERENCES `amazon_bot_db`.`History` (`HistoryId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  ALTER TABLE `amazon_bot_db`.`User` 
DROP FOREIGN KEY `fk_User_1`;
ALTER TABLE `amazon_bot_db`.`User` 
DROP INDEX `fk_User_1_idx` ;

ALTER TABLE `amazon_bot_db`.`History` 
CHANGE COLUMN `HistoryId` `HistoryId` INT(11) NOT NULL AUTO_INCREMENT ;

ALTER TABLE `amazon_bot_db`.`User` 
ADD INDEX `fk_User_1_idx` (`HistoryId` ASC);
ALTER TABLE `amazon_bot_db`.`User` 
ADD CONSTRAINT `fk_User_1`
  FOREIGN KEY (`HistoryId`)
  REFERENCES `amazon_bot_db`.`History` (`HistoryId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
