# Guide de Déploiement - Projet BBM AGRI 🚀

Après suppression de Streamlit, voici comment déployer vos scripts et données.

## Option 1 : Dashboard HTML Statique (RECOMMANDÉ - Plus Simple) ⭐

### Avantages
- ✅ Aucun serveur backend nécessaire
- ✅ Fonctionne directement dans le navigateur
- ✅ Déploiement gratuit et facile
- ✅ Rapide et léger

### Déploiement Local
```bash
# Option A : Python serveur simple
python -m http.server 8000
# Accès : http://localhost:8000

# Option B : Node.js (si installé)
npx http-server -p 8000
# Accès : http://localhost:8000
```

### Déploiement Web Gratuit

#### GitHub Pages
1. Créer un dépôt GitHub
2. Uploader les fichiers HTML dans un dossier `docs/` ou racine
3. Activer GitHub Pages dans Settings → Pages
4. Accès : `https://VOTRE_USERNAME.github.io/nom-depot`

#### Netlify (Drag & Drop)
1. Aller sur [netlify.com](https://netlify.com)
2. Glisser-déposer le dossier dashboard
3. URL automatique générée

#### Vercel
1. Aller sur [vercel.com](https://vercel.com)
2. Connecter le dépôt GitHub
3. Déploiement automatique

---

## Option 2 : Flask (Dashboard Web Python)

### Installation
```bash
pip install Flask Flask-CORS
```

### Fichiers nécessaires
- `app.py` - Application Flask principale
- `templates/` - Fichiers HTML
- `static/` - CSS, JavaScript, images
- `requirements.txt` - Avec Flask ajouté

### Déploiement Local
```bash
python app.py
# Accès : http://localhost:5000
```

### Déploiement Production

#### Heroku
1. Créer `Procfile` : `web: gunicorn app:app`
2. `pip install gunicorn`
3. `heroku create bbmagri-dashboard`
4. `git push heroku main`

#### Railway/Render
1. Connecter le dépôt GitHub
2. Détection automatique de Flask
3. Déploiement automatique

#### VPS avec Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Option 3 : Application Desktop (PyQt/Tkinter)

### Avantages
- ✅ Application native Windows
- ✅ Pas besoin de serveur web
- ✅ Accès direct aux fichiers Excel

### Compiler en exécutable (.exe)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed app.py
# Génère : dist/app.exe
```

---

## Option 4 : Dash (Alternative à Streamlit)

### Installation
```bash
pip install dash
```

### Similaire à Streamlit mais plus flexible

---

## Option 5 : Partager les fichiers Excel uniquement

### Solution la plus simple
1. Utiliser les fichiers Excel nettoyés directement
2. Les partager via :
   - OneDrive / Google Drive
   - SharePoint
   - Email
   - Réseau local

Les fichiers Excel contiennent déjà :
- Données nettoyées
- Formatage professionnel
- Graphiques possibles (à ajouter dans Excel)

---

## Recommandation

### Pour un déploiement rapide et simple
→ **Option 1 : Dashboard HTML Statique**

### Pour un dashboard interactif avec backend
→ **Option 2 : Flask**

### Pour une application desktop
→ **Option 3 : Application Desktop**

### Pour continuer avec Excel uniquement
→ **Option 5 : Partager les fichiers Excel**

---

## Prochaines étapes

Quelle option préférez-vous ? Je peux créer les fichiers nécessaires pour l'option choisie :
- Dashboard HTML statique complet
- Application Flask avec API
- Application Desktop
- Scripts de compilation

---

**Je recommande l'Option 1 (HTML Statique) pour commencer rapidement !** 🚀
