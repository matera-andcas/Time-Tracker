"""
Gerenciador de Cards - Lógica de negócio e persistência
"""
from typing import List, Optional
from models import Card
from database import Database


class CardManager:
    """Gerencia a lista de cards e suas operações"""
    
    def __init__(self, db: Database):
        self.db = db
        self.cards: List[Card] = []
        self.load_from_database()
    
    def load_from_database(self):
        """Carrega os cards do banco de dados"""
        cards_data = self.db.load_cards()
        self.cards = [Card.from_dict(data) for data in cards_data]
    
    def save_to_database(self):
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
    
    def add_card(self, name: str = "") -> Card:
        """Adiciona um novo card"""
        card = Card(name=name)
        self.cards.append(card)
        
        # Salvar imediatamente no banco
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
        
        return card
    
    def remove_card(self, card: Card):
        """Remove um card específico"""
        if card in self.cards:
            if card.db_id:
                self.db.delete_card(card.db_id)
            self.cards.remove(card)
    
    def remove_selected_cards(self):
        """Remove todos os cards selecionados"""
        cards_to_remove = [c for c in self.cards if c.is_selected]
        for card in cards_to_remove:
            self.remove_card(card)
    
    def get_card_by_id(self, card_id: int) -> Optional[Card]:
        """Retorna um card pelo ID"""
        for card in self.cards:
            if card.id == card_id:
                return card
        return None
    
    def select_all(self, selected: bool):
        """Marca ou desmarca todos os cards"""
        for card in self.cards:
            card.is_selected = selected
    
    def has_selected_cards(self) -> bool:
        """Verifica se há cards selecionados"""
        return any(card.is_selected for card in self.cards)
    
    def get_all_cards(self) -> List[Card]:
        """Retorna todos os cards"""
        return self.cards
    
    def auto_save(self):
        """Auto-salva os cards periodicamente"""
        self.save_to_database()
