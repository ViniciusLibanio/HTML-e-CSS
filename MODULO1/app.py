import sys
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget
)

app = QApplication(sys.argv)

app.setStyle('Fusion')

window = QWidget()

layout = QVBoxLayout(window)

layout.addWidget(QPushButton('Um'))
layout.addWidget(QPushButton('Dois'))
layout.addWidget(QPushButton('Três'))
layout.addWidget(QPushButton('Quatro'))
layout.addWidget(QPushButton('Cinco'))
layout.addWidget(QPushButton('Seis'))

window.show()

sys.exit(app.exec())
