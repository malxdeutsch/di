-- Database: dvdrental

-- DROP DATABASE dvdrental;

-- select * from customer;
-- select first_name || ' ' || last_name from customer as full_name;
-- select distinct create_date from customer;
-- select * from customer order by first_name desc;
-- select film_id, release_year, title, description, rental_rate from film order by rental_rate asc;
-- select address, phone from address where district = 'Texas'
-- select * from film where film_id = 15 or film_id = 150;
-- select film_id, title, description, length, rating from film where title = ‘Arabia Dogma’;
-- select film_id, title, description, length, rating from film where title ilike ‘%ar%‘;
-- select film_id, title, description, length, rating from film where title ilike ‘%Ar%‘;
-- select film_id, title, description, length, rating from film where title like ‘%AR%’;
-- select * from film order by rental_rate limit 10;
-- select * from film order by rental_rate offset 10 fetch first 10 row only;
-- select customer.customer_id, customer.first_name, customer.last_name as full_name, payment.amount, payment.payment_date inner join payment on payment.customer_id = customer.customer_id order by customer.customer_id asc;
-- select * customers where film != inventory