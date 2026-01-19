"""
Testes unitários para o Time Tracker
"""
import sys
import time
from models import Card
from card_manager import CardManager


def test_card_creation():
    """Testa criação de card"""
    print("✓ Testando criação de card...")
    card = Card(id=1, name="TEST-001")
    assert card.id == 1
    assert card.name == "TEST-001"
    assert card.is_running == False
    assert card.elapsed_seconds == 0
    print("  ✅ Card criado corretamente")


def test_card_timer():
    """Testa funcionamento do timer"""
    print("✓ Testando timer do card...")
    card = Card(id=1, name="TEST-001")
    
    # Iniciar timer
    card.start()
    assert card.is_running == True
    assert card.start_time is not None
    print("  ✅ Timer iniciado")
    
    # Simular passagem de tempo
    time.sleep(2)
    card.tick()
    assert card.elapsed_seconds >= 2
    print(f"  ✅ Tempo decorrido: {card.get_formatted_time()}")
    
    # Pausar timer
    card.pause()
    assert card.is_running == False
    assert card.end_time is not None
    print("  ✅ Timer pausado")


def test_card_manager():
    """Testa gerenciador de cards"""
    print("✓ Testando gerenciador de cards...")
    manager = CardManager()
    
    # Adicionar cards
    card1 = manager.add_card("CARD-001")
    card2 = manager.add_card("CARD-002")
    assert len(manager.get_all_cards()) == 2
    print("  ✅ Cards adicionados")
    
    # Selecionar todos
    manager.select_all(True)
    assert all(c.is_selected for c in manager.get_all_cards())
    print("  ✅ Seleção em massa funcionando")
    
    # Remover selecionados
    manager.remove_selected_cards()
    assert len(manager.get_all_cards()) == 0
    print("  ✅ Remoção de cards funcionando")


def test_formatted_time():
    """Testa formatação de tempo"""
    print("✓ Testando formatação de tempo...")
    card = Card(id=1)
    
    card.elapsed_seconds = 0
    assert card.get_formatted_time() == "00:00:00"
    
    card.elapsed_seconds = 65
    assert card.get_formatted_time() == "00:01:05"
    
    card.elapsed_seconds = 3661
    assert card.get_formatted_time() == "01:01:01"
    
    print("  ✅ Formatação de tempo correta")


def run_tests():
    """Executa todos os testes"""
    print("\n" + "="*50)
    print("  TIME TRACKER - TESTES UNITÁRIOS")
    print("="*50 + "\n")
    
    try:
        test_card_creation()
        test_card_timer()
        test_card_manager()
        test_formatted_time()
        
        print("\n" + "="*50)
        print("  ✅ TODOS OS TESTES PASSARAM!")
        print("="*50 + "\n")
        return 0
        
    except AssertionError as e:
        print(f"\n❌ ERRO: {e}\n")
        return 1
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
