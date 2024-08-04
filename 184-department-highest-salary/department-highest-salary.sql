SELECT Department, Employee, Salary
FROM (
    SELECT d.name AS Department, e.NAME AS Employee, e.Salary,
           RANK() OVER (PARTITION BY d.name ORDER BY e.Salary DESC) AS rnk
    FROM EMPLOYEE e
    JOIN department d ON e.departmentId = d.id
) AS ranked
WHERE rnk = 1;
