-- Types
INSERT INTO types VALUES
(1, 'Electric'), (2, 'Fire'), (3, 'Water'), (4, 'Grass');

-- Regions
INSERT INTO regions VALUES
(1, 'Kanto'), (2, 'Johto'), (3, 'Hoenn');

-- Pokémon species
INSERT INTO pokemon_species VALUES
(25, 'Pikachu', 1, 40, 6, 112),
(26, 'Raichu', 1, 80, 30, 218),
(1, 'Bulbasaur', 1, 70, 7, 64),
(2, 'Ivysaur', 1, 100, 13, 142);

-- Pokémon types
INSERT INTO pokemon_types VALUES
(25, 1), (26, 1), -- Pikachu & Raichu: Electric
(1, 4), (1, 3),   -- Bulbasaur: Grass/Water (demo)
(2, 4), (2, 3);

-- Abilities
INSERT INTO abilities VALUES
(1, 'Static', 'May cause paralysis on contact'),
(2, 'Overgrow', 'Boosts Grass moves when HP is low');

-- Pokémon abilities
INSERT INTO pokemon_abilities VALUES
(25, 1, FALSE), (1, 2, FALSE), (2, 2, FALSE);

-- Evolutions
INSERT INTO evolutions VALUES
(25, 26, NULL),   -- Pikachu → Raichu
(1, 2, 16);       -- Bulbasaur → Ivysaur at level 16

-- Pokémon regions
INSERT INTO pokemon_regions VALUES
(25, 1), (26, 1), (1, 1), (2, 1);
