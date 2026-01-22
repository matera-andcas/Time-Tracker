"""
Custom UI Widgets - Improved interaction patterns and accessibility
"""
import re
import webbrowser
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor


class CardNameWidget(QWidget):
    """Widget inteligente que alterna entre link e campo editável"""
    
    text_changed = pyqtSignal()
    
    def __init__(self, card, on_text_changed_callback):
        super().__init__()
        self.card = card
        self.on_text_changed_callback = on_text_changed_callback
        
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(8, 4, 8, 4)
        self.setLayout(self.layout)
        
        self.line_edit = None
        self.label = None
        
        self.refresh_widget()
    
    def is_url(self, text: str) -> bool:
        """Verifica se o texto é uma URL válida"""
        if not text:
            return False
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        return bool(url_pattern.match(text.strip()))
    
    def refresh_widget(self):
        """Atualiza o widget baseado no conteúdo"""
        # Clear existing widgets
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if self.is_url(self.card.name):
            self.show_link_label()
        else:
            self.show_edit_field()
    
    def show_link_label(self):
        """Mostra o link clicável"""
        self.label = QLabel()
        self.label.setText(
            f'<a href="{self.card.name}" style="color: #007bff; '
            f'text-decoration: none; font-weight: 500;">{self.card.name}</a>'
        )
        self.label.setOpenExternalLinks(False)
        self.label.linkActivated.connect(self.open_link)
        self.label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label.setToolTip("Click to open link | Double-click to edit")
        self.label.mouseDoubleClickEvent = lambda event: self.switch_to_edit()
        self.layout.addWidget(self.label)
    
    def show_edit_field(self):
        """Mostra o campo editável"""
        # Clear existing widgets
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        self.line_edit = QLineEdit(self.card.name)
        self.line_edit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.line_edit.setPlaceholderText("Enter task name or URL...")
        self.line_edit.textChanged.connect(self.on_text_changed)
        self.line_edit.editingFinished.connect(self.on_editing_finished)
        
        # Prevent text selection when clicking elsewhere
        self.line_edit.setAttribute(Qt.WidgetAttribute.WA_InputMethodEnabled, False)
        
        # Override focus out event
        original_focus_out = self.line_edit.focusOutEvent
        def custom_focus_out(event):
            original_focus_out(event)
            self.on_editing_finished()
        self.line_edit.focusOutEvent = custom_focus_out
        
        self.layout.addWidget(self.line_edit)
    
    def switch_to_edit(self):
        """Alterna para modo de edição"""
        self.show_edit_field()
    
    def on_text_changed(self, text: str):
        """Handler para mudança de texto"""
        self.card.name = text
        self.on_text_changed_callback()
        self.text_changed.emit()
    
    def on_editing_finished(self):
        """Quando termina de editar, verifica se é URL e atualiza"""
        if not self.line_edit:
            return
            
        text = self.line_edit.text().strip()
        if text != self.card.name:
            self.card.name = text
            self.on_text_changed_callback()
        
        if self.is_url(text):
            self.refresh_widget()
    
    def open_link(self, url: str):
        """Abre o link no navegador padrão (multiplataforma)"""
        try:
            webbrowser.open(url, new=2)
        except Exception as e:
            print(f"Erro ao abrir link: {e}")

