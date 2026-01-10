# Projet BBM AGRI - Traitement des Données Commerciales

## Scripts de Nettoyage des Fichiers Excel

Ce projet contient des scripts Python pour nettoyer et traiter les fichiers Excel de données commerciales BBM AGRI.

### Scripts disponibles

#### 1. Nettoyage Clients par Familles
- **`clean_cltfam24.py`** : Nettoie les fichiers CLTFAM*.xlsx (Clients par Familles)
- Génère des fichiers Excel nettoyés : `CLTFAM*_clean.xlsx`

#### 2. Nettoyage Clients par Articles
- **`clean_cltart24.py`** : Nettoie les fichiers CLTART*.xlsx (Clients par Articles)
- Génère des fichiers Excel nettoyés : `CLTART*_clean.xlsx`

#### 3. Nettoyage Statistiques par Famille
- **`clean_statartfam.py`** : Nettoie les fichiers STATARTFAM*.xlsx (Statistiques Articles par Famille)
- Génère des fichiers Excel nettoyés : `STATARTFAM_clean.xlsx`

#### 4. Nettoyage Statistiques par Article
- **`clean_statartart.py`** : Nettoie les fichiers STATARTART*.xlsx (Statistiques Articles)
- Génère des fichiers Excel nettoyés : `STATARTART_clean.xlsx`

### Autres scripts

- **`statcollfam.py`** : Traitement STATCOLL-FAM.xlsx (avec KPI)
- **`statcoll_articles.py`** : Traitement STATCOLL-ART.xlsx (avec KPI)
- **`stat_cltfam.py`** : Analyse simple des fichiers CLTFAM

## Utilisation

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Exécuter un script de nettoyage

```bash
# Clients par Familles
python clean_cltfam24.py CLTFAM24.xlsx
python clean_cltfam24.py CLTFAM25.xlsx

# Clients par Articles
python clean_cltart24.py CLTART24.xlsx
python clean_cltart24.py CLTART25.xlsx

# Statistiques par Famille
python clean_statartfam.py STATARTFAM.xlsx

# Statistiques par Article
python clean_statartart.py STATARTART.xlsx
```

### Scripts STATCOLL

```bash
# Statistiques Collaborateurs/Famille
python statcollfam.py STATCOLL-FAM.xlsx

# Statistiques Collaborateurs/Articles
python statcoll_articles.py STATCOLL-ART.xlsx
```

## Fichiers Excel générés

### Fichiers nettoyés disponibles
- `CLTFAM24_clean.xlsx` - Clients par Familles 2024
- `CLTFAM25_clean.xlsx` - Clients par Familles 2025
- `CLTART24_clean.xlsx` - Clients par Articles 2024
- `CLTART25_clean.xlsx` - Clients par Articles 2025
- `STATARTFAM_clean.xlsx` - Statistiques par Famille
- `STATARTART_clean.xlsx` - Statistiques par Article

### Fichiers STATCOLL générés
- `STATCOLL-FAM_PERIODE_*.xlsx` - Statistiques Collaborateurs/Famille avec KPI
- `STATCOLL-ART_PERIODE_*.xlsx` - Statistiques Collaborateurs/Articles avec KPI

## Dépendances

Les dépendances sont définies dans `requirements.txt` :
- pandas >= 2.0.0
- plotly >= 5.17.0
- openpyxl >= 3.1.0

## Structure des fichiers nettoyés

### CLTFAM*_clean.xlsx
- Commercial
- Code Famille
- Intitulé
- CA HT Net
- % Remise
- Marge
- % Marge/CA

### CLTART*_clean.xlsx
- Client
- Code Article
- Désignation
- CA HT Net
- % Remise
- Marge
- % Marge/CA

### STATARTFAM_clean.xlsx
- Code Famille
- Désignation
- CA Net HT
- Qtés vendues
- Marge
- % Marge/CA

### STATARTART_clean.xlsx
- Code Article
- Désignation
- CA Net HT
- Qtés vendues
- Marge
- % Marge/CA

---

**BBM AGRI** | Traitement des données commerciales
