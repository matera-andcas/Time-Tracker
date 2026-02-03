# Technical Context: Time Tracker

## Technology Stack

### Core Technologies

#### Python 3.8+
**Version**: 3.8 minimum, tested with 3.10+
**Purpose**: Primary programming language
**Why Chosen**:
- Cross-platform compatibility
- Rich ecosystem of libraries
- Excellent PyQt6 integration
- Easy distribution with PyInstaller

#### PyQt6 6.6.0+
**Purpose**: GUI framework
**Why Chosen**:
- Native look and feel
- Cross-platform (Linux/Windows)
- Rich widget library
- Excellent documentation
- Performance and stability

**Key Modules Used**:
- `QtWidgets`: Core UI components
- `QtCore`: Event system, timers, signals/slots
- `QtGui`: Graphics and styling

#### SQLite3
**Purpose**: Data persistence
**Why Chosen**:
- Built into Python
- Zero configuration
- File-based (no server)
- ACID compliant
- Perfect for single-user desktop apps

### Build & Distribution

#### PyInstaller 6.0.0+
**Purpose**: Create standalone executables
**Configuration**: `TimeTracker.spec`
**Capabilities**:
- Bundles Python interpreter
- Includes all dependencies
- Creates single executable
- Cross-platform builds

## Development Setup

### Prerequisites

#### Linux
```bash
# System requirements
- Ubuntu 20.04+ or equivalent
- Python 3.8+
- python3-venv
- python3-full

# Installation
sudo apt update
sudo apt install python3-venv python3-full
```

#### Windows
```cmd
# System requirements
- Windows 10/11
- Python 3.8+ (from python.org)
- Add Python to PATH during installation
```

### Environment Setup

#### Virtual Environment Creation
```bash
# Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate.bat
```

#### Dependency Installation
```bash
pip install -r requirements.txt
```

**Dependencies**:
- `PyQt6>=6.6.0`: GUI framework
- `pyinstaller>=6.0.0`: Executable builder

### Running the Application

#### Development Mode
```bash
# Linux
./run.sh
# or
python3 main.py

# Windows
run.bat
# or
python main.py
```

#### Build Mode
```bash
# Linux
./build.sh

# Windows
build.bat
```

## Technical Constraints

### Platform Limitations

#### Linux
- Requires display server (X11/Wayland)
- Desktop file for system integration
- Package dependencies for PyQt6

#### Windows
- Requires Windows 10 or later
- May need Visual C++ Redistributable
- PATH configuration critical

### Performance Constraints
- Timer precision: 1 second granularity
- Auto-save interval: 5 seconds
- Database: Single-file SQLite (no concurrency issues)
- Memory: Minimal footprint (< 100MB typical)

### Security Constraints
- Local data storage only
- No encryption (single-user system)
- File system permissions apply
- No network communication

## Dependencies

### Runtime Dependencies
```
PyQt6>=6.6.0
```

### Build Dependencies
```
pyinstaller>=6.0.0
```

### System Dependencies

#### Linux
- `python3-venv`: Virtual environment support
- `python3-full`: Complete Python installation
- Display server (X11/Wayland)
- Qt platform plugins

#### Windows
- Python 3.8+ installer
- Visual C++ Redistributable (usually included)

## Tool Usage Patterns

### PyQt6 Patterns

#### Signal/Slot Connections
```python
# Connect signals to slots
button.clicked.connect(self.on_button_clicked)

# Custom signals
class MyWidget(QWidget):
    custom_signal = pyqtSignal(str)
    
    def emit_signal(self):
        self.custom_signal.emit("data")
```

#### Timer Usage
```python
# Create repeating timer
self.timer = QTimer()
self.timer.timeout.connect(self.update_display)
self.timer.start(1000)  # milliseconds
```

#### Layout Management
```python
# Vertical layout
layout = QVBoxLayout()
layout.addWidget(widget)
layout.addStretch()
```

### SQLite Patterns

#### Connection Management
```python
import sqlite3

# Connect
conn = sqlite3.connect('timetracker.db')
conn.row_factory = sqlite3.Row  # Dict-like access

# Execute
cursor = conn.cursor()
cursor.execute("SELECT * FROM cards")
results = cursor.fetchall()

# Always close
conn.close()
```

#### Schema Management
```python
# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY,
        name TEXT,
        start_time TEXT,
        end_time TEXT,
        elapsed INTEGER
    )
''')
conn.commit()
```

### PyInstaller Patterns

#### Basic Build
```bash
pyinstaller --onefile --windowed main.py
```

#### Advanced Configuration (TimeTracker.spec)
```python
# Spec file for customization
a = Analysis(['main.py'])
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, name='TimeTracker')
```

## File Structure Details

### Configuration Files
- `requirements.txt`: Python dependencies
- `TimeTracker.spec`: PyInstaller configuration
- `timetracker.desktop`: Linux desktop integration

### Build Scripts
- `install.sh / install.bat`: Setup virtual environment and dependencies
- `run.sh / run.bat`: Execute application in development mode
- `build.sh / build.bat`: Create standalone executable
- `test_windows.bat`: Windows-specific testing

### Data Files
- `timetracker.db`: SQLite database (created at runtime)
- User data directory: Same as executable location

## Development Workflow

### Standard Development Cycle
1. Activate virtual environment
2. Make code changes
3. Run with `python main.py`
4. Test functionality
5. Commit changes
6. Build executable for distribution

### Build Workflow
1. Ensure all changes committed
2. Run build script (`./build.sh` or `build.bat`)
3. Test executable in `dist/` directory
4. Verify on target platform
5. Distribute executable

### Database Schema Updates
1. Modify schema in `database.py`
2. Add migration logic if needed
3. Test with fresh database
4. Test with existing database
5. Document changes

## Platform-Specific Considerations

### Linux
- **Desktop Integration**: Uses `.desktop` file in `utils/`
- **Permissions**: Scripts need execute permission (`chmod +x`)
- **Dependencies**: May need system Qt libraries
- **Distribution**: AppImage or DEB package potential

### Windows
- **Execution Policy**: May need to allow script execution
- **Path Issues**: Backslashes in file paths
- **UAC**: May need admin for installation
- **Distribution**: Single EXE or installer package

## Environment Variables
Currently none required. All configuration in code.

## Logging & Debugging

### Current Approach
- Print statements for debugging
- Qt warning messages in console
- SQLite errors caught and displayed

### Future Enhancements
- Structured logging with Python `logging` module
- Log file rotation
- Debug vs production modes
- Performance profiling

## Performance Considerations

### Optimization Points
- Timer updates: Only repaint changed widgets
- Database: Batch operations when possible
- Auto-save: Only save modified cards
- UI: Minimize layout recalculations

### Resource Usage
- CPU: Low (timer updates only)
- Memory: < 100MB typical
- Disk: Minimal (small SQLite database)
- Network: None

## Known Technical Issues
- None currently documented
- Track in `progress.md` as they arise

## Future Technical Considerations
- Add logging framework
- Implement database migrations
- Add unit tests
- Consider async database operations
- Theme customization beyond dark/light
