"""
Notes Dialog - Notepad for tags and descriptions
"""
import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QWidget, QTableWidget, QHeaderView,
    QLineEdit, QAbstractItemView, QMessageBox
)
from PyQt6.QtCore import Qt, QByteArray, QSize
from PyQt6.QtGui import QGuiApplication, QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer


def get_icon_path(filename: str) -> str:
    """Retorna o caminho completo para um arquivo de ícone"""
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
        self.setMinimumSize(730, 500)
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
        # Container principal sem margens para linha ocupar toda largura
        header = QWidget()
        header.setObjectName("notesDialogHeader")
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        header.setLayout(main_layout)
        
        # Widget de conteúdo com margens
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(24, 20, 24, 20)
        content_layout.setSpacing(4)
        content_widget.setLayout(content_layout)
        
        title = QLabel("Notes")
        title.setObjectName("notesDialogTitle")
        content_layout.addWidget(title)
        
        subtitle = QLabel("Gerencie suas tags e descrições")
        subtitle.setObjectName("notesDialogSubtitle")
        content_layout.addWidget(subtitle)
        
        main_layout.addWidget(content_widget)
        
        # Linha verde decorativa no final do header
        green_line = QWidget()
        green_line.setFixedHeight(2)
        green_line.setStyleSheet("background-color: #6BFF50;")
        main_layout.addWidget(green_line)
        
        return header
    
    def create_content(self) -> QWidget:
        """Cria o conteúdo principal do diálogo"""
        content = QWidget()
        content.setObjectName("notesDialogContent")
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        content.setLayout(layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["", "Tag", "Description", ""])
        
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table.verticalHeader().setDefaultSectionSize(74)
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
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 60)
        
        layout.addWidget(self.table)
        
        return content
    
    def create_footer(self) -> QWidget:
        """Cria o rodapé com botões de ação"""
        footer = QWidget()
        footer.setObjectName("notesDialogFooter")
        
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)
        footer.setLayout(layout)
        
        # Botão Add Note
        add_btn = QPushButton("+ Add Note")
        add_btn.setObjectName("notesAddButton")
        add_btn.clicked.connect(self.on_add_note)
        layout.addWidget(add_btn)
        
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
            copy_btn = QPushButton()
            copy_btn.setObjectName("notesCopyButton")
            copy_btn.setFixedSize(40, 40)
            copy_btn.setToolTip("Copy tag")
            copy_icon = create_colored_icon("copy-svgrepo-com.svg", 20)
            copy_btn.setIcon(copy_icon)
            copy_btn.setIconSize(QSize(20, 20))
            copy_btn.clicked.connect(lambda checked, t=note['tag']: self.on_copy_tag(t))
            
            copy_widget = QWidget()
            copy_layout = QHBoxLayout()
            copy_layout.addWidget(copy_btn) 
            copy_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            copy_layout.setContentsMargins(0, 0, 16, 0)
            copy_widget.setLayout(copy_layout)
            self.table.setCellWidget(row, 0, copy_widget)
            
            # Campo Tag
            tag_field = QLineEdit(note['tag'])
            tag_field.setObjectName("notesTagField")
            tag_field.textChanged.connect(lambda text, r=row: self.on_tag_changed(r, text))
            
            tag_widget = QWidget()
            tag_layout = QHBoxLayout()
            tag_layout.addWidget(tag_field)
            #tag_layout.setContentsMargins(0, 3, 0, 3)
            tag_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
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
            #desc_layout.setContentsMargins(6, 6, 6, 6)
            desc_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
            desc_widget.setLayout(desc_layout)
            self.table.setCellWidget(row, 2, desc_widget)
            
            # Botão deletar
            del_btn = QPushButton()
            del_btn.setObjectName("notesDeleteButton")
            del_btn.setFixedSize(40, 40)
            del_btn.setToolTip("Delete note")
            del_icon = create_colored_icon("trash-bin-minimalistic-svgrepo-com.svg", "#dc3545", 20)
            del_btn.setIcon(del_icon)
            del_btn.setIconSize(QSize(20, 20))
            del_btn.clicked.connect(lambda checked, r=row: self.on_delete_note(r))
            
            del_widget = QWidget()
            del_layout = QHBoxLayout()
            del_layout.addWidget(del_btn)
            del_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            del_layout.setContentsMargins(0, 0, 16, 0)
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
            # Confirmação com mesma identidade visual do delete card
            msg = QMessageBox(self)
            msg.setWindowTitle("Delete")
            msg.setText("Are you sure you want to delete this note?")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | 
                QMessageBox.StandardButton.No
            )
            msg.setDefaultButton(QMessageBox.StandardButton.Yes)
            
            # Customiza os botões para seguir o padrão da aplicação
            yes_btn = msg.button(QMessageBox.StandardButton.Yes)
            no_btn = msg.button(QMessageBox.StandardButton.No)
            yes_btn.setText("Excluir")
            no_btn.setText("Cancelar")
            yes_btn.setObjectName("deleteConfirmButton")
            
            # Remover ícones dos botões
            empty_icon = yes_btn.style().standardIcon(yes_btn.style().StandardPixmap.SP_CustomBase)
            yes_btn.setIcon(empty_icon)
            no_btn.setIcon(empty_icon)
            
            # Forçar aplicação do stylesheet
            yes_btn.style().unpolish(yes_btn)
            yes_btn.style().polish(yes_btn)
            
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
