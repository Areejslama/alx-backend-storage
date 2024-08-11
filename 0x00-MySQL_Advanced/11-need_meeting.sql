-- this script to create view
CREATE VIEW need_meeting 
AS SELECT name, score, last_meeting
FROM students
WHERE score < 80 
AND (last_meeting IS NULL 
	OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
