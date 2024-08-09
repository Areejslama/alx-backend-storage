-- this script to create stored procedure
DELIMITER //

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
	DECLARE project_id INT DEFAULT 0;
	DECLARE project_number INT DEFAULT 0;

	SELECT COUNT(id) 
	INTO project_number
	FROM projects
	WHERE name = project_name
	IF  project_number = 0 THEN
		INSERT INTO projects(name)
		VALUES(project_name)
	END IF;

	SELECT id
	INTO project_id
	FROM projects
	WHERE name = project_name
	INSERT INTO corrections(user_id,  project_name, score)
	VALUES(user_id,  project_name, score)

END //

DELIMITER ;
