# Contexto Técnico: Time Tracker

## Stack Tecnológico

### Tecnologias Principais

#### Python 3.8+
**Versão**: 3.8 mínimo, testado com 3.10+
**Propósito**: Linguagem de programação primária
**Por Que Foi Escolhido**:
- Compatibilidade multi-plataforma
- Ecossistema rico de bibliotecas
- Excelente integração com PyQt6
- Fácil distribuição com PyInstaller

#### PyQt6 6.6.0+
**Propósito**: Framework GUI
**Por Que Foi Escolhido**:
- Aparência nativa
- Multi-plataforma (Linux/Windows)
- Biblioteca rica de widgets
- Excelente documentação
- Performance e estabilidade

**Módulos Chave Utilizados**:
- `QtWidgets`: Componentes de UI principais
- `QtCore`: Sistema de eventos, timers, signals/slots
- `QtGui`: Gráficos e estilização

#### SQLite3
**Propósito**: Persistência de dados
**Por Que Foi Escolhido**:
- Integrado ao Python
- Zero configuração
- Baseado em arquivo (sem servidor)
- Compatível com ACID
- Perfeito para apps desktop de usuário único

### Build e Distribuição

#### PyInstaller 6.0.0+
**Propósito**: Criar executáveis standalone
**Configuração**: `TimeTracker.spec`
**Capacidades**:
- Empacota interpretador Python
- Inclui todas as dependências
- Cria executável único
- Builds multi-plataforma

## Configuração de Desenvolvimento

### Pré-requisitos

#### Linux
```bash
# Requisitos do sistema
- Ubuntu 20.04+ ou equivalente
- Python 3.8+
- python3-venv
- python3-full

# Instalação
sudo apt update
sudo apt install python3-venv python3-full
```

#### Windows
```cmd
# Requisitos do sistema
- Windows 10/11
- Python 3.8+ (de python.org)
- Adicionar Python ao PATH durante instalação
```

### Configuração do Ambiente

#### Criação de Ambiente Virtual
```bash
# Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate.bat
```

#### Instalação de Dependências
```bash
pip install -r requirements.txt
```

**Dependências**:
- `PyQt6>=6.6.0`: Framework GUI
- `pyinstaller>=6.0.0`: Construtor de executáveis

### Executando a Aplicação

#### Modo de Desenvolvimento
```bash
# Linux
./run.sh
# ou
python3 main.py

# Windows
run.bat
# ou
python main.py
```

#### Modo de Build
```bash
# Linux
./build.sh

# Windows
build.bat
```

## Restrições Técnicas

### Limitações de Plataforma

#### Linux
- Requer servidor de display (X11/Wayland)
- Arquivo desktop para integração com sistema
- Dependências de pacote para PyQt6

#### Windows
- Requer Windows 10 ou posterior
- Pode precisar de Visual C++ Redistributable
- Configuração de PATH crítica

### Restrições de Performance
- Precisão do timer: granularidade de 1 segundo
- Intervalo de auto-save: 5 segundos
- Banco de dados: SQLite de arquivo único (sem problemas de concorrência)
- Memória: Footprint mínimo (< 100MB típico)

### Restrições de Segurança
- Armazenamento de dados apenas local
- Sem encriptação (sistema de usuário único)
- Permissões de sistema de arquivos aplicam
- Sem comunicação de rede

## Dependências

### Dependências de Runtime
```
PyQt6>=6.6.0
```

### Dependências de Build
```
pyinstaller>=6.0.0
```

### Dependências do Sistema

#### Linux
- `python3-venv`: Suporte a ambiente virtual
- `python3-full`: Instalação completa do Python
- Servidor de display (X11/Wayland)
- Plugins de plataforma Qt

#### Windows
- Instalador Python 3.8+
- Visual C++ Redistributable (geralmente incluído)

## Padrões de Uso de Ferramentas

### Padrões PyQt6

#### Conexões Signal/Slot
```python
# Conectar signals a slots
button.clicked.connect(self.on_button_clicked)

# Signals customizados
class MyWidget(QWidget):
    custom_signal = pyqtSignal(str)
    
    def emit_signal(self):
        self.custom_signal.emit("data")
```

#### Uso de Timer
```python
# Criar timer repetitivo
self.timer = QTimer()
self.timer.timeout.connect(self.update_display)
self.timer.start(1000)  # milissegundos
```

#### Gerenciamento de Layout
```python
# Layout vertical
layout = QVBoxLayout()
layout.addWidget(widget)
layout.addStretch()
```

### Padrões SQLite

#### Gerenciamento de Conexão
```python
import sqlite3

# Conectar
conn = sqlite3.connect('timetracker.db')
conn.row_factory = sqlite3.Row  # Acesso tipo dict

# Executar
cursor = conn.cursor()
cursor.execute("SELECT * FROM cards")
results = cursor.fetchall()

# Sempre fechar
conn.close()
```

#### Gerenciamento de Schema
```python
# Criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY,
        name TEXT,
        start_time TEXT,
        end_time TEXT,
        elapsed INTEGER
    )
''')
conn.commit()
```

### Padrões PyInstaller

#### Build Básico
```bash
pyinstaller --onefile --windowed main.py
```

#### Configuração Avançada (TimeTracker.spec)
```python
# Arquivo spec para customização
a = Analysis(['main.py'])
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, name='TimeTracker')
```

## Detalhes da Estrutura de Arquivos

### Arquivos de Configuração
- `requirements.txt`: Dependências Python
- `TimeTracker.spec`: Configuração PyInstaller
- `timetracker.desktop`: Integração desktop Linux

### Scripts de Build
- `install.sh / install.bat`: Setup de ambiente virtual e dependências
- `run.sh / run.bat`: Executar aplicação em modo desenvolvimento
- `build.sh / build.bat`: Criar executável standalone
- `test_windows.bat`: Testes específicos para Windows

### Arquivos de Dados
- `timetracker.db`: Banco de dados SQLite (criado em runtime)
- Diretório de dados do usuário: Mesmo local do executável

## Workflow de Desenvolvimento

### Ciclo de Desenvolvimento Padrão
1. Ativar ambiente virtual
2. Fazer mudanças no código
3. Executar com `python main.py`
4. Testar funcionalidade
5. Fazer commit das mudanças
6. Fazer build do executável para distribuição

### Workflow de Build
1. Garantir que todas mudanças estão commitadas
2. Executar script de build (`./build.sh` ou `build.bat`)
3. Testar executável no diretório `dist/`
4. Verificar na plataforma alvo
5. Distribuir executável

### Atualizações de Schema do Banco de Dados
1. Modificar schema em `database.py`
2. Adicionar lógica de migração se necessário
3. Testar com banco de dados fresco
4. Testar com banco de dados existente
5. Documentar mudanças

## Considerações Específicas de Plataforma

### Linux
- **Integração Desktop**: Usa arquivo `.desktop` em `utils/`
- **Permissões**: Scripts precisam de permissão de execução (`chmod +x`)
- **Dependências**: Pode precisar de bibliotecas Qt do sistema
- **Distribuição**: Potencial para AppImage ou pacote DEB

### Windows
- **Política de Execução**: Pode precisar permitir execução de scripts
- **Problemas de Path**: Barras invertidas em caminhos de arquivo
- **UAC**: Pode precisar de admin para instalação
- **Distribuição**: EXE único ou pacote instalador

## Variáveis de Ambiente
Atualmente nenhuma requerida. Toda configuração no código.

## Logging e Debugging

### Abordagem Atual
- Declarações print para debugging
- Mensagens de warning do Qt no console
- Erros SQLite capturados e exibidos

### Aprimoramentos Futuros
- Logging estruturado com módulo `logging` do Python
- Rotação de arquivos de log
- Modos debug vs produção
- Profiling de performance

## Considerações de Performance

### Pontos de Otimização
- Atualizações de timer: Apenas repintar widgets alterados
- Banco de dados: Operações em lote quando possível
- Auto-save: Apenas salvar cards modificados
- UI: Minimizar recálculos de layout

### Uso de Recursos
- CPU: Baixo (apenas atualizações de timer)
- Memória: < 100MB típico
- Disco: Mínimo (banco SQLite pequeno)
- Rede: Nenhum

## Problemas Técnicos Conhecidos
- Nenhum atualmente documentado
- Rastrear em `progress.md` conforme surgem

## Componentes de UI Customizados

### PaddedSpinBox
**Localização**: `src/ui/time_widgets.py`
**Propósito**: QSpinBox com display zero-padded (00-99) e botões de seta customizados

**Recursos Chave**:
- Display de número zero-padded via `textFromValue()`
- Controles QPushButton customizados com setas Unicode (▲ ▼)
- Posicionamento dinâmico de botões via `resizeEvent()`
- Símbolo NoButtons definido para ocultar controles padrão
- Dimensões mínimas: 120px largura × 65px altura (acomoda fonte 22pt bold)

**Notas de Implementação**:
- Triângulos CSS eram não confiáveis entre temas
- Abordagem QPushButton fornece melhor controle e visibilidade
- Botões posicionados em (width-32, 1) e (width-32, 33)
- Usa objectName "timePickerCustomButton" para estilização

### TimePickerDialog
**Localização**: `src/ui/time_widgets.py`
**Propósito**: Interface moderna de seleção de tempo

**Recursos Chave**:
- Controles PaddedSpinBox grandes para hora/minuto
- Separador ":" centralizado verticalmente usando layout de container com 36px de espaçamento superior
- Botão de ação rápida "Set Current Time"
- Diálogo herda stylesheet do parent via `setStyleSheet(parent.styleSheet())`
- ObjectName "timePickerDialog" para estilização específica
- Qt.WindowType.Dialog padrão para arrasto nativo de janela

**Harmonia de Tema (Dark)**:
- Background: #0d1117 (base), #161b22 (controles)
- Borders: #21262d (sutil), #30363d (hover)
- Accent: #58a6ff (azul primário)
- Text: #e6edf3 (primário), #8b949e (secundário)

### DateEditDialog  
**Localização**: `src/ui/time_widgets.py`
**Propósito**: Seleção de data baseada em calendário

**Recursos Chave**:
- QCalendarWidget com estilização moderna
- Label de display de data mostrando seleção formatada
- Diálogo herda stylesheet do parent
- ObjectName "dateEditDialog" para estilização específica
- Qt.WindowType.Dialog padrão para arrasto nativo
- Paleta de cores consistente com TimePickerDialog

### EditableDateWidget
**Localização**: `src/ui/time_widgets.py`
**Propósito**: Label de data clicável que abre DateEditDialog

**Recursos Chave**:
- Clique único para editar (mudado de clique duplo para melhor UX)
- Feedback visual de hover
- Formato de data: dd/mm/yy
- Previne múltiplas instâncias de diálogo com flag dialog_open

### TimeRangeWidget
**Localização**: `src/ui/time_widgets.py`
**Propósito**: Entrada dupla de tempo (horários de início/fim)

**Recursos Chave**:
- Duas instâncias de TimePickerWidget
- Layout horizontal com espaçamento
- Sinais individuais de mudança de tempo
- Estilização consistente com tema principal

## Padrões de Design UI/UX Estabelecidos

### Herança de Estilização de Diálogo
Todas subclasses de QDialog devem herdar o stylesheet do parent:
```python
if parent and parent.styleSheet():
    self.setStyleSheet(parent.styleSheet())
```
Isso garante consistência de tema ao alternar entre modos claro/escuro.

### Melhores Práticas de Controles Customizados
- Usar QPushButton ao invés de pseudo-elementos CSS quando confiabilidade é crítica
- Símbolos Unicode (▲ ▼) são mais confiáveis que triângulos de border CSS
- Posicionamento dinâmico via `resizeEvent()` para layouts responsivos

### Estratégia de Alinhamento Vertical
Usar layouts de container com `addSpacing()` para centralização vertical precisa:
```python
container = QVBoxLayout()
container.addSpacing(36)  # Offset para alinhar com outros elementos
container.addWidget(widget)
container.addStretch()
```

### Diretrizes de Harmonia de Cores
**Paleta Tema Dark**:
- #0d1117: Background base
- #161b22: Superfícies elevadas (cards, controles)
- #21262d: Borders sutis e estados de hover
- #30363d: Estados de hover interativos
- #58a6ff: Accent primário (links, highlights)
- #e6edf3: Texto primário
- #8b949e: Texto secundário

**Dimensionamento de SpinBox para Fontes Bold**:
- Fonte 22pt bold requer largura mínima de 120px
- Padding: 10px 36px 10px 20px (previne truncamento de número)
- Altura: mínimo 65px para interação confortável
