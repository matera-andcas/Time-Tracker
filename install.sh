#!/bin/bash
# Script de instalação do Time Tracker

echo "==================================="
echo "  Time Tracker - Instalação"
echo "==================================="
echo ""

# Verificar se python3-venv está instalado
if ! python3 -m venv --help &> /dev/null; then
    echo "⚠️  python3-venv não encontrado!"
    echo ""
    echo "Instalando python3-venv..."
    sudo apt install -y python3-venv python3-full
    echo ""
fi

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
    
    if [ $? -ne 0 ]; then
        echo "❌ Erro ao criar ambiente virtual!"
        echo ""
        echo "Tente manualmente:"
        echo "  sudo apt install python3-venv python3-full"
        echo "  python3 -m venv venv"
        exit 1
    fi
    echo "✅ Ambiente virtual criado!"
    echo ""
else
    echo "✅ Ambiente virtual já existe."
    echo ""
fi

# Ativar ambiente virtual
echo "📦 Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo "📦 Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📦 Instalando PyQt6..."
pip install PyQt6

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Instalação concluída com sucesso!"
    echo ""
    echo "Para executar a aplicação:"
    echo "  ./run.sh"
    echo ""
    echo "Ou manualmente:"
    echo "  source venv/bin/activate"
    echo "  python3 main.py"
    echo ""
else
    echo ""
    echo "❌ Erro na instalação!"
    echo ""
    echo "Tente manualmente:"
    echo "  source venv/bin/activate"
    echo "  pip install PyQt6"
    echo ""
    exit 1
fi
