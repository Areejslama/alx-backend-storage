-- this script to sort bands
SELECT band_name, (2022, split - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
