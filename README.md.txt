Description du parcours utilisateur:

L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
Affichage de sa description, un magasin où l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.

Sélectionner un substitut[Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
Affichage de sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.

L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.


L'utilisateur sélectionne le 2. Le programme affiche les relations produit/substitut déjà enregistrées.
L'utilisateur a la possibilité de revenir au menu principal.



Technologies utilisées:

Tableau Trello pour définir et organiser les étapes du projet.
API Openfoodfacts pour collecter les données.
Mysql et Mysqlconnector pour initialiser et communiquer avec la base de donnée.




Installation et Utilisation:

```
pip install -r requirements.txt
python3 main.py
```
