"""
Ce fichier contient la définition des modèles de données.
Ces modèles correspondent aux tables dans la base de données MySQL.
"""

from . import db

class ReferentielFonds(db.Model):
    __tablename__ = 'referentiel_fonds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class ReferentielInstruments(db.Model):
    __tablename__ = 'referentiel_instruments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Positions(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    fond_id = db.Column(db.Integer, db.ForeignKey('referentiel_fonds.id'), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey('referentiel_instruments.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    fond = db.relationship('ReferentielFonds', backref='positions')
    instrument = db.relationship('ReferentielInstruments', backref='positions')
