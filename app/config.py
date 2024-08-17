"""
Ce fichier définit l'URI de la base de données MySQL (l'adresse et les 
informations de connexion à la base de données).
"""
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/portfolio_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
