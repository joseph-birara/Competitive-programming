SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Department d
JOIN Employee e ON d.id = e.departmentId
WHERE (e.salary, e.departmentId) IN (
    SELECT MAX(salary), departmentId
    FROM Employee
    GROUP BY departmentId
);
