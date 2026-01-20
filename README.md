# Time Tracker ⏱️

Aplicação desktop **leve, rápida e moderna** para gerenciamento de tempo por card, para Linux e desenvolvida 100% por IA.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Sobre

O Time Tracker é uma ferramenta de produtividade que permite controlar o tempo gasto em múltiplos cards/tarefas de forma simples e intuitiva. Perfeito para desenvolvedores que precisam rastrear tempo em diferentes issues, tickets ou projetos.

## ✨ Características

- 🚀 **Leve e Rápida**: Aplicação nativa com PyQt6
- ⏱️ **Timers Independentes**: Controle múltiplos cards simultaneamente
- 🕐 **Registro Automático**: Horários de início e fim preenchidos automaticamente
- ☑️ **Seleção em Massa**: Select All para operações rápidas
- 💾 **Persistência SQLite**: Dados salvos automaticamente em banco de dados
- 🔗 **Links Clicáveis**: URLs são detectadas e abrem no navegador
- 🌓 **Tema Escuro/Claro**: Alterne entre temas com preferência salva

## 🎯 Funcionalidades

- ✅ **Adicionar cards** com nomes personalizados ou URLs
- ▶️ **Play/Pause** para cada card independentemente
- ⏱️ **Timer preciso** no formato HH:MM:SS
- 🕐 **Hora inicial** preenchida ao clicar em Play
- 🕐 **Hora final** preenchida ao clicar em Pause
- 🗑️ **Exclusão** de cards selecionados
- ✏️ **Edição** do nome do card a qualquer momento
- 💾 **Auto-save** - Dados salvos a cada 5 segundos
- 🌓 **Tema escuro/claro** - Preferência salva entre sessões
- 📅 **Data automática** - Dia atual exibido para cada card

## 📦 Requisitos

- **Sistema**: Linux
- **Python**: 3.8 ou superior
- **PyQt6**: 6.6.0+

## 🚀 Instalação Rápida

### 1. Instalar python3-venv (se necessário)

```bash
sudo apt update
sudo apt install python3-venv python3-full
```

### 2. Instalar dependências

**Opção A - Script automático (recomendado):**
```bash
./install.sh
```

Este script irá:
- Criar um ambiente virtual Python (`venv/`)
- Instalar o PyQt6 no ambiente isolado
- Configurar tudo automaticamente

**Opção B - Manual:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install PyQt6
```

## ▶️ Como Executar

**Opção A - Script:**
```bash
./run.sh
```

**Opção B - Direto:**
```bash
python3 main.py
```


### Dicas

- 💡 Vários timers podem rodar ao mesmo tempo
- 💡 O tempo é acumulado ao pausar e retomar
- 💡 Use "Select All" para operações em massa
- 💡 Cole uma URL no campo Card e ela vira link clicável
- 💡 Duplo-clique em um link para editá-lo
- 💡 Os dados são salvos automaticamente no SQLite

## 🏗️ Arquitetura do Projeto (MVC)

```
timeTracker/
├── src/
│   ├── domain/              # MODEL - Entidades e lógica de negócio
│   │   ├── models.py        # Entidade Card
│   │   └── services.py      # CardService (operações de negócio)
│   │
│   ├── infrastructure/      # Persistência
│   │   └── database.py      # Database SQLite
│   │
│   ├── ui/                  # VIEW - Interface gráfica
│   │   ├── main_window.py   # Janela principal
│   │   ├── widgets.py       # Widgets customizados
│   │   └── styles.py        # Temas claro/escuro
│   │
│   ├── application/         # CONTROLLER - Orquestração
│   │   └── controller.py    # TimeTrackerController
│   │
│   └── config.py            # Configurações
│
├── main.py                  # Entry point (inicialização)
├── requirements.txt         # Dependências Python
├── timetracker.db          # Banco de dados SQLite (criado automaticamente)
├── install.sh              # Script de instalação
├── run.sh                  # Script de execução
└── timetracker.desktop     # Atalho para desktop
```

### 💾 Persistência de Dados

- Os dados são salvos automaticamente em `timetracker.db` (SQLite)
- Auto-save acontece a cada 5 segundos
- Todos os cards e configurações são persistidos
- Ao reabrir a aplicação, tudo é restaurado


## 🔧 Solução de Problemas

**Erro: "No module named 'PyQt6'"**
```bash
python3 -m pip install --user PyQt6
```

**Erro: "pip não encontrado"**
```bash
sudo apt install python3-pip
```

## 📄 Licença

Este projeto é de código aberto para uso pessoal e educacional.

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas! Consulte o código-fonte para entender a arquitetura.

---

**Desenvolvido com ❤️ para a comunidade Linux**
