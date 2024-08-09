-- this script to create trigger
DELIMITER //

CREATE TRIGGER account BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	UPDATE valid_email
	SET username = CONCAT(username, NEW.email)
	WHERE name = NEW.valid_email;
END;
//

DELIMITER ;
