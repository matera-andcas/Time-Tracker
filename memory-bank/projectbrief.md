# Project Brief: Time Tracker

## Project Overview
Time Tracker is a lightweight, cross-platform desktop application for tracking time spent on multiple cards/tasks simultaneously. Built with Python and PyQt6, it provides a modern, fast, and intuitive interface for developers to manage time across different issues, tickets, or projects.

## Core Goals
1. **Lightweight & Fast**: Native desktop application with minimal resource usage
2. **Multi-card Management**: Track multiple tasks simultaneously with independent timers
3. **Cross-platform**: Support for both Linux and Windows environments
4. **Automatic Persistence**: All data automatically saved to SQLite database
5. **User-friendly**: Simple, intuitive interface with dark/light theme support

## Key Requirements

### Functional Requirements
- Add cards with custom names or URLs
- Independent Play/Pause controls for each card
- Precise timer display (HH:MM:SS format)
- Automatic start/end time recording
- Bulk selection and deletion
- Card name editing
- URL detection and clickable links
- Dark/Light theme toggle with preference persistence
- Automatic date assignment for each card

### Technical Requirements
- Python 3.8+
- PyQt6 6.6.0+ for UI
- SQLite for data persistence
- Cross-platform compatibility (Linux/Windows)
- Auto-save functionality (every 5 seconds)
- Distributable as standalone executable

## Project Scope
- **In Scope**: Desktop time tracking, SQLite persistence, basic CRUD operations, theme support
- **Out of Scope**: Web version, mobile apps, team collaboration features, cloud sync

## Target Users
Developers, freelancers, and professionals who need to track time across multiple tasks or projects simultaneously.

## Success Criteria
- Application runs smoothly on Linux and Windows
- Timers are accurate and reliable
- Data persists across sessions
- Interface is responsive and intuitive
- Executable builds successfully for distribution

## Project Constraints
- Must use Python and PyQt6
- Must be lightweight (minimal dependencies)
- Must support offline operation
- Must not require external services
