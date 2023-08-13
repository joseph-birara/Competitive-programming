-- Retrieve names of employees who earn more than their managers.
SELECT e.name AS Employee
FROM employee e
JOIN employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
