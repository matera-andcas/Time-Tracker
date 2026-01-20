"""
UI Styles - Modern Light and Dark themes with semantic colors
"""


def get_light_stylesheet() -> str:
    """Retorna o stylesheet do tema claro"""
    return """
        /* Main Window */
        QMainWindow {
            background-color: #f8f9fa;
        }
        
        /* Header */
        QLabel#titleLabel {
            font-size: 28px;
            font-weight: 700;
            color: #1a1a1a;
            padding: 0;
        }
        
        QLabel#subtitleLabel {
            font-size: 14px;
            color: #6c757d;
            font-weight: 400;
        }
        
        /* Table */
        QTableWidget {
            background-color: #ffffff;
            border: none;
            border-radius: 12px;
            gridline-color: transparent;
            font-size: 14px;
            color: #1a1a1a;
            padding: 8px;
        }
        
        QTableWidget::item {
            padding: 12px;
            border-bottom: 1px solid #f0f0f0;
        }
        
        QHeaderView::section {
            background-color: #ffffff;
            padding: 14px 12px;
            border: none;
            border-bottom: 2px solid #e9ecef;
            font-weight: 600;
            font-size: 13px;
            color: #495057;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Input Fields */
        QLineEdit {
            padding: 8px 10px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            background-color: #ffffff;
            font-size: 14px;
            color: #1a1a1a;
            selection-background-color: #007bff;
            min-height: 20px;
        }
        
        QLineEdit:hover {
            border-color: #dee2e6;
        }
        
        QLineEdit:focus {
            border-color: #007bff;
            background-color: #ffffff;
            outline: none;
        }
        
        /* Buttons - Primary Action */
        QPushButton#addButton {
            background-color: #007bff;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            border: none;
        }
        
        QPushButton#addButton:hover {
            background-color: #0056b3;
        }
        
        QPushButton#addButton:pressed {
            background-color: #004085;
        }
        
        /* Buttons - Danger */
        QPushButton#deleteButton {
            background-color: #dc3545;
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            border: none;
        }
        
        QPushButton#deleteButton:hover {
            background-color: #c82333;
        }
        
        QPushButton#deleteButton:pressed {
            background-color: #bd2130;
        }
        
        /* Buttons - Theme Toggle */
        QPushButton#themeToggle {
            background-color: #6c757d;
            color: #ffffff;
            border-radius: 20px;
            font-size: 20px;
            border: none;
        }
        
        QPushButton#themeToggle:hover {
            background-color: #5a6268;
        }
        
        /* Buttons - Play (Success) */
        QPushButton#playButton {
            background-color: #28a745;
            color: #ffffff;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }
        
        QPushButton#playButton:hover:enabled {
            background-color: #218838;
        }
        
        QPushButton#playButton:pressed:enabled {
            background-color: #1e7e34;
        }
        
        QPushButton#playButton:disabled {
            background-color: #e9ecef;
            color: #adb5bd;
        }
        
        /* Buttons - Pause (Warning) */
        QPushButton#pauseButton {
            background-color: #ffc107;
            color: #1a1a1a;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }
        
        QPushButton#pauseButton:hover:enabled {
            background-color: #e0a800;
        }
        
        QPushButton#pauseButton:pressed:enabled {
            background-color: #d39e00;
        }
        
        QPushButton#pauseButton:disabled {
            background-color: #e9ecef;
            color: #adb5bd;
        }
        
        /* Checkboxes */
        QCheckBox {
            font-size: 14px;
            spacing: 8px;
            color: #1a1a1a;
            font-weight: 500;
        }
        
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 4px;
            border: 2px solid #ced4da;
            background-color: #ffffff;
        }
        
        QCheckBox::indicator:hover {
            border-color: #007bff;
        }
        
        QCheckBox::indicator:checked {
            background-color: #007bff;
            border-color: #007bff;
            image: url(none);
        }
        
        QCheckBox#selectAllCheckbox {
            font-weight: 500;
        }
        
        /* Labels */
        QLabel#durationLabel {
            font-size: 16px;
            font-weight: 700;
            color: #1a1a1a;
            font-family: 'Consolas', 'Monaco', monospace;
            padding: 2px 0px;
        }
        
        QLabel#dateLabel {
            font-size: 11px;
            color: #6c757d;
            font-weight: 500;
            padding: 2px 0px;
        }
        
        QLabel#timeRangeLabel {
            font-size: 12px;
            color: #495057;
            font-weight: 500;
            padding: 1px 0px;
        }
        
        QLabel#runningLabel {
            font-size: 12px;
            color: #28a745;
            font-weight: 600;
            padding: 1px 0px;
        }
        
        /* Status Indicators */
        QLabel#statusIndicatorRunning {
            background-color: #28a745;
            border-radius: 6px;
        }
        
        QLabel#statusIndicatorIdle {
            background-color: #ced4da;
            border-radius: 6px;
        }
        
        /* Message Box */
        QMessageBox {
            background-color: #ffffff;
        }
        
        QMessageBox QLabel {
            color: #1a1a1a;
            font-size: 14px;
        }
        
        QMessageBox QPushButton {
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
            min-width: 80px;
        }
        
        QMessageBox QPushButton:default {
            background-color: #007bff;
            color: #ffffff;
            border: none;
        }
        
        QMessageBox QPushButton:default:hover {
            background-color: #0056b3;
        }
        
        QMessageBox QPushButton:!default {
            background-color: #f8f9fa;
            color: #1a1a1a;
            border: 1px solid #dee2e6;
        }
        
        QMessageBox QPushButton:!default:hover {
            background-color: #e9ecef;
            border-color: #ced4da;
        }
    """


def get_dark_stylesheet() -> str:
    """Retorna o stylesheet do tema escuro"""
    return """
        /* Main Window */
        QMainWindow {
            background-color: #0d1117;
        }
        
        /* Header */
        QLabel#titleLabel {
            font-size: 28px;
            font-weight: 700;
            color: #e6edf3;
            padding: 0;
        }
        
        QLabel#subtitleLabel {
            font-size: 14px;
            color: #7d8590;
            font-weight: 400;
        }
        
        /* Table */
        QTableWidget {
            background-color: #161b22;
            border: none;
            border-radius: 12px;
            gridline-color: transparent;
            font-size: 14px;
            color: #e6edf3;
            padding: 8px;
        }
        
        QTableWidget::item {
            padding: 12px;
            border-bottom: 1px solid #21262d;
        }
        
        QHeaderView::section {
            background-color: #161b22;
            padding: 14px 12px;
            border: none;
            border-bottom: 2px solid #21262d;
            font-weight: 600;
            font-size: 13px;
            color: #7d8590;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Input Fields */
        QLineEdit {
            padding: 8px 10px;
            border: 2px solid #30363d;
            border-radius: 8px;
            background-color: #0d1117;
            font-size: 14px;
            color: #e6edf3;
            selection-background-color: #1f6feb;
            min-height: 20px;
        }
        
        QLineEdit:hover {
            border-color: #484f58;
        }
        
        QLineEdit:focus {
            border-color: #1f6feb;
            background-color: #0d1117;
            outline: none;
        }
        
        /* Buttons - Primary Action */
        QPushButton#addButton {
            background-color: #238636;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            border: none;
        }
        
        QPushButton#addButton:hover {
            background-color: #2ea043;
        }
        
        QPushButton#addButton:pressed {
            background-color: #196c2e;
        }
        
        /* Buttons - Danger */
        QPushButton#deleteButton {
            background-color: #da3633;
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            border: none;
        }
        
        QPushButton#deleteButton:hover {
            background-color: #f85149;
        }
        
        QPushButton#deleteButton:pressed {
            background-color: #b62324;
        }
        
        /* Buttons - Theme Toggle */
        QPushButton#themeToggle {
            background-color: #21262d;
            color: #e6edf3;
            border-radius: 20px;
            font-size: 20px;
            border: 1px solid #30363d;
        }
        
        QPushButton#themeToggle:hover {
            background-color: #30363d;
            border-color: #484f58;
        }
        
        /* Buttons - Play (Success) */
        QPushButton#playButton {
            background-color: #238636;
            color: #ffffff;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }
        
        QPushButton#playButton:hover:enabled {
            background-color: #2ea043;
        }
        
        QPushButton#playButton:pressed:enabled {
            background-color: #196c2e;
        }
        
        QPushButton#playButton:disabled {
            background-color: #21262d;
            color: #484f58;
        }
        
        /* Buttons - Pause (Warning) */
        QPushButton#pauseButton {
            background-color: #f0883e;
            color: #0d1117;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }
        
        QPushButton#pauseButton:hover:enabled {
            background-color: #f69d62;
        }
        
        QPushButton#pauseButton:pressed:enabled {
            background-color: #d67d32;
        }
        
        QPushButton#pauseButton:disabled {
            background-color: #21262d;
            color: #484f58;
        }
        
        /* Checkboxes */
        QCheckBox {
            font-size: 14px;
            spacing: 8px;
            color: #e6edf3;
            font-weight: 500;
        }
        
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 4px;
            border: 2px solid #30363d;
            background-color: #0d1117;
        }
        
        QCheckBox::indicator:hover {
            border-color: #1f6feb;
        }
        
        QCheckBox::indicator:checked {
            background-color: #1f6feb;
            border-color: #1f6feb;
            image: url(none);
        }
        
        QCheckBox#selectAllCheckbox {
            font-weight: 500;
        }
        
        /* Labels */
        QLabel#durationLabel {
            font-size: 16px;
            font-weight: 700;
            color: #e6edf3;
            font-family: 'Consolas', 'Monaco', monospace;
            padding: 2px 0px;
        }
        
        QLabel#dateLabel {
            font-size: 11px;
            color: #7d8590;
            font-weight: 500;
            padding: 2px 0px;
        }
        
        QLabel#timeRangeLabel {
            font-size: 12px;
            color: #8b949e;
            font-weight: 500;
            padding: 1px 0px;
        }
        
        QLabel#runningLabel {
            font-size: 12px;
            color: #3fb950;
            font-weight: 600;
            padding: 1px 0px;
        }
        
        /* Status Indicators */
        QLabel#statusIndicatorRunning {
            background-color: #3fb950;
            border-radius: 6px;
        }
        
        QLabel#statusIndicatorIdle {
            background-color: #30363d;
            border-radius: 6px;
        }
        
        /* Message Box */
        QMessageBox {
            background-color: #161b22;
        }
        
        QMessageBox QLabel {
            color: #e6edf3;
            font-size: 14px;
        }
        
        QMessageBox QPushButton {
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
            min-width: 80px;
        }
        
        QMessageBox QPushButton:default {
            background-color: #da3633;
            color: #ffffff;
            border: none;
        }
        
        QMessageBox QPushButton:default:hover {
            background-color: #f85149;
        }
        
        QMessageBox QPushButton:!default {
            background-color: #21262d;
            color: #e6edf3;
            border: 1px solid #30363d;
        }
        
        QMessageBox QPushButton:!default:hover {
            background-color: #30363d;
            border-color: #484f58;
        }
    """
