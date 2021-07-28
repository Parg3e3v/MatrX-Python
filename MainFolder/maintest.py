import speech_recognition as sr
import time
import datetime
import webbrowser
import pyttsx3
import random
import os
import sys
from menu_2 import Ui_Dialog
from cmdlist import Ui_List
from updateMenu import Ui_Update
from log import Ui_Log
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMenu, QSystemTrayIcon
from PyQt5.QtGui import QIcon
import threading
from pyttsx3.drivers import sapi5
import requests
from bs4 import BeautifulSoup as BS


#    Version
versionMain = '0.0.4'


r = requests.get('https://matrx.herokuapp.com/')
html = BS(r.content, 'html.parser')

for el in html.select('.version > p > a'):
	vers = el.text

if vers != versionMain:
	print('update avilable')

#           UrlDownload

for el in html.select('.url > a'):
	urlDown = el.text

#           MatrX
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

#           tray

trayIcon = QSystemTrayIcon(QIcon('./icon/MatrX_Tray3.png'), parent=app)
trayIcon.setToolTip('MatrX')


#           List

appL = QtWidgets.QApplication(sys.argv)
ListL = QtWidgets.QDialog()
uiL = Ui_List()
uiL.setupUi(ListL)

#           Update
appUpdate = QtWidgets.QApplication(sys.argv)
Up = QtWidgets.QDialog()
uiU = Ui_Update()
uiU.setupUi(Up)

#           Login

appLog = QtWidgets.QApplication(sys.argv)
Log = QtWidgets.QDialog()
uiLog = Ui_Log()
uiLog.setupUi(Log)

#           Queu

uiLog.label.setText(f"v.{versionMain} alpha")
Dialog.setWindowTitle(f"MatrX v{versionMain} Alpha")
ui.label.setText(f"v.{versionMain} alpha")
uiU.label.setText(f"v.{versionMain} alpha")
uiL.label.setText(f"v.{versionMain} alpha")

global queue
 
class Queue(object):
 
    def __init__(self):
        self.item = []
 
    def __str__(self):
        return "{}".format(self.item)
 
    def __repr__(self):
        return "{}".format(self.item)
 
    def enque(self, item):
        """
        Insert the elements in queue
        :param item: Any
        :return: Bool
        """
        self.item.insert(0, item)
        return True
 
    def size(self):
        """
        Return the size of queue
        :return: Int
        """
        return len(self.item)
 
    def dequeue(self):
        """
        Return the elements that came first
        :return: Any
        """
        if self.size() == 0:
            return None
        else:
            return self.item.pop()
 
    def peek(self):
        """
        Check the Last elements
        :return: Any
        """
        if self.size() == 0:
            return None
        else:
            return self.item[-1]
 
    def isEmpty(self):
        """
        Check is the queue is empty
        :return: bool
        """
        if self.size() == 0:
            return True
        else:
            return False
    def clear(self):
    	self.item = []
 
queue = Queue()



speak_engine = pyttsx3.init()
r = sr.Recognizer()


def speak(what):
    # print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()

#   Перетащи все в menu.py 



def record_audio(ask = False):
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = ''
		try:
			voice_data = r.recognize_google(audio, language="ru-RU")
			# RecognizeLabel.config(text=voice_data)
			ui.cmd_lbl.setText(voice_data)
			voice_data = voice_data.lower()
			# queue.enque(voice_data)
		except sr.UnknownValueError:
			ui.cmd_lbl.setText("Я вас не поняла")
		except sr.RequestError:
			ui.cmd_lbl.setText("Извените, что-то не так. Проверьте подключение к интернету")
		queue.enque(voice_data)


# Команды

lst = {
	"name": ("clock", "some", "hello", "name", "search", "location", "prog", "end", "sps", "_end"),

	"commands": {
		"clock": ("час", "время"),
		"SomeQuestion": ("дела", "самочувствие"),
		"hello": ("привет", "здравствуй", "хай", "Hello"),
		"AskName": ("имя", "название", "зовут"),
		"search": ("поиск", "поищи", "найди", "найти"),
		"geolocation": ("геолокацию", "геолокация", "карта", "местоположение", "карту"),
		"pr": ("программу", "экзешник", "прогу"),
		"end": ("отключись", "выключись"),
		"sps": ("спс", "спасибо"),
		"sleep": ("спать", "отрубись")
	}
}

def respond(voice_data):

	cmd = ""

	# print(lst["commands"].items())
	c = 0
	for i in lst["commands"]:
		c += 1
		for v in lst["commands"][i]:
			try:
				if v in voice_data:
					c -= 1
					cmd = lst["name"][c]
					# print("-------------" + cmd)
					c = 0
					break
			except TypeError:
				pass

	if cmd == "some":
		sp = ["Хорошо", "Нормально", "Лучше не бывало", "Отлично", "Как я могу себя чувствовать плохо, когда имею такого босса"]
		speak(sp[random.randint(0, len(sp) - 1)])

	if cmd == "hello":
		speak("Здравствуйте сэр")

	if cmd == "name":
		speak("Меня зовут Матрица")

	if cmd == "clock":
		now = datetime.datetime.now()
		speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

	if cmd == "search":
		speak('что хотите найти?')
		voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
		voicee.start()
		voicee.join()
		voice_data = queue.dequeue()
		
		search = voice_data
		if search == "":
			speak("Я не поняла запрос")
		else:
			url = 'https://google.com/search?q=' + search
			webbrowser.get().open(url)
			speak('Вот что я нашла')

	#   Когда руки дойдут

	# if cmd == "prog":
	# 	speak('какую именно?')
	# 	search = record_audio('какую именно?')
	# 	search
		
	# 	speak('Открываю ' + search)

	if cmd == "location":
		speak('что хотите поискать?')

		voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
		voicee.start()
		voicee.join()
		voice_data = queue.dequeue()
		

		location = voice_data
		if location == "":
			speak("Я не поняла запрос")
		else:

			location.replace(" ", "+")
			url = 'https://www.google.ru/maps/place/' + location + '/&amp;'
			webbrowser.get().open(url)
			speak('Вот что я нашла на карте')

	if cmd == "end":
		speak('До новых встреч')
		app.quit()

	if cmd == "_end":
		speak('Перехожу в спящий режим')
		ui.cmd_lbl.setText("Скажите 'Матрица'")

		def activate_wait():
			voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
			voicee.start()
			voicee.join()
			voice_data = queue.dequeue()
			

			activate_cmd = voice_data
			if "матрица" in activate_cmd:
				speak("Я тут")
			else:
				activate_wait()

		activate_wait()


	if cmd == "sps":
		speak("Незачто")
	queue.clear()
	# voice_data = record_audio()
	# respond(voice_data)
	voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
	voicee.start()
	voicee.join()
	voice_data = queue.dequeue()
	
	threading.Thread(target=respond, args=(voice_data,), daemon=True).start()


# def data():
# 	try:
# 		voice_data = queue.dequeue()
# 		
# 		respond(voice_data)
# 	except TypeError:
# 		data()




#  Radio Button

# def st_():
# 	m = sr.Microphone(device_index=1)
# 	if ui.StartButton.isChecked():
		

# 		with m as source:
# 			r.adjust_for_ambient_noise(source)

	    

# 		voices = speak_engine.getProperty('voices')
# 		speak_engine.setProperty('voice', voices[4].id)

# 		# time.sleep(1)
# 		ui.cmd_lbl.setText('Говорите')

# 		voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
# 		voicee.start()
# 		# voicee.join()
# 		voice_data = queue.dequeue()
# 		# respond(voice_data)
# 		resp = threading.Thread(target=respond, args=(voice_data,), daemon=True).start()
# 	else:
# 		def activate_wait():
# 			voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
# 			voicee.start()
# 			voicee.join()
# 			voice_data = queue.dequeue()
			

# 			activate_cmd = voice_data
# 			if "матрица" in activate_cmd:
# 				speak("Я тут")
# 			else:
# 				activate_wait()
		

def st():

	m = sr.Microphone(device_index=1)

	with m as source:
		r.adjust_for_ambient_noise(source)

    

	voices = speak_engine.getProperty('voices')
	speak_engine.setProperty('voice', voices[4].id)

	# time.sleep(1)
	ui.cmd_lbl.setText('Говорите')

	voicee = threading.Thread(target=record_audio, args=(None,), daemon=True)
	voicee.start()
	# voicee.join()
	voice_data = queue.dequeue()
	# respond(voice_data)
	resp = threading.Thread(target=respond, args=(voice_data,), daemon=True).start()



	
	
 	
    # # check is value is complete in queue
	# while True:
	# 	flag = queue.isEmpty()
    
	# 	if flag:
	# 		pass
	# 	else:
	# 		respond(queue.dequeue())
	# 		break

# st()
msg = QMessageBox()
msg.setIcon(QMessageBox.Information)
# msg.setStyleSheet("QLabel{min-width: 100px; min-height: 80px;}");

def LstClick(item):
	st = ""
	temp_strN = ""
	m = 0
	for i in lst["commands"]:
		m += 1
		for v in lst["commands"][i]:
			temp_strN += (v + ", ")
		if temp_strN == item.text():
			st = i
			break
		else:
			temp_strN = ""

	Message = {
		"info": ("Матрица говорит конкретное время", "Простой вопрос", "Приветствие", "Говорит своё имя", "Включает поиск в гугле", 
									"Ищет объект на гугл карте", "(В разработке)", "Выключение", "спасибо", "Переход в спчщий режим"),

		"description": ("Время говорится в форманте\n'hh:mm'\n\nГоворится толко конкретное время на данный момент ", "Диалог", "Диалог", "Диалог", 
						"Поиск исполняется благодаря js фишке google.\n\nК шаблону поиска добавляется фраза сказанная пользователем",
						 "Поиск исполняется благодаря js фишке google.\n\nК шаблону поиска добавляется фраза сказанная пользователем",
						 "Может открывать программы на компьютере", "Программа выключается при пимощи\n\napp.quit()", "Диалог",
						  "Матрица больше не реагирует ни на одно слово, кроме своего имени.\n\n Если сказать 'Матрица', то всё будет как прежде.\n\nЭто сделано для временного отключения Матрицы при разговоре с кем-то или при других обстоятельствах.")
	}

	msg.setText("<p align='left'>Тип Команды: " + st + "</p>")
	msg.setInformativeText("<p align='left'>" + Message["info"][m - 1] + "</p>")
	msg.setWindowTitle("Info")
	msg.setDetailedText("Описание:\n\n" + Message["description"][m - 1])
	msg.setStandardButtons(QMessageBox.Ok)
	msg.show()

def showList():
	Dialog.hide()
	uiL.listWidget.setWindowTitle('Command List')
	uiL.listWidget.clear()
	temp_str = ""
	for i in lst["commands"]:
		temp_str = ""
		for v in lst["commands"][i]:
			temp_str += (v + ", ")

		uiL.listWidget.addItem(temp_str)

	uiL.listWidget.itemClicked.connect(LstClick)

	# uiL.listWidget.addItems(lst["commands"])

	ListL.show()

def showMain():
	Dialog.show()
	ListL.hide()


menu = QMenu()
exitAction = menu.addAction('Exit')
def exit():
	trayIcon.hide()
	app.quit()
exitAction.triggered.connect(exit)
showAction = menu.addAction('Show')
def show():
	Dialog.show()
	ListL.hide()
	trayIcon.hide()
showAction.triggered.connect(show)
trayIcon.setContextMenu(menu)

def tray():
	trayIcon.show()
	Dialog.hide()
	ListL.hide()

def OK():
	tempCmd = ui.cmd_lineedit.text()
	voices = speak_engine.getProperty('voices')
	speak_engine.setProperty('voice', voices[4].id)
	try:
		os.startfile(tempCmd)
	except:
		resp = threading.Thread(target=respond, args=(tempCmd,), daemon=True).start()  #поиск, локация и сон работают криво


def DownloadUpdate():
	webbrowser.open(urlDown)
	app.quit()

def login():
	username = uiLog.login.text()
	password = uiLog.password.text()
	r = requests.get('https://matrx.herokuapp.com/db.html')
	html = BS(r.content, 'html.parser')

	for el in html.select('.user > .login'):
		templogin = el.text
		if templogin == username:
			for ps in html.select('.user > .password'):
				temppass = ps.text
				if temppass == password and ps.get('id') == el.get('id'):
					Dialog.show()
					Log.hide()
				else:
					pass

		else:
			pass
		uiLog.error.setText("Invalid login or password. Please try again")

	
		

uiU.myButton.clicked.connect(DownloadUpdate)

uiL.myButton.clicked.connect(showMain)

uiLog.myButton.clicked.connect(login)

ui.myButton.clicked.connect(st)
ui.minimize_button.clicked.connect(tray)
ui.myButton_2.clicked.connect(app.quit)
ui.OK_button.clicked.connect(OK)
# ui.StartButton.toggled.connect(st_)
ui.cmd_button.clicked.connect(showList)
if versionMain == vers:
	Log.show()
else:
	Up.show()


sys.exit(app.exec_())