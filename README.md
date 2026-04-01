# Projet-Transversal

Projet BAC1 — Transversal EPHEC

**Nom du projet :** MasterDaube

## Objectif

Créer un jeu MasterMind en utilisant un Raspberry Pi et quelques composants électroniques.

## Technologies et matériel

### Partie développement
- Python 3 + Flask (framework web)
- HTML5, CSS3, JavaScript

### Partie électronique
- 2 breadboards (1 pour le maître / 1 pour le joueur)
- 2 Raspberry Pi (Raspberry Pi 3.5 et Raspberry Pi 2)
- 2 × 4–5 LED RGB

## Fonctionnalités
- Afficher le nombre de couleurs sélectionnées ou manquantes
- Allumer la LED correspondante sur la breadboard du joueur lorsqu'il devine correctement
- (Optionnel) Indicateur lumineux clignotant pendant le choix de la couleur pour l'effet visuel
- Affichage du score / état de la partie sur un écran OLED ou LCD

## Exemple d'une partie

1. Alice (maître) configure sa séquence de couleurs sur sa breadboard (par ex. rouge, vert, bleu, jaune).
2. Bob (joueur) tente de deviner la séquence, une position à la fois, dans le bon ordre.
3. Lorsqu'une couleur est correctement devinée pour une position donnée :
   - la LED correspondante sur la breadboard de Bob s'allume.
4. Si le joueur trouve toute la séquence : affichage "Vous avez gagné !" et fin de la partie.
5. Sinon, on continue ; on peut afficher combien de couleurs il manque (ex. "Il vous manque 3 couleurs") et fournir des indices.

## Affichage et feedback
- Utiliser un petit écran (OLED/LCD) pour afficher le score, le nombre d'essais, et des messages d'état.
- Ajouter des effets lumineux (clignotement) pour améliorer le ressenti du choix de couleur.

## Lancement
### Branchement
- Cable ETHERNET en direct vers une machine windows.
- connecter le PC hôte a un réseaux éxtérieur a eduroam (4G/5G)
### Lancer le site
- ```env/bin/activate```
- ```sudo flask run --host="ip du raspberry sur le même résaux que le PC hôte" --port="port non utilisé du PC hôte (8000)"
