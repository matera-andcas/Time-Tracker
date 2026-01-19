# Guia de Instalação e Uso - Time Tracker

## 📋 Pré-requisitos

- **Sistema Operacional**: Linux
- **Python**: 3.8 ou superior (já instalado ✅)
- **pip**: Gerenciador de pacotes Python

## 🚀 Instalação

### Passo 1: Instalar python3-venv (se necessário)

```bash
sudo apt update
sudo apt install python3-venv python3-full
```

### Passo 2: Instalar dependências

Você pode usar o script automático:

```bash
./install.sh
```

Ou instalar manualmente:

```bash
python3 -m venv venv
source venv/bin/activate
pip install PyQt6
```

**Por que usar ambiente virtual?**

O Ubuntu/Debian moderno usa "externally-managed-environment" para proteger os pacotes Python do sistema. Um ambiente virtual (`venv`) cria um espaço isolado para as dependências do projeto, sem afetar o sistema.

## ▶️ Como Executar

### Opção 1: Script de execução

```bash
./run.sh
```

### Opção 2: Executar diretamente

```bash
python3 main.py
```

## 📖 Como Usar a Aplicação

### Interface Principal

A aplicação possui uma tabela com as seguintes colunas:

1. **☑ Checkbox**: Seleciona o card individualmente
2. **Card**: Campo de texto editável para o nome do card (ex: CADCT-1301)
3. **▶ Play**: Botão verde para iniciar o timer
4. **⏸ Pause**: Botão vermelho para pausar o timer
5. **Tempo**: Mostra o tempo decorrido (HH:MM:SS)
6. **Hr Inicial**: Preenchida automaticamente ao clicar em Play
7. **Hr Final**: Preenchida automaticamente ao clicar em Pause

### Funcionalidades

#### ➕ Adicionar Card
- Clique no botão **"➕ Adicionar Card"** no canto inferior direito
- Um novo card vazio será adicionado à lista
- Digite o nome do card no campo de texto

#### ▶️ Iniciar Timer
- Clique no botão **▶** (verde) do card desejado
- O timer começará a contar automaticamente
- A hora inicial será preenchida com o horário atual
- O botão Play ficará desabilitado enquanto o timer estiver rodando

#### ⏸ Pausar Timer
- Clique no botão **⏸** (vermelho) do card em execução
- O timer será pausado mantendo o tempo acumulado
- A hora final será preenchida com o horário atual
- Você pode clicar em Play novamente para continuar

#### ☑️ Selecionar Cards
- **Seleção individual**: Clique no checkbox de cada card
- **Select All**: Use o checkbox "Select All" no rodapé para selecionar/desmarcar todos

#### 🗑️ Deletar Cards
- Selecione os cards que deseja remover
- Clique no botão **"🗑 Deletar Selecionados"**
- Apenas os cards selecionados serão removidos

### 💡 Dicas de Uso

- **Múltiplos timers**: Você pode ter vários cards rodando ao mesmo tempo
- **Edição a qualquer momento**: O nome do card pode ser editado mesmo com o timer rodando
- **Tempo acumulado**: Pausar e retomar mantém o tempo total acumulado
- **Sem perda de dados**: Enquanto a aplicação estiver aberta, todos os dados ficam em memória

## 🎨 Características da Interface

- ✨ Design moderno e limpo
- 🎨 Cores intuitivas (verde para play, vermelho para pause)
- 📱 Layout responsivo
- ⚡ Interface rápida e fluida
- 🖱️ Interação simples e direta

## 🔧 Estrutura do Projeto

```
timeTracker/
├── main.py              # Arquivo principal com a interface gráfica
├── models.py            # Modelo de dados (Card)
├── card_manager.py      # Gerenciador de cards (lógica de negócio)
├── requirements.txt     # Dependências do projeto
├── install.sh           # Script de instalação
├── run.sh              # Script de execução
├── README.md           # Documentação básica
└── GUIA.md             # Este guia detalhado
```

## 🐛 Solução de Problemas

### Erro: "externally-managed-environment"

Este é o comportamento correto do Ubuntu/Debian moderno. Use o ambiente virtual:

```bash
./install.sh
```

Ou manualmente:
```bash
python3 -m venv venv
source venv/bin/activate
pip install PyQt6
```

### Erro: "No module named 'PyQt6'"

```bash
source venv/bin/activate
pip install PyQt6
```

### Erro: "python3-venv não encontrado"

```bash
sudo apt install python3-venv python3-full
```

### A aplicação não abre

1. Verifique se o Python está instalado:
   ```bash
   python3 --version
   ```

2. Verifique se o PyQt6 está instalado:
   ```bash
   python3 -c "import PyQt6; print('PyQt6 OK')"
   ```

## 📝 Notas

- Os dados são mantidos em memória durante a execução
- Ao fechar a aplicação, os dados serão perdidos
- Para persistência futura, pode ser adicionada exportação para CSV ou banco de dados

## 🚀 Próximas Melhorias Possíveis

- [ ] Exportar dados para CSV
- [ ] Salvar histórico em arquivo
- [ ] Adicionar notificações
- [ ] Relatórios de produtividade
- [ ] Temas claro/escuro
- [ ] Atalhos de teclado

## 📧 Suporte

Para questões ou melhorias, consulte o código-fonte ou a documentação do projeto.
