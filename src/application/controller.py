"""
Application Controller - Orchestrates UI, Domain and Infrastructure
"""
from typing import List
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QMessageBox
from src.domain import Card, CardService
from src.infrastructure import Database
from src.ui import MainWindow


class TimeTrackerController:
    """Controller principal da aplicação - padrão MVC"""
    
    def __init__(self):
        # Infrastructure
        self.db = Database()
        
        # Domain
        self.cards: List[Card] = []
        self.load_cards_from_db()
        self.card_service = CardService(self.cards)
        
        # UI
        self.view = MainWindow()
        self.setup_view()
        self.setup_timers()
        
        # Carregar preferências
        dark_mode = self.db.get_setting('dark_mode', 'false') == 'true'
        self.view.set_dark_mode(dark_mode)
        
        # Primeira renderização
        self.refresh_view()
    
    def setup_view(self):
        """Conecta os eventos da UI aos handlers do controller"""
        self.view.add_btn.clicked.connect(self.on_add_card)
        self.view.delete_btn.clicked.connect(self.on_delete_selected)
        self.view.select_all_cb.stateChanged.connect(self.on_select_all)
        self.view.theme_btn.clicked.connect(self.on_toggle_theme)
    
    def setup_timers(self):
        """Configura os timers de atualização"""
        # Timer para atualizar display
        self.display_timer = QTimer()
        self.display_timer.timeout.connect(self.update_display)
        self.display_timer.start(100)
        
        # Timer para auto-save
        self.autosave_timer = QTimer()
        self.autosave_timer.timeout.connect(self.auto_save)
        self.autosave_timer.start(5000)
    
    def load_cards_from_db(self):
        """Carrega os cards do banco de dados"""
        cards_data = self.db.load_cards()
        self.cards = [Card.from_dict(data) for data in cards_data]
    
    def save_cards_to_db(self):
        """Salva todos os cards no banco de dados"""
        for card in self.cards:
            card_data = card.to_dict()
            db_id = self.db.save_card(
                card_id=card.db_id,
                name=card_data['name'],
                elapsed_seconds=card_data['elapsed_seconds'],
                start_time=card_data['start_time'],
                end_time=card_data['end_time'],
                is_running=card_data['is_running']
            )
            if card.db_id is None:
                card.db_id = db_id
    
    def refresh_view(self):
        """Atualiza a view completa"""
        self.view.refresh_table(
            cards=self.card_service.get_all_cards(),
            on_checkbox_changed=self.on_card_selected,
            on_text_changed=self.on_card_text_changed,
            on_play_clicked=self.on_play_card,
            on_pause_clicked=self.on_pause_card,
            on_time_changed=self.on_time_changed
        )
    
    def update_display(self):
        """Atualiza apenas o display dos timers"""
        self.view.update_timer_display(self.card_service.get_all_cards())
    
    def auto_save(self):
        """Auto-salva periodicamente"""
        self.save_cards_to_db()
    
    # Event handlers
    
    def on_add_card(self):
        """Handler para adicionar card"""
        card = self.card_service.add_card()
        card_data = card.to_dict()
        db_id = self.db.save_card(
            card_id=None,
            name=card_data['name'],
            elapsed_seconds=card_data['elapsed_seconds'],
            start_time=card_data['start_time'],
            end_time=card_data['end_time'],
            is_running=card_data['is_running']
        )
        card.db_id = db_id
        self.refresh_view()
    
    def on_delete_selected(self):
        """Handler para deletar cards selecionados"""
        if not self.card_service.has_selected_cards():
            return
        
        # Contar quantos cards estão selecionados
        selected_count = len([c for c in self.cards if c.is_selected])
        
        # Criar diálogo de confirmação
        msg = QMessageBox(self.view)
        msg.setWindowTitle("Delete")
        
        if selected_count == 1:
            msg.setText("Deseja realmente excluir este card?")
        else:
            msg.setText(f"Deseja realmente excluir {selected_count} cards?")
        
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.Yes)
        
        # Customizar textos dos botões (sem ícones)
        yes_btn = msg.button(QMessageBox.StandardButton.Yes)
        no_btn = msg.button(QMessageBox.StandardButton.No)
        yes_btn.setText("Excluir")
        no_btn.setText("Cancelar")
        yes_btn.setIcon(yes_btn.style().standardIcon(yes_btn.style().StandardPixmap.SP_CustomBase))
        no_btn.setIcon(no_btn.style().standardIcon(no_btn.style().StandardPixmap.SP_CustomBase))
        
        # Identificar botão para estilização CSS
        yes_btn.setObjectName("deleteConfirmButton")
        
        # Forçar aplicação do stylesheet
        yes_btn.style().unpolish(yes_btn)
        yes_btn.style().polish(yes_btn)
        
        # Mostrar diálogo e verificar resposta
        if msg.exec() == QMessageBox.StandardButton.Yes:
            # Deletar do banco antes de remover da lista
            for card in [c for c in self.cards if c.is_selected]:
                if card.db_id:
                    self.db.delete_card(card.db_id)
            
            self.card_service.remove_selected_cards()
            self.view.select_all_cb.setChecked(False)
            self.refresh_view()
    
    def on_select_all(self, state):
        """Handler para select all"""
        self.card_service.select_all(state == Qt.CheckState.Checked.value)
        self.refresh_view()
    
    def on_toggle_theme(self):
        """Handler para alternar tema"""
        new_mode = not self.view.dark_mode
        self.view.set_dark_mode(new_mode)
        self.db.save_setting('dark_mode', 'true' if new_mode else 'false')
    
    def on_card_selected(self, card: Card, state):
        """Handler para seleção de card"""
        card.is_selected = (state == Qt.CheckState.Checked.value)
    
    def on_card_text_changed(self):
        """Handler para mudança no texto do card"""
        self.save_cards_to_db()
    
    def on_time_changed(self):
        """Handler para mudança nos horários do card"""
        self.save_cards_to_db()
    
    def on_play_card(self, card: Card):
        """Handler para iniciar card"""
        card.start()
        self.update_display()
    
    def on_pause_card(self, card: Card):
        """Handler para pausar card"""
        card.pause()
        self.update_display()
    
    def on_close(self):
        """Handler para fechamento da aplicação"""
        self.save_cards_to_db()
    
    def show(self):
        """Mostra a janela principal"""
        self.view.show()
