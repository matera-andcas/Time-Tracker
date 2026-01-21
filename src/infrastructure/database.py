"""
Database Layer - SQLite persistence
"""
import sqlite3
from typing import List, Optional


class Database:
    """Gerencia a conexão e operações com SQLite"""
    
    def __init__(self, db_path: str = "timetracker.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Retorna uma conexão com o banco de dados"""
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        """Inicializa o banco de dados e cria as tabelas"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                elapsed_seconds INTEGER DEFAULT 0,
                start_time TEXT,
                end_time TEXT,
                is_running BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_card(self, card_id: Optional[int], name: str, elapsed_seconds: int, 
                  start_time: Optional[str], end_time: Optional[str], is_running: bool) -> int:
        """Salva ou atualiza um card no banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if card_id is None or card_id == 0:
            cursor.execute('''
                INSERT INTO cards (name, elapsed_seconds, start_time, end_time, is_running)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, elapsed_seconds, start_time, end_time, is_running))
            card_id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE cards 
                SET name = ?, elapsed_seconds = ?, start_time = ?, end_time = ?, 
                    is_running = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (name, elapsed_seconds, start_time, end_time, is_running, card_id))
        
        conn.commit()
        conn.close()
        return card_id
    
    def load_cards(self) -> List[dict]:
        """Carrega todos os cards do banco"""
        from datetime import datetime
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, name, elapsed_seconds, start_time, end_time, is_running, created_at
            FROM cards
            ORDER BY id
        ''')
        
        cards = []
        for row in cursor.fetchall():
            # Converte created_at para formato dd/mm/yy
            created_date = None
            if row[6]:  # created_at
                try:
                    # Formato do SQLite: YYYY-MM-DD HH:MM:SS
                    dt = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
                    created_date = dt.strftime('%d/%m/%y')
                except:
                    created_date = datetime.now().strftime('%d/%m/%y')
            
            cards.append({
                'id': row[0],
                'name': row[1],
                'elapsed_seconds': row[2],
                'start_time': row[3],
                'end_time': row[4],
                'is_running': bool(row[5]),
                'created_date': created_date
            })
        
        conn.close()
        return cards
    
    def delete_card(self, card_id: int):
        """Remove um card do banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cards WHERE id = ?', (card_id,))
        conn.commit()
        conn.close()
    
    def clear_all(self):
        """Remove todos os cards"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cards')
        conn.commit()
        conn.close()
    
    def save_setting(self, key: str, value: str):
        """Salva uma configuração"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO settings (key, value)
            VALUES (?, ?)
        ''', (key, value))
        conn.commit()
        conn.close()
    
    def get_setting(self, key: str, default: str = None) -> str:
        """Carrega uma configuração"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return row[0]
        return default
