#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import rdict

app = QApplication([])
app.setStyle('Fusion')

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

output_layout = QHBoxLayout()
output_box = QPlainTextEdit()
output_box.setReadOnly(True)
output_layout.addWidget(output_box)

output_window.setLayout(output_layout)
output_window.show()

window = QWidget()

layout = QVBoxLayout()
layout.addWidget(input_window)
layout.addWidget(output_window)

window.setLayout(layout)
window.setWindowTitle('F4T Dictionary')
window.show()

rdict.parse()

def go():
	output_box.setPlainText('')
	output_box.appendHtml(rdict.define(input_box.text()))
	output_box.verticalScrollBar().setValue(output_box.verticalScrollBar().minimum())

input_button.clicked.connect(go)

app.exec_()
