import sys
import pyodbc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtCore import Qt

server = 'servername'
database = 'databasename'

class HotelApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('SQL Server Interface')
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel('Database Table')
        self.layout.addWidget(self.label)

        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        self.button_width = 150  
        self.button_height = 40  
        self.button_font_size = 11
        self.button_font_weight = 'bold'

        self.addButton = QPushButton('Add')
        self.addButton.setStyleSheet(f"background-color: green; color: white; font-size: {self.button_font_size}px; font-weight: {self.button_font_weight};")
        self.addButton.clicked.connect(self.addingDataWindow)
        self.addButton.setFixedSize(self.button_width, self.button_height) 
        self.layout.addWidget(self.addButton, alignment=Qt.AlignCenter | Qt.AlignHCenter)

        self.showButton = QPushButton('Show and Refresh Table')
        self.showButton.setStyleSheet(f"background-color: green; color: white; font-size: {self.button_font_size}px; font-weight: {self.button_font_weight};")
        self.showButton.clicked.connect(self.refresh)
        self.showButton.setFixedSize(self.button_width, self.button_height) 
        self.layout.addWidget(self.showButton, alignment=Qt.AlignCenter | Qt.AlignHCenter)

        self.updateButton = QPushButton('Update Table')
        self.updateButton.setStyleSheet(f"background-color: green; color: white; font-size: {self.button_font_size}px; font-weight: {self.button_font_weight};")
        self.updateButton.clicked.connect(self.updatingDataWindow)
        self.updateButton.setFixedSize(self.button_width, self.button_height) 
        self.layout.addWidget(self.updateButton, alignment=Qt.AlignCenter | Qt.AlignHCenter)

        self.deleteButton = QPushButton('Delete')
        self.deleteButton.setStyleSheet(f"background-color: red; color: white; font-size: {self.button_font_size}px; font-weight: {self.button_font_weight};")
        self.deleteButton.clicked.connect(self.deleteData)
        self.deleteButton.setFixedSize(self.button_width, self.button_height) 
        self.layout.addWidget(self.deleteButton, alignment=Qt.AlignCenter | Qt.AlignHCenter)

        self.central_widget.setLayout(self.layout)
        self.connection_string = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database
        self.conn = None


    def refresh(self):
        try:
            if not self.conn:
                self.conn = pyodbc.connect(self.connection_string)

            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM HotelReservation')
            
            column_names = [column[0] for column in cursor.description]
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            
            data = cursor.fetchall()

            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(column_names))

            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)
        except Exception as e:
            print("Error:", str(e))
    

    def addingDataWindow(self):
        input_dialog = DataAddDialog(self)
        input_dialog.exec_()
        self.refresh()
        

    def updatingDataWindow(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            return

        row = selected_items[0].row()
        data = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
        update_dialog = DataUpdateDialog(self, data)
        update_dialog.exec_()
        self.refresh()
        

    def deleteData(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            return
        
        row_id = selected_items[0].text()
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirmation")
        confirm_dialog.setText(f"Do you want to delete the selected information?\nHotel ID : {row_id}")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = confirm_dialog.exec_()
        
        if result == QMessageBox.Yes:
            try:
                if not self.conn:
                    self.conn = pyodbc.connect(self.connection_string)

                query = 'DELETE FROM HotelReservation WHERE HotelID = ?'
                cursor = self.conn.cursor()
                cursor.execute(query, row_id)
                self.conn.commit()
                self.refresh()
            except Exception as e:
                print("Error:", str(e))
            finally:
                pass


class DataAddDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Add Data')
        self.setGeometry(200, 200, 400, 200)
        self.layout = QVBoxLayout()
        self.input_fields = []

        cursor = pyodbc.connect(self.parent.connection_string).cursor()
        cursor.execute('SELECT * FROM HotelReservation')
        column_names = [column[0] for column in cursor.description]
        
        for column_name in column_names:
            label = QLabel(column_name)
            input_field = QLineEdit()
            self.layout.addWidget(label)
            self.layout.addWidget(input_field)
            self.input_fields.append(input_field)

        self.saveButton = QPushButton('Save')
        self.saveButton.clicked.connect(self.save)
        self.layout.addWidget(self.saveButton)
        self.setLayout(self.layout)


    def save(self):
        try:
            values = [field.text() for field in self.input_fields]
            conn = pyodbc.connect(self.parent.connection_string)
            query = 'INSERT INTO HotelReservation VALUES (?, ?, ?, ?, ?)' 
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            
            self.close()
        except Exception as e:
            print("Error:", str(e))


class DataUpdateDialog(QDialog):
    def __init__(self, parent, data):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Update Data')
        self.setGeometry(200, 200, 400, 200)
        self.layout = QVBoxLayout()
        self.input_fields = []

        cursor = pyodbc.connect(self.parent.connection_string).cursor()
        cursor.execute('SELECT * FROM HotelReservation')
        column_names = [column[0] for column in cursor.description]
        
        for i, column_name in enumerate(column_names):
            label = QLabel(column_name)
            input_field = QLineEdit()
            input_field.setText(data[i])
            self.layout.addWidget(label)
            self.layout.addWidget(input_field)
            self.input_fields.append(input_field)

        self.saveButton = QPushButton('Save')
        self.saveButton.clicked.connect(self.save)
        self.layout.addWidget(self.saveButton)
        self.setLayout(self.layout)


    def save(self):
        try:
            values = [field.text() for field in self.input_fields]
            conn = pyodbc.connect(self.parent.connection_string)
            query = 'UPDATE HotelReservation SET MemberName = ?, Room = ?, Day = ?, ReservationDate = ? WHERE HotelID = ?'
            
            cursor = conn.cursor()
            values.append(values[0]) 
            del values[0] 
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            
            self.close()
        except Exception as e:
            print("Error:", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec_())
