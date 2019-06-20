#!/usr/bin/env python3
from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import rdict
import hdict

print('Word Book. Alpha version. Developer: Rishabh Ranjan')
appctxt = ApplicationContext() # 1. Instantiate ApplicationContext
app = QApplication(sys.argv)
app.setStyle('Fusion')

# upper_window = QWidget()
# 
# upper_layout = QVBoxLayout()
# 
# upper_title = QLabel('<b><span style="color: #4d2600">Word Book</span></b>')
# upper_title.setFont(QFont('Chalkboard', 48))
# upper_layout.addWidget(upper_title, alignment = Qt.AlignCenter)
# 
# upper_subtitle = QLabel('Make words your best friends!')
# upper_subtitle.setFont(QFont('Chalkboard', 20))
# upper_layout.addWidget(upper_subtitle, alignment = Qt.AlignCenter)
# 
# upper_layout.setAlignment(Qt.AlignTop)
# upper_window.setLayout(upper_layout)
# 
# lower_window = QWidget()
# 
# lower_layout = QVBoxLayout()
# lower_label = QLabel('Click to continue...')
# lower_label.setFont(QFont('Chalkboard', 20))
# lower_layout.addWidget(lower_label, alignment = Qt.AlignCenter)
# 
# lower_layout.setAlignment(Qt.AlignBottom)
# lower_window.setLayout(lower_layout)
# 
# cover_layout = QVBoxLayout()
# cover_layout.addWidget(upper_window)
# cover_layout.addWidget(lower_window)
cover_window = QWidget()
bg_img = QImage(appctxt.get_resource('bad_bg.jpeg'))
palette = QPalette()
palette.setBrush(10, QBrush(bg_img))
cover_window.setPalette(palette)
cover_window.setFixedSize(600, 600)
# cover_window.setLayout(cover_layout)
cover_window.show()

header_window = QWidget()

header_layout = QHBoxLayout() 
header_left_label = QLabel()
header_left_img = QPixmap(appctxt.get_resource('f4t_logo.png')).scaledToHeight(64, Qt.SmoothTransformation)
header_left_label.setPixmap(header_left_img)
header_layout.addWidget(header_left_label)

header_right_label = QLabel()
header_right_img = QPixmap(appctxt.get_resource('nss_logo.png')).scaledToHeight(64, Qt.SmoothTransformation)
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
window.resize(600, 600)
window.setWindowTitle('Word Book')
# window.show()
def f(*argv):
    window.show()
    cover_window.hide()
cover_window.mousePressEvent = f

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
