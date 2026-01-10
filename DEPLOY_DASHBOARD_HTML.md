# Déploiement Dashboard HTML - Guide Complet 🚀

## ✅ Dashboard généré avec succès !

Le dashboard HTML statique a été généré dans le dossier `dashboard/`.

### Fichiers générés :
- ✅ `dashboard/index.html` - Dashboard principal
- ✅ `dashboard/data.json` - Données en JSON (19,859 lignes)

---

## 🚀 Déploiement Local (3 méthodes)

### Méthode 1 : Ouvrir directement (Le plus simple) ⭐

1. **Ouvrir l'Explorateur Windows**
2. **Naviguer vers le dossier `dashboard`**
3. **Double-cliquer sur `index.html`**
4. **Le dashboard s'ouvre dans votre navigateur**

✅ **Pas besoin de serveur !**

---

### Méthode 2 : Serveur Python simple

```bash
# Depuis le dossier du projet
python -m http.server 8000
```

Puis ouvrir dans le navigateur : **http://localhost:8000/dashboard/index.html**

Ou depuis le dossier dashboard :
```bash
cd dashboard
python -m http.server 8000
```

Puis : **http://localhost:8000**

---

### Méthode 3 : Serveur Node.js (si installé)

```bash
# Installer http-server globalement (une seule fois)
npm install -g http-server

# Lancer depuis le dossier dashboard
cd dashboard
http-server -p 8000
```

Accès : **http://localhost:8000**

---

## 🌐 Déploiement Web Gratuit (3 options)

### Option 1 : GitHub Pages (GRATUIT) ⭐ RECOMMANDÉ

1. **Créer un dépôt GitHub** (ex: `bbmagri-dashboard`)

2. **Uploader le dossier dashboard** :
```bash
# Initialiser git
git init

# Ajouter les fichiers
git add dashboard/

# Commit
git commit -m "Dashboard BBM AGRI"

# Ajouter remote (remplacer USERNAME et REPO)
git remote add origin https://github.com/USERNAME/bbmagri-dashboard.git
git branch -M main
git push -u origin main
```

3. **Activer GitHub Pages** :
   - Aller dans Settings → Pages
   - Source : `main` branch
   - Folder : `/dashboard` (ou `/root` si vous avez mis index.html à la racine)
   - Save

4. **Accéder au dashboard** :
   - URL : `https://USERNAME.github.io/bbmagri-dashboard/`
   - Génération automatique en 1-2 minutes

✅ **HTTPS automatique et gratuit !**

---

### Option 2 : Netlify (GRATUIT - Le plus rapide) ⭐

1. **Aller sur [netlify.com](https://netlify.com)**

2. **Méthode Drag & Drop** :
   - Glisser-déposer le dossier `dashboard`
   - URL automatique générée (ex: `https://random-name-123.netlify.app`)

3. **Méthode Git** :
   - Connecter votre dépôt GitHub
   - Build command : (vide)
   - Publish directory : `dashboard`
   - Deploy

✅ **Déploiement instantané !**

---

### Option 3 : Vercel (GRATUIT)

1. **Aller sur [vercel.com](https://vercel.com)**

2. **Connecter le dépôt GitHub**

3. **Configuration** :
   - Framework Preset : Other
   - Root Directory : `dashboard`
   - Build Command : (vide)
   - Output Directory : `.`

4. **Deploy**

✅ **Déploiement automatique à chaque push !**

---

## 📱 Accès depuis le réseau local

Pour accéder depuis d'autres appareils sur le même Wi-Fi :

```bash
# Trouver votre IP locale
ipconfig
# Cherchez "Adresse IPv4" (ex: 192.168.1.100)

# Lancer le serveur avec accès réseau
python -m http.server 8000 --bind 0.0.0.0

# Accéder depuis un autre appareil
http://192.168.1.100:8000/dashboard
```

⚠️ **Note** : Autorisez le port 8000 dans Windows Firewall si nécessaire.

---

## 🔄 Mettre à jour le dashboard

Quand vous avez de nouveaux fichiers Excel nettoyés :

1. **Régénérer le dashboard** :
```bash
python generer_dashboard_html.py
```

2. **Redéployer** :
   - **Local** : Recharger la page dans le navigateur (F5)
   - **GitHub Pages** : `git push` (déploiement automatique)
   - **Netlify** : Glisser-déposer le nouveau dossier ou `git push`
   - **Vercel** : `git push` (déploiement automatique)

---

## 📊 Fonctionnalités du dashboard

### KPI Cards (En haut)
- 💰 CA Total HT
- 📈 Marge Totale
- 👥 Nombre de Commerciaux
- 📦 Nombre d'Articles

### Filtres
- Année
- Commercial
- Famille

### Onglets
1. **Vue d'ensemble** :
   - Graphique CA par année (barres)
   - Répartition CA par famille (camembert)

2. **Par Commercial** :
   - Top 10 commerciaux par CA
   - Tableau récapitulatif

3. **Par Famille** :
   - Graphique CA par famille
   - Tableau détaillé

4. **Par Article** :
   - Top 20 articles par CA
   - Tableau Top 50

---

## 🎨 Personnalisation

Vous pouvez modifier le dashboard en éditant :
- `dashboard/index.html` - Structure et style CSS
- `generer_dashboard_html.py` - Génération du HTML

---

## 🐛 Résolution de problèmes

### ❌ Le dashboard ne charge pas
**Solution** : Utilisez un serveur local (Méthode 2 ou 3) au lieu d'ouvrir directement le fichier

### ❌ Les graphiques ne s'affichent pas
**Solution** : Vérifiez votre connexion Internet (Plotly.js est chargé depuis CDN)

### ❌ Données manquantes
**Solution** : Régénérez le dashboard avec `python generer_dashboard_html.py`

---

## 📦 Structure du dossier dashboard

```
dashboard/
├── index.html          # Dashboard principal (tout-en-un)
└── data.json          # Données en JSON (optionnel, pour référence)
```

**Note** : `index.html` contient toutes les données intégrées, donc il fonctionne même sans `data.json`.

---

## 🚀 Déploiement Rapide (30 secondes)

### Local immédiat
```bash
# Double-cliquer sur :
dashboard/index.html
```

### Web gratuit (GitHub Pages)
1. Uploader `dashboard/` sur GitHub
2. Activer Pages dans Settings
3. C'est tout !

---

**Votre dashboard HTML est prêt à être utilisé ! 🎉**
