-- Lists number of records with same score in the
-- table second_table of the database hbtn_0c_0
SELECT score, COUNT(score) as number 
FROM second_table
GROUP BY score
ORDER BY number DESC;
