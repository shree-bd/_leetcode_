# Write your MySQL query statement below
SELECT name as Department, Employee, Salary
FROM (select d.name, E.NAME AS Employee, Salary,
dense_rank() over (partition by d.name order by salary desc) as rnk
FROM EMPLOYEE e join department d ON e.departmentId = d.id) as ranked
WHERE rnk=1
