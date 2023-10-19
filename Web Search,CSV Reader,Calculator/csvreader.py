import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QFileDialog, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class CSVViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('CSV Viewer')
        self.setGeometry(100, 100, 800, 900)

        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet('background-color:DimGrey;')
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.load_button = QPushButton('Upload CSV File', self)
        self.load_button.setStyleSheet('QPushButton{background-color:CadetBlue; font-weight:bold; font-size:14px; color:white;}QPushButton:hover{background-color:seagreen;}')
        self.load_button.clicked.connect(self.loadCSV)
        self.layout.addWidget(self.load_button)
        
        self.table_widget = QTableWidget(self)
        self.table_widget.setStyleSheet('background-color:SteelBlue;')
        self.layout.addWidget(self.table_widget)

        self.show()

    def loadCSV(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select CSV File', '', 'CSV Files (*.csv);;All Files (*)', options=options)

        if file_path:
            data = pd.read_csv(file_path, encoding='iso-8859-9')

            self.table_widget.setRowCount(data.shape[0])
            self.table_widget.setColumnCount(data.shape[1])

            for i, column_name in enumerate(data.columns):
                self.table_widget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))

                for j, cell_value in enumerate(data[column_name]):
                    item = QTableWidgetItem(str(cell_value))
                    
                    if j % 2 == 0: 
                        item.setBackground(QColor('DarkSlateGrey'))
                        item.setForeground(QColor('white'))
                    else: 
                        item.setBackground(QColor('SlateGrey'))
                        item.setForeground(QColor('white'))
                    self.table_widget.setItem(j, i, item)

           
            self.table_widget.resizeColumnsToContents()
            self.table_widget.resizeRowsToContents()
            self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

def csvrun():
    app = QApplication(sys.argv)
    window = CSVViewer()
    sys.exit(app.exec_())

if __name__ == '__main__':
    csvrun()
