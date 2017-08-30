#CREATE DATABASE pants;
# You must run the above line in the mysql interpreter first
# Then run mysql -u root -p pants < data/scripts/create_pants_db.sql
# Then run python data/product_loader.py
CREATE TABLE `pants`.`tbl_products` (
  `id` BIGINT AUTO_INCREMENT,
  `product_id` INT NULL,
  `product_name` VARCHAR(50) NULL,
  `product_image` VARCHAR(300) NULL,
  `product_description` VARCHAR(300) NULL,
  PRIMARY KEY (`id`));