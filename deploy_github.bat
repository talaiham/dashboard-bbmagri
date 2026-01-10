@echo off
title Deploiement GitHub Pages - Dashboard BBM AGRI
color 0B

echo ========================================
echo Deploiement Dashboard sur GitHub Pages
echo ========================================
echo.

REM Changer vers le répertoire du script
cd /d "%~dp0"

echo 1. Generation du dashboard...
echo.
python generer_dashboard_html.py

if errorlevel 1 (
    echo [ERREUR] Echec de la generation du dashboard!
    pause
    exit /b 1
)

echo.
echo 2. Verification que index.html est a la racine...
if not exist "index.html" (
    echo [ERREUR] index.html non trouve a la racine!
    echo Le fichier doit etre a la racine pour GitHub Pages.
    echo.
    echo Generation du fichier...
    python generer_dashboard_html.py
    if errorlevel 1 (
        echo [ERREUR] Echec de la generation!
        pause
        exit /b 1
    )
)

if exist "index.html" (
    echo [OK] index.html existe a la racine
    echo      Taille: ~4 MB (contient toutes les donnees)
) else (
    echo [ERREUR] index.html toujours introuvable a la racine!
    pause
    exit /b 1
)
echo.

echo 3. Verification Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] Git n'est pas installe!
    echo Installez Git depuis: https://git-scm.com/downloads
    echo.
    echo Vous pouvez quand meme uploader index.html manuellement:
    echo   1. Allez sur votre depot GitHub
    echo   2. Cliquez sur "uploading an existing file"
    echo   3. Glissez-deposez index.html
    echo   4. Activez GitHub Pages dans Settings
    pause
    exit /b 0
)

echo [OK] Git est installe
echo.

REM Vérifier si git est initialisé
if not exist ".git" (
    echo Initialisation du depot Git...
    git init
    echo [OK] Depot Git initialise
    echo.
)

echo.
echo 4. Ajout des fichiers a Git...
git add index.html

REM Ajouter README et .gitignore s'ils existent
if exist "README.md" git add README.md
if exist ".gitignore" git add .gitignore

echo [OK] Fichiers ajoutes
echo.

echo 5. Commit...
git commit -m "Dashboard BBM AGRI - Deploy on GitHub Pages" >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] Pas de changements a commiter
    echo (Le dashboard est deja a jour)
) else (
    echo [OK] Commit cree
)

echo.
echo 6. Configuration du remote...
echo.
echo Avez-vous deja configure le remote GitHub?
set /p has_remote="(O/N): "

if /i "%has_remote%"=="N" (
    echo.
    set /p github_user="Entrez votre nom d'utilisateur GitHub: "
    set /p repo_name="Entrez le nom du depot (ex: dashboard-bbmagri): "
    
    git remote add origin https://github.com/%github_user%/%repo_name%.git
    
    if errorlevel 1 (
        echo [ATTENTION] Le remote existe deja ou erreur
    ) else (
        echo [OK] Remote configure: https://github.com/%github_user%/%repo_name%.git
    )
    
    echo.
    echo Renommer la branche en main...
    git branch -M main
) else (
    echo Remote deja configure
)

echo.
echo 7. Push vers GitHub...
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo [ATTENTION] Erreur lors du push!
    echo.
    echo Solutions possibles:
    echo   1. Vérifier vos credentials GitHub
    echo   2. Configurer Git:
    echo      git config --global user.name "Votre Nom"
    echo      git config --global user.email "votre@email.com"
    echo   3. Ou utiliser GitHub Desktop (plus simple)
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo [OK] DASHBOARD DEPLOYE SUR GITHUB!
echo ========================================
echo.
echo Prochaines etapes:
echo.
echo 1. Allez sur votre depot GitHub:
echo    https://github.com/VOTRE_USERNAME/dashboard-bbmagri
echo.
echo 2. Verifiez que index.html est visible a la racine
echo    (Dans l'onglet Code, index.html doit etre directement visible)
echo.
echo 3. Activez GitHub Pages:
echo    - Settings ^> Pages
echo    - Source: Deploy from a branch
echo    - Branch: main
echo    - Folder: / (root)
echo    - Save
echo.
echo 4. Attendez 1-2 minutes pour le deploiement
echo.
echo 5. Accedez au dashboard:
echo    https://VOTRE_USERNAME.github.io/dashboard-bbmagri/
echo.
echo ========================================
pause
