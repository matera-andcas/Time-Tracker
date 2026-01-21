"""
Main Window - View
"""
from datetime import datetime
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QHeaderView,
    QCheckBox, QAbstractItemView, QApplication, QLabel
)
from PyQt6.QtCore import Qt
from .widgets import CardNameWidget
from .time_widgets import TimeRangeWidget
from .styles import get_light_stylesheet, get_dark_stylesheet


class MainWindow(QMainWindow):
    """Janela principal da aplicação"""
    
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.init_ui()
    
    def init_ui(self):
        """Inicializa a interface do usuário"""
        self.setWindowTitle("Time Tracker")
        self.setMinimumSize(900, 600)
        self.resize(1100, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)
        central_widget.setLayout(main_layout)
        
        # Header section
        header_layout = self.create_header()
        main_layout.addLayout(header_layout)
        
        # Cards table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "", "Task / Card", "Duration", "Time Range", "Controls", ""
        ])
        
        self.table.mousePressEvent = lambda event: self.clear_all_focus()
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table.verticalHeader().setDefaultSectionSize(72)
        self.table.setShowGrid(False)
        
        # Column sizing
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(2, 130)
        self.table.setColumnWidth(3, 180)
        self.table.setColumnWidth(4, 140)
        self.table.setColumnWidth(5, 50)
        
        main_layout.addWidget(self.table, 1)
        
        # Action bar
        action_bar = self.create_action_bar()
        main_layout.addLayout(action_bar)
        
        self.apply_theme()
    
    def create_header(self) -> QHBoxLayout:
        """Cria o cabeçalho da aplicação"""
        header_layout = QHBoxLayout()
        header_layout.setSpacing(16)
        
        # Title and subtitle
        title_container = QVBoxLayout()
        title_container.setSpacing(4)
        
        title_label = QLabel("⏱️ Time Tracker")
        title_label.setObjectName("titleLabel")
        title_container.addWidget(title_label)
        
        subtitle_label = QLabel("Track your tasks and manage time efficiently")
        subtitle_label.setObjectName("subtitleLabel")
        title_container.addWidget(subtitle_label)
        
        header_layout.addLayout(title_container)
        header_layout.addStretch()
        
        # Theme toggle
        self.theme_btn = QPushButton("🌙")
        self.theme_btn.setObjectName("themeToggle")
        self.theme_btn.setFixedSize(40, 40)
        self.theme_btn.setToolTip("Toggle dark mode")
        header_layout.addWidget(self.theme_btn)
        
        return header_layout
    
    def create_action_bar(self) -> QHBoxLayout:
        """Cria a barra de ações"""
        action_layout = QHBoxLayout()
        action_layout.setSpacing(12)
        
        # Left side - bulk actions
        self.select_all_cb = QCheckBox("Select all")
        self.select_all_cb.setObjectName("selectAllCheckbox")
        action_layout.addWidget(self.select_all_cb)
        
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setObjectName("deleteButton")
        action_layout.addWidget(self.delete_btn)
        
        action_layout.addStretch()
        
        # Right side - primary action
        self.add_btn = QPushButton("+ New Task")
        self.add_btn.setObjectName("addButton")
        action_layout.addWidget(self.add_btn)
        
        return action_layout
    
    def set_dark_mode(self, enabled: bool):
        """Define o modo escuro"""
        self.dark_mode = enabled
        self.theme_btn.setText("☀️" if self.dark_mode else "🌙")
        self.theme_btn.setToolTip("Switch to light mode" if self.dark_mode else "Switch to dark mode")
        self.apply_theme()
    
    def apply_theme(self):
        """Aplica o tema atual"""
        if self.dark_mode:
            self.setStyleSheet(get_dark_stylesheet())
        else:
            self.setStyleSheet(get_light_stylesheet())
    
    def clear_all_focus(self):
        """Remove o foco de todos os widgets"""
        focused_widget = QApplication.focusWidget()
        if focused_widget:
            focused_widget.clearFocus()
    
    def refresh_table(self, cards, on_checkbox_changed, on_text_changed, 
                      on_play_clicked, on_pause_clicked, on_time_changed):
        """Atualiza a tabela com os dados dos cards"""
        self.table.setRowCount(len(cards))
        
        for row, card in enumerate(cards):
            # Selection checkbox
            checkbox = QCheckBox()
            checkbox.setChecked(card.is_selected)
            checkbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            checkbox.stateChanged.connect(lambda state, c=card: on_checkbox_changed(c, state))
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout()
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_widget.setLayout(checkbox_layout)
            self.table.setCellWidget(row, 0, checkbox_widget)
            
            # Task name field
            card_widget = CardNameWidget(card, on_text_changed)
            self.table.setCellWidget(row, 1, card_widget)
            self.table.setRowHeight(row, 72)
            
            # Duration display
            duration_widget = self.create_duration_widget(card)
            self.table.setCellWidget(row, 2, duration_widget)
            
            # Time range display with editable fields
            time_range_widget = TimeRangeWidget(card, on_time_changed)
            self.table.setCellWidget(row, 3, time_range_widget)
            
            # Control buttons
            controls_widget = self.create_controls_widget(card, on_play_clicked, on_pause_clicked)
            self.table.setCellWidget(row, 4, controls_widget)
            
            # Status indicator
            status_widget = self.create_status_indicator(card)
            self.table.setCellWidget(row, 5, status_widget)
    
    def create_duration_widget(self, card) -> QWidget:
        """Cria widget para exibir duração"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        widget.setLayout(layout)
        
        time_label = QLabel(card.get_formatted_time())
        time_label.setObjectName("durationLabel")
        time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(time_label)
        
        # Usa a data de criação do card, ou data atual se não existir
        card_date = card.created_date if card.created_date else datetime.now().strftime("%d/%m/%y")
        date_label = QLabel(card_date)
        date_label.setObjectName("dateLabel")
        date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(date_label)
        
        return widget
    
    def create_time_range_widget(self, card) -> QWidget:
        """Cria widget para exibir intervalo de tempo"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        widget.setLayout(layout)
        
        if card.start_time:
            start_label = QLabel(f"Started: {card.start_time}")
            start_label.setObjectName("timeRangeLabel")
            layout.addWidget(start_label)
        
        if card.end_time and not card.is_running:
            end_label = QLabel(f"Ended: {card.end_time}")
            end_label.setObjectName("timeRangeLabel")
            layout.addWidget(end_label)
        elif card.is_running:
            running_label = QLabel("⏱️ In Progress...")
            running_label.setObjectName("runningLabel")
            layout.addWidget(running_label)
        
        return widget
    def create_controls_widget(self, card, on_play_clicked, on_pause_clicked) -> QWidget:
        """Cria widget com botões de controle"""
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(6)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layout)
        
        # Play button
        play_btn = QPushButton("▶")
        play_btn.setObjectName("playButton")
        play_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        play_btn.setEnabled(not card.is_running)
        play_btn.setFixedSize(40, 40)
        play_btn.setToolTip("Start timer")
        play_btn.clicked.connect(lambda: on_play_clicked(card))
        layout.addWidget(play_btn)
        
        # Pause button
        pause_btn = QPushButton("⏸")
        pause_btn.setObjectName("pauseButton")
        pause_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        pause_btn.setEnabled(card.is_running)
        pause_btn.setFixedSize(40, 40)
        pause_btn.setToolTip("Pause timer")
        pause_btn.clicked.connect(lambda: on_pause_clicked(card))
        layout.addWidget(pause_btn)
        
        return widget
        return widget
    
    def create_status_indicator(self, card) -> QWidget:
        """Cria indicador visual de status"""
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layout)
        
        indicator = QLabel()
        indicator.setFixedSize(12, 12)
        indicator.setObjectName("statusIndicatorRunning" if card.is_running else "statusIndicatorIdle")
        layout.addWidget(indicator)
        
        return widget
    
    def update_timer_display(self, cards):
        """Atualiza apenas o display dos timers sem recriar widgets"""
        for row, card in enumerate(cards):
            if row < self.table.rowCount():
                # Update duration display
                duration_widget = self.table.cellWidget(row, 2)
                if duration_widget:
                    time_label = duration_widget.findChild(QLabel, "durationLabel")
                    if time_label:
                        time_label.setText(card.get_formatted_time())
                
                # NÃO recria o time range widget - apenas atualiza se mudou de estado
                time_range_widget = self.table.cellWidget(row, 3)
                if time_range_widget and isinstance(time_range_widget, TimeRangeWidget):
                    # Verifica se o estado mudou (running/paused)
                    children = time_range_widget.findChildren(QLabel, "runningLabel")
                    has_running_label = len(children) > 0
                    
                    needs_recreate = False
                    if has_running_label and not card.is_running:
                        needs_recreate = True
                    elif not has_running_label and card.is_running:
                        needs_recreate = True
                    
                    if needs_recreate:
                        # Só recria se mudou de estado (running <-> paused)
                        new_widget = TimeRangeWidget(card, lambda: None)
                        self.table.setCellWidget(row, 3, new_widget)
                    else:
                        # Apenas atualiza os valores sem recriar
                        time_range_widget.update_times()
                
                # Update control buttons state
                controls_widget = self.table.cellWidget(row, 4)
                if controls_widget:
                    buttons = controls_widget.findChildren(QPushButton)
                    if len(buttons) >= 2:
                        play_btn = buttons[0]
                        pause_btn = buttons[1]
                        play_btn.setEnabled(not card.is_running)
                        pause_btn.setEnabled(card.is_running)
                
                # Update status indicator
                status_widget = self.table.cellWidget(row, 5)
                if status_widget:
                    new_indicator = self.create_status_indicator(card)
                    self.table.setCellWidget(row, 5, new_indicator)
