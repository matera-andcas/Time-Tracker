"""
Exemplo de extensão futura: Exportar dados para CSV
Este arquivo demonstra como adicionar funcionalidade de exportação
"""
import csv
from datetime import datetime
from typing import List
from models import Card


class DataExporter:
    """Classe para exportar dados dos cards"""
    
    @staticmethod
    def export_to_csv(cards: List[Card], filename: str = None):
        """
        Exporta a lista de cards para um arquivo CSV
        
        Args:
            cards: Lista de cards para exportar
            filename: Nome do arquivo (opcional, padrão: timetracker_YYYYMMDD_HHMMSS.csv)
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"timetracker_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Card', 'Tempo Total', 'Hr Inicial', 'Hr Final', 'Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for card in cards:
                writer.writerow({
                    'Card': card.name,
                    'Tempo Total': card.get_formatted_time(),
                    'Hr Inicial': card.start_time or '',
                    'Hr Final': card.end_time or '',
                    'Status': 'Em execução' if card.is_running else 'Pausado'
                })
        
        return filename
    
    @staticmethod
    def export_daily_report(cards: List[Card], filename: str = None):
        """
        Gera um relatório diário formatado
        
        Args:
            cards: Lista de cards para incluir no relatório
            filename: Nome do arquivo (opcional)
        """
        if filename is None:
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"relatorio_{date_str}.txt"
        
        total_seconds = sum(card.elapsed_seconds for card in cards)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write(f"RELATÓRIO DE TEMPO - {datetime.now().strftime('%d/%m/%Y')}\n")
            f.write("="*60 + "\n\n")
            
            for card in cards:
                f.write(f"Card: {card.name or 'Sem nome'}\n")
                f.write(f"  Tempo: {card.get_formatted_time()}\n")
                if card.start_time:
                    f.write(f"  Início: {card.start_time}\n")
                if card.end_time:
                    f.write(f"  Fim: {card.end_time}\n")
                f.write("\n")
            
            f.write("-"*60 + "\n")
            f.write(f"TEMPO TOTAL: {hours:02d}:{minutes:02d}:00\n")
            f.write("="*60 + "\n")
        
        return filename


# Exemplo de uso futuro:
"""
Para adicionar botão de exportação na interface:

1. No main.py, adicionar botão:
   export_btn = QPushButton("💾 Exportar CSV")
   export_btn.clicked.connect(self.export_data)

2. Adicionar método na classe TimeTrackerApp:
   def export_data(self):
       from data_exporter import DataExporter
       cards = self.card_manager.get_all_cards()
       filename = DataExporter.export_to_csv(cards)
       QMessageBox.information(self, "Sucesso", f"Dados exportados para {filename}")
"""
