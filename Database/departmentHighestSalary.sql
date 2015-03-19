'''
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

If there is no result in certain Department, omit the department on the result.
'''


select s.Department as Department, e1.Name as Employee, s.Salary as Salary
from 
(
	select d.Name as Department, max(e.Salary) as Salary, d.Id as Id
	from Department d inner join Employee e
	on e.DepartmentId = d.Id
	group by d.Id, d.Name
) s inner join Employee e1
on e1.DepartmentId = s.Id 
and e1.Salary = s.Salary







































