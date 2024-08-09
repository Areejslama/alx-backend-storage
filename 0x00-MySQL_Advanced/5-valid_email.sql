-- this script to create trigger
DELIMETER //

CREATE TRIGGER account AFTER INSERT ON users
FOR EACH ROW
BEGIN
	update valid_email
	SET username = username + NEW.email
	WHERE name = NEW.valid_email
END;
//

DELIMETER ;
