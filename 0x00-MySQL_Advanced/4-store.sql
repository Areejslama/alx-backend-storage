-- this script to define trigger
CREATE TRIGGER quantity AFTER INSERT ON items
FOR EACH ROW
BEGIN
	SET @order = @order - NEW.quantity_id
END
