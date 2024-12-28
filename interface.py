from PyQt5.QtWidgets import (
QApplication, QWidget, QPushButton, QListWidget, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

app = QWidget()
window = QApplication([])

photo = QPixmap()

group_button = QHBoxLayout()
group_button.addWidget(left)
group_button.addWidget(right)
group_button.addWidget(mirror)
group_button.addWidget(blur)
group_button.addWidget(bw)

v_layout =QVBoxLayout()
v_layout.addWidget(photo_label)
v_layout.addLayout(group_button)

list_layout = QVBoxLayout()
list_layout.addWidget(folder)
list_layout.addWidget(fo)