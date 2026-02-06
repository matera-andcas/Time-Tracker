"""
Icon Utils - Funções utilitárias para manipulação de ícones SVG
"""
import os
import sys
from PyQt6.QtCore import Qt, QByteArray, QSize
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer


def get_icon_path(filename: str) -> str:
    """Retorna o caminho completo para um arquivo de ícone"""
    if getattr(sys, 'frozen', False):
        # Rodando como executável PyInstaller
        base_dir = sys._MEIPASS
    else:
        # Rodando como script Python normal
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base_dir, 'icon', filename)


def create_colored_icon(svg_filename: str, color: str = "#000023", size: int = 24) -> QIcon:
    """Cria um QIcon a partir de um arquivo SVG com cor customizada"""
    svg_path = get_icon_path(svg_filename)
    
    try:
        with open(svg_path, 'r') as f:
            svg_content = f.read()
        
        # Substitui a cor do fill no SVG
        svg_content = svg_content.replace('fill="#1C274C"', f'fill="{color}"')
        
        # Cria um QPixmap a partir do SVG modificado
        svg_bytes = QByteArray(svg_content.encode())
        renderer = QSvgRenderer(svg_bytes)
        
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        
        return QIcon(pixmap)
    except Exception as e:
        print(f"Erro ao carregar ícone {svg_filename}: {e}")
        return QIcon()
