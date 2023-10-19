import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore

def run_web_search_app():
    app = QApplication(sys.argv)
    window = WebSearchApp()
    window.show()
    sys.exit(app.exec_())

class WebSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Web Arama Uygulaması')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color:silver;")

        layout = QVBoxLayout()
        layout_input = QHBoxLayout()

        back_icon = QIcon('back.png')   
        self.back_button = QPushButton(back_icon, '')
        self.back_button.setFixedSize(30, 30)  
        self.back_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.back_button.setStyleSheet('border:none; outline:none;')

        forward_icon = QIcon('forward.png')
        self.forward_button = QPushButton(forward_icon, '')
        self.forward_button.setFixedSize(30, 30)   
        self.forward_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.forward_button.setStyleSheet('border:none; outline:none;')
        
        layout_input.addWidget(self.back_button)
        layout_input.addWidget(self.forward_button)

        reload_icon = QIcon('refresh-arrow.png')
        self.reload_button = QPushButton(reload_icon, '')
        self.reload_button.setFixedSize(30, 30)   
        self.reload_button.clicked.connect(self.reload)
        self.reload_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.reload_button.setStyleSheet('border:none; outline:none;')
        layout_input.addWidget(self.reload_button)

        self.search_input = QLineEdit()
        self.search_input.returnPressed.connect(self.search)
        self.search_input.setFixedHeight(30)
        self.search_input.setPlaceholderText('Search...')
        self.search_input.setStyleSheet('background-color:skyblue; font-size:14px; border-radius:15px; border:3px solid black; padding-left:10px; padding-bottom:3px; font-weight: bold;')
        layout_input.addWidget(self.search_input)
        layout.addLayout(layout_input)

        searc_icon = QIcon('search.png')
        self.search_button = QPushButton(searc_icon, '')
        self.search_button.setFixedSize(100, 30)  
        self.search_button.clicked.connect(self.search)
        self.search_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.search_button.setStyleSheet('QPushButton{background-color:cornflowerblue; border:3px solid black; border-radius:5px} QPushButton:hover{background-color:powderblue;}')
        layout_input.addWidget(self.search_button)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        self.central_widget.setLayout(layout)

        self.showMaximized()

    def search(self):
        search_query = self.search_input.text()
        url = f'https://www.google.com/search?q={search_query}'
        self.web_view.setUrl(QUrl(url))
        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button.clicked.connect(self.web_view.forward)

    def reload(self):
        self.web_view.reload()

if __name__ == '__main__':
    run_web_search_app()
