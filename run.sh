#!/bin/bash
# Script para executar o Time Tracker

cd "$(dirname "$0")"

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo ""
    echo "Execute primeiro:"
    echo "  ./install.sh"
    echo ""
    exit 1
fi

# Ativar ambiente virtual e executar
echo "🚀 Iniciando Time Tracker..."
source venv/bin/activate
python3 main.py
