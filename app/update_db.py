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

# Définir les fonctions pour mettre à jour , ajouter et supprimer les données
def update_fond(cursor, fond_id, new_nom, new_type, new_gestionnaire, new_objectif, new_date_creation, new_aum, new_devise, new_code_isin):
    try:
        cursor.execute("""
        UPDATE referentiel_fonds 
        SET nom_fond = %s, type_fond = %s, nom_gestionnaire = %s, objectif_fond = %s, date_creation = %s, aum = %s, valeur_liquidative = %s,  devise_fond = %s,  code_isin = %s 
        WHERE id = %s
        """, (new_nom, new_type, new_gestionnaire, new_objectif, new_date_creation, new_aum, new_devise, new_code_isin, fond_id))
        print(f"Fond {fond_id} mis à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour du fond {fond_id}: {err}")

def delete_fond(cursor, fond_id):
    try:
        cursor.execute("DELETE FROM referentiel_fonds WHERE id = %s", (fond_id,))
        print(f"Fond {fond_id} supprimé avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression du fond {fond_id}: {err}")

def add_fond(cursor, nom, type_fond, gestionnaire, objectif, date_creation, aum, valeur_liquidative, devise, code_isin):
    try:
        cursor.execute("""
        INSERT INTO referentiel_fonds (nom_fond, type_fond, nom_gestionnaire, objectif_fond, date_creation, aum, valeur_liquidative, devise_fond, code_isin) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nom, type_fond, gestionnaire, objectif, date_creation, aum, valeur_liquidative, devise, code_isin))
        print(f"Nouveau fond ajouté avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout du fond: {err}")

def update_instrument(cursor, instrument_id, new_nom, new_type, new_secteur, new_code_isin, new_devise, new_prix, new_volatilite):
    try:
        cursor.execute("""
        UPDATE referentiel_instruments 
        SET nom_instrument = %s, type_instrument = %s, secteur = %s, code_isin = %s, devise = %s, prix_actuel = %s, volatilite = %s 
        WHERE id = %s
        """, (new_nom, new_type, new_secteur, new_code_isin, new_devise, new_prix, new_volatilite, instrument_id))
        print(f"Instrument {instrument_id} mis à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour de l'instrument {instrument_id}: {err}")

def delete_instrument(cursor, instrument_id):
    try:
        cursor.execute("DELETE FROM referentiel_instruments WHERE id = %s", (instrument_id,))
        print(f"Instrument {instrument_id} supprimé avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression de l'instrument {instrument_id}: {err}")

def add_instrument(cursor, nom, type_, secteur, code_isin, devise, prix, volatilite):
    try:
        cursor.execute("""
        INSERT INTO referentiel_instruments (nom_instrument, type_instrument, secteur, code_isin, devise, prix_actuel, volatilite) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nom, type_, secteur, code_isin, devise, prix, volatilite))
        print(f"Nouvel instrument ajouté avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout de l'instrument: {err}")

def update_position(cursor, position_id, new_quantite, new_prix_achat, new_date_achat, new_prix_actuel, new_valeur_totale, new_rendement, new_date_transaction):
    try:
        cursor.execute("""
        UPDATE positions 
        SET quantite = %s, prix_achat = %s, date_achat = %s, prix_actuel = %s, valeur_totale = %s, rendement = %s, date_derniere_transaction = %s 
        WHERE id = %s
        """, (new_quantite, new_prix_achat, new_date_achat, new_prix_actuel, new_valeur_totale, new_rendement, new_date_transaction, position_id))
        print(f"Position {position_id} mise à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour de la position {position_id}: {err}")

def delete_position(cursor, position_id):
    try:
        cursor.execute("DELETE FROM positions WHERE id = %s", (position_id,))
        print(f"Position {position_id} supprimée avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression de la position {position_id}: {err}")

def add_position(cursor,  instrument_id, quantite, prix_achat, date_achat, prix_actuel, valeur_totale, rendement, date_derniere_transaction):
    try:
        cursor.execute("""
        INSERT INTO positions ( instrument_id, quantite, prix_achat, date_achat, prix_actuel, valeur_totale, rendement, date_derniere_transaction) 
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)
        """, ( instrument_id, quantite, prix_achat, date_achat, prix_actuel, valeur_totale, rendement, date_derniere_transaction))
        print(f"Nouvelle position ajoutée avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout de la position: {err}")


# Exemple de tests avec des IDs spécifiques
try:
    update_fond(cursor, 1, 'Fonds Alpha Modifié', 'Actions', 'Gestionnaire Alpha', 'Objectif modifié', '2024-02-01', 1100000.00, 155.00, 'USD', 'US0000000001')
    delete_fond(cursor, 3)  # Suppression d'un fond avec un ID au hasard
    add_fond(cursor, 'Nouveau Fond', 'Obligations', 'Gestionnaire Nouveau', 'Objectif nouveau', '2024-03-01', 3000000.00, 100.00, 'EUR', 'EU0000000003')

    update_instrument(cursor, 1, 'Apple Inc. Modifié', 'Action', 'Technologie', 'US0378331005', 'USD', 155.00, 1.25)
    delete_instrument(cursor, 3)  # Suppression d'un instrument avec un ID au hasard
    add_instrument(cursor, 'Microsoft Inc.', 'Action', 'Technologie', 'US5949181045', 'USD', 300.00, 0.40)

    update_position(cursor, 1, 120, 155.00, '2024-01-15', 180.00, 21600.00, 16.67, '2024-02-01')
    delete_position(cursor, 3)  # Suppression d'une position avec un ID au hasard
    add_position(cursor, 2, 100, 150.00, '2024-02-01', 170.00, 17000.00, 13.33, '2024-02-15')
except mysql.connector.Error as err:
    print(f"Erreur lors de l'exécution des opérations: {err}")

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()