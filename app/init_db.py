# Ce script Python utilise la bibliothèque mysql.connector pour interagir directement avec MySQL. 

import mysql.connector

# Configuration de la connexion à MySQL
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'portfolio_db'
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
    type_fond VARCHAR(50),
    nom_gestionnaire VARCHAR(100),
    objectif_fond TEXT,
    date_creation DATE,
    aum DECIMAL(15, 2),
    valeur_liquidative DECIMAL(15, 2),
    devise_fond VARCHAR(10),
    code_isin VARCHAR(12) UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS referentiel_instruments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom_instrument VARCHAR(100) NOT NULL,
    type_instrument VARCHAR(50),
    secteur VARCHAR(50),
    code_isin VARCHAR(12) UNIQUE,
    devise VARCHAR(10),
    prix_actuel DECIMAL(15, 2),
    volatilite DECIMAL(5, 2)
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
    prix_actuel DECIMAL(15, 2),
    valeur_totale DECIMAL(15, 2),
    rendement DECIMAL(5, 2),
    date_derniere_transaction DATE,
    FOREIGN KEY (fond_id) REFERENCES referentiel_fonds(id),
    FOREIGN KEY (instrument_id) REFERENCES referentiel_instruments(id)
)
""")

# Insérer des données d'exemple
cursor.execute("""
INSERT INTO referentiel_fonds (nom_fond, type_fond, nom_gestionnaire, objectif_fond, date_creation, aum, valeur_liquidative, devise_fond, code_isin)
VALUES 
    (' Alpha', 'Actions', 'Gestionnaire Alpha', 'Croissance à long terme', '2024-01-01', 1000000.00, 150.00, 'USD', 'US0000000001'),
    (' Beta', 'Obligations', 'Gestionnaire Beta', 'Revenus stables', '2024-02-01', 2000000.00, 95.00, 'EUR', 'EU0000000002')
""")

cursor.execute("""
INSERT INTO referentiel_instruments (nom_instrument, type_instrument, secteur, code_isin, devise, prix_actuel, volatilite)
VALUES 
    ('Apple Inc.', 'Action', 'Technologie', 'US0378331005', 'USD', 150.00, 1.20),
    ('Obligation US 10 ans', 'Obligation', 'Government', 'US912828W185', 'USD', 102.50, 0.30)
""")

cursor.execute("""
INSERT INTO positions (fond_id, instrument_id, quantite, prix_achat, date_achat, prix_actuel, valeur_totale, rendement, date_derniere_transaction)
VALUES 
    (1, 1, 100, 150.00, '2024-01-01', 155.00, 15500.00, 3.33, '2024-02-01'),
    (1, 2, 50, 102.50, '2024-02-01', 105.00, 5250.00, 2.44, '2024-03-01'),
    (2, 1, 200, 145.00, '2024-03-01', 150.00, 30000.00, 3.45, '2024-04-01')
""")

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()

print("Base de données et tables créées avec succès.")
