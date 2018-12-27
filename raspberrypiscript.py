#!python3
import sys
from PyQt5 import QtCore
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
class Life2CodingLoad(QDialog):
	got_image = QtCore.pyqtSignal(str)
	def __init__(self, parent=None):
		super(Life2CodingLoad,self).__init__(parent)
		loadUi('File12.ui',self)
		self.setWindowTitle('Life2Coding PyQt5 Gui')
		self.last_call = 0
	@pyqtSlot()
	def on_pushButtonLoad_clicked(self):
		if time.time() - self.last_call < 1:
			return
		fname, _filter = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
		self.got_image.emit(fname)

		time.sleep(1)
		self.last_call = time.time()
	def on_valueChanged(self):
		self.Test.setText(str(self.ZoomSlider.value()))
"""

class Life2Coding(QDialog):
	def __init__(self):
		super(Life2Coding,self).__init__()
		loadUi('File1.ui',self)
		self.setWindowTitle('APP')
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

		self.pushButtonA.clicked.connect(self.on_pushButtonA_clicked)
		self.pushButtonB.clicked.connect(self.on_pushButtonB_clicked)
		self.pushButtonC.clicked.connect(self.on_pushButtonC_clicked)
		self.pushButtonD.clicked.connect(self.on_pushButtonD_clicked)
		self.pushButtonHide.clicked.connect(self.on_pushButtonHide_clicked)
		self.pushButtonNext.clicked.connect(self.on_pushButtonNext_clicked)
		self.pushButtonPrev.clicked.connect(self.on_pushButtonPrev_clicked)
		self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)
		self.pushButtonClose.clicked.connect(self.on_pushButtonClose_clicked)

		#self.ZoomSlider = QSlider(Qt.Horizontal)
		self.ZoomSlider.setMinimum(0)
		self.ZoomSlider.setMaximum(100)
		self.ZoomSlider.setValue(0)
		self.ZoomSlider.setTickInterval(5)
		self.ZoomSlider.valueChanged.connect(self.on_valueChanged)

		self.last_call = 0

	@pyqtSlot()
	def on_pushButtonA_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "A")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonB_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "B")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonC_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "C")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonD_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "D")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonHide_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "Hide")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonNext_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "Next")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonPrev_clicked(self):
		if time.time() - self.last_call < 1:
			return
		client.send_message("/filter", "Prev")
		time.sleep(1)
		self.last_call = time.time()
	def on_pushButtonLoad_clicked(self):
		if time.time() - self.last_call < 1:
			return
		"""
		dialog = Life2CodingLoad(self)
		dialog.got_image.connect(self.show_it)
		dialog.show()
		"""
		fname, _filter = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
		self.label_2.setPixmap(QPixmap(fname))
		##

		time.sleep(1)
		self.last_call = time.time()
	def on_valueChanged(self):
		self.Test.setText(str(self.ZoomSlider.value()))	
	def on_pushButtonClose_clicked(self):
		self.close()

"""
	def show_it(self, the_image):
		print(the_image)
		self.label_2.setPixmap(QPixmap(the_image))
"""

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", default="192.168.1.14",
	  help="The ip of the OSC server")
	parser.add_argument("--port", type=int, default=5005,
	  help="The port the OSC server is listening on")
	args = parser.parse_args()

	client = udp_client.SimpleUDPClient(args.ip, args.port)

	print('dat werkt precies')
	app=QApplication(sys.argv)
	widget=Life2Coding()
	widget.show()
	sys.exit(app.exec_())






