-- this script to define trigger
DELIMITER //
CREATE TRIGGER value AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.quantity_ordered
	WHERE name = NEW.item_name;
END;
//
DELIMITER ;
