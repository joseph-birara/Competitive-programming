# Write your MySQL query statement below

SELECT Person.firstName as firstName, Person.lastName as lastName, Address.city as city, Address.state as state
FROM Person LEFT JOIN Address ON Person.personId = Address.personId