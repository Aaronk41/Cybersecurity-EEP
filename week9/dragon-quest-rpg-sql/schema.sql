CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT,
    level INTEGER,
    join_date DATE
);

CREATE TABLE monsters (
    monster_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    hp INTEGER,
    attack INTEGER
);

CREATE TABLE quests (
    quest_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    difficulty TEXT,
    location TEXT,
    reward_gold INTEGER
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    power INTEGER
);

CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY,
    player_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE TABLE battles (
    battle_id INTEGER PRIMARY KEY,
    player_id INTEGER,
    monster_id INTEGER,
    location TEXT,
    result TEXT,
    battle_date DATE,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (monster_id) REFERENCES monsters(monster_id)
);
