CREATE TABLE IF NOT EXISTS users(
    ID INT UNSIGNED AUTO_INCREMENT,
    Username VARCHAR(100) NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Admin BOOLEAN NOT NULL,
    CONSTRAINT pkID PRIMARY KEY (ID),
    CONSTRAINT uqUsername UNIQUE (Username)
);
INSERT INTO users (Username, PasswordHash, Admin) -- Insert admin user if not exists
VALUES (
        'admin',
        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
        TRUE
    ) ON DUPLICATE KEY
UPDATE ID = ID;