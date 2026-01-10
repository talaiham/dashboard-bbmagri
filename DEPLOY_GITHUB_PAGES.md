# Déploiement sur GitHub Pages - Guide Complet 🚀

## ✅ Prérequis

- Un compte GitHub (gratuit)
- Le fichier `index.html` à la racine du dépôt

## 📋 Étapes de déploiement

### 1. Générer le dashboard (si pas déjà fait)

```bash
python generer_dashboard_html.py
```

Le fichier `index.html` sera créé **à la racine** du projet (nécessaire pour GitHub Pages).

---

### 2. Créer un dépôt GitHub

1. **Aller sur [github.com](https://github.com)**
2. **Cliquer sur "New repository"**
3. **Configurer** :
   - Repository name : `dashboard-bbmagri` (ou autre nom)
   - Description : "Dashboard Commercial BBM AGRI"
   - Public (recommandé pour Pages gratuit)
   - **Ne pas** cocher "Initialize with README" (on a déjà les fichiers)
4. **Créer le dépôt**

---

### 3. Uploader les fichiers sur GitHub

#### Méthode A : Via GitHub Desktop (Simple)

1. Installer [GitHub Desktop](https://desktop.github.com/)
2. Cloner le dépôt créé
3. Copier `index.html` dans le dossier cloné
4. Commit et Push

#### Méthode B : Via ligne de commande (Git)

```bash
# Initialiser git (si pas déjà fait)
git init

# Ajouter les fichiers nécessaires
git add index.html
git add README.md
git add .gitignore

# Commit
git commit -m "Dashboard BBM AGRI - Initial commit"

# Ajouter le remote (remplacer USERNAME et REPO)
git remote add origin https://github.com/USERNAME/dashboard-bbmagri.git

# Renommer la branche en main (si nécessaire)
git branch -M main

# Push vers GitHub
git push -u origin main
```

#### Méthode C : Via interface GitHub (Drag & Drop)

1. Aller sur votre dépôt GitHub
2. Cliquer sur "uploading an existing file"
3. Glisser-déposer `index.html` directement
4. Commit directement sur GitHub

**⚠️ Important** : Le fichier `index.html` doit être **directement visible** dans l'onglet Code (pas dans un sous-dossier).

---

### 4. Activer GitHub Pages

1. **Aller dans votre dépôt GitHub**
2. **Cliquer sur "Settings"** (onglet en haut à droite)
3. **Dans le menu de gauche, cliquer sur "Pages"**
4. **Configurer** :
   - Source : `Deploy from a branch`
   - Branch : `main` (ou `master`)
   - Folder : `/ (root)` ⭐ **IMPORTANT**
   - Save
5. **Attendre 1-2 minutes** pour le déploiement

---

### 5. Accéder au dashboard

Après activation, votre dashboard sera accessible sur :

```
https://VOTRE_USERNAME.github.io/dashboard-bbmagri/
```

Exemple : Si votre username est `johndoe` et le dépôt `dashboard-bbmagri` :
```
https://johndoe.github.io/dashboard-bbmagri/
```

---

## ✅ Vérification

### Vérifier que tout est correct

1. **Dans l'onglet Code du dépôt** :
   - ✅ `index.html` est visible à la racine (pas dans un sous-dossier)
   - ✅ Le fichier fait environ 4 MB

2. **Dans Settings → Pages** :
   - ✅ Source : `Deploy from a branch`
   - ✅ Branch : `main`
   - ✅ Folder : `/ (root)`
   - ✅ Status : "Your site is live at..."

3. **Tester le dashboard** :
   - ✅ Aller sur l'URL générée
   - ✅ Le dashboard se charge
   - ✅ Les graphiques s'affichent

---

## 🔄 Mettre à jour le dashboard

### Quand vous avez de nouveaux fichiers Excel

1. **Régénérer le dashboard** :
```bash
python generer_dashboard_html.py
```

2. **Mettre à jour sur GitHub** :

```bash
# Méthode A : Ligne de commande
git add index.html
git commit -m "Mise à jour du dashboard"
git push

# Méthode B : GitHub Desktop
# Commit et Push depuis l'interface

# Méthode C : Interface GitHub
# Uploader le nouveau index.html
```

3. **Attendre 1-2 minutes** : GitHub Pages redéploie automatiquement !

---

## 📁 Structure du dépôt GitHub

### Structure correcte (pour GitHub Pages) ✅

```
dashboard-bbmagri/
├── index.html          ← À LA RACINE (IMPORTANT!)
├── README.md           (optionnel)
├── .gitignore          (optionnel)
└── dashboard/
    └── data.json       (optionnel, pour référence)
```

### Structure incorrecte ❌

```
dashboard-bbmagri/
├── dashboard/
│   └── index.html      ← MAUVAIS! Pas accessible directement
└── README.md
```

**Solution** : Déplacer `index.html` à la racine !

---

## 🎯 Script automatique pour GitHub

Créez un fichier `deploy_github.bat` :

```batch
@echo off
echo Generation du dashboard...
python generer_dashboard_html.py

echo.
echo Verification que index.html est a la racine...
if exist "index.html" (
    echo [OK] index.html existe a la racine
) else (
    echo [ERREUR] index.html non trouve a la racine!
    pause
    exit /b 1
)

echo.
echo Ajout des fichiers a git...
git add index.html README.md .gitignore

echo.
echo Commit...
git commit -m "Dashboard BBM AGRI - Update"

echo.
echo Push vers GitHub...
git push

echo.
echo [OK] Dashboard deploye sur GitHub!
echo Attendez 1-2 minutes, puis allez sur:
echo https://VOTRE_USERNAME.github.io/dashboard-bbmagri/
pause
```

---

## 🌐 Domaine personnalisé (Optionnel)

Si vous avez votre propre domaine :

1. **Dans Settings → Pages** :
   - Ajouter votre domaine dans "Custom domain"
   - Configurer DNS : `CNAME` pointant vers `VOTRE_USERNAME.github.io`

---

## 📊 Vérifier le statut du déploiement

### Dans Settings → Pages

Vous verrez :
- ✅ Status : "Your site is live at..."
- ✅ URL : `https://VOTRE_USERNAME.github.io/dashboard-bbmagri/`
- ✅ Dernier déploiement : Date et heure

### Dans l'onglet Actions (optionnel)

Si GitHub Actions est activé, vous pouvez voir l'historique des déploiements.

---

## 🔧 Personnaliser l'URL

### URL par défaut
```
https://USERNAME.github.io/REPOSITORY-NAME/
```

### Changer le nom du dépôt
1. Settings → General → Repository name
2. Renommer le dépôt
3. L'URL changera automatiquement

---

## 📱 Partager le dashboard

Une fois déployé, vous pouvez partager le lien :
- Par email
- Sur un site web
- Via QR code
- Dans des rapports

Le dashboard est accessible 24/7 sur Internet ! 🌐

---

## ⚠️ Problèmes courants

### ❌ "404 - File not found"

**Causes** :
1. `index.html` n'est pas à la racine
2. GitHub Pages n'est pas activé
3. Le déploiement n'est pas terminé (attendre 2-3 minutes)

**Solutions** :
1. Vérifier que `index.html` est visible dans l'onglet Code à la racine
2. Réactiver GitHub Pages dans Settings
3. Attendre quelques minutes et réessayer

### ❌ Les graphiques ne s'affichent pas

**Cause** : Plotly.js non chargé (problème de connexion Internet)

**Solution** : Vérifier votre connexion Internet

### ❌ Dashboard vide ou erreur

**Cause** : Le fichier JSON dans le HTML est invalide

**Solution** : Régénérer le dashboard :
```bash
python generer_dashboard_html.py
git add index.html
git commit -m "Regeneration dashboard"
git push
```

---

## 🎯 Checklist finale

Avant de déployer, vérifiez :

- [ ] `index.html` est à la racine du dépôt (visible dans l'onglet Code)
- [ ] Le fichier fait environ 4 MB (contient les données)
- [ ] GitHub Pages est activé (Settings → Pages)
- [ ] Branch : `main`
- [ ] Folder : `/ (root)`
- [ ] Le dépôt est Public (pour Pages gratuit)

---

**Votre dashboard sera accessible 24/7 sur GitHub Pages ! 🚀**

Pour plus d'aide, consultez : [GitHub Pages Documentation](https://docs.github.com/en/pages)
