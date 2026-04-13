@echo off
title Generador de Landings
color 0A

:: Ir al directorio del archivo
cd /d "%~dp0"

:: Verificar que .env existe y tiene la clave de Gemini
findstr /C:"GEMINI_API_KEY=" .env >nul 2>&1
if %errorlevel% neq 0 (
    echo  [!] No se encontro el archivo .env con tus claves.
    echo  [!] Ejecuta INSTALAR.bat primero.
    pause
    exit
)

:: Verificar si ya hay una instancia corriendo en el puerto 8502
netstat -an | findstr ":8502" >nul 2>&1
if %errorlevel% equ 0 (
    echo  [OK] La app ya esta corriendo. Abriendo navegador...
    start "" "http://localhost:8502"
    exit
)

echo.
echo  Iniciando Generador de Landings...
echo  El navegador se abrira automaticamente en unos segundos.
echo.
echo  Para cerrar la herramienta, cierra esta ventana.
echo.

:: Abrir el navegador despues de 4 segundos en paralelo
start /b cmd /c "timeout /t 4 /nobreak >nul && start "" http://localhost:8502"

:: Lanzar Streamlit
python -m streamlit run app.py --browser.gatherUsageStats false --server.headless true
