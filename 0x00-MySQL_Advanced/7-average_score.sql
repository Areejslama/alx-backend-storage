-- this script to create procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id DECIMAL)
BEGIN
	DECLARE project_id INT DEFAULT 0;
	DECLARE avg_score FLOAT;

	SELECT AVG(score)
	INTO average_score
	FROM users
	WHERE id = user_id;


        INSERT INTO correction(user_id, project_id, score)
        VALUES(user_id, project_id, average_score)
END //

DELIMITER ;
