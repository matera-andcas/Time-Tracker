""" 
Time Tracker - Aplicação Desktop
Interface gráfica moderna para gerenciamento de tempo por card
"""
import sys
import re
import webbrowser
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QCheckBox, QLineEdit, QAbstractItemView, QLabel
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QIcon, QColor, QFont
from card_manager import CardManager
from models import Card
from database import Database


class ClickableCardWidget(QWidget):
    """Widget que alterna entre link clicável e campo editável"""
    
    def __init__(self, card: Card, parent_app):
        super().__init__()
        self.card = card
        self.parent_app = parent_app
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(8, 0, 8, 0)
        self.setLayout(self.layout)
        
        self.line_edit = None
        self.label = None
        
        self.refresh_widget()
    
    def is_url(self, text):
        """Verifica se o texto é uma URL"""
        url_pattern = re.compile(r'https?://[^\s]+')
        return bool(url_pattern.search(text))
    
    def refresh_widget(self):
        """Atualiza o widget baseado no conteúdo"""
        # Limpar layout
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if self.is_url(self.card.name):
            # Criar label clicável
            self.label = QLabel()
            self.label.setText(f'<a href="{self.card.name}" style="color: #2196F3; text-decoration: underline;">{self.card.name}</a>')
            self.label.setOpenExternalLinks(False)
            self.label.linkActivated.connect(self.open_link)
            self.label.setCursor(Qt.CursorShape.PointingHandCursor)
            self.label.mouseDoubleClickEvent = lambda event: self.switch_to_edit()
            self.layout.addWidget(self.label)
        else:
            # Criar campo editável
            self.show_edit_field()
    
    def show_edit_field(self):
        """Mostra o campo editável"""
        # Limpar layout
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        self.line_edit = QLineEdit(self.card.name)
        self.line_edit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.line_edit.textChanged.connect(self.on_text_changed)
        self.line_edit.editingFinished.connect(self.on_editing_finished)
        # Detectar quando perde o foco
        original_focus_out = self.line_edit.focusOutEvent
        def custom_focus_out(event):
            original_focus_out(event)
            self.on_editing_finished()
        self.line_edit.focusOutEvent = custom_focus_out
        self.layout.addWidget(self.line_edit)
        self.line_edit.setFocus()
    
    def switch_to_edit(self):
        """Alterna para modo de edição"""
        self.show_edit_field()
    
    def on_text_changed(self, text):
        """Handler para mudança de texto"""
        self.card.name = text
        self.parent_app.card_manager.save_to_database()
    
    def on_editing_finished(self):
        """Quando termina de editar, verifica se é URL e atualiza"""
        if self.is_url(self.card.name):
            self.refresh_widget()
    
    def open_link(self, url):
        """Abre o link no navegador"""
        import subprocess
        try:
            # Abre em nova janela do Chrome
            subprocess.Popen(['google-chrome', '--new-window', url])
        except FileNotFoundError:
            try:
                subprocess.Popen(['chromium', '--new-window', url])
            except FileNotFoundError:
                webbrowser.open(url, new=1)
    
    def bring_chrome_to_front(self):
        """Método não utilizado - mantido para compatibilidade"""
        pass


class TimeTrackerApp(QMainWindow):
    """Janela principal da aplicação"""
    
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.card_manager = CardManager(self.db)
        # Carregar tema salvo
        self.dark_mode = self.db.get_setting('dark_mode', 'false') == 'true'
        self.init_ui()
        self.setup_timer()
        self.setup_autosave()
    
    def init_ui(self):
        """Inicializa a interface do usuário"""
        self.setWindowTitle("Time Tracker")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet(self.get_stylesheet())
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Tabela de cards
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "☑", "Card", "Play", "Pause", "Tempo", "Dia", "Hora Inicial", "Hora Final"
        ])
        
        # Remover foco ao clicar na tabela
        self.table.mousePressEvent = lambda event: self.clear_all_focus()
        
        # Configurações da tabela
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Remove foco da tabela
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)  # Remove seleção de linhas
        
        # Definir altura padrão das linhas
        self.table.verticalHeader().setDefaultSectionSize(60)
        self.table.verticalHeader().setDefaultSectionSize(60)  # altura em pixels
        
        # Ajustar largura das colunas
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Fixed)
        
        self.table.setColumnWidth(0, 50)   # Checkbox
        self.table.setColumnWidth(2, 70)   # Play
        self.table.setColumnWidth(3, 70)   # Pause
        self.table.setColumnWidth(4, 100)  # Tempo
        self.table.setColumnWidth(5, 100)  # Dia
        self.table.setColumnWidth(6, 100)  # Hr Inicial
        self.table.setColumnWidth(7, 100)  # Hr Final
        
        main_layout.addWidget(self.table)
        
        # Layout inferior com controles
        bottom_layout = QHBoxLayout()
        
        # Checkbox "Select All"
        self.select_all_cb = QCheckBox("Select All")
        self.select_all_cb.stateChanged.connect(self.on_select_all)
        bottom_layout.addWidget(self.select_all_cb)
        
        bottom_layout.addStretch()
        
        # Botão de tema
        self.theme_btn = QPushButton("🌙 Tema Escuro")
        self.theme_btn.setObjectName("themeButton")
        self.theme_btn.clicked.connect(self.toggle_theme)
        bottom_layout.addWidget(self.theme_btn)
        
        # Botão de deletar
        self.delete_btn = QPushButton("Deletar")
        self.delete_btn.setObjectName("deleteButton")
        self.delete_btn.clicked.connect(self.delete_selected)
        bottom_layout.addWidget(self.delete_btn)
        
        # Botão de adicionar
        self.add_btn = QPushButton("➕ Adicionar Card")
        self.add_btn.setObjectName("addButton")
        self.add_btn.clicked.connect(self.add_card)
        bottom_layout.addWidget(self.add_btn)
        
        main_layout.addLayout(bottom_layout)
        
        # Carregar cards existentes
        self.refresh_table()
        
        # Aplicar tema salvo
        if self.dark_mode:
            self.theme_btn.setText("☀️ Tema Claro")
        self.setStyleSheet(self.get_stylesheet())
    
    def setup_timer(self):
        """Configura o timer global para atualizar os contadores"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer_display)
        self.timer.start(100)  # Atualiza a cada 100ms para display suave
    
    def setup_autosave(self):
        """Configura auto-save periódico"""
        self.autosave_timer = QTimer()
        self.autosave_timer.timeout.connect(self.auto_save)
        self.autosave_timer.start(5000)  # Auto-save a cada 5 segundos
    
    def update_timer_display(self):
        """Atualiza apenas o display dos timers sem recriar widgets"""
        cards = self.card_manager.get_all_cards()
        for row, card in enumerate(cards):
            if row < self.table.rowCount():
                # Atualizar apenas o texto do tempo
                time_item = self.table.item(row, 4)
                if time_item:
                    time_item.setText(card.get_formatted_time())
                
                # Atualizar hora inicial
                start_item = self.table.item(row, 6)
                if start_item:
                    start_item.setText(card.start_time or "")
                
                # Atualizar hora final
                end_item = self.table.item(row, 7)
                if end_item:
                    if card.is_running:
                        end_item.setText("")
                    elif card.end_time:
                        end_item.setText(card.end_time)
                
                # Atualizar estado dos botões
                play_btn = self.table.cellWidget(row, 2)
                pause_btn = self.table.cellWidget(row, 3)
                if play_btn and pause_btn:
                    play_btn.setEnabled(not card.is_running)
                    pause_btn.setEnabled(card.is_running)
    
    def add_card(self):
        """Adiciona um novo card"""
        card = self.card_manager.add_card()
        self.refresh_table()
    
    def auto_save(self):
        """Salva automaticamente os cards"""
        self.card_manager.auto_save()
    
    def delete_selected(self):
        """Deleta os cards selecionados"""
        if self.card_manager.has_selected_cards():
            self.card_manager.remove_selected_cards()
            self.select_all_cb.setChecked(False)
            self.refresh_table()
    
    def on_select_all(self, state):
        """Handler para o checkbox Select All"""
        self.card_manager.select_all(state == Qt.CheckState.Checked.value)
        self.refresh_table()
    
    def toggle_theme(self):
        """Alterna entre tema claro e escuro"""
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.theme_btn.setText("☀️ Tema Claro")
        else:
            self.theme_btn.setText("🌙 Tema Escuro")
        # Salvar preferência no banco
        self.db.save_setting('dark_mode', 'true' if self.dark_mode else 'false')
        self.setStyleSheet(self.get_stylesheet())
    
    def refresh_table(self):
        """Atualiza a tabela com os dados dos cards"""
        cards = self.card_manager.get_all_cards()
        self.table.setRowCount(len(cards))
        
        for row, card in enumerate(cards):
            # Checkbox
            checkbox = QCheckBox()
            checkbox.setChecked(card.is_selected)
            checkbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            checkbox.stateChanged.connect(
                lambda state, c=card: self.on_card_selected(c, state)
            )
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout()
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_widget.setLayout(checkbox_layout)
            self.table.setCellWidget(row, 0, checkbox_widget)
            
            # Campo Card (editável ou link clicável)
            card_widget = ClickableCardWidget(card, self)
            self.table.setCellWidget(row, 1, card_widget)
            
            # Definir altura da linha
            self.table.setRowHeight(row, 60)
            
            # Botão Play
            play_btn = QPushButton("▶")
            play_btn.setObjectName("playButton")
            play_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            play_btn.setEnabled(not card.is_running)
            play_btn.clicked.connect(lambda _, c=card: self.start_card(c))
            self.table.setCellWidget(row, 2, play_btn)
            
            # Botão Pause
            pause_btn = QPushButton("⏸")
            pause_btn.setObjectName("pauseButton")
            pause_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            pause_btn.setEnabled(card.is_running)
            pause_btn.clicked.connect(lambda _, c=card: self.pause_card(c))
            self.table.setCellWidget(row, 3, pause_btn)
            
            # Tempo
            time_item = QTableWidgetItem(card.get_formatted_time())
            time_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            time_item.setFont(QFont("Monospace", 11, QFont.Weight.Bold))
            time_item.setForeground(QColor("#666666"))
            time_item.setFlags(time_item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEnabled)
            self.table.setItem(row, 4, time_item)
            
            # Dia
            from datetime import datetime
            day_item = QTableWidgetItem(datetime.now().strftime("%d/%m/%y"))
            day_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            day_item.setFont(QFont("Monospace", 11, QFont.Weight.Bold))
            day_item.setForeground(QColor("#666666"))
            day_item.setFlags(day_item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEnabled)
            self.table.setItem(row, 5, day_item)
            
            # Hr Inicial
            start_item = QTableWidgetItem(card.start_time or "")
            start_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            start_item.setFont(QFont("Monospace", 11, QFont.Weight.Bold))
            start_item.setFlags(start_item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEnabled)
            self.table.setItem(row, 6, start_item)
            
            # Hr Final
            end_item = QTableWidgetItem(card.end_time or "")
            end_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            end_item.setFont(QFont("Monospace", 11, QFont.Weight.Bold))
            end_item.setFlags(end_item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEnabled)
            self.table.setItem(row, 7, end_item)
    
    def start_card(self, card: Card):
        """Inicia o timer de um card"""
        card.start()
        self.update_timer_display()  # Atualiza apenas display
    
    def pause_card(self, card: Card):
        """Pausa o timer de um card"""
        card.pause()
        self.update_timer_display()  # Atualiza apenas display
    
    def on_card_selected(self, card: Card, state):
        """Handler para seleção de card"""
        card.is_selected = (state == Qt.CheckState.Checked.value)
    
    def on_card_name_changed(self, card: Card, text: str):
        """Handler para mudança no nome do card"""
        card.name = text
        # Auto-salvar quando o nome mudar
        self.card_manager.save_to_database()
    
    def clear_all_focus(self):
        """Remove o foco de todos os widgets"""
        focused_widget = QApplication.focusWidget()
        if focused_widget:
            focused_widget.clearFocus()
    
    def closeEvent(self, event):
        """Handler para fechamento da aplicação"""
        # Salvar tudo antes de fechar
        self.card_manager.save_to_database()
        event.accept()
    
    def get_stylesheet(self) -> str:
        """Retorna o stylesheet CSS da aplicação"""
        if self.dark_mode:
            return self.get_dark_stylesheet()
        return self.get_light_stylesheet()
    
    def get_light_stylesheet(self) -> str:
        """Retorna o stylesheet do tema claro"""
        return """
            QMainWindow {
                background-color: #f5f5f5;
            }
            
            QTableWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                gridline-color: #f0f0f0;
                font-size: 13px;
                color: #000000;
            }
            
            QTableWidget::item {
                padding: 8px;
                background-color: white;
            }
            
            QTableWidget::item:selected {
                background-color: white;
            }
            
            QTableWidget::item:focus {
                outline: none;
                border: none;
            }
            
            QHeaderView::section {
                background-color: #fafafa;
                padding: 10px;
                border: none;
                border-bottom: 2px solid #e0e0e0;
                font-weight: bold;
                font-size: 13px;
                color: #000000;
            }
            
            QLineEdit {
                padding: 8px;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                background-color: white;
                font-size: 13px;
                color: #000000;
            }
            
            QLineEdit:focus {
                border: 2px solid #4CAF50;
                background-color: white;
            }
            
            QPushButton {
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: bold;
                border: none;
            }
            
            QPushButton#playButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
            }
            
            QPushButton#playButton:hover {
                background-color: #45a049;
            }
            
            QPushButton#playButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            
            QPushButton#pauseButton {
                background-color: #f44336;
                color: white;
                font-size: 16px;
            }
            
            QPushButton#pauseButton:hover {
                background-color: #da190b;
            }
            
            QPushButton#pauseButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            
            QPushButton#addButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
            }
            
            QPushButton#addButton:hover {
                background-color: #0b7dda;
            }
            
            QPushButton#deleteButton {
                background-color: #ff9800;
                color: white;
                padding: 10px 20px;
            }
            
            QPushButton#deleteButton:hover {
                background-color: #e68900;
            }
            
            QPushButton#themeButton {
                background-color: #9c27b0;
                color: white;
                padding: 10px 20px;
            }
            
            QPushButton#themeButton:hover {
                background-color: #7b1fa2;
            }
            
            QCheckBox {
                font-size: 13px;
                spacing: 8px;
                color: #000000;
            }
            
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 3px;
                border: 2px solid #bdbdbd;
            }
            
            QCheckBox::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
        """
    
    def get_dark_stylesheet(self) -> str:
        """Retorna o stylesheet do tema escuro"""
    def get_dark_stylesheet(self) -> str:
        """Retorna o stylesheet do tema escuro"""
        return """
            QMainWindow {
                background-color: #1e1e1e;
            }
            
            QTableWidget {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                gridline-color: #3d3d3d;
                font-size: 13px;
                color: #e0e0e0;
            }
            
            QTableWidget::item {
                padding: 8px;
                background-color: #2d2d2d;
                color: #e0e0e0;
            }
            
            QTableWidget::item:selected {
                background-color: #2d2d2d;
            }
            
            QTableWidget::item:focus {
                outline: none;
                border: none;
            }
            
            QHeaderView::section {
                background-color: #252525;
                padding: 10px;
                border: none;
                border-bottom: 2px solid #3d3d3d;
                font-weight: bold;
                font-size: 13px;
                color: #e0e0e0;
            }
            
            QLineEdit {
                padding: 8px;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                background-color: #2d2d2d;
                font-size: 13px;
                color: #e0e0e0;
            }
            
            QLineEdit:focus {
                border: 2px solid #4CAF50;
                background-color: #2d2d2d;
            }
            
            QPushButton {
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: bold;
                border: none;
            }
            
            QPushButton#playButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
            }
            
            QPushButton#playButton:hover {
                background-color: #45a049;
            }
            
            QPushButton#playButton:disabled {
                background-color: #3d3d3d;
                color: #666666;
            }
            
            QPushButton#pauseButton {
                background-color: #f44336;
                color: white;
                font-size: 16px;
            }
            
            QPushButton#pauseButton:hover {
                background-color: #da190b;
            }
            
            QPushButton#pauseButton:disabled {
                background-color: #3d3d3d;
                color: #666666;
            }
            
            QPushButton#addButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
            }
            
            QPushButton#addButton:hover {
                background-color: #0b7dda;
            }
            
            QPushButton#deleteButton {
                background-color: #ff9800;
                color: white;
                padding: 10px 20px;
            }
            
            QPushButton#deleteButton:hover {
                background-color: #e68900;
            }
            
            QPushButton#themeButton {
                background-color: #9c27b0;
                color: white;
                padding: 10px 20px;
            }
            
            QPushButton#themeButton:hover {
                background-color: #7b1fa2;
            }
            
            QCheckBox {
                font-size: 13px;
                spacing: 8px;
                color: #e0e0e0;
            }
            
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 3px;
                border: 2px solid #5d5d5d;
                background-color: #2d2d2d;
            }
            
            QCheckBox::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
        """


def main():
    """Função principal"""
    app = QApplication(sys.argv)
    app.setApplicationName("timeTracker")
    app.setDesktopFileName("timetracker.desktop")
    app.setStyle('Fusion')  # Estilo moderno
    window = TimeTrackerApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
