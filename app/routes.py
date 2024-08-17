"""
Ce fichier contient les routes  de l'application. 
Les routes sont des URL spécifiques qui mènent à des fonctions définies dans ce fichier,
appelées vues. Chaque vue traite une requête HTTP et retourne une réponse, souvent sous la forme 
d'une page HTML rendue à l'aide d'un template
"""
from flask import Blueprint, render_template
from . import db
from .models import ReferentielFonds, ReferentielInstruments, Positions

# Créer un blueprint
main = Blueprint('main', __name__)

"""
Un Blueprint est une fonctionnalité de Flask qui permet de structurer et organiser une application en modules 
ou composants réutilisables et indépendants
"""

@main.route('/')
def home():
    return "Bienvenue sur la page d'accueil !"


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
    return render_template('/positions.html', positions=positions)
