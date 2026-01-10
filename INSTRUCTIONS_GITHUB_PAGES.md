# Instructions GitHub Pages - Dashboard BBM AGRI 📋

## ✅ IMPORTANT : Structure Requise

Pour que GitHub Pages fonctionne, **`index.html` DOIT être à la racine du dépôt**, pas dans un sous-dossier.

### ✅ Structure Correcte

```
dashboard-bbmagri/
├── index.html          ← ✅ À LA RACINE (OBLIGATOIRE!)
├── README.md
└── .gitignore
```

### ❌ Structure Incorrecte

```
dashboard-bbmagri/
├── dashboard/
│   └── index.html      ← ❌ MAUVAIS! GitHub Pages ne le trouvera pas
└── README.md
```

---

## 🚀 Déploiement en 5 Étapes

### Étape 1 : Générer le dashboard (si pas déjà fait)

```bash
python generer_dashboard_html.py
```

**Vérifier** : Le fichier `index.html` existe à la racine du projet.

---

### Étape 2 : Créer un dépôt GitHub

1. Aller sur [github.com](https://github.com)
2. Cliquer sur "New repository" (+ en haut à droite)
3. Nommer : `dashboard-bbmagri` (ou autre nom)
4. Description : "Dashboard Commercial BBM AGRI"
5. Public (recommandé pour Pages gratuit)
6. **Ne pas** initialiser avec README
7. Créer le dépôt

---

### Étape 3 : Uploader index.html sur GitHub

#### Option A : Script automatique ⭐ RECOMMANDÉ

```bash
# Double-cliquez sur :
deploy_github.bat
```

Le script :
- Génère le dashboard
- Vérifie que `index.html` est à la racine
- Configure Git
- Push vers GitHub

#### Option B : Interface GitHub (Drag & Drop) ⭐ SIMPLE

1. Aller sur votre dépôt GitHub (vide)
2. Cliquer sur "uploading an existing file"
3. **Glisser-déposer `index.html` directement** (pas dans un sous-dossier!)
4. Message de commit : "Dashboard BBM AGRI"
5. Cliquer sur "Commit changes"

**⚠️ IMPORTANT** : Le fichier `index.html` doit être **directement visible** dans l'onglet Code après upload.

#### Option C : Git en ligne de commande

```bash
# Si Git est installé
git init
git add index.html README.md .gitignore
git commit -m "Dashboard BBM AGRI"
git remote add origin https://github.com/VOTRE_USERNAME/dashboard-bbmagri.git
git branch -M main
git push -u origin main
```

---

### Étape 4 : Vérifier dans GitHub

**Aller dans l'onglet "Code" du dépôt** :

- ✅ **`index.html` est visible directement** (pas dans un sous-dossier)
- ✅ Vous pouvez cliquer dessus et voir le contenu
- ✅ Le fichier fait environ 4 MB

**Si `index.html` est dans un sous-dossier** :

❌ **PROBLÈME** : Il faut le déplacer à la racine !

**Solution** :
1. Dans GitHub, cliquer sur le fichier
2. Cliquer sur "Edit" (icône crayon)
3. Copier tout le contenu (Ctrl+A, Ctrl+C)
4. Aller à la racine du dépôt
5. Cliquer sur "Add file" → "Create new file"
6. Nommer : `index.html`
7. Coller le contenu (Ctrl+V)
8. Commit : "Move index.html to root"
9. Supprimer l'ancien fichier dans le sous-dossier

---

### Étape 5 : Activer GitHub Pages

1. **Aller dans Settings** (onglet en haut à droite)

2. **Dans le menu de gauche, cliquer sur "Pages"**

3. **Configurer** :
   - **Source** : `Deploy from a branch`
   - **Branch** : `main` (ou `master` si vous utilisez master)
   - **Folder** : `/ (root)` ⭐ **IMPORTANT - DOIT ÊTRE ROOT!**
   - Cliquer sur **Save**

4. **Attendre 1-2 minutes**

5. **Vérifier** :
   - Vous verrez : "Your site is live at..."
   - URL : `https://VOTRE_USERNAME.github.io/dashboard-bbmagri/`

---

## ✅ Vérification Finale

### Checklist dans GitHub :

Dans l'onglet **Code** :
- [ ] `index.html` est **directement visible** (première ligne)
- [ ] **Pas** dans un sous-dossier comme `dashboard/index.html`
- [ ] Le fichier fait environ 4 MB

Dans **Settings → Pages** :
- [ ] Source : `Deploy from a branch`
- [ ] Branch : `main`
- [ ] **Folder : `/ (root)`** ⭐
- [ ] Status : "Your site is live at..."

---

## 🌐 Accéder au Dashboard

Votre dashboard sera accessible sur :

```
https://VOTRE_USERNAME.github.io/dashboard-bbmagri/
```

**Exemple** :
- Username : `johndoe`
- Repo : `dashboard-bbmagri`
- URL : `https://johndoe.github.io/dashboard-bbmagri/`

---

## 🔄 Mettre à Jour le Dashboard

1. **Régénérer** :
```bash
python generer_dashboard_html.py
```

2. **Vérifier** : `index.html` est toujours à la racine

3. **Mettre à jour sur GitHub** :
```bash
# Option A : Script
deploy_github.bat

# Option B : Git
git add index.html
git commit -m "Mise à jour dashboard"
git push

# Option C : Interface GitHub
# Uploader le nouveau index.html
```

4. **Attendre 1-2 minutes** : Déploiement automatique !

---

## ⚠️ Problèmes Courants

### ❌ "404 - File not found"

**Causes** :
1. `index.html` n'est pas à la racine
2. GitHub Pages pas activé
3. Folder configuré sur `/dashboard` au lieu de `/ (root)`

**Solutions** :
1. Vérifier dans l'onglet Code : `index.html` doit être à la racine
2. Réactiver GitHub Pages
3. **Folder : `/ (root)`** (pas `/dashboard`)

### ❌ Dashboard vide ou erreur

**Cause** : Fichier HTML corrompu ou données invalides

**Solution** : Régénérer le dashboard :
```bash
python generer_dashboard_html.py
```

---

## 📝 Récapitulatif Rapide

**Pour GitHub Pages, `index.html` DOIT être à la racine du dépôt !**

1. ✅ Générer : `python generer_dashboard_html.py`
2. ✅ Vérifier : `index.html` à la racine
3. ✅ Uploader : Sur GitHub (racine du dépôt)
4. ✅ Activer : Settings → Pages → Folder : `/ (root)`
5. ✅ Accéder : `https://USERNAME.github.io/dashboard-bbmagri/`

---

**Votre dashboard sera en ligne sur GitHub Pages ! 🚀**
