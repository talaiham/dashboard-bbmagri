# Déploiement Rapide - Dashboard HTML 🚀

## ✅ Dashboard HTML Généré !

Le dashboard HTML statique est prêt à être utilisé.

**Fichier généré** : `dashboard/index.html` (4.2 MB - contient toutes les données)

---

## 🚀 Déploiement en 3 étapes

### Option 1 : Local - Le Plus Simple ⭐

```bash
# Double-cliquez simplement sur :
dashboard/index.html
```

Le dashboard s'ouvre directement dans votre navigateur !

⚠️ **Note** : Si les graphiques ne s'affichent pas, utilisez l'Option 2 (serveur local).

---

### Option 2 : Local avec Serveur (Recommandé)

**Script automatique** :
```bash
# Double-cliquez sur :
lancer_dashboard_html.bat
```

**Ou commande manuelle** :
```bash
cd dashboard
python -m http.server 8000
```

Puis allez sur : **http://localhost:8000**

---

### Option 3 : Déploiement Web Gratuit

#### GitHub Pages (Gratuit - Recommandé)

1. **Créer un dépôt GitHub**
2. **Uploader le dossier `dashboard`** :
```bash
git init
git add dashboard/
git commit -m "Dashboard BBM AGRI"
git remote add origin https://github.com/VOTRE_USERNAME/bbmagri-dashboard.git
git push -u origin main
```

3. **Activer GitHub Pages** :
   - Settings → Pages
   - Source : `main` branch
   - Folder : `/dashboard`
   - Save

4. **Accès** : `https://VOTRE_USERNAME.github.io/bbmagri-dashboard/`

#### Netlify (Gratuit - Le plus rapide)

1. Aller sur [netlify.com](https://netlify.com)
2. Glisser-déposer le dossier `dashboard`
3. URL automatique générée (30 secondes)

---

## 📊 Mettre à jour le dashboard

Quand vous avez de nouveaux fichiers Excel :

```bash
# Régénérer le dashboard
python generer_dashboard_html.py

# Redéployer
# - Local : Recharger la page (F5)
# - GitHub/Netlify : git push ou drag & drop
```

---

## 🎯 Résumé des fichiers

- ✅ `generer_dashboard_html.py` - Script de génération
- ✅ `dashboard/index.html` - Dashboard complet (tout-en-un)
- ✅ `dashboard/data.json` - Données en JSON (pour référence)
- ✅ `lancer_dashboard_html.bat` - Script de lancement Windows

---

## 📱 Utilisation

1. **Ouvrir le dashboard** : Double-cliquez sur `dashboard/index.html`
2. **Utiliser les filtres** : Sélectionnez Année, Commercial, Famille
3. **Naviguer entre les onglets** : Vue d'ensemble, Par Commercial, Par Famille, Par Article
4. **Explorer les graphiques** : Zoom, survol, export possible

---

## 🌐 Déploiement Web en 5 minutes

### GitHub Pages
1. Uploader `dashboard/` sur GitHub
2. Activer Pages
3. C'est tout !

### Netlify
1. Drag & drop `dashboard/`
2. URL générée automatiquement

---

**Le dashboard est prêt à être utilisé !** 🎉

Pour plus de détails, consultez : `DEPLOY_DASHBOARD_HTML.md`
