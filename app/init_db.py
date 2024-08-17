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

# Créer la base de données
cursor.execute("CREATE DATABASE IF NOT EXISTS portfolio_db")
cursor.execute("USE portfolio_db")

# Créer les tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS referentiel_fonds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS referentiel_instruments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS positions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fond_id INT,
    instrument_id INT,
    quantity INT,
    price FLOAT,
    FOREIGN KEY (fond_id) REFERENCES referentiel_fonds(id),
    FOREIGN KEY (instrument_id) REFERENCES referentiel_instruments(id)
)
""")

# Fermer la connexion
cursor.close()
conn.close()

print("Base de données et tables créées avec succès.")