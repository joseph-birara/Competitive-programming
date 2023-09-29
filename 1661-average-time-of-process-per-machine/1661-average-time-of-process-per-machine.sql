# Write your MySQL query statement below


SELECT machine_id, 
       ROUND(SUM(timestamp * (CASE WHEN activity_type = 'end' THEN 1 ELSE -1 END)) / 
             COUNT(DISTINCT process_id), 3) AS processing_time
  FROM Activity
GROUP BY machine_id;
