# Active Context: Time Tracker

**Last Updated**: 2026-01-27
**Current Phase**: Maintenance & Enhancement
**Status**: Stable, Functional

## Current Work Focus

### Immediate Tasks
1. Memory Bank initialization complete
2. Project documentation established
3. Ready for new feature requests or bug fixes

### Next Steps
- Await user direction for:
  - New features to implement
  - Bugs to fix
  - Performance improvements
  - UI/UX enhancements
  - Platform-specific optimizations

## Recent Changes
- Memory Bank structure created with all core files
- Project documentation comprehensive and up-to-date
- Custom instructions configured for memory persistence

## Active Decisions & Considerations

### Architecture Decisions
- **MVC Pattern**: Maintaining strict separation between layers
- **PyQt6**: Committed to this framework for foreseeable future
- **SQLite**: Local-first approach, no plans for cloud sync

### Design Decisions
- **Theme System**: Dark/light toggle sufficient for now
- **Auto-save**: 5-second interval balanced between safety and performance
- **Timer Precision**: 1-second granularity meets user needs

### Technical Decisions
- **Single File Database**: Simplifies backup and portability
- **No External Dependencies**: Keep minimal dependency footprint
- **Cross-platform First**: All features must work on Linux and Windows

## Important Patterns & Preferences

### Code Style
- **Clear Separation**: Keep MVC layers distinct
- **Type Hints**: Use when helpful for clarity
- **Docstrings**: Document all public methods
- **Comments**: Explain "why" not "what"

### UI/UX Patterns
- **Immediate Feedback**: All actions provide visual response
- **No Hidden State**: User always knows what's happening
- **Consistent Spacing**: Use layouts, not hardcoded positions
- **Theme Consistency**: All custom widgets support both themes

### Data Patterns
- **Auto-save Everything**: User never thinks about saving
- **Preserve State**: Application remembers settings
- **Fail Gracefully**: Never lose user data

### Development Patterns
- **Test on Both Platforms**: Changes must work on Linux and Windows
- **Build Before Release**: Always test standalone executable
- **Document Changes**: Update relevant memory bank files

## Project Insights & Learnings

### What Works Well
1. **PyQt6 Integration**: Signal/slot system is elegant and reliable
2. **SQLite Persistence**: Zero-configuration database perfect for this use case
3. **Timer Implementation**: QTimer provides accurate, low-overhead updates
4. **Theme System**: Simple toggle meets user needs without complexity
5. **Auto-save**: Users love not thinking about saving

### Key Discoveries
1. **URL Detection**: Users often paste issue URLs as card names
2. **Multiple Cards**: Users frequently track 3-5 tasks simultaneously
3. **Theme Preference**: Persistent theme selection is highly valued
4. **One-click Actions**: Minimizing clicks improves user satisfaction
5. **Visual Feedback**: Hover states and button animations matter

### Technical Learnings
1. **QTimer Reliability**: More reliable than Python's threading.Timer
2. **SQLite Row Factory**: Using Row factory simplifies data access
3. **PyInstaller Quirks**: Spec file needed for icon and metadata
4. **Cross-platform Paths**: Always use os.path.join or pathlib
5. **Virtual Environments**: Essential for consistent builds

### User Preferences (Inferred)
- Minimalist UI preferred
- Dark theme is primary choice
- Speed matters more than features
- Reliability is critical
- No configuration desired

## Known Issues & Considerations

### Current Limitations
1. No cloud sync (by design)
2. No export functionality yet
3. No reporting/analytics
4. No keyboard shortcuts
5. No undo functionality

### Future Enhancement Ideas
1. Export time data to CSV
2. Keyboard shortcuts for common actions
3. Statistics/reporting dashboard
4. Card categories or tags
5. Time goal tracking
6. Notification on timer milestones

### Platform-Specific Considerations
- **Linux**: Desktop file integration works well
- **Windows**: EXE builds cleanly with PyInstaller
- **Both**: Font rendering differences acceptable

## Development Environment State

### Current Setup
- Virtual environment with PyQt6 6.6.0+
- Python 3.8+ (tested on 3.10+)
- PyInstaller 6.0.0+ for builds
- All dependencies in requirements.txt

### Build Status
- Build scripts functional for both platforms
- Executable tested and working
- Icon integration successful

### Database State
- Schema stable
- No migrations needed currently
- Data persistence reliable

## Communication Patterns

### With Users
- Keep technical jargon minimal
- Focus on functionality, not implementation
- Provide clear, actionable feedback
- Document workarounds when needed

### In Code
- Self-documenting code preferred
- Comments for complex logic only
- Docstrings for all public APIs
- Clear variable names

## Context for Future Sessions

### Quick Start Reference
- **Main Entry**: `main.py`
- **Controller**: `src/application/controller.py`
- **UI**: `src/ui/main_window.py`
- **Database**: `src/infrastructure/database.py`
- **Models**: `src/domain/models.py`

### Common Tasks
1. **Add Feature**: Start in controller, add UI in main_window, update models/database as needed
2. **Fix Bug**: Identify layer (UI/Controller/Database), isolate issue, fix and test
3. **Update UI**: Modify `main_window.py` and `styles.py`, ensure theme support
4. **Schema Change**: Update `database.py`, add migration logic, test thoroughly

### Key Files to Reference
- `README.md`: User documentation
- `requirements.txt`: Dependencies
- `TimeTracker.spec`: Build configuration
- Memory Bank files: Project context and decisions

## Ready for Next Task
The application is stable and functional. Memory Bank is complete and ready to guide future development. Awaiting user input for next enhancement or fix.
