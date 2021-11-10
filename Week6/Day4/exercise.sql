-- Database: day4

-- DROP DATABASE day4;

-- select distinct first_name as FirstName, last_name as Last_Name from employees

-- select distinct employee_id from employees

-- select * from employees order by first_name desc

-- select distinct first_name, last_name, salary, ROUND(salary*0.15, 2) as PF from employees 

-- select distinct employee_id, first_name, last_name, salary from employees order by salary asc

-- select sum(salary) from employees

-- select max(salary) from employees

-- select min(salary) from employees

-- select avg(salary) from employees

-- select distinct count (employee_id) from employees

-- select upper(first_name) from employees

-- SELECT SUBSTR(FIRST_NAME, 1 , 3 ) FROM EMPLOYEES; 

-- select CONCAT(first_name, ' ', last_name) as FullName from employees

-- select first_name, last_name, length(CONCAT(first_name, last_name)) from employees

-- select * from employees where first_name ~ '\d';

-- select * from employees limit 10

--EXERCISE 2

-- select first_name, last_name, salary from employees where salary >10000 and salary < 15000

-- select first_name, last_name, hire_date from employees where DATE_PART('year', hire_date) = 1987

-- select first_name from employees where first_name like '%c%' and first_name like '%e%'

-- select last_name, job_title, salary 
-- from employees 
-- inner join jobs on employees.job_id = jobs.job_id 
-- where job_title != 'Programmers' 
-- or job_title != 'Shipping clerks'
-- and salary != 4500 
-- or salary!= 10000 
-- or salary != 15000

--select last_name from employees where length(last_name) = 6

-- select last_name from employees where SUBSTRING(last_name, 3 , 1) = 'e'

-- select distinct job_title
-- from jobs
-- inner join employees on jobs.job_id = employees.job_id

-- select * from employees where last_name in ('Blake', 'Ford', 'Scott', 'King', 'Jones')
