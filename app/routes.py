"""
Ce fichier contient les routes  de l'application. 
Les routes sont des URL spécifiques qui mènent à des fonctions définies dans ce fichier,
appelées vues. Chaque vue traite une requête HTTP et retourne une réponse, souvent sous la forme 
d'une page HTML rendue à l'aide d'un template
"""
from flask import Blueprint, render_template, request, redirect, url_for
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
    positions = Positions.query.filter_by(fond_id=fond_id).all()
    return render_template('positions.html', positions=positions)

# Route pour mettre à jour un fond
@main.route('/update_fond/<int:fond_id>', methods=['POST'])
def update_fond_route(fond_id):
    fond = ReferentielFonds.query.get_or_404(fond_id)
    fond.nom_fond = request.form['new_name']
    fond.description = request.form['new_description']
    db.session.commit()
    return redirect(url_for('main.view_fonds'))

# Route pour supprimer un fond
@main.route('/delete_fond/<int:fond_id>')
def delete_fond_route(fond_id):
    fond = ReferentielFonds.query.get_or_404(fond_id)
    db.session.delete(fond)
    db.session.commit()
    return redirect(url_for('main.view_fonds'))

# Route pour mettre à jour un instrument
@main.route('/update_instrument/<int:instrument_id>', methods=['POST'])
def update_instrument_route(instrument_id):
    instrument = ReferentielInstruments.query.get_or_404(instrument_id)
    instrument.nom_instrument = request.form['new_name']
    instrument.type_instrument = request.form['new_type']
    instrument.description = request.form['new_description']
    db.session.commit()
    return redirect(url_for('main.view_instruments'))

# Route pour supprimer un instrument
@main.route('/delete_instrument/<int:instrument_id>')
def delete_instrument_route(instrument_id):
    instrument = ReferentielInstruments.query.get_or_404(instrument_id)
    db.session.delete(instrument)
    db.session.commit()
    return redirect(url_for('main.view_instruments'))

# Route pour mettre à jour une position
@main.route('/update_position/<int:position_id>', methods=['POST'])
def update_position_route(position_id):
    position = Positions.query.get_or_404(position_id)
    position.quantite = request.form['new_quantite']
    position.prix_achat = request.form['new_prix_achat']
    position.date_achat = request.form['new_date_achat']
    db.session.commit()
    return redirect(url_for('main.view_positions', fond_id=position.fond_id))

# Route pour supprimer une position
@main.route('/delete_position/<int:position_id>')
def delete_position_route(position_id):
    position = Positions.query.get_or_404(position_id)
    fond_id = position.fond_id
    db.session.delete(position)
    db.session.commit()
    return redirect(url_for('main.view_positions', fond_id=fond_id))