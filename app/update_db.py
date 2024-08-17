"""
ce fichier contient un script autonome pour effectuer des mises à jour
et des suppressions dans la base de données.
"""

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

# Définir les fonctions pour mettre à jour et supprimer les données
def update_fond(cursor, fond_id, new_name, new_description):
    try:
        cursor.execute("""
        UPDATE referentiel_fonds 
        SET nom_fond = %s, description = %s 
        WHERE id = %s
        """, (new_name, new_description, fond_id))
        print(f"Fond {fond_id} mis à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour du fond {fond_id}: {err}")

def delete_fond(cursor, fond_id):
    try:
        cursor.execute("DELETE FROM referentiel_fonds WHERE id = %s", (fond_id,))
        print(f"Fond {fond_id} supprimé avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression du fond {fond_id}: {err}")

def add_fond(cursor, name, description):
    try:
        cursor.execute("""
        INSERT INTO referentiel_fonds (nom_fond, description) 
        VALUES (%s, %s)
        """, (name, description))
        print(f"Nouveau fond ajouté avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout du fond: {err}")

def update_instrument(cursor, instrument_id, new_name, new_type, new_description):
    try:
        cursor.execute("""
        UPDATE referentiel_instruments 
        SET nom_instrument = %s, type_instrument = %s, description = %s 
        WHERE id = %s
        """, (new_name, new_type, new_description, instrument_id))
        print(f"Instrument {instrument_id} mis à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour de l'instrument {instrument_id}: {err}")

def delete_instrument(cursor, instrument_id):
    try:
        cursor.execute("DELETE FROM referentiel_instruments WHERE id = %s", (instrument_id,))
        print(f"Instrument {instrument_id} supprimé avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression de l'instrument {instrument_id}: {err}")

def add_instrument(cursor, name, type_, description):
    try:
        cursor.execute("""
        INSERT INTO referentiel_instruments (nom_instrument, type_instrument, description) 
        VALUES (%s, %s, %s)
        """, (name, type_, description))
        print(f"Nouvel instrument ajouté avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout de l'instrument: {err}")

def update_position(cursor, position_id, new_quantite, new_prix_achat, new_date_achat):
    try:
        cursor.execute("""
        UPDATE positions 
        SET quantite = %s, prix_achat = %s, date_achat = %s 
        WHERE id = %s
        """, (new_quantite, new_prix_achat, new_date_achat, position_id))
        print(f"Position {position_id} mise à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour de la position {position_id}: {err}")

def delete_position(cursor, position_id):
    try:
        cursor.execute("DELETE FROM positions WHERE id = %s", (position_id,))
        print(f"Position {position_id} supprimée avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression de la position {position_id}: {err}")

# Exemple de tests avec des IDs spécifiques
try:
    update_fond(cursor, 1, 'Fonds Alpha Modifié', 'Description mise à jour pour le Fonds Alpha.')
    delete_fond(cursor, 3)  # Suppression d'un fond avec un ID au hasard
    add_fond(cursor, 'Nouveau Fond', 'Description pour le nouveau fond.')

    update_instrument(cursor, 1, 'Apple Inc. Modifié', 'Action', 'Action de la société Apple Inc. mise à jour.')
    delete_instrument(cursor, 3)  # Suppression d'un instrument avec un ID au hasard
    add_instrument(cursor, 'Microsoft Inc.', 'Action', 'Action de la société Microsoft.')

    update_position(cursor, 1, 120, 155.00, '2024-01-15')
    delete_position(cursor, 3)  # Suppression d'une position avec un ID au hasard
except mysql.connector.Error as err:
    print(f"Erreur lors de l'exécution des opérations: {err}")

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()
