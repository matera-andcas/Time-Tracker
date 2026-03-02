"""
Database Layer - SQLite persistence
"""
import sqlite3
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional


class Database:
    """Gerencia a conexão e operações com SQLite"""
    
    def __init__(self, db_path: str = "timetracker.db"):
        # Garantir que o caminho do banco seja absoluto e multiplataforma
        if not os.path.isabs(db_path):
            # Coloca o banco de dados no diretório do usuário
            user_data_dir = self._get_user_data_dir()
            user_data_dir.mkdir(parents=True, exist_ok=True)
            self.db_path = str(user_data_dir / db_path)
        else:
            self.db_path = db_path
        self.init_database()
    
    @staticmethod
    def _get_user_data_dir() -> Path:
        """Retorna o diretório de dados do usuário de forma multiplataforma"""
        system = os.name
        
        if system == 'nt':  # Windows
            base_path = Path(os.environ.get('APPDATA', Path.home()))
            return base_path / 'TimeTracker'
        else:  # Linux/Mac
            base_path = Path.home()
            return base_path / '.timetracker'
    
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
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_date TEXT
            )
        ''')
        
        # Migração: Adiciona coluna created_date se não existir
        try:
            cursor.execute("SELECT created_date FROM cards LIMIT 1")
        except sqlite3.OperationalError:
            # Coluna não existe, vamos adicioná-la
            cursor.execute("ALTER TABLE cards ADD COLUMN created_date TEXT")
            conn.commit()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_card(self, card_id: Optional[int], name: str, elapsed_seconds: int, 
                  start_time: Optional[str], end_time: Optional[str], is_running: bool,
                  created_date: Optional[str] = None) -> int:
        """Salva ou atualiza um card no banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if card_id is None or card_id == 0:
            cursor.execute('''
                INSERT INTO cards (name, elapsed_seconds, start_time, end_time, is_running, created_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, elapsed_seconds, start_time, end_time, is_running, created_date))
            card_id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE cards 
                SET name = ?, elapsed_seconds = ?, start_time = ?, end_time = ?, 
                    is_running = ?, created_date = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (name, elapsed_seconds, start_time, end_time, is_running, created_date, card_id))
        
        conn.commit()
        conn.close()
        return card_id
    
    def load_cards(self) -> List[dict]:
        """Carrega todos os cards do banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, name, elapsed_seconds, start_time, end_time, is_running, created_at, created_date
            FROM cards
            ORDER BY id
        ''')
        
        cards = []
        for row in cursor.fetchall():
            # Usa created_date se existir, senão converte created_at
            created_date = row[7]  # created_date
            if not created_date and row[6]:  # fallback para created_at
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
    
    def save_note(self, note_id: Optional[int], tag: str, description: str) -> int:
        """Salva ou atualiza uma nota no banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if note_id is None or note_id == 0:
            cursor.execute('''
                INSERT INTO notes (tag, description)
                VALUES (?, ?)
            ''', (tag, description))
            note_id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE notes 
                SET tag = ?, description = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (tag, description, note_id))
        
        conn.commit()
        conn.close()
        return note_id
    
    def load_notes(self) -> List[dict]:
        """Carrega todas as notas do banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, tag, description
            FROM notes
            ORDER BY id
        ''')
        
        notes = []
        for row in cursor.fetchall():
            notes.append({
                'id': row[0],
                'tag': row[1],
                'description': row[2]
            })
        
        conn.close()
        return notes
    
    def delete_note(self, note_id: int):
        """Remove uma nota do banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        conn.close()
    
    def save_notes_batch(self, notes: List[dict]):
        """Salva múltiplas notas de uma vez"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Primeiro, pega os IDs existentes
        existing_ids = set()
        for note in notes:
            if note.get('id'):
                existing_ids.add(note['id'])
        
        # Deleta notas que não estão mais na lista
        if existing_ids:
            placeholders = ','.join('?' * len(existing_ids))
            cursor.execute(f'SELECT id FROM notes WHERE id NOT IN ({placeholders})', tuple(existing_ids))
        else:
            cursor.execute('SELECT id FROM notes')
        
        ids_to_delete = [row[0] for row in cursor.fetchall()]
        for note_id in ids_to_delete:
            cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        
        # Salva/atualiza as notas
        for note in notes:
            note_id = note.get('id')
            tag = note.get('tag', '')
            description = note.get('description', '')
            
            if note_id:
                cursor.execute('''
                    UPDATE notes 
                    SET tag = ?, description = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (tag, description, note_id))
            else:
                cursor.execute('''
                    INSERT INTO notes (tag, description)
                    VALUES (?, ?)
                ''', (tag, description))
                note['id'] = cursor.lastrowid
        
        conn.commit()
        conn.close()
