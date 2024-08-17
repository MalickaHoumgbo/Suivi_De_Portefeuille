"""
Ce fichier contient les routes  de l'application. 
Les routes sont des URL spécifiques qui mènent à des fonctions définies dans ce fichier,
appelées vues. Chaque vue traite une requête HTTP et retourne une réponse, souvent sous la forme 
d'une page HTML rendue à l'aide d'un template
"""
from flask import render_template
from . import db
from .models import ReferentielFonds, ReferentielInstruments, Positions

@app.route('/fonds')
def view_fonds():
    fonds = ReferentielFonds.query.all()
    return render_template('fonds.html', fonds=fonds)

@app.route('/instruments')
def view_instruments():
    instruments = ReferentielInstruments.query.all()
    return render_template('static/templates/instruments.html', instruments=instruments)

@app.route('/positions/<int:fond_id>')
def view_positions(fond_id):
    positions = Positions.query.filter_by(fond_id=fond_id).all()
    return render_template('static/templates/positions.html', positions=positions)
