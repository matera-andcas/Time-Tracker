"""
Domain Models - Core business entities
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from PyQt6.QtCore import QElapsedTimer


@dataclass
class Card:
    """Representa um card de time tracking"""
    id: Optional[int] = None
    name: str = ""
    is_running: bool = False
    elapsed_seconds: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_selected: bool = False
    timer: Optional[QElapsedTimer] = field(default=None, repr=False, compare=False)
    _db_id: Optional[int] = None
    
    def __post_init__(self):
        """Inicializa o card após criação"""
        if self._db_id is None:
            self._db_id = self.id
    
    @property
    def db_id(self) -> Optional[int]:
        """Retorna o ID do banco de dados"""
        return self._db_id
    
    @db_id.setter
    def db_id(self, value: int):
        """Define o ID do banco de dados"""
        self._db_id = value
        if self.id is None:
            self.id = value
    
    def start(self):
        """Inicia o timer do card"""
        if not self.is_running:
            self.is_running = True
            if self.start_time is None:
                self.start_time = datetime.now().strftime("%H:%M")
            self.end_time = None
            if self.timer is None:
                self.timer = QElapsedTimer()
            self.timer.start()
    
    def pause(self):
        """Pausa o timer do card"""
        if self.is_running and self.timer:
            self.is_running = False
            self.end_time = datetime.now().strftime("%H:%M")
            self.elapsed_seconds += self.timer.elapsed() // 1000
            self.timer = None
    
    def get_current_elapsed_seconds(self) -> int:
        """Retorna o tempo total incluindo o tempo atual se estiver rodando"""
        if self.is_running and self.timer:
            return self.elapsed_seconds + (self.timer.elapsed() // 1000)
        return self.elapsed_seconds
    
    def get_formatted_time(self) -> str:
        """Retorna o tempo formatado como HH:MM:SS"""
        total_seconds = self.get_current_elapsed_seconds()
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def reset(self):
        """Reseta o timer do card"""
        self.elapsed_seconds = 0
        self.start_time = None
        self.end_time = None
        self.is_running = False
        self.timer = None
    
    def to_dict(self) -> dict:
        """Converte o card para dicionário (para salvar no DB)"""
        return {
            'id': self._db_id,
            'name': self.name,
            'elapsed_seconds': self.get_current_elapsed_seconds() if self.is_running else self.elapsed_seconds,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'is_running': False
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Card':
        """Cria um card a partir de um dicionário (do DB)"""
        card = Card(
            id=data['id'],
            name=data['name'],
            elapsed_seconds=data['elapsed_seconds'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            is_running=False
        )
        card._db_id = data['id']
        return card
