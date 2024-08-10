-- this script to create procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id DECIMAL)
BEGIN
	DECLARE project_id INT DEFAULT 0;
	
	SELECT id
	INTO project_id
	FROM projects
	WHERE name = project_name;

	INSERT INTO USERS(user_id, project_id)
	VALUES(user_id, project_id)
END //

DELIMITER ;
