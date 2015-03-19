'''
The SQL below will give you the correct answer – 
but you will have to plug in an actual value for N of course. 
This SQL to find the Nth highest salary should work in 
SQL Server, MySQL, DB2, Oracle, Teradata, and almost any other RDBMS:
'''

SELECT max(Emp1.Salary) /*the max() is to prevent from multiple return entries, see examples below*/
FROM Employee Emp1
WHERE (N-1) = ( /* Subquery starts here */
SELECT COUNT(DISTINCT(Emp2.Salary))
FROM Employee Emp2
WHERE Emp2.Salary > Emp1.Salary)

##e.g find the second highest salary in emp1 table
select emp1.salary
from Employee emp1
where (1) = (select count(distinct(emp2.salary))
			 from Employee emp2
			 where emp2.salary > emp1.salary)


'''
Explaination:

The query above can be quite confusing if you have not seen anything like it before – 
pay special attention to the fact that “Emp1″ appears in both the subquery 
(also known as an inner query) and the “outer” query. 
The outer query is just the part of the query that is not the subquery/inner query – 
both parts of the query are clearly labeled in the comments.


The subquery is a correlated subquery

The subquery in the SQL above is actually a specific type of subquery known as a correlated subquery. 
The reason it is called a correlated subquery is because the the subquery uses a value from the outer 
query in it’s WHERE clause. In this case that value is the Emp1 table alias as we pointed out earlier. 
A normal subquery can be run independently of the outer query, but a correlated subquery can NOT be run 
independently of the outer query. 


A more visualized explaination:
Let’s assume that we are using this data:

       Employee
Employee ID	| Salary
	3		|  200
	4		|  800
	7		|  450
	8       |  450
The first thing that the query above does is process the very first row of the Employee table, 
which has an alias of Emp1.

The salary in the first row of the Employee table is 200. Because the subquery is correlated to 
the outer query through the alias Emp1, it means that when the first row is processed, the query 
will essentially look like this – note that all we did is replace Emp1.Salary with the value of 200:
'''
SELECT max(Salary)
FROM Employee Emp1
WHERE (1) = (
SELECT COUNT(DISTINCT(Emp2.Salary))
FROM Employee Emp2
WHERE Emp2.Salary > 200)

'''
So, what exactly is happening when that first row is processed? 
Well, if you pay special attention to the subquery you will notice that it’s basically
searching for the count of salary entries in the Employee table that are greater than 200. 

Basically, the subquery is trying to find how many salary entries are greater than 200. 
Then, that count of salary entries is checked to see if it equals 1 in the outer query, 
and if so then everything from that particular row in Emp1 will be returned.

In the above case the count in the subquery is 2.
So, what happens next? Well, the SQL processor will move on to the next row which is 800, 
and the resulting query looks like this:'''

SELECT max(Emp1.Salary)
FROM Employee Emp1
WHERE (1) = (
SELECT COUNT(DISTINCT(Emp2.Salary))
FROM Employee Emp2
WHERE Emp2.Salary > 800)


'''
Clearly it returns 0 in the above case.

Since there are no salaries greater than 800, the query will move on to the last row and 
will of course find the answer as 450. This is because 800 is greater than 450, and the count will be 1.
like below'''

SELECT max(Emp1.Salary)
FROM Employee Emp1
WHERE (1) = (
SELECT COUNT(DISTINCT(Emp2.Salary))
FROM Employee Emp2
WHERE Emp2.Salary > 450)

'''
In the above case, when Emp1.Salary = 450, the where clause in the outer query satisfies.
Note that if the max() method is not used, then it will give an error of "subquery returns more than 1 row"

!!!!!
This is because if where clause is used like this "where x = ", it only expects one value, can not be equal to
multiple values.
If you actually want more than one result, restructure it like this:

           where disease_id IN (subquery returning multiple rows...)
!!!!!!!
Note that Emp1 and Emp2 are both aliases for the same table – Employee. 
Emp2 is only being used in the subquery to compare all the salary values to the current s
alary value chosen in Emp1. This allows us to find the number of salary entries (the count) 
that are greater than 200. And if this number is equal to N-1 (which is 1 in our case) 
then we know that we have a winner – and that we have found our answer.


'''

'''
We can also write as the following in MySQL:

'''
SELECT Salary FROM Employee 
ORDER BY Salary DESC LIMIT n-1,1


'''
and specifically for the second highest, another way is:
'''
select max(salary) as SecondHighestSalary
from Employee
where salary < (select max(salary) from Employee )
'''
The key part of the query to pay attention to is the “LIMIT N-1, 1″. 
The LIMIT clause takes two arguments in that query – the first argument 
specifies the offset of the first row to return, and the second specifies 
the maximum number of rows to return. So, it’s saying that the offset of the first row to return 
should be N-1, and the max number of rows to return is 1. What exactly is the offset? 
Well, the offset is just a numerical value that represents the number of rows from the very first row, 
and since the rows are arranged in descending order we know that the row at an offset of N-1 will 
contain the (N-1)th highest salary.
'''

'''
source : http://www.programmerinterview.com/index.php/database-sql/find-nth-highest-salary-sql/
'''