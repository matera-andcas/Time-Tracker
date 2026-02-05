# Padrões do Sistema: Time Tracker

## Visão Geral da Arquitetura

### Estilo Arquitetural
Padrão **Model-View-Controller (MVC)** com clara separação de responsabilidades:
- **Model**: Entidades de domínio e lógica de negócio
- **View**: Componentes de UI PyQt6
- **Controller**: Coordenação de aplicação e gerenciamento de estado

### Estrutura de Diretórios
```
timeTracker/
├── main.py                 # Ponto de entrada da aplicação
├── src/
│   ├── config.py          # Constantes de configuração
│   ├── application/       # Camada de controller
│   │   └── controller.py
│   ├── domain/            # Camada de lógica de negócio
│   │   ├── models.py
│   │   └── services.py
│   ├── infrastructure/    # Camada de persistência de dados
│   │   └── database.py
│   └── ui/                # Camada de view
│       ├── main_window.py
│       ├── styles.py
│       ├── time_widgets.py
│       └── widgets.py
├── utils/                 # Scripts utilitários
├── docs/                  # Documentação
└── build/                 # Artefatos de build
```

## Decisões Técnicas Chave

### 1. Escolha de Framework: PyQt6
**Por quê**: 
- Performance nativa e aparência nativa
- Suporte multi-plataforma (Linux/Windows)
- Biblioteca rica de widgets
- Mecanismo de sinais/slots para tratamento de eventos
- Maduro e bem documentado

**Implicações**:
- Requer dependência PyQt6
- Usa event loop do Qt
- Considerações de threading para tarefas em segundo plano

### 2. Banco de Dados: SQLite
**Por quê**:
- Banco de dados sem servidor, baseado em arquivo
- Zero configuração
- Integrado ao Python
- Perfeito para apps desktop de usuário único
- Transações ACID confiáveis

**Implicações**:
- Dados apenas locais (sem sincronização na nuvem)
- Considerações de bloqueio de arquivo
- Migrações de schema tratadas manualmente

### 3. Implementação do Timer
**Decisão**: Atualizações baseadas em QTimer a cada 1000ms
**Por quê**:
- Integra com event loop do Qt
- Preciso o suficiente para precisão de nível de segundo
- Baixo overhead de CPU
- Confiável entre plataformas

### 4. Sistema de Build: PyInstaller
**Por quê**:
- Cria executáveis standalone
- Suporte multi-plataforma
- Empacota todas as dependências
- Configuração simples com arquivo .spec

## Padrões de Design em Uso

### 1. MVC (Model-View-Controller)
**Implementação**:
- `models.py`: Modelos de dados (Card, TimeEntry)
- `main_window.py`: Componentes de view
- `controller.py`: Orquestração e lógica de negócio

### 2. Padrão Repository
**Implementação**: `database.py`
- Abstrai acesso a dados
- Fornece operações CRUD
- Manipula conexões de banco de dados
- Encapsula especificidades do SQLite

### 3. Camada de Serviço
**Implementação**: `services.py`
- Lógica de negócio para cálculos de tempo
- Operações de gerenciamento de cards
- Regras de validação
- Operações de domínio

### 4. Padrão Observer (Sinais/Slots Qt)
**Implementação**:
- Eventos de UI disparam sinais
- Slots tratam lógica de negócio
- Desacopla UI da lógica
- Exemplo: Botão Play → sinal start_timer → Slot do Controller

## Relacionamentos de Componentes

### Componentes Principais

#### 1. TimeTrackerController (application/controller.py)
**Responsabilidades**:
- Inicializar aplicação
- Coordenar entre UI e domínio
- Tratar ações do usuário
- Gerenciar estado da aplicação
- Controlar timer de auto-save

**Dependências**:
- MainWindow (UI)
- CardService (domain)
- DatabaseManager (infrastructure)

#### 2. MainWindow (ui/main_window.py)
**Responsabilidades**:
- Exibir componentes de UI
- Emitir sinais de ações do usuário
- Atualizar display baseado em dados
- Gerenciar alternância de tema

**Dependências**:
- CardWidget (ui/widgets.py)
- Módulo Styles (ui/styles.py)

#### 3. CardService (domain/services.py)
**Responsabilidades**:
- Lógica de negócio para cards
- Cálculos de tempo
- Validação
- Gerenciamento de estado de card

**Dependências**:
- Modelo Card (domain/models.py)
- DatabaseManager (infrastructure)

#### 4. DatabaseManager (infrastructure/database.py)
**Responsabilidades**:
- Inicialização do banco de dados
- Operações CRUD
- Gerenciamento de conexão
- Persistência de dados

**Dependências**:
- Modelo Card (domain/models.py)
- SQLite

## Caminhos Críticos de Implementação

### 1. Fluxo de Inicialização da Aplicação
```
main.py
  → Inicialização do QApplication
  → Criação do TimeTrackerController
    → DatabaseManager.initialize()
    → Criação do MainWindow
    → Carregar cards existentes do banco de dados
    → Exibir UI
  → Event loop inicia
```

### 2. Fluxo de Criação de Card
```
Usuário clica "Adicionar Card"
  → MainWindow emite sinal add_card
  → Controller.on_add_card()
    → Criar modelo Card
    → CardService.validate()
    → DatabaseManager.insert_card()
    → MainWindow.add_card_widget()
```

### 3. Fluxo de Início do Timer
```
Usuário clica botão Play
  → CardWidget emite sinal start_timer
  → Controller.on_start_timer(card_id)
    → Atualizar card.start_time
    → Iniciar QTimer para este card
    → DatabaseManager.update_card()
    → CardWidget.update_display()
```

### 4. Fluxo de Auto-Save
```
A cada 5 segundos
  → QTimer timeout
  → Controller.auto_save()
    → Para cada card modificado
      → DatabaseManager.update_card()
    → Limpar flags de modificação
```

### 5. Fluxo de Alternância de Tema
```
Usuário clica botão de tema
  → MainWindow.toggle_theme()
    → Atualizar flag is_dark_mode
    → styles.apply_theme(window, is_dark_mode)
    → Salvar preferência no banco de dados
    → Atualizar todos os widgets
```

## Padrões de Fluxo de Dados

### Operações de Leitura
```
Requisição UI → Controller → Service → Database → Model → Service → Controller → UI
```

### Operações de Escrita
```
Ação UI → Controller → Service (validar) → Database (persistir) → UI (atualizar display)
```

### Atualizações de Timer
```
Tick QTimer → Controller → Calcular decorrido → Atualização UI (sem escrita em banco até pausar)
```

## Considerações de Threading

### Thread Principal (Thread de UI)
- Todas operações de UI
- Atualizações de timer
- Interações do usuário

### Operações em Segundo Plano
- Atualmente todas operações síncronas
- Futuro: Operações de banco de dados poderiam usar threads
- Auto-save já em timer (não-bloqueante)

## Estratégia de Tratamento de Erros

### Erros de Banco de Dados
- Capturar exceções SQLite
- Logar erros
- Mostrar mensagem amigável ao usuário
- Degradação graciosa

### Erros de UI
- Tratamento de exceções do Qt
- Prevenir crashes
- Manter estado da aplicação

### Erros de Timer
- Validar cálculos de tempo
- Tratar mudanças de relógio
- Prevenir durações negativas

## Gerenciamento de Configuração

### Constantes (config.py)
- Caminho do banco de dados
- Intervalo de auto-save
- Tema padrão
- Dimensões da janela
- Metadados da aplicação

### Preferências do Usuário
- Seleção de tema
- Posição/tamanho da janela
- Armazenado no banco de dados

## Estratégia de Testes

### Testes Manuais
- Testes multi-plataforma (Linux/Windows)
- Testes de interação de UI
- Validação de precisão do timer
- Verificação de persistência de dados

### Considerações Futuras
- Testes unitários para serviços
- Testes de integração para banco de dados
- Testes de automação de UI
