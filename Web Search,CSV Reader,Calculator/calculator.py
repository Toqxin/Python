import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')
        central_widget = QWidget()
        central_widget.setStyleSheet('background-color:dimgrey;')
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.returnPressed.connect(self.calculate)
        self.input_box.setStyleSheet("font-size: 20px; width:400px; height:40px; border:2px solid black; background-color:white;")
        input_layout.addWidget(self.input_box)
        layout.addLayout(input_layout)


        buttons_layout = QVBoxLayout()
        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'DEL']  
        ]

        for row in button_grid:
            row_layout = QHBoxLayout()

            for button in row:
                button_obj = QPushButton(button)

                if button == 'C':
                    button_obj.clicked.connect(self.clear_input)

                elif button == 'DEL': 
                    button_obj.clicked.connect(self.clear_last_input)

                else:
                    button_obj.clicked.connect(self.button_click)

                button_obj.setStyleSheet("QPushButton{font-size: 24px; height:70px; font-weight:bold; border:2px solid black; background-color:orange; border-radius:15px;} QPushButton:hover{background-color:#FFE4C4;}")
                row_layout.addWidget(button_obj)
            buttons_layout.addLayout(row_layout)

        layout.addLayout(buttons_layout)
        central_widget.setLayout(layout)
        layout.addStretch(1)
        input_layout.addStretch(1)

    def button_click(self):
        button_text = self.sender().text()
        
        if button_text == '=':
            try:
                result = eval(self.input_box.text())
                self.input_box.setText(str(result))
            except:
                self.input_box.setText('Error')
        else:
            self.input_box.setText(self.input_box.text() + button_text)

    def clear_input(self):
        self.input_box.clear()

    def clear_last_input(self):
        current_text = self.input_box.text()
        self.input_box.setText(current_text[:-1])  

    def calculate(self):
        current_text = self.input_box.text()
        try:
            result = eval(current_text)
            self.input_box.setText(str(result))
        except:
            self.input_box.setText('Error')

def run_calculator_app():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_calculator_app()
