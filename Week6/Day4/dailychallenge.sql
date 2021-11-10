-- Database: day4

-- DROP DATABASE day4;

-- create table orders(
-- 	order_id serial primary key,
-- 	order_name varchar(250) not null
-- );

-- create table items(
-- 	item_id serial primary key,
-- 	item_names varchar(300) not null,
-- 	price int,
-- 	fk_order_id int not null,
-- 	foreign key (fk_order_id) references orders (order_id) on delete cascade
-- )


-- insert into orders (order_id, order_name)
-- values
-- (1,'Smith'),
-- (2,'Johns'),
-- (3,'Campbell');

-- insert into items(item_names, price, fk_order_id)
-- values
-- ('shirt', 30, 1),
-- ('sweater', 40, 2),
-- ('shoes', 50,3);

-- DROP FUNCTION total_price(integer,integer)
-- CREATE OR REPLACE FUNCTION total_price(ord int, prc int)
-- RETURNS int AS $total_price$
-- BEGIN
--    RETURN(SELECT items.price FROM items join orders on items.fk_order_id = orders.order_id WHERE orders.order_id = ord AND items.price= prc);
-- END;
-- $total_price$ LANGUAGE plpgsql;

-- SELECT * from total_price (2, 40);