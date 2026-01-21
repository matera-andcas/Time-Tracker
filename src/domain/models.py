"""
Domain Models - Core business entities
"""
from dataclasses import dataclass, field
from datetime import datetime
import re
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
    created_date: Optional[str] = None  # Data de criação no formato dd/mm/yy
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
            # Só define start_time se for o primeiro start (nunca foi iniciado antes)
            if self.start_time is None and self.elapsed_seconds == 0:
                self.start_time = datetime.now().strftime("%H:%M")
            # Se já tem elapsed_seconds, é um resume, não altera start_time
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
    
    def validate_time_format(self, time_str: str) -> bool:
        """Valida se o horário está no formato HH:MM válido"""
        if not time_str:
            return True  # Empty is valid
        
        pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$')
        if not pattern.match(time_str):
            return False
        
        parts = time_str.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        
        return 0 <= hours <= 23 and 0 <= minutes <= 59
    
    def update_start_time(self, time_str: str) -> bool:
        """Atualiza o start time com validação SEM recalcular elapsed_seconds"""
        if time_str and not self.validate_time_format(time_str):
            return False
        self.start_time = time_str if time_str else None
        return True
    
    def update_end_time(self, time_str: str) -> bool:
        """Atualiza o end time com validação SEM recalcular elapsed_seconds"""
        if time_str and not self.validate_time_format(time_str):
            return False
        self.end_time = time_str if time_str else None
        return True
    
    def to_dict(self) -> dict:
        """Converte o card para dicionário (para salvar no DB)"""
        # Sempre salva o elapsed_seconds atualizado
        current_elapsed = self.elapsed_seconds
        if self.is_running and self.timer:
            current_elapsed = self.elapsed_seconds + (self.timer.elapsed() // 1000)
        
        return {
            'id': self._db_id,
            'name': self.name,
            'elapsed_seconds': current_elapsed,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'is_running': False  # Sempre salva como não rodando
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
            is_running=False,
            created_date=data.get('created_date')
        )
        card._db_id = data['id']
        return card
