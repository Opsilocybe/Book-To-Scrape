-----------------------------------------------------------------------------               READ ME             -------------------------------------------------------------------------
- Présentation du projet

Ceci est la notice d'utilisation pour le fichier "main.py" présent dans le dépôt GitHub: Ce programme servira à la création d'un système de surveillance des prix pour le site BookToScrape.
Le fichier "main" est contenu dans le dossier "Nice_One"
Il sert à recueillir toutes les données des livres du site et les placera dans un fichier .CSV différent pour chaque catégorie de livres et téléchargera les couvertures des livres dans un autre dossier. 




- Installation et configuration

Étape 1 :
Créez votre environnement virtuel à l'aide de la commande : "python -m venv env"
Initiez votre environnement virtuel avec la commande : "env\Scripts\activate"

Étape 2 : 
Vous trouverez ci-joint un fichier "requierment.txt" qui servira à télécharger tous les modules nécessaires pour le fonctionnement du code.
Pour l'installer, ouvrez votre console et écrivez : "pip install -r requirements.txt"

Étape 3 :
Lancez le programme grâce à la commande : " py main.py"




- Utilisation

Une fois le programme lancé, tout se fera automatiquement, trois dossiers seront créés:
- Le dossier "Info-livre" : il va servir à stocker les deux dossiers ci-dessous.
- Le dossier "All_the_csv" : il va regrouper toutes les informations des livres et les trier par catégorie, toutes ces informations seront collectées dans un fichier .CSV différent
- Le dossier "Image-produit": toutes les couvertures de livres téléchargées seront regroupées dans ce dossier. 

Pendant le téléchargement de toutes les données le module TQDM va fournir une barre de progression pour suivre le téléchargement des éléments.



- Contribuer

Le programme peut être amélioré en regroupant les images par catégories de livres dans des dossiers séparés.


- Licence

Fait avec python 3
