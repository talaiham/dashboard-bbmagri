# Checklist GitHub Pages - Dashboard BBM AGRI ✅

## ✅ Vérifications Avant Déploiement

### 1. Fichier index.html à la racine ✅

**Vérifier dans l'onglet Code du dépôt GitHub** :

```
dashboard-bbmagri/
├── index.html          ← ✅ DOIT ÊTRE ICI (à la racine)
├── README.md           (optionnel)
└── .gitignore          (optionnel)
```

❌ **INCORRECT** :
```
dashboard-bbmagri/
├── dashboard/
│   └── index.html      ← ❌ MAUVAIS! Pas accessible
└── README.md
```

---

### 2. Générer le dashboard (si pas fait)

```bash
python generer_dashboard_html.py
```

**Vérifier** :
- ✅ `index.html` existe à la racine du projet
- ✅ Taille : ~4 MB (contient les données)
- ✅ Le fichier est visible dans l'Explorateur Windows

---

### 3. Uploader sur GitHub

#### Option A : Script automatique (Recommandé)

```bash
# Double-cliquez sur :
deploy_github.bat
```

#### Option B : Manuel (Git)

```bash
git init
git add index.html README.md .gitignore
git commit -m "Dashboard BBM AGRI"
git remote add origin https://github.com/VOTRE_USERNAME/dashboard-bbmagri.git
git branch -M main
git push -u origin main
```

#### Option C : Interface GitHub (Drag & Drop)

1. Aller sur votre dépôt GitHub
2. Cliquer sur "uploading an existing file"
3. **Glisser-déposer `index.html` directement** (pas dans un sous-dossier)
4. Commit

---

### 4. Vérifier dans GitHub

**Dans l'onglet Code du dépôt** :

- ✅ `index.html` est **directement visible** (pas dans un sous-dossier)
- ✅ Vous pouvez cliquer dessus et voir le contenu
- ✅ Le fichier fait environ 4 MB

**Si `index.html` est dans un sous-dossier** :

❌ **Problème** : GitHub Pages ne le trouvera pas automatiquement.

✅ **Solution** :
1. Cliquer sur le fichier
2. Cliquer sur "Edit" (crayon)
3. Copier tout le contenu
4. Revenir à la racine du dépôt
5. Cliquer sur "Add file" → "Create new file"
6. Nommer le fichier `index.html`
7. Coller le contenu
8. Commit

---

### 5. Activer GitHub Pages

1. **Aller dans Settings** (onglet en haut à droite du dépôt)

2. **Dans le menu de gauche, cliquer sur "Pages"**

3. **Configurer** :
   - **Source** : `Deploy from a branch`
   - **Branch** : `main` (ou `master`)
   - **Folder** : `/ (root)` ⭐ **IMPORTANT - Doit être root!**
   - Cliquer sur **Save**

4. **Attendre 1-2 minutes**

5. **Vérifier** :
   - Vous verrez : "Your site is live at..."
   - URL : `https://VOTRE_USERNAME.github.io/dashboard-bbmagri/`

---

## ✅ Checklist Finale

Avant de dire que c'est déployé, vérifiez :

- [ ] `index.html` est **visible à la racine** dans l'onglet Code
- [ ] `index.html` fait **environ 4 MB**
- [ ] Le dépôt est **Public** (pour Pages gratuit)
- [ ] GitHub Pages est **activé** (Settings → Pages)
- [ ] Source : `Deploy from a branch`
- [ ] Branch : `main`
- [ ] Folder : `/ (root)` ⭐
- [ ] Status : "Your site is live at..."

---

## 🌐 Accéder au Dashboard

Une fois déployé, votre dashboard sera accessible sur :

```
https://VOTRE_USERNAME.github.io/dashboard-bbmagri/
```

**Exemple** :
- Username : `johndoe`
- Repo : `dashboard-bbmagri`
- URL : `https://johndoe.github.io/dashboard-bbmagri/`

---

## 🔄 Mettre à Jour le Dashboard

1. **Régénérer le dashboard** :
```bash
python generer_dashboard_html.py
```

2. **Vérifier que `index.html` est à la racine**

3. **Mettre à jour sur GitHub** :
```bash
git add index.html
git commit -m "Mise à jour dashboard"
git push
```

4. **Attendre 1-2 minutes** : Déploiement automatique !

---

## ⚠️ Problèmes Courants

### ❌ "404 - File not found"

**Cause** : `index.html` n'est pas à la racine

**Solution** :
1. Vérifier dans l'onglet Code
2. `index.html` doit être visible directement (pas dans un sous-dossier)
3. Si nécessaire, déplacer le fichier à la racine

### ❌ Dashboard vide

**Cause** : Les données JSON dans le HTML sont invalides

**Solution** : Régénérer le dashboard :
```bash
python generer_dashboard_html.py
git add index.html
git commit -m "Regeneration dashboard"
git push
```

### ❌ GitHub Pages ne se déploie pas

**Cause** : Configuration incorrecte

**Solution** :
1. Vérifier Settings → Pages
2. Folder doit être `/ (root)` (pas `/dashboard`)
3. Réactiver GitHub Pages

---

## 📝 Commandes Utiles Git

```bash
# Vérifier le statut
git status

# Voir les fichiers à la racine
git ls-files

# Vérifier que index.html est suivi
git ls-files | findstr index.html

# Forcer le push si nécessaire
git push -f origin main
```

---

**Votre dashboard sera accessible sur GitHub Pages une fois `index.html` est à la racine et GitHub Pages activé !** 🚀
