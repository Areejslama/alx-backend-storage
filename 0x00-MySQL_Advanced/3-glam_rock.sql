-- this script to sort bands
SELECT band_name, (split(2022, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
