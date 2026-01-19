# Time Tracker ⏱️

Aplicação desktop **leve, rápida e moderna** para gerenciamento de tempo por card, desenvolvida para Linux.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Sobre

O Time Tracker é uma ferramenta de produtividade que permite controlar o tempo gasto em múltiplos cards/tarefas de forma simples e intuitiva. Perfeito para desenvolvedores que precisam rastrear tempo em diferentes issues, tickets ou projetos.

## ✨ Características

- 🚀 **Leve e Rápida**: Aplicação nativa com PyQt6
- 🎨 **Interface Moderna**: Design limpo e profissional
- ⏱️ **Timers Independentes**: Controle múltiplos cards simultaneamente
- 🕐 **Registro Automático**: Horários de início e fim preenchidos automaticamente
- ☑️ **Seleção em Massa**: Select All para operações rápidas
- 💾 **Zero Configuração**: Funciona direto após instalação

## 🎯 Funcionalidades

- ✅ **Adicionar cards** com nomes personalizados (ex: CADCT-1301)
- ▶️ **Play/Pause** para cada card independentemente
- ⏱️ **Timer preciso** no formato HH:MM:SS
- 🕐 **Hora inicial** preenchida ao clicar em Play
- 🕐 **Hora final** preenchida ao clicar em Pause
- ☑️ **Seleção individual ou em massa** de cards
- 🗑️ **Exclusão** de cards selecionados
- ✏️ **Edição** do nome do card a qualquer momento

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

## 📖 Guia de Uso

### Interface Principal

| Coluna | Descrição |
|--------|-----------|
| ☑ | Checkbox para selecionar o card |
| **Card** | Campo editável com o nome do card |
| ▶ | Botão Play (verde) - Inicia o timer |
| ⏸ | Botão Pause (vermelho) - Pausa o timer |
| **Tempo** | Contador HH:MM:SS |
| **Hr Inicial** | Preenchida automaticamente ao iniciar |
| **Hr Final** | Preenchida automaticamente ao pausar |

### Fluxo de Trabalho

1. **Adicionar Card**: Clique em "➕ Adicionar Card"
2. **Nomear**: Digite o identificador (ex: ISSUE-123)
3. **Iniciar**: Clique no botão ▶ verde
4. **Trabalhar**: O timer conta automaticamente
5. **Pausar**: Clique no botão ⏸ vermelho
6. **Continuar**: Clique em ▶ novamente para retomar

### Dicas

- 💡 Vários timers podem rodar ao mesmo tempo
- 💡 O tempo é acumulado ao pausar e retomar
- 💡 Use "Select All" para operações em massa
- 💡 Os dados ficam em memória durante a execução

## 🏗️ Estrutura do Projeto

```
timeTracker/
├── main.py              # Interface gráfica (PyQt6)
├── models.py            # Modelo de dados do Card
├── card_manager.py      # Lógica de gerenciamento
├── test.py              # Testes unitários
├── requirements.txt     # Dependências
├── install.sh           # Script de instalação
├── run.sh              # Script de execução
├── timetracker.desktop  # Atalho para desktop
├── README.md           # Este arquivo
└── GUIA.md             # Guia detalhado
```

## 🧪 Testes

Execute os testes unitários:

```bash
python3 test.py
```

## 🛠️ Tecnologias

- **Python 3**: Linguagem principal
- **PyQt6**: Framework de interface gráfica
- **Qt Fusion Style**: Estilo moderno da interface

## 📸 Preview da Interface

A interface possui:
- Tabela limpa com bordas arredondadas
- Botões coloridos intuitivos (verde = play, vermelho = pause)
- Campos editáveis inline
- Layout responsivo e espaçado
- Tipografia clara e legível

## 🔧 Solução de Problemas

**Erro: "No module named 'PyQt6'"**
```bash
python3 -m pip install --user PyQt6
```

**Erro: "pip não encontrado"**
```bash
sudo apt install python3-pip
```

**Verificar instalação:**
```bash
python3 -c "import PyQt6; print('PyQt6 instalado com sucesso!')"
```

## 🚀 Melhorias Futuras

- [ ] Exportar dados para CSV
- [ ] Persistência em banco de dados SQLite
- [ ] Notificações de tempo
- [ ] Relatórios diários/semanais
- [ ] Tema escuro/claro
- [ ] Atalhos de teclado
- [ ] Backup automático
- [ ] Sincronização em nuvem

## 📝 Notas

- Os dados atuais são mantidos apenas em memória
- Fechar a aplicação resultará na perda dos dados
- Para uso profissional, considere implementar persistência

## 📄 Licença

Este projeto é de código aberto para uso pessoal e educacional.

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas! Consulte o código-fonte para entender a arquitetura.

---

**Desenvolvido com ❤️ para a comunidade Linux**
