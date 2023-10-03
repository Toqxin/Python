import sys
import wikipediaapi
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox, QMenu, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WikipediaSearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.language = 'en'
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wikipedia Search App')
        self.icon = QIcon('wiki.png')  
        self.setWindowIcon(self.icon)
        self.setStyleSheet("background-color: grey;")
        self.setGeometry(600, 100, 900, 700)

        main_layout = QVBoxLayout(self)

        language_search_layout = QHBoxLayout()

        self.search_input = QTextEdit()
        self.search_input.setPlaceholderText('Search...')
        self.search_input.setFixedHeight(30) 
        self.search_input.setStyleSheet("font-family: 'Garamond, serif'; font-size: 15px; background-color: darkslategray; color: white; font-weight: bold; border: 3px solid black;")
        self.search_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        language_search_layout.addWidget(self.search_input)

        self.language_button = QPushButton('Language 🌐')
        self.language_button.setStyleSheet("QPushButton{font-family:'Garamond, serif'; font-size: 15px; background-color: darkslategray; color: white; font-weight: bold; border: 3px solid black;} QPushButton:hover{background-color: teal;}")
        self.language_button.setFixedWidth(200)
        self.language_button.setFixedHeight(30)
        self.language_button.clicked.connect(self.show_language_menu)
        language_search_layout.addWidget(self.language_button)


        self.language_menu = QMenu(self.language_button)
        self.language_menu.setStyleSheet("QMenu{font-family:'Garamond, serif'; font-size: 15px; background-color: darkslategray; color: white; font-weight: bold; border-width: 0 6px 6px 3px; border-style: solid; border-color: black; text-align:center;}"
                                        "QMenu:item{padding:10px 50px 10px 50px;}"
                                        "QMenu:item:selected{background-color: teal;}")
        
        self.tr_action = self.language_menu.addAction('Türkçe')
        self.tr_action.triggered.connect(lambda: self.set_language('tr'))
        self.en_action = self.language_menu.addAction('English')
        self.en_action.triggered.connect(lambda: self.set_language('en'))
        self.de_action = self.language_menu.addAction('Deutsch')
        self.de_action.triggered.connect(lambda: self.set_language('de'))
        self.ru_action = self.language_menu.addAction('Русский')
        self.ru_action.triggered.connect(lambda: self.set_language('ru'))
        self.es_action = self.language_menu.addAction('Español')
        self.es_action.triggered.connect(lambda: self.set_language('es'))
        main_layout.addLayout(language_search_layout)

        self.search_button = QPushButton('Search 📡')
        self.search_button.clicked.connect(self.search_wikipedia)
        self.search_button.setFixedWidth(200)
        self.search_button.setFixedHeight(30)
        self.search_button.setStyleSheet("QPushButton{font-family: 'Garamond, serif'; font-size: 15px; background-color: darkslategray; color: white; font-weight: bold; border: 3px solid black;} QPushButton:hover {background-color: teal;}")
        main_layout.addWidget(self.search_button)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("font-family: 'Garamond, serif'; font-size: 15px;background-color: darkslategray; color: white; font-weight: bold; border: 3px solid black;")
        main_layout.addWidget(self.result_display)

        self.exit_button = QPushButton('Exit 🧹..')
        self.exit_button.clicked.connect(self.exit_message)
        self.exit_button.setStyleSheet("QPushButton{font-family: 'Garamond, serif'; font-size: 15px; background-color: red; color: white; font-weight: bold; border: 3px solid black;} QPushButton:hover {background-color: darkred;}")
        self.exit_button.setFixedWidth(100)
        self.exit_button.setFixedHeight(30)
        main_layout.addWidget(self.exit_button)

        self.setLayout(main_layout)

    def search_wikipedia(self):
        search_text = self.search_input.toPlainText()
        if not search_text.strip():
            return

        wiki_wiki = wikipediaapi.Wikipedia(user_agent='wikipeiAI', language=self.language)
        page = wiki_wiki.page(search_text)

        if page.exists():
            content = page.text
            self.result_display.setPlainText(content)
        else:
            self.result_display.setPlainText(f"{search_text} no Wikipedia page about it was found.")

    def exit_message(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Wikipedia Search App')
        self.msg.setText('Exiting...')
        self.icon = QIcon('wiki.png')
        self.pixmap = self.icon.pixmap(70, 70)  
        self.msg.setWindowIcon(self.icon) 
        self.msg.setIconPixmap(self.pixmap)
        self.msg.setStyleSheet("background-color: teal; font-family: 'Garamond, serif'; font-size: 15px; font-weight: bold; width:150px;")
       
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ok_button = self.msg.button(QMessageBox.Ok)
        cancel_button = self.msg.button(QMessageBox.Cancel)
        ok_button.setStyleSheet("QPushButton{background-color: slategray; color: white;} QPushButton:hover {background-color: dimgray;}")
        cancel_button.setStyleSheet("QPushButton{background-color: red; color: white;} QPushButton:hover {background-color: darkred;}")
        self.result = self.msg.exec_()

        if self.result == QMessageBox.Ok:
            self.close_app()

    def close_app(self):
        self.close()
    
    def show_language_menu(self):
        self.language_menu.exec_(self.language_button.mapToGlobal(self.language_button.rect().bottomLeft()))
    
    def set_language(self, language):
        self.language = language
        self.language_button.setText(f'Language 🌐 ({language})')
        self.search_wikipedia()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WikipediaSearchApp()
    window.show()
    sys.exit(app.exec_())