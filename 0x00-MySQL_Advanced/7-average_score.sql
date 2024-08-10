-- this script to create procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE score_sum INT;
	DECLARE score_count INT;

	SELECT SUM(score)
	INTO score_sum
	FROM corrections
	WHERE corrections.user_id = user_id;


	SELECT COUNT(*)
	INTO  score_count	
	FROM  corrections
	WHERE  corrections.user_id = user_id;

	update users

	SET users.average_score =  IF(score_count = 0, 0, score_count / score_count)
        WHERE users.id = users.id;
END //

DELIMITER ;
