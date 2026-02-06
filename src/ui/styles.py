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
        
        /* Main Window Header */
        QWidget#mainWindowHeader {
            background-color: #000023;
            border-radius: 0px;
        }
        
        QLabel#mainWindowHeaderStrip {
            background-color: #6BFF50;
            min-height: 4px;
            max-height: 4px;
        }
        
        /* Header */
        QWidget#mainWindowHeader QLabel#titleLabel {
            font-size: 28px;
            font-weight: 200;
            font-family: 'Orbitron', 'Organetto', 'Impact', 'Anton', sans-serif;
            color: #6BFF50;
            padding: 0;
            letter-spacing: 1.5px;
        }
        
        QWidget#mainWindowHeader QLabel#subtitleLabel {
            font-size: 14px;
            color: #ffffff;
            font-weight: 400;
            opacity: 0.9;
        }
        
        /* Header Icon Buttons */
        QWidget#mainWindowHeader QPushButton#themeToggle,
        QWidget#mainWindowHeader QPushButton#notesButton,
        QWidget#mainWindowHeader QPushButton#settingsButton {
            background-color: transparent;
            border-radius: 20px;
            border: none;
            outline: none;
        }
        
        QWidget#mainWindowHeader QPushButton#themeToggle:hover,
        QWidget#mainWindowHeader QPushButton#notesButton:hover,
        QWidget#mainWindowHeader QPushButton#settingsButton:hover {
            background-color: rgba(107, 255, 80, 0.12);
        }
        
        QWidget#mainWindowHeader QPushButton#themeToggle:pressed,
        QWidget#mainWindowHeader QPushButton#notesButton:pressed,
        QWidget#mainWindowHeader QPushButton#settingsButton:pressed {
            background-color: rgba(107, 255, 80, 0.20);
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
        
        /* Hide scrollbar */
        QTableWidget QScrollBar:vertical {
            width: 0px;
        }
        
        QTableWidget QScrollBar:horizontal {
            height: 0px;
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
            background-color: #000023;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            border: none;
            outline: none;
        }
        
        QPushButton#addButton:hover {
            background-color: #1a2847;
        }
        
        QPushButton#addButton:pressed {
            background-color: #00001a;
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
            outline: none;
        }
        
        QPushButton#deleteButton:hover {
            background-color: #c82333;
        }
        
        QPushButton#deleteButton:pressed {
            background-color: #bd2130;
        }
        
        /* Buttons - Icon Buttons (No Border, Modern) */
        QPushButton#themeToggle,
        QPushButton#notesButton,
        QPushButton#settingsButton {
            background-color: transparent;
            color: #495057;
            border-radius: 20px;
            font-size: 18px;
            border: none;
            outline: none;
        }
        
        QPushButton#themeToggle:hover,
        QPushButton#notesButton:hover,
        QPushButton#settingsButton:hover {
            background-color: #f0f0f0;
            color: #1a1a1a;
        }
        
        QPushButton#themeToggle:pressed,
        QPushButton#notesButton:pressed,
        QPushButton#settingsButton:pressed {
            background-color: #e0e0e0;
        }
        
        /* Buttons - Play (Success) */
        QPushButton#playButton {
            background-color: #28a745;
            color: #ffffff;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            outline: none;
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
            outline: none;
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
            border-color: #000023;
        }
        
        QCheckBox::indicator:checked {
            background-color: #000023;
            border-color: #000023;
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
        
        QLabel#editableDateLabel {
            font-size: 11px;
            color: #6c757d;
            font-weight: 500;
            padding: 4px 8px;
            border-radius: 4px;
            background-color: transparent;
        }
        
        QLabel#editableDateLabel:hover {
            background-color: #f0f0f0;
            color: #495057;
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
        
        /* Time Widgets */
        QLabel#timeFieldLabel {
            font-size: 11px;
            color: #6c757d;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        QLabel#editableTimeValue {
            font-size: 13px;
            color: #007bff;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            background-color: #f0f8ff;
        }
        
        QLabel#editableTimeValue:hover {
            background-color: #e3f2fd;
        }
        
        /* Time Picker Dialog - Modern Design */
        QWidget#timePickerContainer {
            background-color: #ffffff;
            border-radius: 12px;
            border: 1px solid #dee2e6;
        }
        
        QWidget#timePickerHeader {
            background-color: #f8f9fa;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            border-bottom: 1px solid #e9ecef;
        }
        
        QWidget#timePickerFooter {
            background-color: #f8f9fa;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            border-top: 1px solid #e9ecef;
        }
        
        QLabel#timePickerTitle {
            color: #1a1a1a;
        }
        
        QLabel#timePickerSubtitle {
            color: #6c757d;
        }
        
        QLabel#timePickerLabel {
            color: #6c757d;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        QLabel#timePickerSeparator {
            color: #adb5bd;
            padding: 0px 8px;
        }
        
        QSpinBox#timePickerSpinBox {
            background-color: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            padding: 8px 36px 8px 8px;
            color: #1a1a1a;
        }
        
        QSpinBox#timePickerSpinBox:focus {
            border-color: #007bff;
            background-color: #ffffff;
        }
        
        QPushButton#timePickerCustomButton {
            background-color: transparent;
            color: #007bff;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
            outline: none;
        }
        
        QPushButton#timePickerCustomButton:hover {
            background-color: #e7f1ff;
            color: #0056b3;
        }
        
        QPushButton#timePickerCustomButton:pressed {
            background-color: #cce5ff;
        }
        
        QPushButton#timePickerOkButton {
            background-color: #007bff;
            color: #ffffff;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: none;
            outline: none;
        }
        
        QPushButton#timePickerOkButton:hover {
            background-color: #0056b3;
        }
        
        QPushButton#timePickerCancelButton {
            background-color: transparent;
            color: #6c757d;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #dee2e6;
            outline: none;
        }
        
        QPushButton#timePickerCancelButton:hover {
            background-color: #f8f9fa;
            border-color: #adb5bd;
        }
        
        QPushButton#timePickerNowButton {
            background-color: #e7f3ff;
            color: #007bff;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 13px;
            border: 1px solid #cce5ff;
            outline: none;
        }
        
        QPushButton#timePickerNowButton:hover {
            background-color: #cce5ff;
            border-color: #99cfff;
        }
        
        /* Calendar Dialog Container */
        QWidget#calendarDialogContainer {
            background-color: #ffffff;
            border-radius: 16px;
            border: 1px solid #e9ecef;
        }
        
        QLabel#calendarDialogTitle {
            font-size: 20px;
            font-weight: 700;
            color: #1a1a1a;
            padding: 0px;
        }
        
        QLabel#calendarDateDisplay {
            font-size: 14px;
            font-weight: 500;
            color: #007bff;
            padding: 0px;
        }
        
        QLabel#calendarDivider {
            background-color: #e9ecef;
        }
        
        /* Modern Calendar Widget */
        QCalendarWidget#modernCalendar {
            background-color: #ffffff;
            border: none;
        }
        
        QCalendarWidget#modernCalendar QWidget {
            alternate-background-color: #ffffff;
        }
        
        QCalendarWidget#modernCalendar QToolButton {
            color: #1a1a1a;
            background-color: transparent;
            border: none;
            padding: 10px;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            min-width: 36px;
            min-height: 36px;
        }
        
        QCalendarWidget#modernCalendar QToolButton:hover {
            background-color: #f0f8ff;
            color: #007bff;
        }
        
        QCalendarWidget#modernCalendar QToolButton:pressed {
            background-color: #e7f1ff;
        }
        
        QCalendarWidget#modernCalendar QToolButton::menu-indicator {
            image: none;
            width: 0px;
        }
        
        QCalendarWidget#modernCalendar QMenu {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 4px;
        }
        
        QCalendarWidget#modernCalendar QMenu::item {
            padding: 8px 16px;
            border-radius: 6px;
        }
        
        QCalendarWidget#modernCalendar QMenu::item:selected {
            background-color: #f0f8ff;
            color: #007bff;
        }
        
        QCalendarWidget#modernCalendar QSpinBox {
            background-color: transparent;
            border: none;
            padding: 8px 12px;
            color: #1a1a1a;
            font-size: 15px;
            font-weight: 600;
            min-width: 80px;
        }
        
        QCalendarWidget#modernCalendar QSpinBox:focus {
            background-color: #f8f9fa;
            border-radius: 6px;
        }
        
        QCalendarWidget#modernCalendar QSpinBox::up-button,
        QCalendarWidget#modernCalendar QSpinBox::down-button {
            width: 0px;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView {
            background-color: #ffffff;
            selection-background-color: #007bff;
            selection-color: #ffffff;
            border: none;
            outline: none;
            padding: 4px;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView:enabled {
            color: #1a1a1a;
            font-size: 14px;
            font-weight: 500;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView:disabled {
            color: #ced4da;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView::item {
            padding: 8px;
            border-radius: 8px;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView::item:hover {
            background-color: #f0f8ff;
            color: #007bff;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView::item:selected {
            background-color: #007bff;
            color: #ffffff;
            font-weight: 600;
        }
        
        QCalendarWidget#modernCalendar QWidget#qt_calendar_navigationbar {
            background-color: #ffffff;
            border: none;
            padding: 12px 8px;
        }
        
        QCalendarWidget#modernCalendar QHeaderView::section {
            background-color: transparent;
            color: #6c757d;
            padding: 12px 8px;
            border: none;
            font-weight: 700;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Calendar Quick Buttons */
        QPushButton#calendarQuickButton {
            background-color: #f8f9fa;
            color: #495057;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 13px;
            border: none;
            outline: none;
        }
        
        QPushButton#calendarQuickButton:hover {
            background-color: #e9ecef;
            color: #1a1a1a;
        }
        
        QPushButton#calendarCancelButton {
            background-color: transparent;
            color: #6c757d;
            padding: 10px 24px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 14px;
            border: 2px solid #dee2e6;
            outline: none;
        }
        
        QPushButton#calendarCancelButton:hover {
            background-color: #f8f9fa;
            border-color: #adb5bd;
            color: #495057;
        }
        
        QPushButton#calendarOkButton {
            background-color: #007bff;
            color: #ffffff;
            padding: 10px 24px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 14px;
            border: none;
            outline: none;
        }
        
        QPushButton#calendarOkButton:hover {
            background-color: #0056b3;
        }
        
        QPushButton#calendarOkButton:pressed {
            background-color: #004085;
        }
        
        /* Calendar Widget */
        QCalendarWidget#calendarWidget {
            background-color: #ffffff;
            border-radius: 8px;
        }
        
        QCalendarWidget#calendarWidget QToolButton {
            color: #1a1a1a;
            background-color: transparent;
            border: none;
            padding: 8px;
            border-radius: 4px;
            font-size: 14px;
        }
        
        QCalendarWidget#calendarWidget QToolButton:hover {
            background-color: #e9ecef;
        }
        
        QCalendarWidget#calendarWidget QToolButton::menu-indicator {
            image: none;
        }
        
        QCalendarWidget#calendarWidget QMenu {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 6px;
        }
        
        QCalendarWidget#calendarWidget QSpinBox {
            background-color: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 6px;
            padding: 4px 8px;
            color: #1a1a1a;
            font-size: 14px;
            min-width: 80px;
        }
        
        QCalendarWidget#calendarWidget QSpinBox:focus {
            border-color: #007bff;
            background-color: #ffffff;
        }
        
        QCalendarWidget#calendarWidget QAbstractItemView {
            background-color: #ffffff;
            selection-background-color: #007bff;
            selection-color: #ffffff;
            border: none;
            outline: none;
        }
        
        QCalendarWidget#calendarWidget QAbstractItemView:enabled {
            color: #1a1a1a;
            font-size: 13px;
        }
        
        QCalendarWidget#calendarWidget QAbstractItemView:disabled {
            color: #adb5bd;
        }
        
        QCalendarWidget#calendarWidget QWidget#qt_calendar_navigationbar {
            background-color: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
            padding: 8px;
        }
        
        QCalendarWidget#calendarWidget QHeaderView::section {
            background-color: #f8f9fa;
            color: #6c757d;
            padding: 8px;
            border: none;
            font-weight: 600;
            font-size: 12px;
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
        
        /* Botão de confirmação de exclusão (vermelho) */
        QMessageBox QPushButton#deleteConfirmButton {
            background-color: #dc3545;
            color: #ffffff;
            padding: 8px 20px;
            border-radius: 6px;
            font-weight: 600;
            border: none;
            min-width: 80px;
        }
        
        QMessageBox QPushButton#deleteConfirmButton:hover {
            background-color: #c82333;
        }
        
        QMessageBox QPushButton#deleteConfirmButton:pressed {
            background-color: #bd2130;
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
        
        /* Notes Dialog - Modern Design */
        QDialog#notesDialog {
            background-color: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 12px;
        }
        
        QWidget#notesDialogHeader {
            background-color: #000023;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom: 1px solid #000023;
        }
        
        QWidget#notesDialogContent {
            background-color: #f8f9fa;
        }
        
        QWidget#notesDialogFooter {
            background-color: #ffffff;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
            border-top: 1px solid #e9ecef;
        }
        
        QLabel#notesDialogTitle {
            font-size: 24px;
            font-weight: 700;
            color: #6BFF50;
        }
        
        QLabel#notesDialogSubtitle {
            font-size: 13px;
            color: #ffffff;
            font-weight: 400;
        }
        
        /* Notes Table */
        QTableWidget#notesTable {
            background-color: #ffffff;
            border: none;
            border-radius: 8px;
            gridline-color: transparent;
        }
        
        QTableWidget#notesTable::item {
            padding: 8px;
            border-bottom: 1px solid #f0f0f0;
        }
        
        QTableWidget#notesTable QScrollBar:vertical {
            background-color: #f8f9fa;
            width: 10px;
            border-radius: 5px;
            margin: 0px;
        }
        
        QTableWidget#notesTable QScrollBar::handle:vertical {
            background-color: #ced4da;
            border-radius: 5px;
            min-height: 30px;
        }
        
        QTableWidget#notesTable QScrollBar::handle:vertical:hover {
            background-color: #adb5bd;
        }
        
        QTableWidget#notesTable QScrollBar::add-line:vertical,
        QTableWidget#notesTable QScrollBar::sub-line:vertical {
            height: 0px;
        }
        
        QTableWidget#notesTable QScrollBar::add-page:vertical,
        QTableWidget#notesTable QScrollBar::sub-page:vertical {
            background: none;
        }
        
        /* Notes Icon Buttons (Copy and Delete) */
        QPushButton#notesCopyButton,
        QPushButton#notesDeleteButton {
            background-color: transparent;
            border: none;
            border-radius: 20px;
            outline: none;
        }
        
        QPushButton#notesCopyButton:hover {
            background-color: rgba(0, 123, 255, 0.08);
        }
        
        QPushButton#notesCopyButton:pressed {
            background-color: rgba(0, 123, 255, 0.15);
        }
        
        QPushButton#notesDeleteButton:hover {
            background-color: rgba(220, 53, 69, 0.08);
        }
        
        QPushButton#notesDeleteButton:pressed {
            background-color: rgba(220, 53, 69, 0.15);
        }
        
        /* Notes Input Fields */
        QLineEdit#notesTagField,
        QLineEdit#notesDescField {
            padding: 10px 10px;
            min-height: 14px;
            border: 2px solid #e9ecef;
            border-radius: 6px;
            background-color: #ffffff;
            font-size: 14px;
            color: #1a1a1a;
        }
        
        QLineEdit#notesTagField:hover,
        QLineEdit#notesDescField:hover {
            border-color: #dee2e6;
        }
        
        QLineEdit#notesTagField:focus,
        QLineEdit#notesDescField:focus {
            border-color: #007bff;
            background-color: #ffffff;
        }
        
        /* Notes Add Button */
        QPushButton#notesAddButton {
            background-color: #000023;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            border: none;
            outline: none;
        }
        
        QPushButton#notesAddButton:hover {
            background-color: #1a2847;
        }
        
        QPushButton#notesAddButton:pressed {
            background-color: #00001a;
        }
        
        /* Notes Close Button */
        QPushButton#notesCloseButton {
            background-color: transparent;
            color: #6c757d;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #dee2e6;
            outline: none;
        }
        
        QPushButton#notesCloseButton:hover {
            background-color: #f8f9fa;
            border-color: #adb5bd;
        }
        
        QPushButton#notesCloseButton:pressed {
            background-color: #e9ecef;
        }
        
        /* Settings Dialog - Modern Design */
        QDialog#settingsDialog {
            background-color: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 12px;
        }
        
        QWidget#settingsDialogHeader {
            background-color: #000023;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom: 1px solid #000023;
        }
        
        QWidget#settingsDialogContent {
            background-color: #f8f9fa;
        }
        
        QWidget#settingsDialogFooter {
            background-color: #ffffff;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
            border-top: 1px solid #e9ecef;
        }
        
        QLabel#settingsDialogTitle {
            font-size: 24px;
            font-weight: 700;
            color: #6BFF50;
        }
        
        QLabel#settingsDialogSubtitle {
            font-size: 13px;
            color: #ffffff;
            font-weight: 400;
        }
        
        QLabel#settingsSectionLabel {
            font-size: 16px;
            font-weight: 700;
            color: #1a1a1a;
            padding-bottom: 8px;
        }
        
        QLabel#settingsOptionTitle {
            font-size: 15px;
            font-weight: 600;
            color: #1a1a1a;
        }
        
        QLabel#settingsHelpText {
            font-size: 13px;
            color: #6c757d;
            font-weight: 400;
            line-height: 1.5;
        }
        
        QPushButton#settingsCancelButton {
            background-color: transparent;
            color: #6c757d;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #dee2e6;
            outline: none;
        }
        
        QPushButton#settingsCancelButton:hover {
            background-color: #f8f9fa;
            border-color: #adb5bd;
        }
        
        QPushButton#settingsCancelButton:pressed {
            background-color: #e9ecef;
        }
        
        QPushButton#settingsSaveButton {
            background-color: #000023;
            color: #ffffff;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: none;
            outline: none;
        }
        
        QPushButton#settingsSaveButton:hover {
            background-color: #1a2847;
        }
        
        QPushButton#settingsSaveButton:pressed {
            background-color: #00001a;
        }
    """


def get_dark_stylesheet() -> str:
    """Retorna o stylesheet do tema escuro"""
    return """
        /* Main Window */
        QMainWindow {
            background-color: #0d1117;
        }
        
        /* Main Window Header */
        QWidget#mainWindowHeader {
            background-color: #000023;
            border-radius: 0px;
        }
        
        QLabel#mainWindowHeaderStrip {
            background-color: #6BFF50;
            min-height: 4px;
            max-height: 4px;
        }
        
        /* Header */
        QWidget#mainWindowHeader QLabel#titleLabel {
            font-size: 28px;
            font-weight: 200;
            font-family: 'Orbitron', 'Organetto', 'Impact', 'Anton', sans-serif;
            color: #6BFF50;
            padding: 0;
            letter-spacing: 1.5px;
        }
        
        QWidget#mainWindowHeader QLabel#subtitleLabel {
            font-size: 14px;
            color: #ffffff;
            font-weight: 400;
            opacity: 0.9;
        }
        
        /* Header Icon Buttons */
        QWidget#mainWindowHeader QPushButton#themeToggle,
        QWidget#mainWindowHeader QPushButton#notesButton,
        QWidget#mainWindowHeader QPushButton#settingsButton {
            background-color: transparent;
            border-radius: 20px;
            border: none;
            outline: none;
        }
        
        QWidget#mainWindowHeader QPushButton#themeToggle:hover,
        QWidget#mainWindowHeader QPushButton#notesButton:hover,
        QWidget#mainWindowHeader QPushButton#settingsButton:hover {
            background-color: rgba(107, 255, 80, 0.12);
        }
        
        QWidget#mainWindowHeader QPushButton#themeToggle:pressed,
        QWidget#mainWindowHeader QPushButton#notesButton:pressed,
        QWidget#mainWindowHeader QPushButton#settingsButton:pressed {
            background-color: rgba(107, 255, 80, 0.20);
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
        
        /* Hide scrollbar */
        QTableWidget QScrollBar:vertical {
            width: 0px;
        }
        
        QTableWidget QScrollBar:horizontal {
            height: 0px;
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
            background-color: #000023;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            border: none;
            outline: none;
        }
        
        QPushButton#addButton:hover {
            background-color: #1a2847;
        }
        
        QPushButton#addButton:pressed {
            background-color: #00001a;
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
            outline: none;
        }
        
        QPushButton#deleteButton:hover {
            background-color: #f85149;
        }
        
        QPushButton#deleteButton:pressed {
            background-color: #b62324;
        }
        
        /* Buttons - Icon Buttons (No Border, Modern) */
        QPushButton#themeToggle,
        QPushButton#notesButton,
        QPushButton#settingsButton {
            background-color: transparent;
            color: #7d8590;
            border-radius: 20px;
            font-size: 18px;
            border: none;
            outline: none;
        }
        
        QPushButton#themeToggle:hover,
        QPushButton#notesButton:hover,
        QPushButton#settingsButton:hover {
            background-color: #21262d;
            color: #e6edf3;
        }
        
        QPushButton#themeToggle:pressed,
        QPushButton#notesButton:pressed,
        QPushButton#settingsButton:pressed {
            background-color: #30363d;
        }
        
        /* Buttons - Play (Success) */
        QPushButton#playButton {
            background-color: #238636;
            color: #ffffff;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            outline: none;
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
            outline: none;
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
        
        QLabel#editableDateLabel {
            font-size: 11px;
            color: #7d8590;
            font-weight: 500;
            padding: 4px 8px;
            border-radius: 4px;
            background-color: transparent;
        }
        
        QLabel#editableDateLabel:hover {
            background-color: #21262d;
            color: #8b949e;
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
        
        /* Time Widgets */
        QLabel#timeFieldLabel {
            font-size: 11px;
            color: #7d8590;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        QLabel#editableTimeValue {
            font-size: 13px;
            color: #58a6ff;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            background-color: #0d1117;
        }
        
        QLabel#editableTimeValue:hover {
            background-color: #161b22;
        }
        
        /* Time Picker Dialog - Harmonious Dark Design */
        QDialog#timePickerDialog {
            background-color: #0d1117;
        }
        
        QWidget#timePickerContainer {
            background-color: #0d1117;
            border-radius: 12px;
        }
        
        QWidget#timePickerHeader {
            background-color: #0d1117;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
        }
        
        QWidget#timePickerFooter {
            background-color: #0d1117;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
        }
        
        QLabel#timePickerTitle {
            color: #e6edf3;
            font-weight: 700;
        }
        
        QLabel#timePickerSubtitle {
            color: #7d8590;
            font-weight: 500;
        }
        
        QLabel#timePickerLabel {
            color: #8b949e;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }
        
        QLabel#timePickerSeparator {
            color: #58a6ff;
            font-weight: 700;
            padding: 0px 8px;
        }
        
        QSpinBox#timePickerSpinBox {
            background-color: #161b22;
            border: 2px solid #21262d;
            border-radius: 8px;
            padding: 10px 36px 10px 20px;
            color: #e6edf3;
            font-size: 16px;
            font-weight: 600;
        }
        
        QSpinBox#timePickerSpinBox:hover {
            border-color: #30363d;
            background-color: #161b22;
        }
        
        QSpinBox#timePickerSpinBox:focus {
            border-color: #58a6ff;
            background-color: #0d1117;
        }
        
        QPushButton#timePickerCustomButton {
            background-color: transparent;
            color: #58a6ff;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
            outline: none;
        }
        
        QPushButton#timePickerCustomButton:hover {
            background-color: #21262d;
            color: #79c0ff;
        }
        
        QPushButton#timePickerCustomButton:pressed {
            background-color: #30363d;
        }
        
        QPushButton#timePickerOkButton {
            background-color: #238636;
            color: #ffffff;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: none;
            outline: none;
        }
        
        QPushButton#timePickerOkButton:hover {
            background-color: #2ea043;
        }
        
        QPushButton#timePickerOkButton:pressed {
            background-color: #1a7f37;
        }
        
        QPushButton#timePickerCancelButton {
            background-color: transparent;
            color: #8b949e;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #21262d;
            outline: none;
        }
        
        QPushButton#timePickerCancelButton:hover {
            background-color: #161b22;
            border-color: #30363d;
            color: #c9d1d9;
        }
        
        QPushButton#timePickerCancelButton:pressed {
            background-color: #21262d;
        }
        
        QPushButton#timePickerNowButton {
            background-color: #161b22;
            color: #58a6ff;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 13px;
            border: 1px solid #30363d;
            outline: none;
        }
        
        QPushButton#timePickerNowButton:hover {
            background-color: #21262d;
            border-color: #58a6ff;
        }
        
        QPushButton#timePickerNowButton:pressed {
            background-color: #0d1117;
        }
        
        /* Calendar Dialog - Harmonious Dark Design */
        QDialog#dateEditDialog {
            background-color: #0d1117;
        }
        
        QWidget#calendarDialogContainer {
            background-color: #0d1117;
            border-radius: 16px;
        }
        
        QLabel#calendarDialogTitle {
            font-size: 20px;
            font-weight: 700;
            color: #e6edf3;
            padding: 0px;
        }
        
        QLabel#calendarDateDisplay {
            font-size: 14px;
            font-weight: 500;
            color: #58a6ff;
            padding: 0px;
        }
        
        QLabel#calendarDivider {
            background-color: #21262d;
        }
        
        /* Modern Calendar Widget - Harmonious Dark */
        QCalendarWidget#modernCalendar {
            background-color: #0d1117;
            border: none;
        }
        
        QCalendarWidget#modernCalendar QWidget {
            alternate-background-color: #0d1117;
        }
        
        QCalendarWidget#modernCalendar QToolButton {
            color: #e6edf3;
            background-color: transparent;
            border: none;
            padding: 10px;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            min-width: 36px;
            min-height: 36px;
        }
        
        QCalendarWidget#modernCalendar QToolButton:hover {
            background-color: #161b22;
            color: #58a6ff;
        }
        
        QCalendarWidget#modernCalendar QToolButton:pressed {
            background-color: #21262d;
        }
        
        QCalendarWidget#modernCalendar QToolButton::menu-indicator {
            image: none;
            width: 0px;
        }
        
        QCalendarWidget#modernCalendar QMenu {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 4px;
        }
        
        QCalendarWidget#modernCalendar QMenu::item {
            padding: 8px 16px;
            border-radius: 6px;
            color: #e6edf3;
        }
        
        QCalendarWidget#modernCalendar QMenu::item:selected {
            background-color: #21262d;
            color: #58a6ff;
        }
        
        QCalendarWidget#modernCalendar QSpinBox {
            background-color: transparent;
            border: none;
            padding: 8px 12px;
            color: #e6edf3;
            font-size: 15px;
            font-weight: 600;
            min-width: 80px;
        }
        
        QCalendarWidget#modernCalendar QSpinBox:hover {
            background-color: #161b22;
            border-radius: 6px;
        }
        
        QCalendarWidget#modernCalendar QSpinBox:focus {
            background-color: #161b22;
            border: 1px solid #58a6ff;
            border-radius: 6px;
        }
        
        QCalendarWidget#modernCalendar QSpinBox::up-button,
        QCalendarWidget#modernCalendar QSpinBox::down-button {
            width: 0px;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView {
            background-color: #0d1117;
            selection-background-color: #58a6ff;
            selection-color: #ffffff;
            border: none;
            outline: none;
            padding: 4px;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView:enabled {
            color: #e6edf3;
            font-size: 14px;
            font-weight: 500;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView:disabled {
            color: #484f58;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView::item {
            padding: 8px;
            border-radius: 8px;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView::item:hover {
            background-color: #161b22;
            color: #58a6ff;
        }
        
        QCalendarWidget#modernCalendar QAbstractItemView::item:selected {
            background-color: #58a6ff;
            color: #ffffff;
            font-weight: 600;
        }
        
        QCalendarWidget#modernCalendar QWidget#qt_calendar_navigationbar {
            background-color: #0d1117;
            border: none;
            padding: 12px 8px;
        }
        
        QCalendarWidget#modernCalendar QHeaderView::section {
            background-color: transparent;
            color: #8b949e;
            padding: 12px 8px;
            border: none;
            font-weight: 600;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }
        
        /* Calendar Action Buttons - Harmonious Dark */
        QPushButton#calendarQuickButton {
            background-color: #161b22;
            color: #8b949e;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 13px;
            border: none;
            outline: none;
        }
        
        QPushButton#calendarQuickButton:hover {
            background-color: #21262d;
            color: #c9d1d9;
        }
        
        QPushButton#calendarQuickButton:pressed {
            background-color: #30363d;
        }
        
        QPushButton#calendarCancelButton {
            background-color: transparent;
            color: #8b949e;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #21262d;
            outline: none;
        }
        
        QPushButton#calendarCancelButton:hover {
            background-color: #161b22;
            border-color: #30363d;
            color: #c9d1d9;
        }
        
        QPushButton#calendarCancelButton:pressed {
            background-color: #21262d;
        }
        
        QPushButton#calendarOkButton {
            background-color: #238636;
            color: #ffffff;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: none;
            outline: none;
        }
        
        QPushButton#calendarOkButton:hover {
            background-color: #2ea043;
        }
        
        QPushButton#calendarOkButton:pressed {
            background-color: #1a7f37;
        }
        
        /* Calendar Widget */
        QCalendarWidget#calendarWidget {
            background-color: #0d1117;
            border-radius: 8px;
        }
        
        QCalendarWidget#calendarWidget QToolButton {
            color: #e6edf3;
            background-color: transparent;
            border: none;
            padding: 8px;
            border-radius: 4px;
            font-size: 14px;
        }
        
        QCalendarWidget#calendarWidget QToolButton:hover {
            background-color: #21262d;
        }
        
        QCalendarWidget#calendarWidget QToolButton::menu-indicator {
            image: none;
        }
        
        QCalendarWidget#calendarWidget QMenu {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 6px;
        }
        
        QCalendarWidget#calendarWidget QSpinBox {
            background-color: #0d1117;
            border: 2px solid #30363d;
            border-radius: 6px;
            padding: 4px 8px;
            color: #e6edf3;
            font-size: 14px;
            min-width: 80px;
        }
        
        QCalendarWidget#calendarWidget QSpinBox:focus {
            border-color: #58a6ff;
            background-color: #161b22;
        }
        
        QCalendarWidget#calendarWidget QAbstractItemView {
            background-color: #0d1117;
            selection-background-color: #1f6feb;
            selection-color: #ffffff;
            border: none;
            outline: none;
        }
        
        QCalendarWidget#calendarWidget QAbstractItemView:enabled {
            color: #e6edf3;
            font-size: 13px;
        }
        
        QCalendarWidget#calendarWidget QAbstractItemView:disabled {
            color: #484f58;
        }
        
        QCalendarWidget#calendarWidget QWidget#qt_calendar_navigationbar {
            background-color: #0d1117;
            border-bottom: 1px solid #21262d;
            padding: 8px;
        }
        
        QCalendarWidget#calendarWidget QHeaderView::section {
            background-color: #0d1117;
            color: #7d8590;
            padding: 8px;
            border: none;
            font-weight: 600;
            font-size: 12px;
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
            background-color: #238636;
            color: #ffffff;
            border: none;
        }
        
        QMessageBox QPushButton:default:hover {
            background-color: #2ea043;
        }
        
        /* Botão de confirmação de exclusão (vermelho) */
        QMessageBox QPushButton#deleteConfirmButton {
            background-color: #da3633;
            color: #ffffff;
            padding: 8px 20px;
            border-radius: 6px;
            font-weight: 600;
            border: none;
            min-width: 80px;
        }
        
        QMessageBox QPushButton#deleteConfirmButton:hover {
            background-color: #f85149;
        }
        
        QMessageBox QPushButton#deleteConfirmButton:pressed {
            background-color: #b62324;
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
        
        /* Notes Dialog - Dark Theme */
        QDialog#notesDialog {
            background-color: #0d1117;
            border: 2px solid #30363d;
            border-radius: 12px;
        }
        
        QWidget#notesDialogHeader {
            background-color: #000023;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom: 1px solid #000023;
        }
        
        QWidget#notesDialogContent {
            background-color: #0d1117;
        }
        
        QWidget#notesDialogFooter {
            background-color: #161b22;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
            border-top: 1px solid #21262d;
        }
        
        QLabel#notesDialogTitle {
            font-size: 24px;
            font-weight: 700;
            color: #6BFF50;
        }
        
        QLabel#notesDialogSubtitle {
            font-size: 13px;
            color: #ffffff;
            font-weight: 400;
        }
        
        /* Notes Table - Dark Theme */
        QTableWidget#notesTable {
            background-color: #161b22;
            border: none;
            border-radius: 8px;
            gridline-color: transparent;
        }
        
        QTableWidget#notesTable::item {
            padding: 8px;
            border-bottom: 1px solid #21262d;
        }
        
        QTableWidget#notesTable QScrollBar:vertical {
            background-color: #0d1117;
            width: 10px;
            border-radius: 5px;
            margin: 0px;
        }
        
        QTableWidget#notesTable QScrollBar::handle:vertical {
            background-color: #30363d;
            border-radius: 5px;
            min-height: 30px;
        }
        
        QTableWidget#notesTable QScrollBar::handle:vertical:hover {
            background-color: #484f58;
        }
        
        QTableWidget#notesTable QScrollBar::add-line:vertical,
        QTableWidget#notesTable QScrollBar::sub-line:vertical {
            height: 0px;
        }
        
        QTableWidget#notesTable QScrollBar::add-page:vertical,
        QTableWidget#notesTable QScrollBar::sub-page:vertical {
            background: none;
        }
        
        /* Notes Icon Buttons (Copy and Delete) - Dark */
        QPushButton#notesCopyButton,
        QPushButton#notesDeleteButton {
            background-color: transparent;
            border: none;
            border-radius: 20px;
            outline: none;
        }
        
        QPushButton#notesCopyButton:hover {
            background-color: rgba(88, 166, 255, 0.1);
        }
        
        QPushButton#notesCopyButton:pressed {
            background-color: rgba(88, 166, 255, 0.18);
        }
        
        QPushButton#notesDeleteButton:hover {
            background-color: rgba(248, 81, 73, 0.1);
        }
        
        QPushButton#notesDeleteButton:pressed {
            background-color: rgba(248, 81, 73, 0.18);
        }
        
        /* Notes Input Fields - Dark */
        QLineEdit#notesTagField,
        QLineEdit#notesDescField {
            padding: 10px 10px;
            min-height: 14px;
            border: 2px solid #30363d;
            border-radius: 6px;
            background-color: #0d1117;
            font-size: 14px;
            color: #e6edf3;
        }
        
        QLineEdit#notesTagField:hover,
        QLineEdit#notesDescField:hover {
            border-color: #484f58;
        }
        
        QLineEdit#notesTagField:focus,
        QLineEdit#notesDescField:focus {
            border-color: #58a6ff;
            background-color: #0d1117;
        }
        
        /* Notes Add Button - Dark */
        QPushButton#notesAddButton {
            background-color: #000023;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            border: none;
            outline: none;
        }
        
        QPushButton#notesAddButton:hover {
            background-color: #1a2847;
        }
        
        QPushButton#notesAddButton:pressed {
            background-color: #00001a;
        }
        
        /* Notes Close Button - Dark */
        QPushButton#notesCloseButton {
            background-color: transparent;
            color: #8b949e;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #21262d;
            outline: none;
        }
        
        QPushButton#notesCloseButton:hover {
            background-color: #161b22;
            border-color: #30363d;
            color: #c9d1d9;
        }
        
        QPushButton#notesCloseButton:pressed {
            background-color: #21262d;
        }
        
        /* Settings Dialog - Dark Theme */
        QDialog#settingsDialog {
            background-color: #0d1117;
            border: 2px solid #30363d;
            border-radius: 12px;
        }
        
        QWidget#settingsDialogHeader {
            background-color: #000023;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom: 1px solid #000023;
        }
        
        QWidget#settingsDialogContent {
            background-color: #0d1117;
        }
        
        QWidget#settingsDialogFooter {
            background-color: #161b22;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
            border-top: 1px solid #21262d;
        }
        
        QLabel#settingsDialogTitle {
            font-size: 24px;
            font-weight: 700;
            color: #6BFF50;
        }
        
        QLabel#settingsDialogSubtitle {
            font-size: 13px;
            color: #ffffff;
            font-weight: 400;
        }
        
        QLabel#settingsSectionLabel {
            font-size: 16px;
            font-weight: 700;
            color: #e6edf3;
            padding-bottom: 8px;
        }
        
        QLabel#settingsOptionTitle {
            font-size: 15px;
            font-weight: 600;
            color: #e6edf3;
        }
        
        QLabel#settingsHelpText {
            font-size: 13px;
            color: #8b949e;
            font-weight: 400;
            line-height: 1.5;
        }
        
        QPushButton#settingsCancelButton {
            background-color: transparent;
            color: #8b949e;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #21262d;
            outline: none;
        }
        
        QPushButton#settingsCancelButton:hover {
            background-color: #161b22;
            border-color: #30363d;
            color: #c9d1d9;
        }
        
        QPushButton#settingsCancelButton:pressed {
            background-color: #21262d;
        }
        
        QPushButton#settingsSaveButton {
            background-color: #000023;
            color: #ffffff;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: none;
            outline: none;
        }
        
        QPushButton#settingsSaveButton:hover {
            background-color: #1a2847;
        }
        
        QPushButton#settingsSaveButton:pressed {
            background-color: #00001a;
        }
    """
