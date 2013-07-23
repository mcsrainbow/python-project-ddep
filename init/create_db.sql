CREATE DATABASE `inventory` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE inventory;
DROP TABLE IF EXISTS `hosts`;
CREATE TABLE `hosts` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) DEFAULT NULL UNIQUE,
  `public_dns` varchar(255) DEFAULT NULL UNIQUE,
  `colo` varchar(255) DEFAULT NULL,
  `environment` varchar(255) DEFAULT NULL,
  `group` varchar(255) DEFAULT NULL,
  `private_ip` varchar(255) DEFAULT NULL,
  `public_ip` varchar(255) DEFAULT NULL,
  `additional_ip` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

GRANT ALL PRIVILEGES ON inventory.* TO 'inventory'@'%' IDENTIFIED BY 'inventory';
