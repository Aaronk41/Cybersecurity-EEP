-- 1. List all players and their class
SELECT name, class, level FROM players;

-- 2. Count how many battles each player has fought
SELECT p.name, COUNT(b.battle_id) AS battles_fought
FROM players p
LEFT JOIN battles b ON p.player_id = b.player_id
GROUP BY p.name;

-- 3. List battles with monster names and result
SELECT p.name AS player, m.name AS monster, b.result, b.location
FROM battles b
JOIN players p ON b.player_id = p.player_id
JOIN monsters m ON b.monster_id = m.monster_id;

-- 4. Top monsters by how many times they were fought
SELECT m.name, COUNT(*) AS appearances
FROM battles b
JOIN monsters m ON b.monster_id = m.monster_id
GROUP BY m.name
ORDER BY appearances DESC;

-- 5. Show each player's inventory
SELECT p.name, i.name AS item, inv.quantity
FROM inventory inv
JOIN players p ON inv.player_id = p.player_id
JOIN items i ON inv.item_id = i.item_id;

-- 6. Quests and their locations
SELECT title, location FROM quests;
