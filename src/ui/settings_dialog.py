"""
Settings Dialog - Configuration window
"""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QWidget
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtProperty, QRect
from PyQt6.QtGui import QPainter, QColor, QPaintEvent


class ToggleSwitch(QWidget):
    """Widget toggle switch animado (botão on/off)"""
    
    def __init__(self, parent=None, checked=False):
        super().__init__(parent)
        self._checked = checked
        self._circle_position = 24 if checked else 2
        
        # Configurações visuais
        self.setFixedSize(50, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Animação
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.setDuration(200)
    
    @pyqtProperty(int)
    def circle_position(self):
        return self._circle_position
    
    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()
    
    def mousePressEvent(self, event):
        """Handle click event"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle()
    
    def toggle(self):
        """Alterna o estado do switch"""
        self._checked = not self._checked
        
        # Anima a transição
        start_pos = 24 if not self._checked else 2
        end_pos = 2 if not self._checked else 24
        
        self.animation.setStartValue(start_pos)
        self.animation.setEndValue(end_pos)
        self.animation.start()
    
    def setChecked(self, checked):
        """Define o estado sem animação"""
        if self._checked != checked:
            self._checked = checked
            self._circle_position = 24 if checked else 2
            self.update()
    
    def isChecked(self):
        """Retorna o estado atual"""
        return self._checked
    
    def paintEvent(self, event: QPaintEvent):
        """Desenha o switch"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Cores baseadas no tema (detecta cor de fundo)
        if self._checked:
            bg_color = QColor("#000023")
            circle_color = QColor("#6BFF50")
        else:
            bg_color = QColor("#ced4da")
            circle_color = QColor("#ffffff")
        
        # Desenha o fundo (track)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(bg_color)
        painter.drawRoundedRect(0, 0, 50, 28, 14, 14)
        
        # Desenha o círculo (thumb)
        painter.setBrush(circle_color)
        painter.drawEllipse(self._circle_position, 2, 24, 24)


class SettingsDialog(QDialog):
    """Diálogo para configurações da aplicação"""
    
    def __init__(self, parent=None, use_time_difference=False):
        super().__init__(parent)
        self.use_time_difference = use_time_difference
        self.init_ui()
        
        # Aplica o stylesheet do parent (mantém consistência de tema)
        if parent:
            self.setStyleSheet(parent.styleSheet())
    
    def init_ui(self):
        """Inicializa a interface do diálogo"""
        self.setWindowTitle("Settings")
        self.setMinimumSize(730, 450)
        self.setObjectName("settingsDialog")
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Content
        content = self.create_content()
        main_layout.addWidget(content, 1)
        
        # Footer
        footer = self.create_footer()
        main_layout.addWidget(footer)
    
    def create_header(self) -> QWidget:
        """Cria o cabeçalho do diálogo"""
        header = QWidget()
        header.setObjectName("settingsDialogHeader")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(4)
        header.setLayout(layout)
        
        title = QLabel("Settings")
        title.setObjectName("settingsDialogTitle")
        layout.addWidget(title)
        
        subtitle = QLabel("Configure application preferences")
        subtitle.setObjectName("settingsDialogSubtitle")
        layout.addWidget(subtitle)
        
        return header
    
    def create_content(self) -> QWidget:
        """Cria o conteúdo principal do diálogo"""
        content = QWidget()
        content.setObjectName("settingsDialogContent")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)
        content.setLayout(layout)
        
        # Duration Mode Section
        section_label = QLabel("Duration Display Mode")
        section_label.setObjectName("settingsSectionLabel")
        layout.addWidget(section_label)
        
        # Container para a configuração com toggle à esquerda
        setting_container = QWidget()
        setting_layout = QHBoxLayout()
        setting_layout.setSpacing(20)
        setting_layout.setContentsMargins(0, 0, 0, 0)
        setting_container.setLayout(setting_layout)
        
        # Toggle Switch à esquerda
        self.toggle_switch = ToggleSwitch(checked=self.use_time_difference)
        setting_layout.addWidget(self.toggle_switch)
        
        # Descrição à direita
        description_container = QWidget()
        description_layout = QVBoxLayout()
        description_layout.setSpacing(8)
        description_layout.setContentsMargins(0, 0, 0, 0)
        description_container.setLayout(description_layout)
        
        # Título da configuração
        setting_title = QLabel("Calculate as End Time - Start Time")
        setting_title.setObjectName("settingsOptionTitle")
        description_layout.addWidget(setting_title)
        
        # Descrição detalhada
        setting_desc = QLabel(
            "When enabled: Duration shows the time difference between start and end times.\n"
            "When disabled: Duration shows the accumulated time while the task is active (default)."
        )
        setting_desc.setObjectName("settingsHelpText")
        setting_desc.setWordWrap(True)
        description_layout.addWidget(setting_desc)
        
        setting_layout.addWidget(description_container, 1)
        
        layout.addWidget(setting_container)
        layout.addStretch()
        
        return content
    
    def create_footer(self) -> QWidget:
        """Cria o rodapé com botões de ação"""
        footer = QWidget()
        footer.setObjectName("settingsDialogFooter")
        
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)
        footer.setLayout(layout)
        
        layout.addStretch()
        
        # Botão Cancelar
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("settingsCancelButton")
        cancel_btn.clicked.connect(self.reject)
        layout.addWidget(cancel_btn)
        
        # Botão Salvar
        save_btn = QPushButton("Save")
        save_btn.setObjectName("settingsSaveButton")
        save_btn.clicked.connect(self.accept)
        layout.addWidget(save_btn)
        
        return footer
    
    def get_use_time_difference(self) -> bool:
        """Retorna o valor configurado para uso de diferença de tempo"""
        return self.toggle_switch.isChecked()

