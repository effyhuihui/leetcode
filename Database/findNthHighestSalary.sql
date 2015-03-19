'''
The SQL below will give you the correct answer – 
but you will have to plug in an actual value for N of course. 
This SQL to find the Nth highest salary should work in 
SQL Server, MySQL, DB2, Oracle, Teradata, and almost any other RDBMS:
'''

SELECT * /*This is the outer query part */
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