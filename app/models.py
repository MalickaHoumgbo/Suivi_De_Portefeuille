"""
Ce fichier contient la définition des modèles de données.
Ces modèles correspondent aux tables dans la base de données MySQL.
"""

from . import db

class ReferentielFonds(db.Model):
    __tablename__ = 'referentiel_fonds'
    id = db.Column(db.Integer, primary_key=True)
    nom_fond = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class ReferentielInstruments(db.Model):
    __tablename__ = 'referentiel_instruments'
    id = db.Column(db.Integer, primary_key=True)
    nom_instrument = db.Column(db.String(100), nullable=False)
    type_instrument = db.Column(db.String(50))
    description = db.Column(db.Text)

class Positions(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    fond_id = db.Column(db.Integer, db.ForeignKey('referentiel_fonds.id'), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey('referentiel_instruments.id'), nullable=False)
    quantite = db.Column(db.Numeric(10, 2), nullable=False)
    prix_achat = db.Column(db.Numeric(10, 2), nullable=False)
    date_achat = db.Column(db.Date, nullable=False)
    fond = db.relationship('ReferentielFonds', backref='positions')
    instrument = db.relationship('ReferentielInstruments', backref='positions')