@echo off
title Instalando Generador de Landings...
color 0A
echo.
echo  ============================================
echo   GENERADOR DE LANDINGS - INSTALACION
echo  ============================================
echo.

:: Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [!] Python no esta instalado.
    echo  [!] Abriendo descarga automatica...
    start https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    echo.
    echo  Instala Python y vuelve a ejecutar este archivo.
    echo  IMPORTANTE: Marca "Add Python to PATH" durante la instalacion.
    pause
    exit
)

echo  [OK] Python detectado.
echo.
echo  Instalando dependencias (puede tardar unos minutos)...
echo.

python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt --quiet

if %errorlevel% neq 0 (
    echo.
    echo  [ERROR] Hubo un problema instalando dependencias.
    echo  Intenta correr este archivo como Administrador.
    pause
    exit
)

echo.
echo  [OK] Dependencias instaladas correctamente.
echo.

:: Crear archivo .env si no existe
if not exist .env (
    echo  Creando archivo de configuracion...
    (
        echo GEMINI_API_KEY=
        echo SHOPIFY_STORE=
        echo SHOPIFY_CLIENT_ID=
        echo SHOPIFY_CLIENT_SECRET=
    ) > .env
    echo  [OK] Archivo .env creado. Abriendolo para que ingreses tus claves...
    start notepad .env
    echo.
    echo  Ingresa tus claves API en el archivo que se abrio,
    echo  guarda los cambios y cierra el Bloc de notas.
    pause
)

:: Crear acceso directo en el escritorio
echo  Creando acceso directo en el escritorio...
set SCRIPT_DIR=%~dp0
set SHORTCUT=%USERPROFILE%\Desktop\Generador de Landings.bat

(
    echo @echo off
    echo cd /d "%SCRIPT_DIR%"
    echo start "" "http://localhost:8502"
    echo python -m streamlit run app.py --browser.gatherUsageStats false --server.headless true
) > "%SHORTCUT%"

echo  [OK] Acceso directo creado en el escritorio.
echo.
echo  ============================================
echo   INSTALACION COMPLETADA
echo   Usa el archivo "Generador de Landings.bat"
echo   en tu escritorio para abrir la herramienta.
echo  ============================================
echo.
pause
