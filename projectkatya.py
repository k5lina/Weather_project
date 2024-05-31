import ctypes
import os
import random
import sys
from win32api import GetSystemMetrics
from pyowm import OWM
from PyQt5.QtGui import QPixmap
from PyQt5 import uic  
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QInputDialog
from pogoda import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Обои по погоде')
        self.label_2.hide() #Прячем все лейблы и кнопки
        self.label_3.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.btn1.hide()
        self.btn2.hide()
        self.btn3.hide()
        self.pushbutton.clicked.connect(self.run) #При нажатии кнопки вызывается функция проверки города

    def set_wallpaper(self, path): #Установка фона рабочего стола
        import ctypes
        cs = ctypes.c_buffer(path.encode())
        SPI_SETDESKWALLPAPER = 0x14
        return ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, cs, 0)

    def weather(self, place): #Получение данных о погоде в определенном городе
        owm = OWM('c52242b2d4d80ae028d6e97b46ce1c39')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        return int(temp), w.detailed_status

    def check(self, status): #Функция, отвечающая за появление картинок 
        if 'snow' in status: # на экране для выбора обоев в зависимости от погоды
            d = 'C:/project/snow/' #Путь к папке с определенной погодой
            self.d1 = d + 's1.jpg' #Путь к файлу с картинкой
            self.d2 = d + 's2.jpg'
            self.d3 = d + 's3.jpg' 
            pixmap1 = QPixmap(self.d1) #Устанавливаем картинку на экране
            w = self.label_5.width() 
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3) #Устанавливаем размеры картинки
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw) # При нажатии кнопки вызывается функция
            self.btn2.clicked.connect(self.runw) # выбора обоев
            self.btn3.clicked.connect(self.runw)   
        elif 'clouds' in status: #Здесь аналогично
            d = 'C:/project/clouds/'
            self.d1 = d + 'cl1.jpg'
            self.d2 = d + 'cl2.jpg'
            self.d3 = d + 'cl3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width();
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width();
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width();
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)
        elif 'rain' in status:
            d = 'C:/project/rain/'
            self.d1 = d + 'r1.jpg'
            self.d2 = d + 'r2.jpg'
            self.d3 = d + 'r3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   
        elif 'thunderstorm' in status:
            d = 'C:/project/thunderstorm/'
            self.d1 = d + 't1.jpg'
            self.d2 = d + 't2.jpg'
            self.d3 = d + 't3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   
        elif 'clear' in status:
            d = 'C:/project/clear/'
            self.d1 = d + 's1.jpg'
            self.d2 = d + 's2.jpg'
            self.d3 = d + 's3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   
        elif 'mist' or 'fog' or 'smog' or 'haze' in status:
            d = 'C:/project/fog/'
            self.d1 = d + 'f1.jpg'
            self.d2 = d + 'f2.jpg'
            self.d3 = d + 'f3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   
        elif 'sand' or 'dust' in status:
            d = 'C:/project/dust/'
            self.d1 = d + 'd1.jpg'
            self.d2 = d + 'd2.jpg'
            self.d3 = d + 'd3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   
        elif 'squall' or 'tornado' in status:
            d = 'C:/project/tornado/'
            self.d1 = d + 't1.jpg'
            self.d2 = d + 't2.jpg'
            self.d3 = d + 't3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   
        elif 'drizzle' in status:
            d = 'C:/project/rain/'
            self.d1 = d + 'r1.jpg'
            self.d2 = d + 'r2.jpg'
            self.d3 = d + 'r3.jpg'
            pixmap1 = QPixmap(self.d1)
            w = self.label_5.width()
            h = self.label_5.height()
            pixmap1 = pixmap1.scaledToWidth(w * 3)
            pixmap1 = pixmap1.scaledToHeight(h * 3)
            self.label_5.setPixmap(pixmap1)
            self.label_5.show()
            pixmap2 = QPixmap(self.d2)
            w = self.label_6.width()
            h = self.label_6.height()
            pixmap2 = pixmap2.scaledToWidth(w * 3)
            pixmap2 = pixmap2.scaledToHeight(h * 3)
            self.label_6.setPixmap(pixmap2)
            self.label_6.show()
            pixmap3 = QPixmap(self.d3)
            w = self.label_7.width()
            h = self.label_7.height()
            pixmap3 = pixmap3.scaledToWidth(w * 3)
            pixmap3 = pixmap3.scaledToHeight(h * 3)
            self.label_7.setPixmap(pixmap3)
            self.label_7.show()
            self.btn1.clicked.connect(self.runw)
            self.btn2.clicked.connect(self.runw)
            self.btn3.clicked.connect(self.runw)   

    def run(self): #Функция, отвечающая за ввод города и проверяющая наличие города в базе
        self.a = self.lineEdit.text()
        try:
            temp, status = self.weather(self.a) #Получаем информацию о температуре и погоде в городе
        except:
            ctypes.windll.user32.MessageBoxW(None, u"Города нет в базе. Попробуйте еще раз", u"Ошибка!", 0)
            self.a = 0 #Если города нет в базе, выдает ошибку
            return
        self.label_3.setText('В городе ' + self.a + ' температура ' + str(temp) + '°C')
        self.label_3.show()
        self.label_2.show()
        self.label_4.show()
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.check(status)

    def runw(self): #Функция, отвечающая за выбор обоев из 3-х вариантов
        if '1' in self.sender().text():
            self.set_wallpaper(self.d1)
        if '2' in self.sender().text():
            self.set_wallpaper(self.d2)
        if '3' in self.sender().text():
            self.set_wallpaper(self.d3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
