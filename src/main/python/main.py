#!/usr/bin/env python3
from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import rdict
import hdict

appctxt = ApplicationContext() # 1. Instantiate ApplicationContext
app = QApplication(sys.argv)
app.setStyle('Fusion')

print('hello... anyone there?')

header_window = QWidget()

header_layout = QHBoxLayout()

header_left_label = QLabel()
header_left_img = QPixmap('/Users/zero/Desktop/F4T Dictionary/rdict/f4t_logo.png').scaledToHeight(64, Qt.SmoothTransformation)
header_left_label.setPixmap(header_left_img)
header_layout.addWidget(header_left_label)

header_right_label = QLabel()
header_right_img = QPixmap('/Users/zero/Desktop/F4T Dictionary/rdict/nss_logo.png').scaledToHeight(64, Qt.SmoothTransformation)
header_right_label.setPixmap(header_right_img)
header_layout.addWidget(header_right_label, alignment = Qt.AlignRight)

header_window.setLayout(header_layout)
header_window.show()

input_window = QWidget()

input_layout = QHBoxLayout()
input_label = QLabel('Type a word: ')
input_box = QLineEdit()
input_button = QPushButton('Search')
input_layout.addWidget(input_label)
input_layout.addWidget(input_box)
input_layout.addWidget(input_button)

input_window.setLayout(input_layout)
input_window.show()

output_window = QWidget()

output_box_english = QPlainTextEdit()
output_box_english.setReadOnly(True)
output_box_hindi = QPlainTextEdit()
output_box_hindi.setReadOnly(True)

output_tabs = QTabWidget()
output_tabs.addTab(output_box_english, 'English')
output_tabs.addTab(output_box_hindi, 'Hindi')

output_layout = QHBoxLayout()
output_layout.addWidget(output_tabs)

output_window.setLayout(output_layout)
output_window.show()

footer_window = QWidget()

footer_layout = QHBoxLayout()
footer_label = QLabel('<font color="#555555">Designed and developed by NSS IITD, in collaboration with F4TF.</font>')
footer_layout.addWidget(footer_label, alignment = Qt.AlignCenter)
footer_window.setLayout(footer_layout)
footer_window.show()

window = QWidget()

layout = QVBoxLayout()
layout.addWidget(header_window)
layout.addWidget(input_window)
layout.addWidget(output_window)
layout.addWidget(footer_window)

window.setLayout(layout)
window.resize(512, 512)
window.setWindowTitle('F4T Dictionary')
window.show()

rdict.parse()
hdict.parse()

def go():
	output_box_english.clear()
	output_box_english.appendHtml(rdict.define(input_box.text()))
	output_box_english.verticalScrollBar().setValue(output_box_english.verticalScrollBar().minimum())

	output_box_hindi.clear()
	output_box_hindi.appendHtml(hdict.define(input_box.text()))
	output_box_hindi.verticalScrollBar().setValue(output_box_hindi.verticalScrollBar().minimum())

input_button.clicked.connect(go)
input_box.returnPressed.connect(go)

exit_code = appctxt.app.exec_() # 2. Invoke appctxt.app.exec_()
sys.exit(exit_code)
