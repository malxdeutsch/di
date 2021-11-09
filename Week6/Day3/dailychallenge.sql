-- Database: postgres

-- DROP DATABASE postgres;

-- CREATE TABLE customer (
--   customer_id SERIAL,
--   customer_name VARCHAR(45) NOT NULL,
--   last_shop date NOT NULL,
--   PRIMARY KEY (customer_id)
-- );

-- CREATE TABLE customer_profile (
--   customer_profile_id INTEGER NOT NULL,
--   credit_card int NOT NULL,
--   PRIMARY KEY (customer_profile_id),
--   CONSTRAINT fk_customer_id FOREIGN KEY (customer_profile_id) REFERENCES customer (customer_id)
-- );
-- INSERT into customer(customer_name, last_shop) 
-- VALUES 
-- ('John Mark', '2021-11-02'),
-- ('Mark John', '2021-11-08'),
-- ('Bryan Thomas', '2021-11-04'),
-- ('Thomas Bryan', '2021-10-28');

-- INSERT into customer_profile(customer_profile_id, credit_card) 
-- VALUES 
-- ((SELECT customer_id FROM customer where customer_name = 'John Mark'),9090),
-- ((SELECT customer_id FROM customer where customer_name = 'Mark John'),9000);

-- SELECT customer.customer_name, customer.last_shop, customer_profile.credit_card 
-- FROM customer
-- FULL OUTER JOIN customer_profile
-- ON customer.customer_id = customer_profile.customer_profile_id;

-- SELECT customer.customer_name, customer.last_shop, customer_profile.credit_card 
-- FROM customer
-- inner JOIN customer_profile
-- ON customer.customer_id = customer_profile.customer_profile_id;

-- SELECT customer.customer_name, customer.last_shop, customer_profile.credit_card 
-- FROM customer
-- RIGHT JOIN customer_profile
-- ON customer.customer_id = customer_profile.customer_profile_id;

-- SELECT customer.customer_name, customer.last_shop, customer_profile.credit_card 
-- FROM customer
-- LEFT JOIN customer_profile
-- ON customer.customer_id = customer_profile.customer_profile_id;

-- create table product(
-- 	product_id serial,
-- 	product_name VARCHAR(45) NOT NULL,
--  last_sold date NOT NULL,
-- 	PRIMARY KEY (product_id)
-- )

-- INSERT into product(product_name, last_sold) 
-- VALUES 
-- ('Watch', '2021-11-02'),
-- ('Tie', '2021-11-08'),
-- ('Sweater', '2021-11-04'),
-- ('Belt', '2021-10-28');

-- create table orders (
--   customer_id INTEGER NOT NULL,
--   product_id INTEGER NOT NULL,
--   PRIMARY KEY (customer_id, product_id),
--   FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE,
--   FOREIGN KEY (product_id) REFERENCES product(product_id) ON UPDATE CASCADE
-- );

-- SELECT customer.customer_name, customer.last_shop, product.product_name, product.last_sold 
-- FROM orders
-- FULL OUTER JOIN customer ON orders.customer_id = customer.customer_id
-- full outer join product on orders.product_id = product.product_id;

-- SELECT customer.customer_name, customer.last_shop, product.product_name, product.last_sold 
-- FROM orders
-- inner JOIN customer ON orders.customer_id = customer.customer_id
-- inner join product on orders.product_id = product.product_id

-- SELECT customer.customer_name, customer.last_shop, product. product_name, product.last_sold 
-- FROM orders
-- right JOIN customer ON orders.customer_id = customer.customer_id
-- right join product on orders.product_id = product.product_id

-- SELECT customer.customer_name, customer.last_shop, prodcut.name, product.last_sold 
-- FROM orders
-- FULL OUTER JOIN customer ON orders.customer_id = customer.customer_id;
-- full outer join product on orders.product_id = product.product_id