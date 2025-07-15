-- Players
INSERT INTO players VALUES
(1, 'Erdrick', 'Warrior', 15, '2024-01-10'),
(2, 'Alena', 'Fighter', 12, '2024-02-05');

-- Monsters
INSERT INTO monsters VALUES
(1, 'Slime', 'Beast', 10, 3),
(2, 'Dracky', 'Flying', 18, 6),
(3, 'Golem', 'Earth', 45, 12);

-- Quests
INSERT INTO quests VALUES
(1, 'Defeat the Golem', 'Stop the rampaging golem in the west cave.', 'Hard', 'West Cave', 300),
(2, 'Clear the Forest', 'Eliminate all Slimes in Emerald Forest.', 'Easy', 'Emerald Forest', 100);

-- Items
INSERT INTO items VALUES
(1, 'Iron Sword', 'Weapon', 10),
(2, 'Potion', 'Consumable', 0),
(3, 'Steel Shield', 'Armor', 5);

-- Inventory
INSERT INTO inventory VALUES
(1, 1, 1, 1),
(2, 1, 2, 3),
(3, 2, 3, 1);

-- Battles
INSERT INTO battles VALUES
(1, 1, 3, 'West Cave', 'Victory', '2024-05-01'),
(2, 2, 1, 'Emerald Forest', 'Victory', '2024-05-02'),
(3, 2, 2, 'Emerald Forest', 'Defeat', '2024-05-03');
