-- this script to sort bands
SELECT band_name, (IFNULL(split, 0) - IFNULL(formed, 0))
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
