# Arquitetura Refatorada - Time Tracker

## 📋 Visão Geral

A aplicação foi refatorada seguindo princípios de **Clean Architecture** com separação clara de responsabilidades.

```
┌─────────────────────────────────────────────────────────────┐
│                    Presentation Layer                        │
│                      (main.py)                              │
│                    - Interface UI                           │
│                    - Event Handlers                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Business Layer                             │
│                  (card_manager.py)                          │
│              - Lógica de negócio                            │
│              - Validações                                    │
│              - Orquestração                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │                              │
┌───────▼────────┐            ┌───────▼────────┐
│   Data Layer   │            │  Domain Layer  │
│  (database.py) │            │   (models.py)  │
│  - SQLite      │            │   - Entities   │
│  - CRUD ops    │            │   - Timer      │
└────────────────┘            └────────────────┘
```

## 🏗️ Camadas da Arquitetura

### 1. **Presentation Layer** (`main.py`)
**Responsabilidade**: Interface com o usuário

- `TimeTrackerApp`: Janela principal Qt
- Renderização da UI
- Captura de eventos do usuário
- Delegação para Business Layer

**Não contém**: Lógica de negócio, acesso ao banco

### 2. **Business Layer** (`card_manager.py`)
**Responsabilidade**: Lógica de negócio

- `CardManager`: Orquestrador principal
- Gerenciamento de estado dos cards
- Validações de negócio
- Coordenação entre Model e Database

**Princípios aplicados**:
- Single Responsibility
- Dependency Injection (recebe Database)

### 3. **Data Layer** (`database.py`)
**Responsabilidade**: Persistência de dados

- `Database`: Abstração do SQLite
- CRUD operations
- Migrations/Schema
- Isolamento da tecnologia de BD

**Vantagens**:
- Fácil trocar SQLite por PostgreSQL
- Testável com mocks
- Queries centralizadas

### 4. **Domain Layer** (`models.py`)
**Responsabilidade**: Entidades do domínio

- `Card`: Entidade principal
- Lógica de timer (QElapsedTimer)
- Validações de domínio
- Conversão to/from dict

**Características**:
- Independente de frameworks
- Rich Domain Model
- Encapsulamento

## 📦 Estrutura de Arquivos

```
timeTracker/
├── main.py              # Presentation - UI
├── card_manager.py      # Business - Lógica
├── database.py          # Data - Persistência
├── models.py            # Domain - Entidades
├── config.py            # Configuration
├── data_exporter.py     # Utilities
└── timetracker.db       # SQLite Database
```

## 🔄 Fluxo de Dados

### Adicionar Card
```
User → [UI] → CardManager.add_card()
                    ↓
              Card() criado
                    ↓
         Database.save_card()
                    ↓
              SQLite INSERT
                    ↓
           Retorna ID → Card.db_id
                    ↓
         [UI] ← refresh_table()
```

### Iniciar Timer
```
User clica Play → [UI] → Card.start()
                              ↓
                    QElapsedTimer.start()
                              ↓
                    Timer atualiza a cada 100ms
                              ↓
                    [UI] update_timer_display()
```

### Auto-Save
```
Timer 5s → auto_save()
              ↓
    CardManager.save_to_database()
              ↓
    Para cada card:
      Database.save_card()
              ↓
         SQLite UPDATE
```

## 🗄️ Schema do Banco de Dados

```sql
CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    elapsed_seconds INTEGER DEFAULT 0,
    start_time TEXT,
    end_time TEXT,
    is_running BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## ✨ Melhorias Implementadas

### 1. **Persistência com SQLite**
- ✅ Dados salvos automaticamente
- ✅ Carregamento ao iniciar
- ✅ Auto-save a cada 5 segundos
- ✅ Save ao fechar aplicação

### 2. **Separação de Responsabilidades**
- ✅ UI não acessa banco diretamente
- ✅ Business layer isolada
- ✅ Database abstraído
- ✅ Models independentes

### 3. **Dependency Injection**
```python
# Antes
card_manager = CardManager()

# Depois
db = Database()
card_manager = CardManager(db)  # DI
```

### 4. **Rich Domain Model**
```python
# Card tem comportamento
card.start()
card.pause()
card.get_formatted_time()

# Card conhece sua persistência
card.to_dict()
Card.from_dict(data)
```

## 🧪 Testabilidade

A nova arquitetura é facilmente testável:

```python
# Mock do Database
class MockDatabase:
    def save_card(self, **kwargs):
        return 1

# Teste do CardManager
db = MockDatabase()
manager = CardManager(db)
card = manager.add_card("TEST-001")
assert card.name == "TEST-001"
```

## 🚀 Benefícios

### Antes
- ❌ Dados perdidos ao fechar
- ❌ Lógica misturada na UI
- ❌ Difícil de testar
- ❌ Acoplamento alto

### Depois
- ✅ Persistência automática
- ✅ Camadas bem definidas
- ✅ Fácil de testar
- ✅ Baixo acoplamento
- ✅ Fácil de estender

## 📈 Próximas Evoluções Possíveis

### Fácil adicionar:
1. **Repository Pattern**
   ```python
   class CardRepository:
       def find_by_name(self, name: str) -> List[Card]
       def find_running(self) -> List[Card]
   ```

2. **Service Layer**
   ```python
   class TimerService:
       def start_timer(self, card_id: int)
       def pause_timer(card_id: int)
   ```

3. **Event System**
   ```python
   class CardEvents:
       on_started = Signal()
       on_paused = Signal()
   ```

4. **Migrations**
   ```python
   class Migration_v2:
       def upgrade():
           # ALTER TABLE cards ADD COLUMN project_id
   ```

## 🎯 Design Patterns Aplicados

1. **Repository Pattern** (Database)
2. **Facade Pattern** (CardManager)
3. **Active Record** (Card)
4. **Dependency Injection** (Database → CardManager)
5. **Observer Pattern** (Qt Signals/Slots)

## 💡 Princípios SOLID

- ✅ **S**ingle Responsibility - Cada classe tem uma responsabilidade
- ✅ **O**pen/Closed - Fácil estender sem modificar
- ✅ **L**iskov Substitution - Database pode ser substituído
- ✅ **I**nterface Segregation - Interfaces pequenas e focadas
- ✅ **D**ependency Inversion - Depende de abstrações

---

**Documentação atualizada em**: 19/01/2026
