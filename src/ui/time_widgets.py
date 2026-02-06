"""
Time Widgets - Interactive time display and picker components
"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QDialog, QSpinBox, QPushButton, QTimeEdit, QCalendarWidget
)
from PyQt6.QtCore import Qt, pyqtSignal, QTime
from PyQt6.QtGui import QCursor, QFont
from datetime import datetime


class PaddedSpinBox(QSpinBox):
    """QSpinBox que sempre exibe valores com zero à esquerda (formato 00-99) com botões customizados"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Esconde os botões padrão e cria botões customizados
        self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.setup_custom_buttons()
    
    def setup_custom_buttons(self):
        """Cria botões customizados com setas visíveis"""
        # Botão de incremento
        self.up_button = QPushButton("▲", self)
        self.up_button.setObjectName("timePickerCustomButton")
        self.up_button.setFixedSize(30, 32)
        self.up_button.clicked.connect(self.stepUp)
        self.up_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        # Botão de decremento  
        self.down_button = QPushButton("▼", self)
        self.down_button.setObjectName("timePickerCustomButton")
        self.down_button.setFixedSize(30, 32)
        self.down_button.clicked.connect(self.stepDown)
        self.down_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    
    def resizeEvent(self, event):
        """Posiciona os botões customizados"""
        super().resizeEvent(event)
        button_x = self.width() - 32
        self.up_button.move(button_x, 1)
        self.down_button.move(button_x, 33)
    
    def textFromValue(self, value: int) -> str:
        """Retorna o texto formatado com zero à esquerda"""
        return f"{value:02d}"
    
    def valueFromText(self, text: str) -> int:
        """Converte o texto de volta para inteiro"""
        return int(text)


class TimePickerDialog(QDialog):
    """Dialog moderno para selecionar horário com spinboxes grandes e intuitivos"""
    
    def __init__(self, initial_time: str = "", parent=None):
        super().__init__(parent)
        self.selected_time = initial_time
        self.setWindowTitle("Set Time")
        self.setObjectName("timePickerDialog")
        # Remove FramelessWindowHint to show standard window decorations
        self.setWindowFlags(Qt.WindowType.Dialog)
        
        # Aplica o stylesheet do parent para herdar o tema
        if parent and parent.styleSheet():
            self.setStyleSheet(parent.styleSheet())
        
        self.init_ui()
        
    def init_ui(self):
        """Inicializa a interface moderna do time picker"""
        self.setModal(True)
        self.setFixedSize(320, 300)
        
        # Container principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 20, 24, 20)
        main_layout.setSpacing(16)
        self.setLayout(main_layout)
        
        # Subtitle
        subtitle = QLabel("Select hours and minutes")
        subtitle.setObjectName("timePickerSubtitle")
        subtitle_font = subtitle.font()
        subtitle_font.setPointSize(10)
        subtitle.setFont(subtitle_font)
        main_layout.addWidget(subtitle)
        
        main_layout.addSpacing(8)
        
        # Parse initial time
        hour, minute = 0, 0
        if self.selected_time:
            try:
                hour, minute = map(int, self.selected_time.split(':'))
            except:
                current = QTime.currentTime()
                hour, minute = current.hour(), current.minute()
        else:
            current = QTime.currentTime()
            hour, minute = current.hour(), current.minute()
        
        # Time picker row with big spinboxes
        time_row = QHBoxLayout()
        time_row.setSpacing(4)
        
        # Hour spinbox
        hour_container = QVBoxLayout()
        hour_container.setSpacing(8)
        hour_label = QLabel("Hour")
        hour_label.setObjectName("timePickerLabel")
        hour_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hour_container.addWidget(hour_label)
        
        self.hour_spin = PaddedSpinBox()
        self.hour_spin.setObjectName("timePickerSpinBox")
        self.hour_spin.setRange(0, 23)
        self.hour_spin.setValue(hour)
        self.hour_spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hour_spin.setMinimumHeight(65)
        self.hour_spin.setMinimumWidth(120)
        self.hour_spin.lineEdit().setReadOnly(False)
        hour_spin_font = self.hour_spin.font()
        hour_spin_font.setPointSize(22)
        hour_spin_font.setBold(True)
        self.hour_spin.setFont(hour_spin_font)
        hour_container.addWidget(self.hour_spin)
        
        time_row.addLayout(hour_container)
        
        # Separator ":" - container para centralizar verticalmente
        separator_container = QVBoxLayout()
        separator_container.addSpacing(36)  # Espaço para alinhar com os spinboxes
        
        separator = QLabel(":")
        separator.setObjectName("timePickerSeparator")
        separator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sep_font = separator.font()
        sep_font.setPointSize(26)
        sep_font.setBold(True)
        separator.setFont(sep_font)
        separator_container.addWidget(separator)
        separator_container.addStretch()
        
        time_row.addLayout(separator_container)
        
        # Minute spinbox
        minute_container = QVBoxLayout()
        minute_container.setSpacing(8)
        minute_label = QLabel("Minute")
        minute_label.setObjectName("timePickerLabel")
        minute_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        minute_container.addWidget(minute_label)
        
        self.minute_spin = PaddedSpinBox()
        self.minute_spin.setObjectName("timePickerSpinBox")
        self.minute_spin.setRange(0, 59)
        self.minute_spin.setValue(minute)
        self.minute_spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minute_spin.setMinimumHeight(65)
        self.minute_spin.setMinimumWidth(120)
        self.minute_spin.lineEdit().setReadOnly(False)
        minute_spin_font = self.minute_spin.font()
        minute_spin_font.setPointSize(22)
        minute_spin_font.setBold(True)
        self.minute_spin.setFont(minute_spin_font)
        minute_container.addWidget(self.minute_spin)
        
        time_row.addLayout(minute_container)
        
        main_layout.addLayout(time_row)
        
        # Espaçamento
        main_layout.addSpacing(12)
        
        # Quick action - Now button
        now_btn = QPushButton("🕐 Set Current Time")
        now_btn.setObjectName("timePickerNowButton")
        now_btn.setMinimumHeight(40)
        now_btn.clicked.connect(self.set_current_time)
        main_layout.addWidget(now_btn)
        
        main_layout.addSpacing(8)
        
        # Action buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        
        button_layout.addStretch()
        
        # Cancel button
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("timePickerCancelButton")
        cancel_btn.setMinimumWidth(90)
        cancel_btn.setMinimumHeight(38)
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        # OK button
        ok_btn = QPushButton("Apply")
        ok_btn.setObjectName("timePickerOkButton")
        ok_btn.setMinimumWidth(90)
        ok_btn.setMinimumHeight(38)
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(self.accept_time)
        button_layout.addWidget(ok_btn)
        
        main_layout.addLayout(button_layout)
    
    def set_current_time(self):
        """Define o horário atual"""
        current = QTime.currentTime()
        self.hour_spin.setValue(current.hour())
        self.minute_spin.setValue(current.minute())
    
    def accept_time(self):
        """Aceita o horário selecionado"""
        hour = self.hour_spin.value()
        minute = self.minute_spin.value()
        self.selected_time = f"{hour:02d}:{minute:02d}"
        self.accept()
    
    def get_time(self) -> str:
        """Retorna o horário selecionado"""
        return self.selected_time


class EditableTimeLabel(QWidget):
    """Label de tempo que pode ser editado com duplo clique"""
    
    time_changed = pyqtSignal(str)  # Emite o novo horário
    
    def __init__(self, label_text: str, initial_time: str = ""):
        super().__init__()
        self.label_text = label_text
        self.current_time = initial_time
        self.dialog_open = False  # Flag para evitar múltiplas aberturas
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        self.setLayout(layout)
        
        # Label fixo com largura fixa para alinhamento
        self.label = QLabel(label_text)
        self.label.setObjectName("timeFieldLabel")
        self.label.setMinimumWidth(55)
        self.label.setMaximumWidth(55)
        layout.addWidget(self.label)
        
        # Valor do tempo (clicável)
        self.time_label = QLabel(self.current_time if self.current_time else "--:--")
        self.time_label.setObjectName("editableTimeValue")
        self.time_label.setMinimumWidth(50)
        self.time_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.time_label.setToolTip("Click to edit time")
        self.time_label.mousePressEvent = self.open_time_picker
        
        font = self.time_label.font()
        font.setFamily("Consolas, Monaco, monospace")
        font.setBold(True)
        self.time_label.setFont(font)
        
        layout.addWidget(self.time_label)
        layout.addStretch()
    
    def open_time_picker(self, event):
        """Abre o dialog de seleção de horário"""
        # Previne múltiplas aberturas
        if self.dialog_open:
            return
        
        event.accept()  # Previne propagação do evento
        self.dialog_open = True
        
        try:
            dialog = TimePickerDialog(self.current_time, self)
            dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
            
            result = dialog.exec()
            
            if result == QDialog.DialogCode.Accepted:
                new_time = dialog.get_time()
                self.set_time(new_time)
                self.time_changed.emit(new_time)
        finally:
            self.dialog_open = False
    
    def set_time(self, time_str: str):
        """Define o horário exibido"""
        self.current_time = time_str
        self.time_label.setText(time_str if time_str else "--:--")
    
    def get_time(self) -> str:
        """Retorna o horário atual"""
        return self.current_time


class TimeRangeWidget(QWidget):
    """Widget para exibir e editar intervalo de tempo (start e end)"""
    
    time_range_changed = pyqtSignal(str, str)  # (start_time, end_time)
    
    def __init__(self, card, on_time_changed_callback):
        super().__init__()
        self.card = card
        self.on_time_changed_callback = on_time_changed_callback
        
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 4, 25, 4)
        layout.setSpacing(4)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(layout)
        
        # Start time
        self.start_field = EditableTimeLabel("Start", self.card.start_time or "")
        self.start_field.time_changed.connect(self.on_start_time_changed)
        layout.addWidget(self.start_field)
        
        # End time or running indicator
        if self.card.is_running:
            running_label = QLabel("◷ In Progress...")
            running_label.setObjectName("runningLabel")
            layout.addWidget(running_label)
        else:
            self.end_field = EditableTimeLabel("End", self.card.end_time or "")
            self.end_field.time_changed.connect(self.on_end_time_changed)
            layout.addWidget(self.end_field)
    
    def on_start_time_changed(self, value: str):
        """Handler para mudança no start time"""
        # Usa o método do Card que recalcula elapsed_seconds
        self.card.update_start_time(value)
        self.on_time_changed_callback()
        self.time_range_changed.emit(self.card.start_time or "", self.card.end_time or "")
    
    def on_end_time_changed(self, value: str):
        """Handler para mudança no end time"""
        # Usa o método do Card que recalcula elapsed_seconds
        self.card.update_end_time(value)
        self.on_time_changed_callback()
        self.time_range_changed.emit(self.card.start_time or "", self.card.end_time or "")
    
    def update_times(self):
        """Atualiza os valores dos horários sem recriar o widget"""
        if hasattr(self, 'start_field'):
            if self.start_field.current_time != (self.card.start_time or ""):
                self.start_field.set_time(self.card.start_time or "")
        
        if hasattr(self, 'end_field') and not self.card.is_running:
            if self.end_field.current_time != (self.card.end_time or ""):
                self.end_field.set_time(self.card.end_time or "")


class EditableDateWidget(QWidget):
    """Widget que exibe uma data como label mas permite edição ao clicar"""
    
    date_changed = pyqtSignal()
    
    def __init__(self, card, on_date_changed_callback, parent=None):
        super().__init__(parent)
        self.card = card
        self.on_date_changed_callback = on_date_changed_callback
        self.init_ui()
        
    def init_ui(self):
        """Inicializa a interface do widget"""
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        
        # Label da data (aparência normal)
        date_text = self.card.created_date if self.card.created_date else datetime.now().strftime("%d/%m/%y")
        self.date_label = QLabel(date_text)
        self.date_label.setObjectName("editableDateLabel")
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.date_label.mousePressEvent = self.on_label_clicked
        layout.addWidget(self.date_label)
        
    def on_label_clicked(self, event):
        """Quando o label é clicado, abre um dialog para editar"""
        dialog = DateEditDialog(self.card.created_date or datetime.now().strftime("%d/%m/%y"), self)
        if dialog.exec():
            new_date = dialog.get_selected_date()
            if new_date:
                self.card.update_created_date(new_date)
                self.date_label.setText(new_date)
                self.date_changed.emit()
                if self.on_date_changed_callback:
                    self.on_date_changed_callback()


class DateEditDialog(QDialog):
    """Dialog com calendário moderno para editar data no formato dd/mm/yy"""
    
    def __init__(self, initial_date: str = "", parent=None):
        super().__init__(parent)
        self.selected_date = initial_date
        self.setWindowTitle("Select Date")
        self.setObjectName("dateEditDialog")
        self.setWindowFlags(Qt.WindowType.Dialog)
        
        # Aplica o stylesheet do parent para herdar o tema
        if parent and parent.styleSheet():
            self.setStyleSheet(parent.styleSheet())
        
        self.init_ui()
        
    def init_ui(self):
        """Inicializa a interface do dialog"""
        self.setModal(True)
        self.setFixedSize(420, 480)
        
        # Container principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(28, 24, 28, 24)
        main_layout.setSpacing(20)
        self.setLayout(main_layout)
        
        # Header
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)
        
        self.title = QLabel("📅 Select Date")
        self.title.setObjectName("calendarDialogTitle")
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header_layout.addWidget(self.title)
        
        # Selected date display
        from PyQt6.QtCore import QDate
        selected_qdate = QDate.currentDate()
        
        if self.selected_date:
            try:
                parts = self.selected_date.split('/')
                if len(parts) == 3:
                    day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
                    full_year = 2000 + year if year < 100 else year
                    selected_qdate = QDate(full_year, month, day)
            except:
                pass
        
        self.date_display = QLabel(selected_qdate.toString("dddd, MMMM d, yyyy"))
        self.date_display.setObjectName("calendarDateDisplay")
        self.date_display.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header_layout.addWidget(self.date_display)
        
        main_layout.addLayout(header_layout)
        
        # Divider
        divider = QLabel()
        divider.setObjectName("calendarDivider")
        divider.setFixedHeight(1)
        main_layout.addWidget(divider)
        
        # Calendar Widget
        self.calendar = QCalendarWidget()
        self.calendar.setObjectName("modernCalendar")
        self.calendar.setSelectedDate(selected_qdate)
        self.calendar.setGridVisible(False)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendar.setMinimumHeight(280)
        self.calendar.setMaximumHeight(320)
        
        # Update date display when selection changes
        self.calendar.selectionChanged.connect(self.update_date_display)
        
        main_layout.addWidget(self.calendar)
        main_layout.addSpacing(8)
        
        # Action buttons
        button_row = QHBoxLayout()
        button_row.setSpacing(12)
        
        button_row.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("calendarCancelButton")
        cancel_btn.setMinimumWidth(100)
        cancel_btn.setMinimumHeight(42)
        cancel_btn.clicked.connect(self.reject)
        button_row.addWidget(cancel_btn)
        
        ok_btn = QPushButton("Select")
        ok_btn.setObjectName("calendarOkButton")
        ok_btn.setMinimumWidth(100)
        ok_btn.setMinimumHeight(42)
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(self.accept)
        button_row.addWidget(ok_btn)
        
        main_layout.addLayout(button_row)
    
    def update_date_display(self):
        """Atualiza o display da data selecionada"""
        date = self.calendar.selectedDate()
        self.date_display.setText(date.toString("dddd, MMMM d, yyyy"))
        
    def get_selected_date(self) -> str:
        """Retorna a data selecionada no formato dd/mm/yy"""
        date = self.calendar.selectedDate()
        day = date.day()
        month = date.month()
        year = date.year() % 100
        return f"{day:02d}/{month:02d}/{year:02d}"
