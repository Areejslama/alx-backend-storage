-- this script to define trigger
delimiter //
CREATE TRIGGER value AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET @quantity = @quantity - NEW.quantity_orderd
	WHERE name = NEW.item_name;
END;//
delimiter;
