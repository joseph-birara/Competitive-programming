# Write your MySQL query statement below
SELECT name AS name FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;
