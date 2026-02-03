# System Patterns: Time Tracker

## Architecture Overview

### Architecture Style
**Model-View-Controller (MVC)** pattern with clear separation of concerns:
- **Model**: Domain entities and business logic
- **View**: PyQt6 UI components
- **Controller**: Application coordination and state management

### Directory Structure
```
timeTracker/
├── main.py                 # Application entry point
├── src/
│   ├── config.py          # Configuration constants
│   ├── application/       # Controller layer
│   │   └── controller.py
│   ├── domain/            # Business logic layer
│   │   ├── models.py
│   │   └── services.py
│   ├── infrastructure/    # Data persistence layer
│   │   └── database.py
│   └── ui/                # View layer
│       ├── main_window.py
│       ├── styles.py
│       ├── time_widgets.py
│       └── widgets.py
├── utils/                 # Utility scripts
├── docs/                  # Documentation
└── build/                 # Build artifacts
```

## Key Technical Decisions

### 1. Framework Choice: PyQt6
**Why**: 
- Native performance and look-and-feel
- Cross-platform support (Linux/Windows)
- Rich widget library
- Signal/slot mechanism for event handling
- Mature and well-documented

**Implications**:
- Requires PyQt6 dependency
- Uses Qt event loop
- Threading considerations for background tasks

### 2. Database: SQLite
**Why**:
- Serverless, file-based database
- Zero configuration
- Built into Python
- Perfect for single-user desktop apps
- Reliable ACID transactions

**Implications**:
- Local data only (no cloud sync)
- File locking considerations
- Schema migrations handled manually

### 3. Timer Implementation
**Decision**: QTimer-based updates every 1000ms
**Why**:
- Integrates with Qt event loop
- Accurate enough for second-level precision
- Low CPU overhead
- Reliable across platforms

### 4. Build System: PyInstaller
**Why**:
- Creates standalone executables
- Cross-platform support
- Bundles all dependencies
- Simple configuration with .spec file

## Design Patterns in Use

### 1. MVC (Model-View-Controller)
**Implementation**:
- `models.py`: Data models (Card, TimeEntry)
- `main_window.py`: View components
- `controller.py`: Orchestration and business logic

### 2. Repository Pattern
**Implementation**: `database.py`
- Abstracts data access
- Provides CRUD operations
- Handles database connections
- Encapsulates SQLite specifics

### 3. Service Layer
**Implementation**: `services.py`
- Business logic for time calculations
- Card management operations
- Validation rules
- Domain operations

### 4. Observer Pattern (Qt Signals/Slots)
**Implementation**:
- UI events trigger signals
- Slots handle business logic
- Decouples UI from logic
- Example: Play button → start_timer signal → Controller slot

## Component Relationships

### Core Components

#### 1. TimeTrackerController (application/controller.py)
**Responsibilities**:
- Initialize application
- Coordinate between UI and domain
- Handle user actions
- Manage application state
- Control auto-save timer

**Dependencies**:
- MainWindow (UI)
- CardService (domain)
- DatabaseManager (infrastructure)

#### 2. MainWindow (ui/main_window.py)
**Responsibilities**:
- Display UI components
- Emit user action signals
- Update display based on data
- Manage theme switching

**Dependencies**:
- CardWidget (ui/widgets.py)
- Styles module (ui/styles.py)

#### 3. CardService (domain/services.py)
**Responsibilities**:
- Business logic for cards
- Time calculations
- Validation
- Card state management

**Dependencies**:
- Card model (domain/models.py)
- DatabaseManager (infrastructure)

#### 4. DatabaseManager (infrastructure/database.py)
**Responsibilities**:
- Database initialization
- CRUD operations
- Connection management
- Data persistence

**Dependencies**:
- Card model (domain/models.py)
- SQLite

## Critical Implementation Paths

### 1. Application Startup Flow
```
main.py
  → QApplication initialization
  → TimeTrackerController creation
    → DatabaseManager.initialize()
    → MainWindow creation
    → Load existing cards from database
    → Display UI
  → Event loop starts
```

### 2. Card Creation Flow
```
User clicks "Adicionar Card"
  → MainWindow emits add_card signal
  → Controller.on_add_card()
    → Create Card model
    → CardService.validate()
    → DatabaseManager.insert_card()
    → MainWindow.add_card_widget()
```

### 3. Timer Start Flow
```
User clicks Play button
  → CardWidget emits start_timer signal
  → Controller.on_start_timer(card_id)
    → Update card.start_time
    → Start QTimer for this card
    → DatabaseManager.update_card()
    → CardWidget.update_display()
```

### 4. Auto-Save Flow
```
Every 5 seconds
  → QTimer timeout
  → Controller.auto_save()
    → For each modified card
      → DatabaseManager.update_card()
    → Clear modification flags
```

### 5. Theme Toggle Flow
```
User clicks theme button
  → MainWindow.toggle_theme()
    → Update is_dark_mode flag
    → styles.apply_theme(window, is_dark_mode)
    → Save preference to database
    → Refresh all widgets
```

## Data Flow Patterns

### Read Operations
```
UI Request → Controller → Service → Database → Model → Service → Controller → UI
```

### Write Operations
```
UI Action → Controller → Service (validate) → Database (persist) → UI (update display)
```

### Timer Updates
```
QTimer tick → Controller → Calculate elapsed → UI update (no database write until pause)
```

## Threading Considerations

### Main Thread (UI Thread)
- All UI operations
- Timer updates
- User interactions

### Background Operations
- Currently all operations synchronous
- Future: Database operations could be threaded
- Auto-save already on timer (non-blocking)

## Error Handling Strategy

### Database Errors
- Catch SQLite exceptions
- Log errors
- Show user-friendly message
- Graceful degradation

### UI Errors
- Qt exception handling
- Prevent crashes
- Maintain application state

### Timer Errors
- Validate time calculations
- Handle clock changes
- Prevent negative durations

## Configuration Management

### Constants (config.py)
- Database path
- Auto-save interval
- Default theme
- Window dimensions
- Application metadata

### User Preferences
- Theme selection
- Window position/size
- Stored in database

## Testing Strategy

### Manual Testing
- Cross-platform testing (Linux/Windows)
- UI interaction testing
- Timer accuracy validation
- Data persistence verification

### Future Considerations
- Unit tests for services
- Integration tests for database
- UI automation tests
