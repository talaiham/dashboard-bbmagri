@echo off
title Verification Structure GitHub Pages - Dashboard BBM AGRI
color 0B

echo ========================================
echo Verification Structure pour GitHub Pages
echo ========================================
echo.

REM Changer vers le répertoire du script
cd /d "%~dp0"

echo 1. Verification de index.html...
echo.

if exist "index.html" (
    echo [OK] index.html existe a la racine
    echo      Taille: ~4 MB (contient toutes les donnees)
    echo      Emplacement: %CD%\index.html
) else (
    echo [ERREUR] index.html NON TROUVE a la racine!
    echo.
    echo Le fichier doit etre a la racine pour GitHub Pages.
    echo Executez: python generer_dashboard_html.py
    echo.
    pause
    exit /b 1
)

echo.
echo 2. Verification des sous-dossiers...
echo.

if exist "dashboard\index.html" (
    echo [ATTENTION] index.html existe aussi dans dashboard/
    echo              Cela peut causer confusion, mais OK si celui a la racine est present
) else (
    echo [OK] Pas de index.html dans dashboard/ (bon)
)

if exist "docs\index.html" (
    echo [ATTENTION] index.html existe dans docs/
    echo              Si vous utilisez /docs dans GitHub Pages Settings, c'est OK
) else (
    echo [OK] Pas de index.html dans docs/
)

echo.
echo 3. Verification .gitignore...
echo.

if exist ".gitignore" (
    echo [OK] .gitignore existe
    findstr /C:"index.html" ".gitignore" >nul 2>&1
    if errorlevel 1 (
        echo [OK] index.html n'est PAS ignore dans .gitignore
    ) else (
        echo [ATTENTION] index.html pourrait etre ignore dans .gitignore
        echo              Vérifiez que !index.html est present pour forcer l'inclusion
    )
) else (
    echo [INFO] .gitignore n'existe pas (OK, optionnel)
)

echo.
echo 4. Verification Git...
echo.

git --version >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] Git n'est pas installe
    echo              Vous pouvez quand meme uploader index.html manuellement sur GitHub
    echo.
    goto :check_complete
)

echo [OK] Git est installe

if exist ".git" (
    echo [OK] Depot Git initialise
    
    echo.
    echo 5. Verification Git status...
    echo.
    git status index.html >nul 2>&1
    if errorlevel 1 (
        echo [ATTENTION] index.html n'est peut-etre pas suivi par Git
        echo              Executez: git add index.html
    ) else (
        echo [OK] index.html est suivi par Git
    )
    
    echo.
    echo 6. Liste des fichiers a la racine (suivis par Git)...
    echo.
    git ls-files | findstr /V "/" | findstr /V "^\." | findstr /I "index.html"
    if errorlevel 1 (
        echo [ATTENTION] index.html n'apparait pas dans les fichiers suivis
        echo              Executez: git add index.html
    ) else (
        echo [OK] index.html est dans les fichiers suivis a la racine
    )
) else (
    echo [INFO] Depot Git non initialise
    echo        Executez: git init
)

:check_complete
echo.
echo ========================================
echo VERIFICATION TERMINEE
echo ========================================
echo.
echo Checklist pour GitHub Pages:
echo.
if exist "index.html" (
    echo [OK] index.html existe a la racine
) else (
    echo [ ] index.html existe a la racine
)
echo [ ] index.html est visible dans l'onglet Code de GitHub (a la racine)
echo [ ] Settings ^> Pages ^> Folder est configure sur: / (root)
echo [ ] Settings ^> Pages ^> Save a ete clique
echo [ ] Attendu 1-2 minutes apres modification
echo.
echo Prochaines etapes:
echo.
echo 1. Si index.html n'existe pas a la racine, executez:
echo    python generer_dashboard_html.py
echo.
echo 2. Uploader index.html sur GitHub (a la racine du depot):
echo    - Via interface GitHub (drag ^& drop)
echo    - Via Git: git add index.html ^&^& git commit ^&^& git push
echo    - Via script: deploy_github.bat
echo.
echo 3. Verifier dans GitHub (onglet Code):
echo    - index.html doit etre DIRECTEMENT visible (pas dans un sous-dossier)
echo.
echo 4. Verifier Settings ^> Pages:
echo    - Folder: / (root) (pas /dashboard!)
echo    - Save
echo.
echo 5. Attendre 1-2 minutes et tester:
echo    https://taliaham.github.io/dashboard-bbmagri/
echo.
echo ========================================
pause
