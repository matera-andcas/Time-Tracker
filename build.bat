@echo off
REM Script para criar executável do Time Tracker para Windows

echo ========================================
echo   Time Tracker - Build Executável
echo ========================================
echo.

REM Ativar ambiente virtual
if not exist "venv\" (
    echo ❌ Ambiente virtual não encontrado!
    echo Execute install.bat primeiro
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

REM Instalar PyInstaller se necessário
echo 📦 Verificando PyInstaller...
pip install pyinstaller

REM Limpar builds anteriores
echo 🧹 Limpando builds anteriores...
if exist "build\" rmdir /s /q build
if exist "dist\" rmdir /s /q dist

REM Criar executável usando o .spec
echo 🔨 Compilando aplicação...
pyinstaller TimeTracker.spec

if %errorlevel% equ 0 (
    echo.
    echo ✅ Build concluído com sucesso!
    echo.
    echo 📦 Executável criado em:
    echo    dist\TimeTracker.exe
    echo.
    echo Para distribuir, envie apenas o arquivo:
    echo    dist\TimeTracker.exe
    echo.
    dir /s dist\TimeTracker.exe | find "TimeTracker.exe"
    echo.
) else (
    echo.
    echo ❌ Erro durante o build!
    echo.
    echo Verifique as mensagens de erro acima.
)

pause
