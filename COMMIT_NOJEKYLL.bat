@echo off
title Ajouter .nojekyll sur GitHub Pages
color 0B

echo ========================================
echo Ajout de .nojekyll pour GitHub Pages
echo ========================================
echo.

REM Changer vers le répertoire du script
cd /d "%~dp0"

echo 1. Verification que .nojekyll existe localement...
echo.

if not exist ".nojekyll" (
    echo [ERREUR] .nojekyll non trouve localement!
    echo Creation du fichier...
    echo. > .nojekyll
    if exist ".nojekyll" (
        echo [OK] Fichier .nojekyll cree
    ) else (
        echo [ERREUR] Impossible de creer .nojekyll
        pause
        exit /b 1
    )
) else (
    echo [OK] .nojekyll existe localement
)

echo.
echo 2. Verification Git...
echo.

git --version >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] Git n'est pas installe!
    echo.
    echo Option alternative: Ajouter .nojekyll via l'interface GitHub:
    echo   1. Aller sur: https://github.com/taliaham/dashboard-bbmagri
    echo   2. Add file ^> Create new file
    echo   3. Nommer: .nojekyll
    echo   4. Laisser vide, commit
    echo.
    pause
    exit /b 0
)

echo [OK] Git est installe
echo.

REM Vérifier si git est initialisé
if not exist ".git" (
    echo [INFO] Depot Git non initialise
    echo        Le fichier .nojekyll est pret a etre uploader via l'interface GitHub
    echo.
    pause
    exit /b 0
)

echo 3. Ajout de .nojekyll a Git...
echo.

git add .nojekyll

if errorlevel 1 (
    echo [ATTENTION] Erreur lors de l'ajout
) else (
    echo [OK] .nojekyll ajoute a Git
)

echo.
echo 4. Commit...
echo.

git commit -m "Add .nojekyll to disable Jekyll for GitHub Pages"

if errorlevel 1 (
    echo [ATTENTION] Pas de changements a commiter
    echo (Le fichier est peut-etre deja commite)
) else (
    echo [OK] Commit cree
)

echo.
echo 5. Configuration du remote...
echo.

git remote -v >nul 2>&1
if errorlevel 1 (
    echo [INFO] Remote non configure
    echo        Configurez le remote manuellement:
    echo        git remote add origin https://github.com/taliaham/dashboard-bbmagri.git
    echo.
    echo        Puis:
    echo        git push origin main
    echo.
    pause
    exit /b 0
)

echo [OK] Remote configure
echo.

echo 6. Push vers GitHub...
echo.

set /p do_push="Voulez-vous push maintenant? (O/N): "

if /i "%do_push%"=="O" (
    git push origin main
    
    if errorlevel 1 (
        echo.
        echo [ATTENTION] Erreur lors du push!
        echo.
        echo Solutions possibles:
        echo   1. Verifier vos credentials GitHub
        echo   2. Ou push manuellement: git push origin main
        echo   3. Ou ajouter via l'interface GitHub (plus simple)
        echo.
    ) else (
        echo.
        echo [OK] .nojekyll a ete pousse sur GitHub!
        echo.
        echo Prochaines etapes:
        echo   1. Attendre 3-5 minutes (deploiement GitHub Pages)
        echo   2. Tester: https://taliaham.github.io/dashboard-bbmagri/
        echo.
    )
) else (
    echo.
    echo [INFO] Push annule
    echo        Vous pouvez push manuellement avec:
    echo        git push origin main
    echo.
    echo        OU ajouter .nojekyll via l'interface GitHub (plus simple)
    echo.
)

echo ========================================
pause
