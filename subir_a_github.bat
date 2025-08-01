@echo off
REM Inicializa el repositorio si no está inicializado
IF NOT EXIST ".git" (
    git init
)

REM Agrega todos los archivos nuevos y cambios
git add .

REM Hace commit de los cambios
git commit -m "Primer commit: subida inicial del proyecto"

REM Agrega el repositorio remoto (solo si aún no está)
git remote remove origin 2>nul
git remote add origin https://github.com/jcarranza71/App-Crear-Imagen-ICO.git

REM Sube al repositorio remoto
git branch -M main
git push -u origin main

pause
