#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.uic import loadUi
import argparse
import random
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client
"""
	@pyqtSlot()
	def on_pushButtonOk_clicked(self):
		words= self.textEdit.toPlainText()
		if words:
			client.send_message("/buttonA", words)
		else:
			client.send_message("/buttonA", "empty")
"""

class TakePictureScreen(QDialog):
	def __init__(self, parent):
		super(TakePictureScreen,self).__init__(parent)
		loadUi('File2D.ui',self)
		self.setWindowTitle('Take Picture')
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
		self.last_call = 0
		self.pushButtonOk.clicked.connect(self.on_pushButtonOk_clicked)
		self.pushButtonCancel.clicked.connect(self.on_pushButtonCancel_clicked)

		self.ZoomSlider.setMinimum(0)
		self.ZoomSlider.setMaximum(100)
		self.ZoomSlider.setValue(0)
		self.ZoomSlider.valueChanged.connect(self.on_valueChanged)
		self.ZoomSlider.setStyleSheet("QSlider::groove:vertical { border: 1px solid;  width: 20px;   margin: 0px;    } QSlider::handle:vertical {    background-color: black;    border: 1px solid;    height: 40px;    width: 40px;    margin: -15px 0px; }")

	@pyqtSlot()
	def on_pushButtonOk_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/takePicture", str(self.ZoomSlider.value()))
		self.close() 
		self.last_call = time.time()
	def on_pushButtonCancel_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/cancelPicture", str(self.ZoomSlider.value()))
		self.close()
		self.last_call = time.time()
	def on_valueChanged(self):
		value = self.ZoomSlider.value()
		myList = [1,50,100]
		if value not in myList:
			self.ZoomSlider.setValue(min(myList, key=lambda x:abs(x-value)))
		client.send_message("/zoomSlider", str(self.ZoomSlider.value()))

		
class FeedbackScreen(QDialog):
	#variable to signal to method in other window
	#got_image = QtCore.pyqtSignal(str)
	def __init__(self, parent):
		super(FeedbackScreen,self).__init__(parent)
		loadUi('File2.ui',self)
		self.setWindowTitle('APP')
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
		self.last_call = 0
		self.isInfoVisible = False

		self.pushButtonHide.clicked.connect(self.on_pushButtonToggle_clicked)
		self.pushButtonA.clicked.connect(self.on_pushButtonA_clicked)
		self.pushButtonA.setIcon(QtGui.QIcon('images/recordtext.png'))
		self.pushButtonB.clicked.connect(self.on_pushButtonB_clicked)
		self.pushButtonB.setIcon(QtGui.QIcon('images/textquestion.png'))
		self.pushButtonC.clicked.connect(self.on_pushButtonC_clicked)
		self.pushButtonC.setIcon(QtGui.QIcon('images/imagequestion.png'))
		self.pushButtonD.clicked.connect(self.on_pushButtonD_clicked)
		self.pushButtonD.setIcon(QtGui.QIcon('images/camera.png'))
	@pyqtSlot()
	def on_pushButtonToggle_clicked(self):
		if time.time() - self.last_call < 1:
			return
		if self.isInfoVisible:
			client.send_message("/hide", ".")
		else: 
			client.send_message("/show", ".")
		self.isInfoVisible = not self.isInfoVisible
		self.last_call = time.time()
	def on_pushButtonA_clicked(self):
		if time.time() - self.last_call < 1:
			return
		#dialog = Life2CodingScreenA(self)
		#dialog.show()
		client.send_message("/buttonA", "A")
		self.close()
		self.last_call = time.time()
	def on_pushButtonB_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/buttonB", "B")
		self.close()
		self.last_call = time.time()
	def on_pushButtonC_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/buttonC", "C")
		self.close()
		self.last_call = time.time()
	def on_pushButtonD_clicked(self):
		if time.time() - self.last_call < 1:
			return
		dialog = TakePictureScreen(self)
		dialog.show()
		self.close()
		self.last_call = time.time()

	"""
	#get picture url through explorer & signal to parent window
	def on_pushButtonLoad_clicked(self):
		fname, _filter = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
		self.got_image.emit(fname)
	"""

class MainScreen(QDialog):
	def __init__(self):
		super(MainScreen,self).__init__()
		loadUi('File1.ui',self)
		self.setWindowTitle('APP')
		#deletes top windowbar
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
		self.last_call = 0
		self.isInfoVisible = False

		self.pushButtonHide.clicked.connect(self.on_pushButtonToggle_clicked)
		self.pushButtonProblem.clicked.connect(self.on_pushButtonProblem_clicked)
		self.pushButtonProblem.setIcon(QtGui.QIcon('images/question_mark.png'))
		self.pushButtonSuggestion.clicked.connect(self.on_pushButtonSuggestion_clicked)
		self.pushButtonSuggestion.setIcon(QtGui.QIcon('images/suggestion.png'))
		self.pushButtonNext.clicked.connect(self.on_pushButtonNext_clicked)
		self.pushButtonNext.setIcon(QtGui.QIcon('images/next.png'))
		self.pushButtonPrev.clicked.connect(self.on_pushButtonPrev_clicked)
		self.pushButtonPrev.setIcon(QtGui.QIcon('images/previous.png'))

		
	@pyqtSlot()
	def on_pushButtonToggle_clicked(self):
		if time.time() - self.last_call < 1:
			return
		if self.isInfoVisible:
			client.send_message("/hide", ".")
		else: 
			client.send_message("/show", ".")
		self.isInfoVisible = not self.isInfoVisible
		self.last_call = time.time()
	def on_pushButtonProblem_clicked(self):
		#if statements prevent multiple signals
		if time.time() - self.last_call < 1:
			return
		client.send_message("/problem", ".")
		#correct send?
		self.last_call = time.time()
	def on_pushButtonNext_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/next", ".")
		self.last_call = time.time()
	def on_pushButtonPrev_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/previous", ".")
		self.last_call = time.time()
	def on_pushButtonSuggestion_clicked(self):
		if time.time() - self.last_call < 1:
			return
		#open other window
		dialog = FeedbackScreen(self)
		#connect signaling method to other window
		#dialog.got_image.connect(self.show_it)
		dialog.show()
		self.last_call = time.time()
"""
	#method to accept signal from other window
	def show_it(self, the_image):
		#set pixmap based on url
		self.label_2.setPixmap(QPixmap(the_image))
"""

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", default="127.0.0.1",
	  help="The ip of the OSC server")
	parser.add_argument("--port", type=int, default=5005,
	  help="The port the OSC server is listening on")
	args = parser.parse_args()

	client = udp_client.SimpleUDPClient(args.ip, args.port)

	print('dat werkt precies')
	app=QApplication(sys.argv)
	widget=MainScreen()
	widget.show()
	sys.exit(app.exec_())






