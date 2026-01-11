# Dépannage 404 GitHub Pages - Dashboard BBM AGRI 🔍

## ❌ Problème : 404 "Site not found"

Vous voyez : `https://taliaham.github.io/dashboard-bbmagri/` → 404

**Cause** : GitHub Pages ne trouve pas `index.html` à l'emplacement configuré.

---

## ✅ Solution Étape par Étape

### Étape 1 : Vérifier la structure dans GitHub

**Aller sur** : `https://github.com/taliaham/dashboard-bbmagri`

**Dans l'onglet "Code"**, vous devez voir :

#### ✅ Structure CORRECTE (obligatoire) :

```
dashboard-bbmagri/
├── index.html          ← ✅ DOIT ÊTRE ICI (à la racine)
├── README.md           (optionnel)
└── .gitignore          (optionnel)
```

#### ❌ Structure INCORRECTE (causes 404) :

```
dashboard-bbmagri/
├── dashboard/
│   └── index.html      ← ❌ MAUVAIS! Pas à la racine
├── README.md
└── autres fichiers
```

**OU**

```
dashboard-bbmagri/
├── docs/
│   └── index.html      ← ❌ MAUVAIS! (sauf si configuré sur /docs)
├── README.md
└── autres fichiers
```

---

### Étape 2 : Corriger si index.html est dans un sous-dossier

**Si `index.html` est dans `dashboard/` ou autre sous-dossier** :

#### Option A : Déplacer vers la racine (RECOMMANDÉ) ⭐

1. **Dans GitHub, ouvrir** `dashboard/index.html` (ou le chemin actuel)
2. **Cliquer sur "Edit"** (icône crayon)
3. **Sélectionner tout** : `Ctrl+A` (Windows) ou `Cmd+A` (Mac)
4. **Copier** : `Ctrl+C` ou `Cmd+C`
5. **Aller à la racine** du dépôt (cliquer sur le nom du dépôt en haut)
6. **Cliquer sur "Add file" → "Create new file"**
7. **Nommer** : `index.html` (exactement comme ça, sans chemin)
8. **Coller le contenu** : `Ctrl+V` ou `Cmd+V`
9. **Scroller en bas** → Message de commit : "Move index.html to root"
10. **Cliquer sur "Commit new file"** (bouton vert)
11. **Supprimer l'ancien** `dashboard/index.html` (cliquer sur le fichier → Delete)

#### Option B : Utiliser le dossier /docs (ALTERNATIVE)

**Si vous préférez garder `index.html` dans un sous-dossier** :

1. **Renommer le dossier** `dashboard/` en `docs/`
2. **Dans Settings → Pages** :
   - Folder : `/docs` (au lieu de `/ (root)`)
   - Save

---

### Étape 3 : Vérifier Settings → Pages

**Aller dans** : `Settings` → `Pages` (menu de gauche)

**Configuration DOIT être** :

- ✅ **Source** : `Deploy from a branch`
- ✅ **Branch** : `main` (ou `master` si vous utilisez master)
- ✅ **Folder** : `/ (root)` ⭐ **IMPORTANT - DOIT ÊTRE ROOT!**
- ✅ **Cliquer sur "Save"** (même si déjà configuré)

**Si Folder est sur `/dashboard` ou autre** :

❌ **PROBLÈME** : C'est pour ça que ça ne fonctionne pas !

✅ **Solution** :
1. Changer en `/ (root)`
2. Cliquer sur "Save"
3. Attendre 1-2 minutes

---

### Étape 4 : Vérifier que index.html est bien uploadé

**Dans l'onglet Code, vérifier** :

1. **`index.html` est visible directement** (première ligne ou visible sans ouvrir de dossier)
2. **Vous pouvez cliquer dessus** et voir le contenu
3. **Le fichier fait environ 4 MB** (contient les données)
4. **Pas de message "File too large"** (GitHub limite à 100 MB)

**Si `index.html` n'apparaît pas** :

❌ **PROBLÈME** : Le fichier n'a pas été uploadé correctement.

✅ **Solution** :
1. Vérifier que vous avez bien commité/pushé
2. Vérifier le `.gitignore` (ne doit pas ignorer `index.html`)
3. Re-uploader le fichier

---

### Étape 5 : Vérifier .gitignore

**Vérifier que `.gitignore` n'ignore pas `index.html`** :

**Dans `.gitignore`, il NE DOIT PAS y avoir** :

```gitignore
index.html        ← ❌ MAUVAIS
*.html            ← ❌ MAUVAIS
dashboard/        ← ❌ MAUVAIS (si index.html est dedans)
```

**Le `.gitignore` DOIT avoir** :

```gitignore
# Exception : garder index.html pour GitHub Pages
!index.html
```

**Si `.gitignore` ignore `index.html`** :

1. Ouvrir `.gitignore`
2. Supprimer la ligne qui ignore `index.html`
3. Ajouter `!index.html` pour forcer l'inclusion
4. Commit et Push

---

### Étape 6 : Régénérer et Re-uploader (si nécessaire)

**Si le problème persiste, régénérer le dashboard** :

1. **Localement** (sur votre machine) :
```bash
python generer_dashboard_html.py
```

2. **Vérifier que `index.html` est à la racine** :
```bash
# Windows PowerShell
Test-Path "index.html"
# Doit retourner : True
```

3. **Re-uploader sur GitHub** :

#### Option A : Interface GitHub (Drag & Drop) ⭐ SIMPLE

1. Aller sur `https://github.com/taliaham/dashboard-bbmagri`
2. Cliquer sur "uploading an existing file"
3. **Supprimer l'ancien `index.html`** (cliquer dessus → Delete)
4. **Glisser-déposer le nouveau `index.html` directement** (pas dans un dossier!)
5. Message : "Re-generate dashboard"
6. Commit

#### Option B : Git (ligne de commande)

```bash
# Vérifier que index.html est bien suivi
git status

# Ajouter index.html
git add index.html

# Commit
git commit -m "Fix: Move index.html to root for GitHub Pages"

# Push
git push origin main
```

#### Option C : Script automatique

```bash
# Double-cliquez sur :
deploy_github.bat
```

---

### Étape 7 : Attendre et Vérifier

**Après avoir corrigé** :

1. **Attendre 1-2 minutes** (temps de déploiement GitHub Pages)
2. **Recharger** : `https://taliaham.github.io/dashboard-bbmagri/`
3. **Vérifier le statut** dans `Settings → Pages` :
   - Status : "Your site is live at..."
   - URL : `https://taliaham.github.io/dashboard-bbmagri/`
   - Dernier déploiement : Date/heure récente

**Si toujours 404** :

1. Vérifier l'onglet "Actions" (s'il y a des erreurs de build)
2. Vérifier l'URL (bon username, bon nom de dépôt)
3. Attendre 5 minutes (parfois plus long)
4. Vider le cache du navigateur (`Ctrl+Shift+R`)

---

## 🔍 Checklist de Vérification

**Dans GitHub (onglet Code)** :

- [ ] `index.html` est **directement visible** (pas dans un sous-dossier)
- [ ] Vous pouvez **cliquer dessus** et voir le contenu HTML
- [ ] Le fichier fait **environ 4 MB** (contient les données)
- [ ] **Pas de dossier `dashboard/` contenant `index.html`** à la racine

**Dans Settings → Pages** :

- [ ] Source : `Deploy from a branch`
- [ ] Branch : `main` (ou `master`)
- [ ] **Folder : `/ (root)`** ⭐ (pas `/dashboard`!)
- [ ] Status : "Your site is live at..."
- [ ] **Bouton "Save" a été cliqué récemment**

**Dans .gitignore** :

- [ ] `index.html` **N'EST PAS ignoré**
- [ ] Il y a `!index.html` (force l'inclusion) si nécessaire

**Test Local** :

- [ ] `index.html` existe à la racine du projet local
- [ ] `python generer_dashboard_html.py` génère bien `index.html`
- [ ] Le fichier s'ouvre dans un navigateur local (test rapide)

---

## 📸 Aide Visuelle

**Structure dans l'onglet Code GitHub (DOIT ressembler à ça)** :

```
📁 dashboard-bbmagri                    ← Nom du dépôt
   📄 index.html                        ← ✅ ICI (à la racine)
   📄 README.md                         (optionnel)
   📄 .gitignore                        (optionnel)
   📁 dashboard/                        (peut exister, mais sans index.html dedans)
      📄 data.json                      (OK si index.html n'est pas dedans)
```

**❌ PAS comme ça** :

```
📁 dashboard-bbmagri
   📄 README.md
   📁 dashboard/
      📄 index.html                     ← ❌ MAUVAIS! Pas à la racine
```

---

## 🚀 Solution Rapide (5 minutes)

**Si vous voulez corriger rapidement** :

1. **Dans GitHub, ouvrir** `dashboard/index.html` (ou le chemin actuel)
2. **Edit → Tout sélectionner → Copier**
3. **Aller à la racine** → `Add file` → `Create new file`
4. **Nommer** : `index.html`
5. **Coller** → Commit
6. **Supprimer** l'ancien fichier dans `dashboard/`
7. **Settings → Pages** → Folder : `/ (root)` → Save
8. **Attendre 2 minutes** → Recharger l'URL

---

## 📞 Besoin d'Aide ?

**Si le problème persiste, vérifier** :

1. **Screenshot de l'onglet Code** : Structure visible?
2. **Screenshot de Settings → Pages** : Configuration visible?
3. **Logs de l'onglet Actions** : Erreurs de build?

**Avec ces infos, on pourra identifier exactement le problème !**

---

**Une fois corrigé, votre dashboard sera accessible sur :**

```
https://taliaham.github.io/dashboard-bbmagri/
```

🚀 **Bon courage !**
