#!/bin/bash
# Script para criar executável do Time Tracker

echo "========================================"
echo "  Time Tracker - Build Executável"
echo "========================================"
echo ""

# Ativar ambiente virtual
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "Execute ./install.sh primeiro"
    exit 1
fi

source venv/bin/activate

# Instalar PyInstaller se necessário
echo "📦 Verificando PyInstaller..."
pip install pyinstaller

# Limpar builds anteriores
echo "🧹 Limpando builds anteriores..."
rm -rf build/ dist/ *.spec

# Criar executável
echo "🔨 Compilando aplicação..."
pyinstaller --onefile \
    --windowed \
    --name="TimeTracker" \
    --add-data="timetracker.db:." \
    --hidden-import="PyQt6.QtCore" \
    --hidden-import="PyQt6.QtGui" \
    --hidden-import="PyQt6.QtWidgets" \
    main.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build concluído com sucesso!"
    echo ""
    echo "📦 Executável criado em:"
    echo "   dist/TimeTracker"
    echo ""
    echo "Para distribuir, envie apenas o arquivo:"
    echo "   dist/TimeTracker"
    echo ""
    echo "Tamanho do executável:"
    ls -lh dist/TimeTracker | awk '{print "   " $5}'
    echo ""
else
    echo ""
    echo "❌ Erro no build!"
    exit 1
fi
