#CREATE DATABASE pants;
# You must run the above line in the mysql interpreter first
# Then run mysql -u root -p pants < data/scripts/create_pants_db.sql
# Then run python data/product_loader.py
CREATE TABLE `pants`.`tbl_products` (
  `product_id` INT NOT NULL,
  `product_name` VARCHAR(50) NULL,
  `product_image` VARCHAR(300) NULL,
  `product_description` VARCHAR(300) NULL,
  PRIMARY KEY (`product_id`));

CREATE TABLE `pants`.`tbl_inventory` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `product_id` INT NULL,
  `waist` INT NULL,
  `length` INT NULL,
  `style` VARCHAR(50) NULL,
  `count` INT NULL,
  FOREIGN KEY fk_prod(product_id)
    REFERENCES tbl_products(product_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);