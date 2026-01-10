# Déploiement Dashboard HTML Statique - Guide Rapide

Le dashboard HTML statique est la solution la plus simple - pas de serveur nécessaire !

## Avantages

- ✅ Aucun serveur backend nécessaire
- ✅ Fonctionne directement dans le navigateur
- ✅ Déploiement gratuit (GitHub Pages, Netlify, etc.)
- ✅ Rapide et léger
- ✅ Fonctionne hors ligne (après chargement initial)

## Structure

```
dashboard/
├── index.html          # Page principale
├── css/
│   └── style.css       # Styles
├── js/
│   ├── main.js         # Logique principale
│   └── charts.js       # Graphiques
├── data/
│   └── *.xlsx          # Fichiers Excel (optionnel)
└── lib/
    └── (bibliothèques JS)
```

## Déploiement

### Option 1 : GitHub Pages (Gratuit) ⭐

1. **Créer un dépôt GitHub**
2. **Uploader les fichiers HTML**
3. **Activer GitHub Pages dans les paramètres**
4. **Accès** : `https://VOTRE_USERNAME.github.io/nom-depot`

### Option 2 : Netlify (Gratuit) ⭐

1. **Aller sur [netlify.com](https://netlify.com)**
2. **Drag & Drop le dossier dashboard**
3. **C'est tout !** URL automatique générée

### Option 3 : Vercel (Gratuit) ⭐

1. **Aller sur [vercel.com](https://vercel.com)**
2. **Connecter votre dépôt GitHub**
3. **Déploiement automatique**

### Option 4 : Serveur Web Simple

```bash
# Avec Python (serveur simple)
cd dashboard
python -m http.server 8000

# Avec Node.js
npx http-server dashboard -p 8000

# Accès : http://localhost:8000
```

### Option 5 : Partage Local (Réseau)

```bash
# Python
python -m http.server 8000 --bind 0.0.0.0

# Accès depuis réseau : http://VOTRE_IP:8000
```

## Hébergement Gratuit Recommandé

| Service | Gratuit | Facilité | Domaine Personnalisé |
|---------|---------|----------|---------------------|
| **GitHub Pages** | ✅ | ⭐⭐ | ✅ |
| **Netlify** | ✅ | ⭐⭐⭐ | ✅ |
| **Vercel** | ✅ | ⭐⭐⭐ | ✅ |
| **Firebase Hosting** | ✅ | ⭐⭐ | ✅ |

## Avantages de l'HTML Statique

- Pas besoin de Python sur le serveur
- Rapide (pas de traitement serveur)
- Fonctionne partout
- Facile à maintenir

---

**Je peux créer un dashboard HTML statique complet pour vous !** 🎨
