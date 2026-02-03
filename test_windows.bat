@echo off
REM Script de teste rápido para verificar compatibilidade Windows

echo ========================================
echo   Time Tracker - Teste de Compatibilidade
echo ========================================
echo.

echo [1/5] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ FALHA: Python não encontrado
    echo    Instale Python 3.8+ de: https://www.python.org/downloads/
    goto :end
) else (
    echo ✅ Python encontrado
)

echo.
echo [2/5] Verificando ambiente virtual...
if not exist "venv\" (
    echo ❌ FALHA: Ambiente virtual não existe
    echo    Execute: install.bat
    goto :end
) else (
    echo ✅ Ambiente virtual OK
)

echo.
echo [3/5] Verificando PyQt6...
call venv\Scripts\activate.bat
python -c "import PyQt6" 2>nul
if %errorlevel% neq 0 (
    echo ❌ FALHA: PyQt6 não instalado
    echo    Execute: install.bat
    goto :end
) else (
    echo ✅ PyQt6 instalado
)

echo.
echo [4/5] Verificando estrutura de pastas...
if not exist "src\domain\models.py" (
    echo ❌ FALHA: Estrutura de pastas incorreta
    goto :end
) else (
    echo ✅ Estrutura OK
)

echo.
echo [5/5] Testando importações...
python -c "from src.application import TimeTrackerController; print('OK')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ FALHA: Erro ao importar módulos
    goto :end
) else (
    echo ✅ Importações OK
)

echo.
echo ========================================
echo   ✅ Todos os testes passaram!
echo ========================================
echo.
echo O aplicativo está pronto para uso.
echo.
echo Próximos passos:
echo   - Executar: run.bat
echo   - Criar executável: build.bat
echo.

:end
pause
