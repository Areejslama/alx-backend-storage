-- this script to define trigger
CREATE TRIGGER value AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	SET @quantity = @quantity - NEW.quantity_orderd
END;
