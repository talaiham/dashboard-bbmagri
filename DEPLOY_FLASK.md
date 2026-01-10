# Déploiement avec Flask - Guide Complet

Flask est un framework web Python simple et puissant pour créer des dashboards.

## Installation

### 1. Mettre à jour requirements.txt

```bash
# Ajouter Flask aux dépendances
echo Flask>=3.0.0 >> requirements.txt
echo Flask-CORS>=4.0.0 >> requirements.txt
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Déploiement Local

### Lancer le serveur Flask

```bash
python app.py
```

Le dashboard sera accessible sur : **http://localhost:5000**

## Déploiement Production

### Option A : VPS avec Gunicorn

```bash
# Installer Gunicorn
pip install gunicorn

# Lancer avec Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option B : Heroku/Railway/Render

#### Heroku
1. Créer un `Procfile` :
```
web: gunicorn app:app
```

2. Déployer :
```bash
heroku create bbmagri-dashboard
git push heroku main
```

#### Railway
1. Connecter votre dépôt GitHub
2. Railway détecte automatiquement Flask
3. Déploiement automatique

#### Render
1. Créer un nouveau service Web
2. Connecter le dépôt
3. Build command : `pip install -r requirements.txt`
4. Start command : `gunicorn app:app`

### Option C : Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## Configuration Nginx (Reverse Proxy)

```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## SSL avec Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d votre-domaine.com
```
