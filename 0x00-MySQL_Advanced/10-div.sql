-- this script to define function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE result float default 0;

	IF b = 0 THEN
		RETURN 0;
	ELSE
		SET result = a / b;
	END IF;
	RETURN result;
END //

DELIMITER ;
