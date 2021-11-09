-- Database: dvdrental

-- DROP DATABASE dvdrental;

-- select distinct name from language

-- select language.name, film.title, film.description
-- from film
-- inner join language on film.film_id=language.language_id 

--select language.name, film.title, film.description
--from language
--right join film on language.language_id = film.film_id

--select language.name, film.title, film.description
--from language
--full join film on language.language_id = film.film_id

-- create table customer_review(
-- review_id serial primary key,
-- film_id int references new_film(id) on delete restrict,
-- langugae_id int references language(language_id),
-- title text,
-- score int,
--	check (score > 0 and score < 11),
--review_text text not null,
--last_update date
-- )

--insert into new_film (id,name)
--values (1, 'Monsters Inc'),
--(2, 'The Stupids'),
--(3, 'Little Rascals');

--insert into customer_review (review_id, film_id,langugae_id, title, score, review_text, last_update)
--values
--(1,1,1, 'The Review of the Monsters', 10, 'This movie is both funny, and educational about charachter development', '2021-11-09'),
--(2,3,1, 'Utopia or Zootopia', 10, 'This movie is both funny, and educational about social reforms', '2021-11-09');

-- DELETE FROM new_film where id = 3;
	--ERROR:  update or delete on table "new_film" violates foreign key constraint "customer_review_film_id_fkey" on table "customer_review"
	-- DETAIL:  Key (id)=(3) is still referenced from table "customer_review".
	-- SQL state: 23503
	
-- EXERCISE TWO	

--update film
--set language_id= 4
--where film_id in (1,2,3);

-- the customer_review referneces the IDs from langugae and new_film; therefore, those IDs (when added)  must be included in the referenced tables

--drop table customer_review;
	--easy step
	
-- select count (*) from rental where return_date = null

--select * 
--from rental 
--inner join film on rental.rental_id = film.film_id 
--where rental.return_date = null 
--order by film.rental_rate desc
--limit 30;

--select title 
--from film
--inner join actor on film.film_id = actor.actor_id 
--where actor.first_name = 'Penelope' and actor.last_name = 'Monroe'


--select film.title
--from (actor join film_actor on actor.actor_id = film_actor.actor_id)
--join film on film.film_id = film_actor.film_id
--where film.description ilike '%shark%'
--and actor.first_name = 'Penelope'
--and actor.last_name = 'Monroe'

-- select film.title
-- from (category join film_category on category.category_id = film_category.category_id)
-- join film on film.film_id = film_category.film_id
-- where category.category_id = 6 
-- and film.rating = 'R'
-- and film.length < 60;


-- select film.title, rental.rental_id
-- from (customer join rental on customer.customer_id = rental.customer_id)
-- join film on film.film_id = customer.customer_id
-- where customer.first_name = 'Matthew' 
-- and customer.last_name = 'Mahan'
-- and film.rental_rate >= 4.00
-- and rental.return_date < '2005-08-01'
-- and rental.return_date >= '2005-07-28';

-- select film.title, film.description
-- from (customer join rental on customer.customer_id = rental.customer_id)
-- join film on film.film_id = rental.rental_id
-- where customer.first_name = 'Matthew' 
-- and customer.last_name = 'Mahan'
-- and film.replacement_cost >= 15.00
-- and film.description ilike '%shark%' 
-- or film.title ilike '%shark%';

