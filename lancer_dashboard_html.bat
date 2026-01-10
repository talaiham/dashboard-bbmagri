@echo off
title Dashboard BBM AGRI - HTML
color 0A

echo ========================================
echo Dashboard Commercial BBM AGRI
echo Version HTML Statique
echo ========================================
echo.

REM Changer vers le répertoire du script
cd /d "%~dp0"

REM Vérifier si le dashboard existe
if not exist "dashboard\index.html" (
    echo [ERREUR] Le dashboard HTML n'existe pas encore!
    echo.
    echo Generation du dashboard...
    python generer_dashboard_html.py
    if errorlevel 1 (
        echo [ERREUR] Echec de la generation du dashboard!
        pause
        exit /b 1
    )
    echo.
)

echo Options de lancement:
echo.
echo 1. Ouvrir directement dans le navigateur (Plus simple)
echo 2. Lancer avec serveur Python local (Recommandé)
echo 3. Acces depuis le reseau local
echo.
set /p choix="Votre choix (1-3): "

if "%choix%"=="1" goto ouvert_direct
if "%choix%"=="2" goto serveur_local
if "%choix%"=="3" goto reseau_local

:ouvert_direct
echo.
echo Ouverture du dashboard dans le navigateur...
start "" "dashboard\index.html"
echo.
echo Dashboard ouvert dans le navigateur!
echo Si les graphiques ne s'affichent pas, utilisez l'option 2 (serveur local).
pause
goto end

:serveur_local
echo.
echo Lancement du serveur Python local...
echo.
echo Le dashboard sera accessible sur:
echo   http://localhost:8000/dashboard/
echo.
echo Pour arreter, appuyez sur Ctrl+C
echo.
cd dashboard
python -m http.server 8000
goto end

:reseau_local
echo.
echo Recuperation de votre adresse IP locale...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"Adresse IPv4"') do (
    set "ip=%%a"
    set "ip=!ip: =!"
    goto :found_ip
)

:found_ip
echo.
echo Votre adresse IP locale: %ip%
echo.
echo Le dashboard sera accessible sur:
echo   - Cet ordinateur: http://localhost:8000/dashboard/
echo   - Autres appareils: http://%ip%:8000/dashboard/
echo.
echo ATTENTION: Cela rend le dashboard accessible a tous sur le meme reseau Wi-Fi.
echo.
set /p confirmer="Continuer? (O/N): "
if /i not "%confirmer%"=="O" (
    echo Annule.
    pause
    exit /b 0
)

echo.
echo Lancement du serveur avec acces reseau...
echo Pour arreter, appuyez sur Ctrl+C
echo.
cd dashboard
python -m http.server 8000 --bind 0.0.0.0

:end
pause
