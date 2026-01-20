"""
Configuration settings
"""

# Application settings
APP_NAME = "Time Tracker"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Time Tracker Team"

# Window settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 400

# Timer settings
TIMER_INTERVAL_MS = 1000
AUTOSAVE_INTERVAL_MS = 5000

# Colors
COLORS = {
    'play': '#4CAF50',
    'play_hover': '#45a049',
    'pause': '#f44336',
    'pause_hover': '#da190b',
    'add': '#2196F3',
    'add_hover': '#0b7dda',
    'delete': '#ff9800',
    'delete_hover': '#e68900',
    'primary': '#4CAF50',
    'background': '#f5f5f5',
    'white': '#ffffff',
    'border': '#e0e0e0',
}

# Fonts
FONTS = {
    'default_size': 13,
    'timer_size': 11,
    'header_size': 13,
}

# Column widths
COLUMN_WIDTHS = {
    'checkbox': 50,
    'card': None,
    'play': 70,
    'pause': 70,
    'time': 100,
    'start_time': 100,
    'end_time': 100,
}

# Database
DATABASE_NAME = "timetracker.db"
