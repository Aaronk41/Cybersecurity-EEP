-- 1. List all Pokémon species and their primary/secondary types
SELECT ps.name AS pokemon, GROUP_CONCAT(t.name ORDER BY pt.type_id) AS types
FROM pokemon_species ps
JOIN pokemon_types pt ON ps.species_id = pt.species_id
JOIN types t ON pt.type_id = t.type_id
GROUP BY ps.species_id;

-- 2. Find all Pokémon that have the ability "Overgrow"
SELECT ps.name AS pokemon
FROM pokemon_species ps
JOIN pokemon_abilities pa ON ps.species_id = pa.species_id
JOIN abilities a ON pa.ability_id = a.ability_id
WHERE a.name = 'Overgrow';

-- 3. Show all evolutions in the format: Bulbasaur -> Ivysaur (Level 16)
SELECT a.name AS evolves_from, b.name AS evolves_to, e.evolution_level
FROM evolutions e
JOIN pokemon_species a ON e.from_species_id = a.species_id
JOIN pokemon_species b ON e.to_species_id = b.species_id;

-- 4. List all Pokémon from the Kanto region
SELECT ps.name AS pokemon
FROM pokemon_species ps
JOIN pokemon_regions pr ON ps.species_id = pr.species_id
JOIN regions r ON pr.region_id = r.region_id
WHERE r.name = 'Kanto';

-- 5. Count how many Pokémon exist per type
SELECT t.name AS type, COUNT(pt.species_id) AS pokemon_count
FROM types t
JOIN pokemon_types pt ON t.type_id = pt.type_id
GROUP BY t.name
ORDER BY pokemon_count DESC;

-- 6. Show Pokémon that have more than one type
SELECT ps.name AS pokemon, COUNT(pt.type_id) AS num_types
FROM pokemon_species ps
JOIN pokemon_types pt ON ps.species_id = pt.species_id
GROUP BY ps.species_id
HAVING COUNT(pt.type_id) > 1;

-- 7. List Pokémon species, their height and weight in metric
SELECT name, height_cm, weight_kg
FROM pokemon_species
ORDER BY height_cm DESC;

-- 8. Show all Pokémon with a hidden ability
SELECT ps.name AS pokemon, a.name AS ability
FROM pokemon_species ps
JOIN pokemon_abilities pa ON ps.species_id = pa.species_id
JOIN abilities a ON pa.ability_id = a.ability_id
WHERE pa.is_hidden = TRUE;
