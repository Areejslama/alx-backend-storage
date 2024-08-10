-- this script to create procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id DECIMAL)
BEGIN
	DECLARE project_id INT DEFAULT 0;
	DECLARE avg_score FLOAT;

	SELECT id
        INTO project_id
        FROM projects
        WHERE name = project_name;

	SELECT AVG(avg_score)
	INTO average_score
	FROM users
	WHERE user_id = user_id;

        INSERT INTO correction(user_id, project_id, score)
        VALUES(user_id, project_id, avg_score)
END //

DELIMITER ;
