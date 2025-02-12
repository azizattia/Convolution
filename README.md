# TP1 - Traitement d'Images

Ce projet contient deux exercices de traitement d'images en Python, utilisant des techniques de convolution et de reconnaissance de code-barres.

## Exercice 1 : Convolution

L'image utilisée pour cet exercice est `tp1_ex1.tif`. L'objectif est d'appliquer différents filtres de convolution sur l'image et d'analyser leurs effets.

### Implémentation

- **Fonction `convolution(image, noyau, padding='zero')`** :
  - Applique la convolution d'une image en niveaux de gris avec un noyau donné.
  - Prend en charge deux types de padding : `zero` (remplissage par zéros) et `mirror` (remplissage miroir).
  - Retourne l'image convoluée.

- **Filtres utilisés** :
  - **Filtre moyenneur (5x5)** : Effet de flou uniforme.
  - **Filtre gaussien (5x5)** : Flou plus doux avec une pondération gaussienne.
  - **Filtre Sobel horizontal (3x3)** : Détection des contours horizontaux.

### Résultats

- Les images filtrées sont enregistrées sous :
  - `convoluted_moyenneur.png`
  - `convoluted_gaussian.png`
  - `convoluted_sobel.png`

- Une visualisation est également générée avec `matplotlib`.

## Exercice 2 : Code-barres mystère

L'image utilisée est `tp1_ex2.png`. L'objectif est d'extraire et de décoder un code-barres Codabar présent dans l'image.

### Implémentation

- **Fonction `process_simple_barcode(chemin_image)`** :
  - Charge l'image et extrait une ligne médiane.
  - Identifie les barres fines et larges pour convertir les motifs en séquences binaires.
  - Décode le code-barres en utilisant un dictionnaire de correspondance Codabar.
  - Affiche le code décodé dans la console.

### Résultat attendu

- Le programme affiche le code Codabar extrait sous forme d'ISBN ou autre format équivalent.

## Installation et Exécution

1. Installer les dépendances :
   ```bash
   pip install numpy imageio matplotlib
   ```
2. Exécuter le script principal :
   ```bash
   python main.py
   ```

## Technologies utilisées

- **Python**
- **Bibliothèques** : `numpy`, `imageio`, `matplotlib`

## Structure du projet
```
TP1/
│── tp1_ex1.tif             # Image pour l'exercice de convolution
│── tp1_ex2.png             # Image du code-barres
│── main.py                 # Script principal
│── README.md               # Documentation
│── results/                # Dossier pour enregistrer les images traitées
```

## Auteur
Développé par Mohamed Aziz Attia dans le cadre du TP1 de traitement d'images.

---
Licence MIT - Vous êtes libre d'utiliser, modifier et partager ce projet.

