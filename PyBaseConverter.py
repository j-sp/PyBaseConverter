## Copyright 2016 Javier Serrano and Adrian Serrano
##
## This file is part of PyBaseConverter.
##
## PyBaseConverter is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## PyBaseConverter is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with PyBaseConverter.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import Number

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.number = Number.Number(1)
        numberFromLabel = QLabel("Number:")
        self.numberFromLine = QLineEdit()
        baseFromLabel = QLabel("From Base:")
        self.baseFromLine = QLineEdit()
        baseToLabel = QLabel("To Base:")
        self.baseToLine = QLineEdit()
        self.submitButton = QPushButton("Go!")
        self.resultLabel = QLabel("")

        vLayout1 = QVBoxLayout()
        vLayout1.addWidget(numberFromLabel)
        vLayout1.addWidget(self.numberFromLine)
        vLayout1.addWidget(baseFromLabel)
        vLayout1.addWidget(self.baseFromLine)
        vLayout1.addWidget(baseToLabel)
        vLayout1.addWidget(self.baseToLine)
        vLayout1.addWidget(self.submitButton)
        vLayout1.addWidget(self.resultLabel)

        self.submitButton.clicked.connect(self.submitNumbers)

        mainLayout = QGridLayout()
        mainLayout.addLayout(vLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Base converter")

    def submitNumbers(self):
        try:
            number_from = self.numberFromLine.text()
            base_from = int(self.baseFromLine.text())
            base_to = int(self.baseToLine.text())
            self.number.set(base_from, number_from)
            result = self.number.get(base_to)
        except ValueError as err:
            self.resultLabel.setText("Value Error: " + str(err))
        else:
            self.resultLabel.setText("The result is " + result)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
