"""
Time Tracker - Aplicação Desktop
Interface gráfica moderna para gerenciamento de tempo por card
"""
import sys
from PyQt6.QtWidgets import QApplication
from src.application import TimeTrackerController


def main():
    """Função principal - Entry point da aplicação"""
    app = QApplication(sys.argv)
    app.setApplicationName("timeTracker")
    app.setDesktopFileName("timetracker.desktop")
    app.setStyle('Fusion')
    
    controller = TimeTrackerController()
    controller.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
