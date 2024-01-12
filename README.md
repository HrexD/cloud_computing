# Gestionnaire d'inventaire
Un système de gestion d'inventaire utilisant Flask

### Prérequis

Pour exécuter ce système, vous aurez besoin de :

- Python 3
- Flask
- SQLALCHEMY
- WTForms

En supposant que vous ayez Python, procédez à l'installation du reste en utilisant la commande suivante :

°°°bash
pip3 install -r requirements.txt
°°°

# Construit avec
- Flask
- SQLAlchemy

# Licence

Ce projet est sous licence MIT - consultez le fichier [LICENSE.md](LICENSE.md) pour plus de détails

# Point de terminaison

- /Overview <=> /
- /Product
- /Location
- /Transferts
- /delete
- /product_search

## GET

    - /Overview => Affiche un produit, la quantité ainsi que la localisation
    - /Product => Affiche tous les produits renseignés
    - /Location => Affiche tous les emplacements renseignés

## POST

    - /Product => Bouton "post" qui va ajouter un produit
    - /Location => Bouton "post" qui va ajouter un emplacement
    - /Transferts => Bouton "déplacer le produit" qui va ajouter un transfert

## MISE À JOUR

    - /Product => Bouton "éditer" qui met à jour un produit
    - /Location => Bouton "éditer" qui met à jour un emplacement

## SUPPRIMER

    - /Product => Bouton "supprimer" qui supprime un produit
    - /Location => Bouton "supprimer" qui supprime un emplacement

## Recherche de produit

    - /product_search => Bouton "rechercher" qui recherche un produit
     
