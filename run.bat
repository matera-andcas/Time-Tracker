@echo off
REM Script para executar o Time Tracker no Windows

cd /d "%~dp0"

REM Verificar se o ambiente virtual existe
if not exist "venv\" (
    echo ❌ Ambiente virtual não encontrado!
    echo.
    echo Execute primeiro:
    echo   install.bat
    echo.
    pause
    exit /b 1
)

REM Ativar ambiente virtual e executar
echo 🚀 Iniciando Time Tracker...
call venv\Scripts\activate.bat
python main.py
