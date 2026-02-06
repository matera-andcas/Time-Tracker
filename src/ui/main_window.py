"""
Main Window - View
"""
import os
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QHeaderView,
    QCheckBox, QAbstractItemView, QApplication, QLabel
)
from PyQt6.QtCore import Qt, QByteArray, QSize, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QCursor
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtSvg import QSvgRenderer
from .widgets import CardNameWidget
from .time_widgets import TimeRangeWidget
from .styles import get_light_stylesheet, get_dark_stylesheet


def get_icon_path(filename: str) -> str:
    """Retorna o caminho completo para um arquivo de ícone"""
    if getattr(sys, 'frozen', False):
        # Rodando como executável PyInstaller
        base_dir = sys._MEIPASS
    else:
        # Rodando como script Python normal
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base_dir, 'icon', filename)


def create_colored_icon(svg_filename: str, color: str = "#000023", size: int = 24) -> QIcon:
    """Cria um QIcon a partir de um arquivo SVG com cor customizada"""
    svg_path = get_icon_path(svg_filename)
    
    try:
        with open(svg_path, 'r') as f:
            svg_content = f.read()
        
        # Substitui a cor do fill no SVG
        svg_content = svg_content.replace('fill="#1C274C"', f'fill="{color}"')
        
        # Cria um QPixmap a partir do SVG modificado
        svg_bytes = QByteArray(svg_content.encode())
        renderer = QSvgRenderer(svg_bytes)
        
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        
        return QIcon(pixmap)
    except Exception as e:
        print(f"Erro ao carregar ícone {svg_filename}: {e}")
        return QIcon()


class CustomCheckBox(QLabel):
    """Checkbox customizado usando ícones SVG"""
    
    stateChanged = pyqtSignal(int)  # Sinal compatível com QCheckBox
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._checked = False
        self.setFixedSize(24, 24)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.update_icon()
    
    def update_icon(self):
        """Atualiza o ícone baseado no estado checked/unchecked"""
        if self._checked:
            icon_path = get_icon_path("checkbox-check-svgrepo-com.svg")
        else:
            icon_path = get_icon_path("checkbox-unchecked-svgrepo-com.svg")
        
        try:
            pixmap = QPixmap(icon_path)
            scaled_pixmap = pixmap.scaled(26, 26, Qt.AspectRatioMode.KeepAspectRatio, 
                                         Qt.TransformationMode.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
        except Exception as e:
            print(f"Erro ao carregar ícone do checkbox: {e}")
    
    def mousePressEvent(self, event):
        """Handler para clique no checkbox"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.setChecked(not self._checked)
        super().mousePressEvent(event)
    
    def setChecked(self, checked: bool):
        """Define o estado do checkbox"""
        if self._checked != checked:
            self._checked = checked
            self.update_icon()
            # Emite sinal compatível com QCheckBox
            self.stateChanged.emit(Qt.CheckState.Checked.value if checked else Qt.CheckState.Unchecked.value)
    
    def isChecked(self) -> bool:
        """Retorna o estado do checkbox"""
        return self._checked
    
    def setFocusPolicy(self, policy):
        """Compatibilidade com QCheckBox"""
        super().setFocusPolicy(policy)
    
    def setObjectName(self, name: str):
        """Compatibilidade com QCheckBox"""
        super().setObjectName(name)
    
    def setToolTip(self, tooltip: str):
        """Compatibilidade com QCheckBox"""
        super().setToolTip(tooltip)


class MainWindow(QMainWindow):
    """Janela principal da aplicação"""
    
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.use_time_difference = False  # Configuração de modo de duração
        self.init_ui()
    
    def init_ui(self):
        """Inicializa a interface do usuário"""
        self.setWindowTitle("Time Tracker")
        self.setMinimumSize(900, 600)
        self.resize(1100, 750)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal sem margens (header ocupará toda largura)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)
        
        # Header section (ocupa toda a largura)
        header_widget = self.create_header()
        main_layout.addWidget(header_widget)
        
        # Container para conteúdo com margens
        content_container = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        content_container.setLayout(content_layout)
        
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
        
        # Cria checkbox "Select All" no header da primeira coluna
        self.select_all_cb = CustomCheckBox()
        self.select_all_cb.setObjectName("selectAllCheckbox")
        self.select_all_cb.setToolTip("Select all tasks")
        self.select_all_cb.setFixedSize(24, 24)  # Define tamanho fixo do checkbox
        self.select_all_cb.setParent(header.viewport())
        self.select_all_cb.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
        
        # Posiciona o checkbox no centro da primeira coluna do header
        self.update_select_all_position()
        
        # Conecta evento de resize para reposicionar o checkbox
        header.sectionResized.connect(lambda: self.update_select_all_position())
        
        content_layout.addWidget(self.table, 1)
        
        # Action bar
        action_bar = self.create_action_bar()
        content_layout.addLayout(action_bar)
        
        # Adiciona o container de conteúdo ao layout principal
        main_layout.addWidget(content_container, 1)
        
        self.apply_theme()
    
    def create_header(self) -> QWidget:
        """Cria o cabeçalho da aplicação"""
        # Container principal do header (sem margens para linha ocupar toda largura)
        header_container = QWidget()
        header_container.setObjectName("mainWindowHeader")
        
        main_header_layout = QVBoxLayout()
        main_header_layout.setContentsMargins(0, 0, 0, 0)
        main_header_layout.setSpacing(0)
        header_container.setLayout(main_header_layout)
        
        # Widget de conteúdo com margens
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 16, 20, 16)
        content_layout.setSpacing(0)
        content_widget.setLayout(content_layout)
        
        # Layout horizontal com conteúdo do header
        header_layout = QHBoxLayout()
        header_layout.setSpacing(16)
        
        # Title and subtitle
        title_container = QVBoxLayout()
        title_container.setSpacing(4)
        
        title_label = QLabel("TIME TRACKER")
        title_label.setObjectName("titleLabel")
        title_container.addWidget(title_label)
        
        subtitle_label = QLabel("Acompanhe suas tarefas e gerencie seu tempo com eficiência")
        subtitle_label.setObjectName("subtitleLabel")
        title_container.addWidget(subtitle_label)
        
        header_layout.addLayout(title_container)
        header_layout.addStretch()
        
        # Notes button
        self.notes_btn = QPushButton()
        self.notes_btn.setObjectName("notesButton")
        self.notes_btn.setFixedSize(40, 40)
        self.notes_btn.setToolTip("Open notes")
        notes_icon = create_colored_icon("document-add-svgrepo-com.svg", "#000023", 24)
        self.notes_btn.setIcon(notes_icon)
        self.notes_btn.setIconSize(QSize(24, 24))
        header_layout.addWidget(self.notes_btn)
        
        # Settings button
        self.settings_btn = QPushButton()
        self.settings_btn.setObjectName("settingsButton")
        self.settings_btn.setFixedSize(40, 40)
        self.settings_btn.setToolTip("Open settings")
        settings_icon = create_colored_icon("settings-svgrepo-com.svg", "#000023", 24)
        self.settings_btn.setIcon(settings_icon)
        self.settings_btn.setIconSize(QSize(24, 24))
        header_layout.addWidget(self.settings_btn)
        
        # Theme toggle
        self.theme_btn = QPushButton()
        self.theme_btn.setObjectName("themeToggle")
        self.theme_btn.setFixedSize(40, 40)
        self.theme_btn.setToolTip("Toggle dark mode")
        moon_icon = create_colored_icon("moon-stars-svgrepo-com.svg", "#000023", 24)
        self.theme_btn.setIcon(moon_icon)
        self.theme_btn.setIconSize(QSize(24, 24))
        header_layout.addWidget(self.theme_btn)
        
        content_layout.addLayout(header_layout)
        main_header_layout.addWidget(content_widget)
        
        # Linha verde decorativa no final do header (ocupa toda a largura)
        green_line = QWidget()
        green_line.setFixedHeight(4)
        green_line.setStyleSheet("background-color: #6BFF50;")
        main_header_layout.addWidget(green_line)
        
        return header_container
    
    def create_action_bar(self) -> QHBoxLayout:
        """Cria a barra de ações"""
        action_layout = QHBoxLayout()
        action_layout.setSpacing(12)
        
        # Left side - bulk actions
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setObjectName("deleteButton")
        action_layout.addWidget(self.delete_btn)
        
        action_layout.addStretch()
        
        # Right side - primary action
        self.add_btn = QPushButton("+ New Task")
        self.add_btn.setObjectName("addButton")
        action_layout.addWidget(self.add_btn)
        
        return action_layout
    
    def update_select_all_position(self):
        """Atualiza a posição do checkbox select_all no header"""
        if hasattr(self, 'select_all_cb') and hasattr(self, 'table'):
            header = self.table.horizontalHeader()
            # Calcula posição central da primeira coluna usando tamanho fixo do checkbox
            checkbox_size = 24
            x = header.sectionViewportPosition(0) + (header.sectionSize(0) - checkbox_size) // 2
            y = (header.height() - checkbox_size) // 2
            self.select_all_cb.move(x, y)
            self.select_all_cb.raise_()  # Garante que o checkbox fique no topo
            self.select_all_cb.show()
    
    def set_dark_mode(self, enabled: bool):
        """Define o modo escuro"""
        self.dark_mode = enabled
        # No dark mode, mostra o sol (para voltar ao light mode)
        # No light mode, mostra a lua (para ir ao dark mode)
        if self.dark_mode:
            sun_icon = create_colored_icon("sun-svgrepo-com.svg", "#7d8590", 24)
            self.theme_btn.setIcon(sun_icon)
        else:
            moon_icon = create_colored_icon("moon-stars-svgrepo-com.svg", "#495057", 24)
            self.theme_btn.setIcon(moon_icon)
        self.theme_btn.setToolTip("Switch to light mode" if self.dark_mode else "Switch to dark mode")
        self.apply_theme()
        
        # Atualiza os outros ícones conforme o tema
        if self.dark_mode:
            notes_icon = create_colored_icon("document-add-svgrepo-com.svg", "#7d8590", 24)
            settings_icon = create_colored_icon("settings-svgrepo-com.svg", "#7d8590", 24)
        else:
            notes_icon = create_colored_icon("document-add-svgrepo-com.svg", "#495057", 24)
            settings_icon = create_colored_icon("settings-svgrepo-com.svg", "#495057", 24)
        
        self.notes_btn.setIcon(notes_icon)
        self.settings_btn.setIcon(settings_icon)
    
    def apply_theme(self):
        """Aplica o tema atual"""
        if self.dark_mode:
            self.setStyleSheet(get_dark_stylesheet())
        else:
            self.setStyleSheet(get_light_stylesheet())
    
    def showEvent(self, event):
        """Evento chamado quando a janela é exibida"""
        super().showEvent(event)
        # Garante que o checkbox select_all seja posicionado corretamente
        self.update_select_all_position()
    
    def clear_all_focus(self):
        """Remove o foco de todos os widgets"""
        focused_widget = QApplication.focusWidget()
        if focused_widget:
            focused_widget.clearFocus()
    
    def refresh_table(self, cards, on_checkbox_changed, on_text_changed, 
                      on_play_clicked, on_pause_clicked, on_time_changed, on_date_changed=None):
        """Atualiza a tabela com os dados dos cards"""
        self.table.setRowCount(len(cards))
        
        for row, card in enumerate(cards):
            # Selection checkbox
            checkbox = CustomCheckBox()
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
            duration_widget = self.create_duration_widget(card, on_date_changed)
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
    
    def create_duration_widget(self, card, on_date_changed=None) -> QWidget:
        """Cria widget para exibir duração"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        widget.setLayout(layout)
        
        # Escolhe o método de formatação baseado na configuração
        if self.use_time_difference:
            time_text = card.get_formatted_time_difference()
        else:
            time_text = card.get_formatted_time()
        
        time_label = QLabel(time_text)
        time_label.setObjectName("durationLabel")
        time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(time_label)
        
        # Importa o widget de data editável
        from .time_widgets import EditableDateWidget
        
        # Usa widget editável para data
        date_widget = EditableDateWidget(card, on_date_changed)
        layout.addWidget(date_widget)
        
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
        play_btn = QPushButton()
        play_btn.setObjectName("playButton")
        play_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        play_btn.setEnabled(not card.is_running)
        play_btn.setFixedSize(40, 40)
        play_btn.setToolTip("Start timer")
        play_icon = create_colored_icon("play-svgrepo-com.svg", "#ffffff", 20)
        play_btn.setIcon(play_icon)
        play_btn.setIconSize(QSize(20, 20))
        play_btn.clicked.connect(lambda: on_play_clicked(card))
        layout.addWidget(play_btn)
        
        # Pause button
        pause_btn = QPushButton()
        pause_btn.setObjectName("pauseButton")
        pause_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        pause_btn.setEnabled(card.is_running)
        pause_btn.setFixedSize(40, 40)
        pause_btn.setToolTip("Pause timer")
        pause_icon = create_colored_icon("pause-svgrepo-com (1).svg", "#000023", 20)
        pause_btn.setIcon(pause_icon)
        pause_btn.setIconSize(QSize(20, 20))
        pause_btn.clicked.connect(lambda: on_pause_clicked(card))
        layout.addWidget(pause_btn)
        
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
                        # Escolhe o método de formatação baseado na configuração
                        if self.use_time_difference:
                            time_text = card.get_formatted_time_difference()
                        else:
                            time_text = card.get_formatted_time()
                        time_label.setText(time_text)
                
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
