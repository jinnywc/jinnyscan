create database demo;
use demo;
CREATE TABLE IF NOT EXISTS `demo`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `url` VARCHAR(100) NOT NULL,
   `name` VARCHAR(100) NOT NULL,
   `password` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `demo` VALUES (1,'http:127.0.0.1','admin','password');