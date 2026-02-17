# Projet-Transversal
Projet BAC1 Transversal EPHEC

Nom du projet :  MasterDaube

but du projet : 
Le but est de à partir d'un raspberry pi et de quelques composants électronique,
de faire un MasterMind.

Technologies utilisée et Matériel utilisée :

Partie dev : 
  - Flask (python3) (framework web)
  - HTML5 CSS3, JavaScript

Partie electro :
  - 2 breadboards (1 pour le master et 1 pour le joueur)
  - 2 raspberry pi (1 raspberry pi 3.5 et 1 raspberry pi 2)
  - 2X 4-5 LED RGB

Fonctionnalité : 

- Affichage du nombre de couleurs séléctionner ou manquante 

Exemple d'une partie :

Joueur 1 -> Alice (Master) à sa breadboard avec toutes les LED allumer qui l'a choisit
Joueur B -> Bob (joueur) à sa breaboard avec toutes les LED non allumer tant qu'il n'a pas trouver une couleur.
Alice choisit pour chaques boules une couleur (ex. rouge,vert,bleu,jaune)
Bob devine DANS L'ORDRE chaque couleur pour chaque boule.

Si le joueur devine une couleur :
- sur sa breadboard la LED correspondante à la couleur choisit s'allume.
- (petit plus si on a le temps) -> pendant que le joueur choisit une couleur une petit lumière clignote.
  pour l'effet du CHOIX.

Via un écran OLED ou LCD affichage du score du joueur :

- si le joueur à tout trouver -> affichage Youpi vous avez gagné :) (fin de la partie)
- sinon tant que le joueur n'a pas trouver :
	- lui afficher combien de couleur il lui manque (ex. il vous manque 3 couleurs) 
        - lui donnée par exemple des petits indices .... (surplus si on a le temps)


choses à rajouter ....
