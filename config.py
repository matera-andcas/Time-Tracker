"""
Configurações globais da aplicação Time Tracker
"""

# Configurações da aplicação
APP_NAME = "Time Tracker"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Time Tracker Team"

# Configurações da interface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 400

# Configurações de timer
TIMER_INTERVAL_MS = 1000  # Atualização a cada 1 segundo

# Configurações de cores
COLORS = {
    'play': '#4CAF50',      # Verde
    'play_hover': '#45a049',
    'pause': '#f44336',     # Vermelho
    'pause_hover': '#da190b',
    'add': '#2196F3',       # Azul
    'add_hover': '#0b7dda',
    'delete': '#ff9800',    # Laranja
    'delete_hover': '#e68900',
    'primary': '#4CAF50',
    'background': '#f5f5f5',
    'white': '#ffffff',
    'border': '#e0e0e0',
}

# Configurações de fontes
FONTS = {
    'default_size': 13,
    'timer_size': 11,
    'header_size': 13,
}

# Configurações de layout
COLUMN_WIDTHS = {
    'checkbox': 50,
    'card': None,  # Stretch
    'play': 70,
    'pause': 70,
    'time': 100,
    'start_time': 100,
    'end_time': 100,
}

# Placeholders
PLACEHOLDERS = {
    'card_name': '',
}

# Textos da interface
UI_TEXTS = {
    'select_all': 'Select All',
    'delete_button': 'Deletar',
    'add_button': '➕ Adicionar Card',
    'play_button': '▶',
    'pause_button': '⏸',
}
