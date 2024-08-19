# Suivi_De_Portefeuille

**Description du projet** : Application web pour la gestion du portefeuille d'une entreprise

## Table des Matières

1. [Introduction](#introduction)
2. [Fonctionnalités](#fonctionnalités)
3. [Prérequis](#prérequis)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Lancement](#lancement)
7. [Structure du Projet](#structure-du-projet)
9. [Contribuer](#contribuer)


## Introduction

C'est une application web qui permet de voir la liste des fonds, la liste des instruments et les positions d'un fond.


## Fonctionnalités

- Gestion des fonds et instruments financiers
- Ajout, mise à jour, et suppression des positions

les technologies utilisées sont: 
- Python et Flask
- HTML, Boostrap et CSS
- JavaScript et Jquery
- MySQL

## Prérequis

- Python 3.x
- MySQL: les identifiants de connexion sont:
  *nom d'utilisateur*: root
  *mot de passe*: root
- Environnement virtuel venv


## Installation

1. Clonez le dépôt :
   Ouvrer un Terminal et taper la commande:
   `git clone https://github.com/votre-utilisateur/votre-projet.git`

2. Accédez au répertoire du projet :
   `cd votre-projet`

3. Créez et activez un environnement virtuel:
   Dans le terminal de votre éditeur de code, à la racine du projet, entrer les commandes suivantes:
    - `python -m venv venv`
    - `source venv/bin/activate`  (Pour Linux/MacOS)
    -`venv\Scripts\activate`  (Pour Windows)
   
5. Installez les dépendances dans l'environnement virtuel :
   `pip install -r requirements.txt`

## Configuration
le fichier `*config.py*` sert à la configuration de l'application

## Utilisation

1. Pour lancer l'application, ouvrer votre terminal dans votre éditeur de code,et lancer ces deux commandes:
   - `python app/init_db.py` : pour initialiser la base de données
   - `python run.py` pour démarrer l'application
2. Accédez à l'application à http://127.0.0.1:5000.

## Structure du Projet
`app`: Ce dossier contient le code principal de ton application Flask. 
  - templates: Ce dossier contient les fichiers HTML de ton application. 
  - static: Ce dossier contient les fichiers statiques, comme les feuilles de styles (CSS), les fichiers JavaScript, et éventuellement les images.
  -  __init__.py: Ce fichier est utilisé pour initialiser ton application Flask
  -  models.py : Ce fichier contient la définition des modèles de données. 
  -  routes.py: Ce fichier contient les routes (ou endpoints) de ton application. 
  -  init_db.py: fichier pour automatiser la base de données
  -  update_db.py: Maintenir à jour les differentes opérations entre les tables
     
`venv`: Ce dossier contient l'environnement virtuel Python de ton proje
`requirements.txt`: Ce fichier liste les bibliothèques Python dont ton application dépend
`run.py`: C'est le point d'entrée de ton application

## Contribuer

1. Forker le dépôt
2. Créer une branche (git checkout -b nouvelle-fonctionnalite)
3. Commiter vos modifications (git commit -am 'Ajoute une nouvelle fonctionnalité')
4. Pousser (git push origin nouvelle-fonctionnalite)
5. Créer une Pull Request
