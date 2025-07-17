-- Table: pokemon_species
CREATE TABLE pokemon_species (
    species_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    generation INT,
    height_cm INT,
    weight_kg INT,
    base_experience INT
);

-- Table: types
CREATE TABLE types (
    type_id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

-- Table: pokemon_types (Many-to-Many)
CREATE TABLE pokemon_types (
    species_id INT,
    type_id INT,
    PRIMARY KEY (species_id, type_id),
    FOREIGN KEY (species_id) REFERENCES pokemon_species(species_id),
    FOREIGN KEY (type_id) REFERENCES types(type_id)
);

-- Table: abilities
CREATE TABLE abilities (
    ability_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    effect TEXT
);

-- Table: pokemon_abilities (Many-to-Many)
CREATE TABLE pokemon_abilities (
    species_id INT,
    ability_id INT,
    is_hidden BOOLEAN,
    PRIMARY KEY (species_id, ability_id),
    FOREIGN KEY (species_id) REFERENCES pokemon_species(species_id),
    FOREIGN KEY (ability_id) REFERENCES abilities(ability_id)
);

-- Table: evolutions (Self-Join)
CREATE TABLE evolutions (
    from_species_id INT,
    to_species_id INT,
    evolution_level INT,
    PRIMARY KEY (from_species_id, to_species_id),
    FOREIGN KEY (from_species_id) REFERENCES pokemon_species(species_id),
    FOREIGN KEY (to_species_id) REFERENCES pokemon_species(species_id)
);

-- Table: regions
CREATE TABLE regions (
    region_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Table: pokemon_regions (Many-to-Many)
CREATE TABLE pokemon_regions (
    species_id INT,
    region_id INT,
    PRIMARY KEY (species_id, region_id),
    FOREIGN KEY (species_id) REFERENCES pokemon_species(species_id),
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);
