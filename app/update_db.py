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
    cursor.execute("""
    UPDATE referentiel_fonds 
    SET nom_fond = %s, description = %s 
    WHERE id = %s
    """, (new_name, new_description, fond_id))
    print(f"Fond {fond_id} mis à jour avec succès.")

def delete_fond(cursor, fond_id):
    cursor.execute("DELETE FROM referentiel_fonds WHERE id = %s", (fond_id,))
    print(f"Fond {fond_id} supprimé avec succès.")

def update_instrument(cursor, instrument_id, new_name, new_type, new_description):
    cursor.execute("""
    UPDATE referentiel_instruments 
    SET nom_instrument = %s, type_instrument = %s, description = %s 
    WHERE id = %s
    """, (new_name, new_type, new_description, instrument_id))
    print(f"Instrument {instrument_id} mis à jour avec succès.")

def delete_instrument(cursor, instrument_id):
    cursor.execute("DELETE FROM referentiel_instruments WHERE id = %s", (instrument_id,))
    print(f"Instrument {instrument_id} supprimé avec succès.")

def update_position(cursor, position_id, new_quantite, new_prix_achat, new_date_achat):
    cursor.execute("""
    UPDATE positions 
    SET quantite = %s, prix_achat = %s, date_achat = %s 
    WHERE id = %s
    """, (new_quantite, new_prix_achat, new_date_achat, position_id))
    print(f"Position {position_id} mise à jour avec succès.")

def delete_position(cursor, position_id):
    cursor.execute("DELETE FROM positions WHERE id = %s", (position_id,))
    print(f"Position {position_id} supprimée avec succès.")

# Appeler les fonctions
update_fond(cursor, 1, 'Fonds Alpha Modifié', 'Description mise à jour pour le Fonds Alpha.')
delete_fond(cursor, 2)

update_instrument(cursor, 1, 'Apple Inc. Modifié', 'Action', 'Action de la société Apple Inc. mise à jour.')
delete_instrument(cursor, 2)

update_position(cursor, 1, 120, 155.00, '2024-01-15')
delete_position(cursor, 2)

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()