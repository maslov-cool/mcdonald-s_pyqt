import sys

from PyQt6.QtWidgets import (QLineEdit, QWidget, QApplication, QPushButton,
                             QVBoxLayout, QPlainTextEdit, QCheckBox, QHBoxLayout)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ в Макдональдсе')

        self.main_layout = QVBoxLayout()
        self.menu_layout = QHBoxLayout()
        self.checkboxes_layout = QVBoxLayout()
        self.inputs_layout = QVBoxLayout()

        self.menu = {
            "Чизбургер": 10,
            "Гамбургер": 20,
            "Кока-кола": 15,
            "Наггетсы": 30
        }

        self.checkboxes = []
        self.inputs = []
        for i in range(len(self.menu.keys())):
            checkbox = QCheckBox(list(self.menu.keys())[i])
            checkbox.stateChanged.connect(lambda checked, i1=i: self.choose(i1))
            self.checkboxes.append(checkbox)

            input = QLineEdit('0')
            input.setEnabled(False)
            self.inputs.append(input)

        self.orderButton = QPushButton('Заказать')
        self.orderButton.clicked.connect(self.cheque)

        self.order = QPlainTextEdit()
        self.order.setReadOnly(True)

        for i in range(len(self.checkboxes)):
            self.checkboxes_layout.addWidget(self.checkboxes[i])
            self.inputs_layout.addWidget(self.inputs[i])
        self.menu_layout.addLayout(self.checkboxes_layout)
        self.menu_layout.addLayout(self.inputs_layout)
        self.main_layout.addLayout(self.menu_layout)
        self.main_layout.addWidget(self.orderButton)
        self.main_layout.addWidget(self.order)

        self.setLayout(self.main_layout)

    def choose(self, i):
        if self.checkboxes[i].isChecked():
            self.inputs[i].setText('1')
            self.inputs[i].setEnabled(True)
        else:
            self.inputs[i].setText('0')
            self.inputs[i].setEnabled(False)

    def cheque(self):
        text = 'Ваш заказ\n\n'
        result = 0
        for i in range(len(self.checkboxes)):
            if self.checkboxes[i].isChecked():
                price_el = str(int(self.inputs[i].text()) * int(self.menu[self.checkboxes[i].text()]))
                text += (self.checkboxes[i].text() + '-' * 5 + self.inputs[i].text() + '-' * 5 +
                         price_el + '\n')
                result += int(price_el)
        text += f'\nИтого: {result}'
        self.order.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MyWidget()
    program.show()
    sys.exit(app.exec())










