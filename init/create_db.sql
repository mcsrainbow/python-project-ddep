CREATE DATABASE `opsdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE opsdb;

DROP TABLE IF EXISTS `colo`;
CREATE TABLE `colo` (
  `colo_id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `colo_name` char(4) NOT NULL,
  `colo_desc` char(30) NOT NULL,
  `colo_pm` int(10) unsigned NOT NULL,
  PRIMARY KEY (`colo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS `hardware`;
CREATE TABLE `hardware` (
  `hw_config` tinyint(4) NOT NULL AUTO_INCREMENT,
  `hw_vendor` char(10) NOT NULL,
  `cpu` char(30) NOT NULL,
  `memory` char(30) NOT NULL,
  `disk` char(30) NOT NULL,
  PRIMARY KEY (`hw_config`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


DROP TABLE IF EXISTS `host`;
CREATE TABLE `host` (
  `host_id` smallint(6) NOT NULL AUTO_INCREMENT,
  `colo_name` char(4) NOT NULL,
  `host_name` varchar(30) NOT NULL,
  `hostgroup_name` char(20) NOT NULL,
  `ip_addr` int(10) unsigned NOT NULL,
  `ipmi_ip_addr` int(10) unsigned DEFAULT NULL,
  `hw_config` tinyint(4) DEFAULT NULL,
  `hw_serial` char(10) DEFAULT NULL,
  `hw_pod` tinyint(4) DEFAULT NULL,
  `hw_cabinet` tinyint(4) DEFAULT NULL,
  `hw_space` tinyint(4) DEFAULT NULL,
  `ec2_local_ipv4` int(10) unsigned DEFAULT NULL,
  `ec2_local_hostname` varchar(60) DEFAULT NULL,
  `ec2_public_ipv4` int(10) unsigned DEFAULT NULL,
  `ec2_public_hostname` varchar(60) DEFAULT NULL,
  `ec2_placement_region` char(7) DEFAULT NULL,
  `ec2_placement_zone` char(10) DEFAULT NULL,
  `ec2_instance_id` char(10) DEFAULT NULL,
  `ec2_instance_type` varchar(15) DEFAULT NULL,
  `active` tinyint(4) NOT NULL,
  `last_modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `in_nagios` tinyint(4) NOT NULL,
  PRIMARY KEY (`host_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


DROP TABLE IF EXISTS `hostgroup`;
CREATE TABLE `hostgroup` (
  `hostgroup_id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `hostgroup_name` char(20) DEFAULT NULL,
  `hostgroup_next` tinyint(4) NOT NULL,
  `colo_name` char(4) NOT NULL,
  PRIMARY KEY (`hostgroup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

GRANT ALL PRIVILEGES ON opsdb.* TO 'opsdb'@'localhost' IDENTIFIED BY 'opsdb';
