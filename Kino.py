import webbrowser
from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
                                                   QLabel, QVBoxLayout, QHBoxLayout)

def get_film():
    webbrowser.open('https://hd.kinopoisk.ru/film/58ed444744414697ae88c0e585ed06a8?from_block=kp-button-suggest')
def get_film2():
    webbrowser.open('https://www.kinopoisk.ru/film/590286/')
def get_film3():
    webbrowser.open('https://www.kinopoisk.ru/series/717455/')
def get_film4():
    webbrowser.open('https://www.kinopoisk.ru/series/762087/')
def get_film5():
    webbrowser.open('https://www.kinopoisk.ru/series/283290/')
def get_film6():
    webbrowser.open('https://www.kinopoisk.ru/film/838/')

def get_random_film():
    film = choice(lst_films)
    if film == 'suprize':
        message = QMessageBox()
        message.setWindowTitle('Окно')
        message.setText('ПАСХАЛКА!!!')
        message.exec()
    else:
        webbrowser.open(film)



lst_films = ['https://hd.kinopoisk.ru/film/58ed444744414697ae88c0e585ed06a8?from_block=kp-button-suggest'
             'https://www.kinopoisk.ru/film/590286/'
             'https://www.kinopoisk.ru/series/717455/'
             'https://www.kinopoisk.ru/series/762087/'
             'https://www.kinopoisk.ru/series/283290/'
             'https://www.kinopoisk.ru/film/838/'
             'suprize']

app = QApplication([])
window = QWidget()
window.resize(400, 300)
window.setWindowTitle('Кинопоиск')

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

text = QLabel('Выберите фильм')
button1 = QPushButton('Три богатыря')
button2 = QPushButton('Бэтмен')
button3 = QPushButton('Третья мировая')
button4 = QPushButton('Футболисты')
button5 = QPushButton('Наруто')
button6 = QPushButton('Человек паук')
button7 = QPushButton('Рандом выбор')

button1.clicked.connect(get_film)
button2.clicked.connect(get_film2)
button3.clicked.connect(get_film3)
button4.clicked.connect(get_film4)
button5.clicked.connect(get_film5)
button6.clicked.connect(get_film6)


line1.addWidget(button1, alignment=Qt.AlignCenter)
line1.addWidget(button2, alignment=Qt.AlignCenter)
line1.addWidget(button3, alignment=Qt.AlignCenter)
line2.addWidget(button4, alignment=Qt.AlignCenter)
line2.addWidget(button5, alignment=Qt.AlignCenter)
line2.addWidget(button6, alignment=Qt.AlignCenter)
line3.addWidget(button7, alignment=Qt.AlignRight)

main_line.addWidget(text, alignment=Qt.AlignCenter)
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addLayout(line3)

window.setLayout(main_line)
window.show()
app.exec()
