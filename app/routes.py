"""
Ce fichier contient les routes  de l'application. 
Les routes sont des URL spécifiques qui mènent à des fonctions définies dans ce fichier,
appelées vues. Chaque vue traite une requête HTTP et retourne une réponse, souvent sous la forme 
d'une page HTML rendue à l'aide d'un template
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import ReferentielFonds, ReferentielInstruments, Positions

# Créer un blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('accueil.html')

@main.route('/fonds')
def view_fonds():
    fonds = ReferentielFonds.query.all()
    return render_template('fonds.html', fonds=fonds)

@main.route('/instruments')
def view_instruments():
    instruments = ReferentielInstruments.query.all()
    return render_template('instruments.html', instruments=instruments)

@main.route('/positions/<int:fond_id>')
def view_positions(fond_id):
    # Récupérez le fond par son ID
    fond = ReferentielFonds.query.get_or_404(fond_id)

    # Récupérez les positions associées au fond
    positions = Positions.query.filter_by(fond_id=fond_id).all()

    # Passez le fond et les positions au template
    return render_template('positions.html', fond=fond, positions=positions)


"""@main.route('/positions/<int:fond_id>')
def view_positions(fond_id):
    positions = Positions.query.filter_by(fond_id=fond_id).all()
    return render_template('positions.html', positions=positions, fond_id=fond_id)"""

# Route pour afficher la page d'ajout d'un fond
@main.route('/ajout_fond', methods=['GET'])
def ajout_fond():
    return render_template('ajout_fond.html')

# Route pour ajouter un nouveau fond
@main.route('/add_fond', methods=['POST'])
def add_fond():
    try:
        name = request.form['new_nom_fond']
        type_fond = request.form['new_type_fond']
        nom_gestionnaire = request.form['new_nom_gestionnaire']
        objectif_fond = request.form['new_objectif_fond']
        date_creation = request.form['new_date_creation']
        aum = float(request.form['new_aum'])
        valeur_liquidative = float(request.form['new_valeur_liquidative'])
        devise_fond = request.form['new_devise_fond']
        code_isin = request.form['new_code_isin']

        if not name or not type_fond or not nom_gestionnaire:
            flash('Tous les champs doivent être remplis!', 'danger')
            return redirect(url_for('main.ajout_fond'))

        new_fond = ReferentielFonds(
            nom_fond=name,
            type_fond=type_fond,
            nom_gestionnaire=nom_gestionnaire,
            objectif_fond=objectif_fond,
            date_creation=date_creation,
            aum=aum,
            valeur_liquidative=valeur_liquidative,
            devise_fond=devise_fond,
            code_isin=code_isin
        )
        db.session.add(new_fond)
        db.session.commit()
        flash('Fonds ajouté avec succès!', 'success')
        return redirect(url_for('main.view_fonds'))
    except Exception as e:
        db.session.rollback()  # Annuler les changements en cas d'erreur
        flash(f'Erreur lors de l\'ajout du fonds: {str(e)}', 'danger')
        return redirect(url_for('main.ajout_fond'))

# Route pour afficher la page d'ajout d'un instrument
@main.route('/ajout_instrument', methods=['GET'])
def ajout_instrument():
    return render_template('ajout_instrument.html')

# Route pour ajouter un nouvel instrument
@main.route('/add_instrument', methods=['POST'])
def add_instrument():
    try:
        name = request.form['new_nom_instrument']
        type_ = request.form['new_type_instrument']
        secteur = request.form['new_secteur']
        code_isin = request.form['new_code_isin']
        devise = request.form['new_devise']
        prix_actuel = float(request.form['new_prix_actuel'])
        volatilite = float(request.form['new_volatilite'])

        if not name or not type_ or not code_isin:
            flash('Tous les champs doivent être remplis!', 'danger')
            return redirect(url_for('main.ajout_instrument'))

        new_instrument = ReferentielInstruments(
            nom_instrument=name,
            type_instrument=type_,
            secteur=secteur,
            code_isin=code_isin,
            devise=devise,
            prix_actuel=prix_actuel,
            volatilite=volatilite
        )
        db.session.add(new_instrument)
        db.session.commit()
        flash('Instrument ajouté avec succès!', 'success')
        return redirect(url_for('main.view_instruments'))
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de l\'ajout de l\'instrument: {str(e)}', 'danger')
        return redirect(url_for('main.ajout_instrument'))

# Route pour afficher la page d'ajout d'une position
@main.route('/ajout_position', methods=['GET'])
def ajout_position():
    fonds = ReferentielFonds.query.all()
    instruments = ReferentielInstruments.query.all()
    return render_template('ajout_position.html', fonds=fonds, instruments=instruments)

# Route pour ajouter une nouvelle position
@main.route('/add_position', methods=['POST'])
def add_position():
    try:
        fond_id = int(request.form['fond_id'])
        instrument_id = int(request.form['instrument_id'])
        quantite = float(request.form['quantite'])
        prix_achat = float(request.form['prix_achat'])
        date_achat = request.form['date_achat']
        prix_actuel = float(request.form['prix_actuel'])
        valeur_totale = float(request.form['valeur_totale'])
        rendement = float(request.form['rendement'])
        date_derniere_transaction = request.form['date_derniere_transaction']

        new_position = Positions(
            fond_id=fond_id,
            instrument_id=instrument_id,
            quantite=quantite,
            prix_achat=prix_achat,
            date_achat=date_achat,
            prix_actuel=prix_actuel,
            valeur_totale=valeur_totale,
            rendement=rendement,
            date_derniere_transaction=date_derniere_transaction
        )
        db.session.add(new_position)
        db.session.commit()
        flash('Position ajoutée avec succès!', 'success')
        return redirect(url_for('main.view_positions', fond_id=fond_id))
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de l\'ajout de la position: {str(e)}', 'danger')
        return redirect(url_for('main.ajout_position'))

# Route pour mettre à jour un fond
@main.route('/update_fond/<int:fond_id>', methods=['POST'])
def update_fond_route(fond_id):
    try:
        fond = ReferentielFonds.query.get_or_404(fond_id)
        fond.nom_fond = request.form['new_nom_fond']
        fond.type_fond = request.form['new_type_fond']
        fond.nom_gestionnaire = request.form['new_nom_gestionnaire']
        fond.objectif_fond = request.form['new_objectif_fond']
        fond.date_creation = request.form['new_date_creation']
        fond.aum = float(request.form['new_aum'])
        fond.valeur_liquidative = float(request.form['new_valeur_liquidative'])
        fond.devise_fond = request.form['new_devise_fond']
        fond.code_isin = request.form['new_code_isin']
        db.session.commit()
        flash('Fonds mis à jour avec succès!', 'success')
        return redirect(url_for('main.view_fonds'))
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la mise à jour du fonds: {str(e)}', 'danger')
        return redirect(url_for('main.view_fonds'))

# Route pour supprimer un fond
@main.route('/delete_fond/<int:fond_id>')
def delete_fond_route(fond_id):
    try:
        fond = ReferentielFonds.query.get_or_404(fond_id)
        db.session.delete(fond)
        db.session.commit()
        flash('Fonds supprimé avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la suppression du fonds: {str(e)}', 'danger')
    return redirect(url_for('main.view_fonds'))

# Route pour mettre à jour un instrument
@main.route('/update_instrument/<int:instrument_id>', methods=['POST'])
def update_instrument_route(instrument_id):
    try:
        instrument = ReferentielInstruments.query.get_or_404(instrument_id)
        instrument.nom_instrument = request.form['new_nom_instrument']
        instrument.type_instrument = request.form['new_type_instrument']
        instrument.secteur = request.form['new_secteur']
        instrument.code_isin = request.form['new_code_isin']
        instrument.devise = request.form['new_devise']
        instrument.prix_actuel = float(request.form['new_prix_actuel'])
        instrument.volatilite = float(request.form['new_volatilite'])
        db.session.commit()
        flash('Instrument mis à jour avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la mise à jour de l\'instrument: {str(e)}', 'danger')
    return redirect(url_for('main.view_instruments'))

# Route pour supprimer un instrument
@main.route('/delete_instrument/<int:instrument_id>')
def delete_instrument_route(instrument_id):
    try:
        instrument = ReferentielInstruments.query.get_or_404(instrument_id)
        db.session.delete(instrument)
        db.session.commit()
        flash('Instrument supprimé avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la suppression de l\'instrument: {str(e)}', 'danger')
    return redirect(url_for('main.view_instruments'))

# Route pour mettre à jour une position
@main.route('/update_position/<int:position_id>', methods=['POST'])
def update_position_route(position_id):
    try:
        position = Positions.query.get_or_404(position_id)
        position.quantite = float(request.form['new_quantite'])
        position.prix_achat = float(request.form['new_prix_achat'])
        position.date_achat = request.form['new_date_achat']
        position.prix_actuel = float(request.form['new_prix_actuel'])
        position.valeur_totale = float(request.form['new_valeur_totale'])
        position.rendement = float(request.form['new_rendement'])
        position.date_derniere_transaction = request.form['new_date_derniere_transaction']
        db.session.commit()
        flash('Position mise à jour avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la mise à jour de la position: {str(e)}', 'danger')
    return redirect(url_for('main.view_positions', fond_id=position.fond_id))

# Route pour supprimer une position
@main.route('/delete_position/<int:position_id>')
def delete_position_route(position_id):
    try:
        position = Positions.query.get_or_404(position_id)
        fond_id = position.fond_id
        db.session.delete(position)
        db.session.commit()
        flash('Position supprimée avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la suppression de la position: {str(e)}', 'danger')
    return redirect(url_for('main.view_positions', fond_id=fond_id))