-- this script to create trigger
DELIMITER //

CREATE TRIGGER account AFTER INSERT ON users
FOR EACH ROW
BEGIN
	update valid_email
	SET username = CONCAT(username,  NEW.email)
	WHERE name = NEW.valid_email;
END;
//

DELIMITER ;
