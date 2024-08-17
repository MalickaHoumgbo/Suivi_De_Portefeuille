# Ce script Python utilise la bibliothèque mysql.connector pour interagir directement avec MySQL. 

import mysql.connector

# Configuration de la connexion à MySQL
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost'
}

# Connexion à MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Supprimer la base de données existante
cursor.execute("DROP DATABASE IF EXISTS portfolio_db")

# Créer la base de données
cursor.execute("CREATE DATABASE IF NOT EXISTS portfolio_db")
cursor.execute("USE portfolio_db")

# Créer les tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS referentiel_fonds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom_fond VARCHAR(100) NOT NULL,
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS referentiel_instruments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom_instrument VARCHAR(100) NOT NULL,
    type_instrument VARCHAR(50),
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS positions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fond_id INT,
    instrument_id INT,
    quantite DECIMAL(10, 2),
    prix_achat DECIMAL(10, 2),
    date_achat DATE,
    FOREIGN KEY (fond_id) REFERENCES referentiel_fonds(id),
    FOREIGN KEY (instrument_id) REFERENCES referentiel_instruments(id)
)
""")

# Insérer des données d'exemple
cursor.execute("""
INSERT INTO referentiel_fonds (nom_fond, description)
VALUES 
    ('Fonds Alpha', 'Fonds axé sur la technologie.'),
    ('Fonds Beta', 'Fonds diversifié à l''échelle mondiale.')
""")

cursor.execute("""
INSERT INTO referentiel_instruments (nom_instrument, type_instrument, description)
VALUES 
    ('Apple Inc.', 'Action', 'Action de la société Apple Inc.'),
    ('Obligation US 10 ans', 'Obligation', 'Obligation du gouvernement américain à 10 ans.')
""")

cursor.execute("""
INSERT INTO positions (fond_id, instrument_id, quantite, prix_achat, date_achat)
VALUES 
    (1, 1, 100, 150.00, '2024-01-01'),
    (1, 2, 50, 102.50, '2024-02-01'),
    (2, 1, 200, 145.00, '2024-03-01')
""")

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()

print("Base de données et tables créées avec succès.")
