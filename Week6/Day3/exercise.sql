-- Database: public

-- DROP DATABASE public;

--select * from items order by price
-- select * from items where price >= 80 order by price desc
-- select * from customers order by f_name limit 3
-- select distinct l_name from customers order by l_name desc

-- alter table customers add column customer_id serial primary key

--insert into purchases(customer_id, item_id)
--values (1,)
					  
--insert into purchases(customer_id,item_id)
--values (4,1), (5,2);
	
--select * from items
--inner join purchases
--on items.item_id = purchases.item_id

--select customers.f_name, customers.l_name, items.item, items.price
--from customers
--inner join purchases on purchases.customer_id = customers.customer_id
--inner join items on purchases.item_id = items.item_id

--where customers.customer_id = 4
-- where items.item = 'Large Desk' and items.item = 'Small Desk'

--insert into items (item , price) values ('Hard Disk',150);
--insert into purchases (item_id,customer_id) values (4,3);

select customers.f_name, customers.l_name, items.item, items.price
from purchases
inner join customers on purchases.customer_id = customers.customer_id
inner join items on purchases.item_id = items.item_id
where f_name = 'Scott'
