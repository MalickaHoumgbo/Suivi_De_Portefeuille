"""
Ce fichier contient la définition des modèles de données.
Ces modèles correspondent aux tables dans la base de données MySQL.
"""

from . import db

class ReferentielFonds(db.Model):
    __tablename__ = 'referentiel_fonds'
    id = db.Column(db.Integer, primary_key=True)
    nom_fond = db.Column(db.String(100), nullable=False)
    type_fond = db.Column(db.String(50))
    nom_gestionnaire = db.Column(db.String(100))
    objectif_fond = db.Column(db.Text)
    date_creation = db.Column(db.Date)
    aum = db.Column(db.Numeric(15, 2))
    valeur_liquidative = db.Column(db.Numeric(15, 2))
    devise_fond = db.Column(db.String(10))
    code_isin = db.Column(db.String(12), unique=True)

    # Relation avec Positions
    # positions = db.relationship('Positions', backref='fond', lazy=True)

class ReferentielInstruments(db.Model):
    __tablename__ = 'referentiel_instruments'
    id = db.Column(db.Integer, primary_key=True)
    nom_instrument = db.Column(db.String(100), nullable=False)
    type_instrument = db.Column(db.String(50))
    secteur = db.Column(db.String(50))
    code_isin = db.Column(db.String(12), unique=True)
    devise = db.Column(db.String(10))
    prix_actuel = db.Column(db.Numeric(15, 2))
    volatilite = db.Column(db.Numeric(5, 2))

    # Relation avec Positions
    # positions = db.relationship('Positions', backref='instrument', lazy=True)

class Positions(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    fond_id = db.Column(db.Integer, db.ForeignKey('referentiel_fonds.id'), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey('referentiel_instruments.id'), nullable=False)
    quantite = db.Column(db.Numeric(10, 2), nullable=False)
    prix_achat = db.Column(db.Numeric(10, 2), nullable=False)
    date_achat = db.Column(db.Date, nullable=False)
    prix_actuel = db.Column(db.Numeric(15, 2))
    valeur_totale = db.Column(db.Numeric(15, 2))
    rendement = db.Column(db.Numeric(5, 2))
    date_derniere_transaction = db.Column(db.Date)

    # Relation avec ReferentielFonds et ReferentielInstruments
    fond = db.relationship('ReferentielFonds', backref='fond_positions', lazy=True)
    instrument = db.relationship('ReferentielInstruments', backref='instrument_positions', lazy=True)
