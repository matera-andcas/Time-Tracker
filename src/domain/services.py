"""
Business Logic Services
"""
from datetime import datetime
from typing import List, Optional
from .models import Card


class CardService:
    """Serviço com lógica de negócio para Cards"""
    
    def __init__(self, cards: List[Card]):
        self.cards = cards
    
    def add_card(self, name: str = "") -> Card:
        """Adiciona um novo card"""
        card = Card(
            name=name,
            created_date=datetime.now().strftime("%d/%m/%y")
        )
        self.cards.append(card)
        return card
    
    def remove_card(self, card: Card) -> bool:
        """Remove um card específico"""
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False
    
    def remove_selected_cards(self) -> int:
        """Remove todos os cards selecionados e retorna quantidade removida"""
        cards_to_remove = [c for c in self.cards if c.is_selected]
        count = len(cards_to_remove)
        for card in cards_to_remove:
            self.remove_card(card)
        return count
    
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
