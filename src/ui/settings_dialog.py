"""
Settings Dialog - Configuration window
"""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QCheckBox, QWidget
)
from PyQt6.QtCore import Qt


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
        self.setFixedSize(500, 300)
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
        
        title = QLabel("⚙️ Settings")
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
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(16)
        content.setLayout(layout)
        
        # Duration Mode Section
        section_label = QLabel("Duration Display")
        section_label.setObjectName("settingsSectionLabel")
        layout.addWidget(section_label)
        
        # Checkbox para modo de duração
        self.time_diff_checkbox = QCheckBox("Calculate duration as End Time - Start Time")
        self.time_diff_checkbox.setObjectName("settingsCheckbox")
        self.time_diff_checkbox.setChecked(self.use_time_difference)
        layout.addWidget(self.time_diff_checkbox)
        
        # Descrição
        help_text = QLabel(
            "When enabled: Duration shows the time difference between start and end times.\n"
            "When disabled: Duration shows the accumulated active time (default behavior)."
        )
        help_text.setObjectName("settingsHelpText")
        help_text.setWordWrap(True)
        layout.addWidget(help_text)
        
        layout.addStretch()
        
        return content
    
    def create_footer(self) -> QWidget:
        """Cria o rodapé com botões de ação"""
        footer = QWidget()
        footer.setObjectName("settingsDialogFooter")
        
        layout = QHBoxLayout()
        layout.setContentsMargins(24, 16, 24, 16)
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
        return self.time_diff_checkbox.isChecked()
