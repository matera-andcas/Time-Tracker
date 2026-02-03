@echo off
REM Script de instalação do Time Tracker para Windows

echo ===================================
echo   Time Tracker - Instalação
echo ===================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado!
    echo.
    echo Por favor, instale o Python 3.8+ de:
    echo   https://www.python.org/downloads/
    echo.
    echo ⚠️  IMPORTANTE: Marque a opção "Add Python to PATH" durante a instalação
    pause
    exit /b 1
)

echo ✅ Python detectado:
python --version
echo.

REM Criar ambiente virtual se não existir
if not exist "venv\" (
    echo 📦 Criando ambiente virtual...
    python -m venv venv
    
    if %errorlevel% neq 0 (
        echo ❌ Erro ao criar ambiente virtual!
        echo.
        echo Tente reinstalar o Python com a opção "Add Python to PATH"
        pause
        exit /b 1
    )
    echo ✅ Ambiente virtual criado!
    echo.
) else (
    echo ✅ Ambiente virtual já existe.
    echo.
)

REM Ativar ambiente virtual
echo 📦 Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Atualizar pip
echo 📦 Atualizando pip...
python -m pip install --upgrade pip

REM Instalar dependências
echo 📦 Instalando dependências...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ✅ Instalação concluída com sucesso!
    echo.
    echo Para executar o Time Tracker:
    echo   run.bat
    echo.
    echo Para criar o executável:
    echo   build.bat
    echo.
) else (
    echo.
    echo ❌ Erro ao instalar dependências!
    echo.
    echo Verifique sua conexão com a internet e tente novamente.
)

pause
