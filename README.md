# Game of Life - MANIVANNAN - TD1-2

## Description du projet
Le Jeu de la Vie est un automate cellulaire inventé par le mathématicien John Horton Conway. Ce projet implémente le Jeu de la Vie en Python, en mode console. Les règles sont simples :
- Les cellules vivantes sont représentées par `#`.
- Les cellules mortes sont représentées par un espace (` `).

Le programme affiche les évolutions successives de la grille selon les règles du Jeu de la Vie.

## Fonctionnalités principales
- Simulation du Jeu de la Vie avec une grille modifiable.
- Possibilité de personnaliser les dimensions et le motif initial.
- Mise à jour automatique des générations avec un intervalle de temps configurable.

## Prérequis
- Python 3.x doit être installé sur votre machine.

## Instructions pour exécuter le projet

### 1. Cloner le dépôt
Clonez ce répertoire sur votre machine locale en utilisant la commande suivante :
```bash
git clone <lien-du-dépôt>
```

### 2. Accéder au répertoire
Naviguez dans le répertoire du projet :
```bash
cd nom-du-repo
```

### 3. Exécuter le script principal
Lancez le programme en exécutant :
```bash
python main.py
```

### 4. Personnalisation
Vous pouvez personnaliser le programme :
- **Dimensions de la grille** : Modifiez les valeurs par défaut des lignes et colonnes dans le script.
- **Motifs initiaux** : Ajoutez ou modifiez les motifs de départ (par exemple, planeur, oscillateurs) en éditant la section correspondante dans `main.py`.

Une fois ces modifications effectuées, relancez le programme pour observer les résultats.

## Contribution

### Processus de contribution
1. **Forkez le dépôt** : Créez une copie de ce projet dans votre espace GitHub.
2. **Clonez votre fork** : Clonez-le localement :
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-repo.git
   ```
3. **Créez une branche** : Travaillez sur une nouvelle fonctionnalité ou correction de bug dans une branche séparée :
   ```bash
   git checkout -b nom-de-la-branche
   ```
4. **Effectuez vos modifications** : Ajoutez ou améliorez les fonctionnalités dans votre branche.
5. **Testez votre code** : Assurez-vous que le programme fonctionne correctement avec vos modifications.
6. **Créez un commit** : Enregistrez vos modifications localement avec un message clair :
   ```bash
   git add .
   git commit -m "[Description claire de vos modifications]"
   ```
7. **Poussez vos modifications** : Envoyez-les vers votre fork sur GitHub :
   ```bash
   git push origin nom-de-la-branche
   ```
8. **Soumettez une Pull Request (PR)** : Sur la page GitHub du projet original, créez une Pull Request en décrivant clairement vos modifications.

### Règles pour contribuer
- Documentez clairement les nouvelles fonctionnalités ajoutées.
- Suivez les conventions de codage existantes (écriture propre et lisible).
- Ajoutez des commentaires au besoin pour expliquer les parties complexes du code.
- Testez rigoureusement votre code avant de soumettre une PR.

### Suggestions de contribution
- Ajouter une interface graphique (par exemple, avec Tkinter).
- Inclure des motifs prédéfinis (planeurs, oscillateurs, etc.).
- Ajouter des tests unitaires pour valider les fonctions principales.
- Optimiser la gestion des grandes grilles pour améliorer les performances.

---
Nous apprécions vos contributions pour améliorer ce projet. Merci de participer ! 😊

