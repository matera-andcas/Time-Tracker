"""
Notes Dialog - Notepad for tags and descriptions
"""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QWidget, QTableWidget, QHeaderView,
    QLineEdit, QAbstractItemView, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication


class NotesDialog(QDialog):
    """Diálogo para gerenciar bloco de notas"""
    
    def __init__(self, parent=None, notes=None):
        super().__init__(parent)
        self.notes = notes if notes else []
        self.init_ui()
        
        # Aplica o stylesheet do parent (mantém consistência de tema)
        if parent:
            self.setStyleSheet(parent.styleSheet())
        
        self.populate_table()
    
    def init_ui(self):
        """Inicializa a interface do diálogo"""
        self.setWindowTitle("Notes")
        self.setMinimumSize(700, 500)
        self.setObjectName("notesDialog")
        
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
        header.setObjectName("notesDialogHeader")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(4)
        header.setLayout(layout)
        
        title = QLabel("📝 Notes")
        title.setObjectName("notesDialogTitle")
        layout.addWidget(title)
        
        subtitle = QLabel("Manage your tags and descriptions")
        subtitle.setObjectName("notesDialogSubtitle")
        layout.addWidget(subtitle)
        
        return header
    
    def create_content(self) -> QWidget:
        """Cria o conteúdo principal do diálogo"""
        content = QWidget()
        content.setObjectName("notesDialogContent")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(16)
        content.setLayout(layout)
        
        # Action bar (botão Add)
        action_bar = QHBoxLayout()
        action_bar.setSpacing(12)
        
        action_bar.addStretch()
        
        add_btn = QPushButton("+ Add Note")
        add_btn.setObjectName("notesAddButton")
        add_btn.clicked.connect(self.on_add_note)
        action_bar.addWidget(add_btn)
        
        layout.addLayout(action_bar)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "", "Tag", "Description", ""
        ])
        
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table.verticalHeader().setDefaultSectionSize(64)
        self.table.setShowGrid(False)
        self.table.setObjectName("notesTable")
        
        # Column sizing
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        
        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(3, 60)
        
        layout.addWidget(self.table)
        
        return content
    
    def create_footer(self) -> QWidget:
        """Cria o rodapé com botões de ação"""
        footer = QWidget()
        footer.setObjectName("notesDialogFooter")
        
        layout = QHBoxLayout()
        layout.setContentsMargins(24, 16, 24, 16)
        layout.setSpacing(12)
        footer.setLayout(layout)
        
        layout.addStretch()
        
        # Botão Close
        close_btn = QPushButton("Close")
        close_btn.setObjectName("notesCloseButton")
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)
        
        return footer
    
    def populate_table(self):
        """Popula a tabela com as notas"""
        self.table.setRowCount(len(self.notes))
        
        for row, note in enumerate(self.notes):
            # Botão copiar
            copy_btn = QPushButton("📋")
            copy_btn.setObjectName("notesCopyButton")
            copy_btn.setFixedSize(40, 40)
            copy_btn.setToolTip("Copy tag")
            copy_btn.clicked.connect(lambda checked, t=note['tag']: self.on_copy_tag(t))
            
            copy_widget = QWidget()
            copy_layout = QHBoxLayout()
            copy_layout.addWidget(copy_btn)
            copy_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            copy_layout.setContentsMargins(0, 0, 0, 0)
            copy_widget.setLayout(copy_layout)
            self.table.setCellWidget(row, 0, copy_widget)
            
            # Campo Tag
            tag_field = QLineEdit(note['tag'])
            tag_field.setObjectName("notesTagField")
            tag_field.setPlaceholderText("e.g., EMP-1333")
            tag_field.textChanged.connect(lambda text, r=row: self.on_tag_changed(r, text))
            
            tag_widget = QWidget()
            tag_layout = QHBoxLayout()
            tag_layout.addWidget(tag_field)
            tag_layout.setContentsMargins(8, 4, 8, 4)
            tag_widget.setLayout(tag_layout)
            self.table.setCellWidget(row, 1, tag_widget)
            
            # Campo Description
            desc_field = QLineEdit(note['description'])
            desc_field.setObjectName("notesDescField")
            desc_field.setPlaceholderText("e.g., Card for meeting hours")
            desc_field.textChanged.connect(lambda text, r=row: self.on_desc_changed(r, text))
            
            desc_widget = QWidget()
            desc_layout = QHBoxLayout()
            desc_layout.addWidget(desc_field)
            desc_layout.setContentsMargins(8, 4, 8, 4)
            desc_widget.setLayout(desc_layout)
            self.table.setCellWidget(row, 2, desc_widget)
            
            # Botão deletar
            del_btn = QPushButton("🗑️")
            del_btn.setObjectName("notesDeleteButton")
            del_btn.setFixedSize(40, 40)
            del_btn.setToolTip("Delete note")
            del_btn.clicked.connect(lambda checked, r=row: self.on_delete_note(r))
            
            del_widget = QWidget()
            del_layout = QHBoxLayout()
            del_layout.addWidget(del_btn)
            del_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            del_layout.setContentsMargins(0, 0, 0, 0)
            del_widget.setLayout(del_layout)
            self.table.setCellWidget(row, 3, del_widget)
    
    def on_add_note(self):
        """Adiciona uma nova nota"""
        new_note = {
            'tag': '',
            'description': ''
        }
        self.notes.append(new_note)
        self.populate_table()
    
    def on_delete_note(self, row: int):
        """Deleta uma nota"""
        if 0 <= row < len(self.notes):
            # Confirmação
            msg = QMessageBox(self)
            msg.setWindowTitle("Delete Note")
            msg.setText("Are you sure you want to delete this note?")
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | 
                QMessageBox.StandardButton.No
            )
            msg.setDefaultButton(QMessageBox.StandardButton.No)
            
            if msg.exec() == QMessageBox.StandardButton.Yes:
                self.notes.pop(row)
                self.populate_table()
    
    def on_copy_tag(self, tag: str):
        """Copia a tag para o clipboard"""
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(tag)
    
    def on_tag_changed(self, row: int, text: str):
        """Handler para mudança no campo tag"""
        if 0 <= row < len(self.notes):
            self.notes[row]['tag'] = text
    
    def on_desc_changed(self, row: int, text: str):
        """Handler para mudança no campo descrição"""
        if 0 <= row < len(self.notes):
            self.notes[row]['description'] = text
    
    def get_notes(self) -> list:
        """Retorna a lista de notas"""
        return self.notes
