select a.FirstName, a.LastName, b.City,b.State
from Person a, Address b
where a.PersonId = b.PersonId

## second highest salary
select max(Salary)
from Employee
where Salary < (select max(Salary) from Employee)

##extends to Nth Highest Salary
SELECT MAX(Salary)
 FROM (SELECT E1.Salary
 FROM Employee as E1 JOIN Employee as E2
 ON E1.Salary < E2.Salary
 GROUP BY E1.Id HAVING COUNT(E2.Id) = N-1
 )  AS SecondHighestSalary
 ORDER BY Salary DESC LIMIT 1;

       select max(NthHighestSalary.Salary)
      from (select E1.Salary
            from Employee E1, Employee E2
            where E1.Salary < E2.Salary
            group by E1.Id
            having count(E2.Id) = N-1) as NthHighestSalary
 
'''


bityotaguests-MacBook-Pro:json effy$ psql
psql (9.4.1)
Type "help" for help.

effy=# select '2015-06-23'::timestamp;
      timestamp
---------------------
 2015-06-23 00:00:00
(1 row)

effy=# select '15-06-23'::timestamp;
ERROR:  date/time field value out of range: "15-06-23"
LINE 1: select '15-06-23'::timestamp;
               ^
HINT:  Perhaps you need a different "datestyle" setting.
effy=# select '2015-06-23 15:03:00'::timestamp;
      timestamp
---------------------
 2015-06-23 15:03:00
(1 row)

effy=# create table trial(col1 varchar, col2 varchar,col3 float, col4 timestamp);
CREATE TABLE

                                      
effy=# insert into trial values('sunnyvale', 'wednesday', 10.00, '2015-06-23 09:30:30');
INSERT 0 1
effy=#
'''
## Between Oct 1, 2013 at 10am PDT and Oct 22, 2013 at 5pm PDT, how many total requests made by unbanned clients each day each city?
select t.city, t.request_at::date as day, count(t.id) as total
from trips t inner join users u
on t.client_id=u.userid
where u.banned=false and t.request_at>= '2013-10-01 10:00:00 PDT' and t.request_at <= '2013-10-22 17:00:00 PDT'
group by t.city, t.request_at::date;

## Between Oct 1, 2013 at 10am PDT and Oct 22, 2013 at 5pm PDT, how many total requests were canceled by unbanned clients each day each city?
select t.city, t.request_at::date as day, count(t.id) as canceled
from trips t inner join users u
on t.client_id=u.userid
where u.banned=false and t.request_at>= '2013-10-01 10:00:00 PDT' and t.request_at <= '2013-10-22 17:00:00 PDT' and t.status::text <>'completed'
group by t.city, t.request_at::date;


## percentage
select A.city, A.day, round((B.canceled::float/A.total::float)::numeric, 2) as cancel_rate
from (  select t.city, t.request_at::date as day, count(t.id) as total
		from trips t inner join users u
		on t.client_id=u.userid
		where u.banned=false and t.request_at>= '2015-10-01 10:00:00 PDT' and t.request_at <= '2013-10-22 17:00:00 PDT'
		group by t.city, t.request_at::date) as T,
      ( select t.city, t.request_at::date as day, count(t.id) as canceled
		from trips t inner join users u
		on t.client_id=u.userid
		where u.banned=false and t.request_at>= '2015-10-01 10:00:00 PDT' and t.request_at <= '2013-10-22 17:00:00 PDT' and t.status::text <>'completed'
		group by t.city, t.request_at::date) as C
where C.city = T.city and C.day = T.day


## For city_ids 1, 6, and 12, list the top three drivers by number of completed trips for each week between June 3, 2013 and June 24, 2013.
select f.week, f.city_id,f.driver_id, f.num_of_trips
from
(select Extract(week from request_at) as week,city_id, driver_id, count(id) as num_of_trips, rank() over (PARTITION BY Extract(week from request_at), city_id order by count(id)) as r
from trips
where city_id in (1,2,6) and status::text = 'completed'
and request_at::date >= '2013-06-03' and request_at::date <= '2013-06-24'
group by Extract(week from request_at), city_id, driver_id) as f
where f.r<=3



##test
select f.week, f.city_id,f.driver_id, f.num_of_trips
from
(select Extract(week from t) as week,city_id, driver_id, count(id) as num_of_trips, rank() over (PARTITION BY Extract(week from t), city_id order by count(id)) as r
from new
where city_id in (1,2,6) and status::text = 'completed'
and t::date >= '2013-06-03' and t::date <= '2013-06-24'
group by Extract(week from t), city_id, driver_id) as f
where f.r<=2


insert into trips values('0001', '')



insert into new values('2013-06-03 12:00:00 PDT',100,1,1000,'completed');
insert into new values('2013-06-04 12:00:00 PDT',100,1,1001,'completed');
insert into new values('2013-06-05 12:00:00 PDT',100,1,1002,'completed');
insert into new values('2013-06-06 12:00:00 PDT',100,1,1003,'completed');
insert into new values('2013-06-07 12:00:00 PDT',100,1,1004,'completed');
insert into new values('2013-06-08 12:00:00 PDT',100,1,1005,'completed');
insert into new values('2013-06-03 12:00:00 PDT',100,1,1006,'completed');
insert into new values('2013-06-04 12:00:00 PDT',100,1,1007,'completed');
insert into new values('2013-06-05 12:00:00 PDT',100,1,1008,'completed');
insert into new values('2013-06-06 12:00:00 PDT',100,1,1009,'completed');
insert into new values('2013-06-07 12:00:00 PDT',100,1,1010,'completed');

insert into new values('2013-06-03 12:00:00 PDT',102,1,1011,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1012,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1011,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1012,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1011,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1012,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1011,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1012,'cancelled_by_driver');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1011,'completed');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1012,'completed');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1011,'completed');
insert into new values('2013-06-03 12:00:00 PDT',102,1,1012,'completed');

insert into new values('2013-06-03 12:00:00 PDT',103,1,1011,'completed');
insert into new values('2013-06-03 12:00:00 PDT',103,1,1012,'completed');
insert into new values('2013-06-03 12:00:00 PDT',103,1,1011,'completed');
insert into new values('2013-06-03 12:00:00 PDT',103,1,1012,'completed');
insert into new values('2013-06-03 12:00:00 PDT',103,1,1011,'completed');
insert into new values('2013-06-03 12:00:00 PDT',103,1,1012,'completed');

select * from 
(
select *, rank() over (PARTITION by ta.w, ta.city_id order by ta.num_of_trips) as r
from
(select Extract(week from t) as w, driver_id, city_id, count(id) as num_of_trips                              
from new                                                                                                       
where city_id in (1,2,6) and status::text = 'completed'                                                        
and t::date >= '2013-06-03' and t::date <= '2013-06-24'                                                        
group by Extract(week from t), city_id, driver_id                                                              
order by Extract(week from t), city_id,count(id) DESC) as ta ) as final
where final.r <=2

