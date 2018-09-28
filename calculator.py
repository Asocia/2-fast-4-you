from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QUrl
from ui_calculator import Ui_Calculator
from operator import add, sub, mul, truediv
import sys
from styles import *


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    firstNumber = 0
    binary_dict = {'+': 0, '-': 1, 'x': 2, '÷': 3}
    typing_second_number = False
    typed_second_number = False
    shortcut_dict = {'+': '+', '-': '-', 'x': '*', '÷': '/', '.': '.'}
    equals_dict = {0: add, 1: sub, 2: mul, 3: truediv}
    current_theme = "Orange"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setWindowIcon(QtGui.QIcon("calc.png"))
        self.digit_buttons = [getattr(self, "pushButton_{}".format(i)) for i in range(10)]
        self.binary_buttons = [self.pushButton_add, self.pushButton_subtract,
                               self.pushButton_multiply, self.pushButton_divide]
        self.unary_buttons = [self.pushButton_percent, self.pushButton_plusMinus]
        self.all_buttons = self.digit_buttons + self.unary_buttons + \
                           self.binary_buttons + [self.pushButton_equals, self.pushButton_clear]
        self.pushButton_decimal.clicked.connect(self.decimal_pressed)
        self.pushButton_equals.clicked.connect(self.equals_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)

        for button in self.digit_buttons:
            button.clicked.connect(self.digit_pressed)
            button.setShortcut(button.text())
        for button in self.unary_buttons:
            button.clicked.connect(self.unary_pressed)
        for button in self.binary_buttons:
            button.clicked.connect(self.binary_pressed)
            button.setShortcut(self.shortcut_dict[button.text()])
            button.setCheckable(True)
            button.setChecked(False)
        self.pushButton_equals.setCheckable(True)
        self.pushButton_equals.setChecked(False)
        self.pushButton_equals.setShortcut("Enter")
        self.pushButton_decimal.setShortcut(".")
        self.pushButton_clear.setShortcut("Delete")
        self.actionQuit.triggered.connect(self.closeEvent)
        self.actionMinimal_Bright_Orange.triggered.connect(self.change_color_scheme)
        self.actionFeather_Light_Blue.triggered.connect(self.change_color_scheme)
        self.actionFeather_Light_Blue.trigger()
        self.actionFeather_Light_Blue.setShortcut("Ctrl+B")
        self.actionMinimal_Bright_Orange.setShortcut("Ctrl+O")
        self.actionSelect_Font.triggered.connect(self.select_font)
        self.actionSelect_Font.setShortcut("Ctrl+F")
        self.actionEnglish.triggered.connect(self.troll)
        self.actionHelp.triggered.connect(self.info)

    def digit_pressed(self):
        button = self.sender()
        if not (self.typing_second_number or self.pushButton_equals.isChecked()):
            if "." in self.label.text():
                self.label.setText(self.label.text() + button.text())
            else:
                label_number = format(float(self.label.text() + button.text()), ".15g")
                self.label.setText(label_number)

        else:
            label_number = format(float(button.text()), ".15g")
            self.typed_second_number = True
            self.typing_second_number = False
            self.pushButton_equals.setChecked(False)
            self.label.setText(label_number)

    def decimal_pressed(self):
        if '.' not in self.label.text() and (not self.typing_second_number or self.typed_second_number):
            self.label.setText(self.label.text() + '.')
        elif self.typing_second_number:
            self.label.setText('0.')
            self.typed_second_number = True
            self.typing_second_number = False

    def unary_pressed(self):
        button = self.sender()
        label_number = float(self.label.text())
        if button.text() == '%':
            label_number *= 0.01
        else:
            label_number *= -1
        label_number = format(label_number, ".15g")
        self.label.setText(label_number)

    def binary_pressed(self):
        button = self.sender()
        self.firstNumber = float(self.label.text())
        self.typing_second_number = True
        selected_operation = self.binary_dict[button.text()]
        for i in range(len(self.binary_buttons)):
            if i == selected_operation:
                self.binary_buttons[i].setChecked(True)
            else:
                self.binary_buttons[i].setChecked(False)

    def equals_pressed(self):
        self.pushButton_equals.setChecked(True)
        button = (btn for btn in self.binary_buttons if btn.isChecked())
        button = list(button)
        if len(button) != 0:
            operation = self.equals_dict[self.binary_dict[button[0].text()]]
            second_number = float(self.label.text())
            if self.typed_second_number:
                result = format(operation(self.firstNumber, second_number), ".15g")
                self.label.setText(result)
                self.firstNumber = second_number
                self.typed_second_number = False
            elif self.firstNumber != 0:
                result = format(operation(second_number, self.firstNumber), ".15g")
                self.label.setText(result)

    def clear_pressed(self):
        for button in self.binary_buttons:
            button.setChecked(False)
        self.firstNumber = 0
        self.typed_second_number = False
        self.typing_second_number = False
        self.label.setText("0")

    def change_color_scheme(self, event):
        theme = self.sender().text()
        if "Blue" in theme:
            for button in self.binary_buttons + self.unary_buttons + [self.pushButton_decimal]:
                button.setStyleSheet(style_blue_binary)
            self.pushButton_equals.setStyleSheet(style_blue_equals)
            self.pushButton_clear.setStyleSheet(style_blue_clear)
        else:
            for button in self.binary_buttons + [self.pushButton_equals]:
                button.setStyleSheet(style_orange_binary)
            for button in self.unary_buttons + [self.pushButton_clear, self.pushButton_decimal]:
                button.setStyleSheet(style_orange_unary)

    def select_font(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            for button in self.all_buttons:
                button.setFont(font)

    def troll(self):
        label = QtWidgets.QLabel()
        label.linkActivated.connect(self.link)
        label.setText(
            'I\'m too lazy to add another language.'
            ' <a href="http://www.bbc.co.uk/learningenglish/">'
            'Learn English</a> instead :)')
        QtWidgets.QMessageBox.question(self, "Hey!", label.text(),
                                       QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Ok)

    def link(self, linkStr):
        QtGui.QDesktopServices.openUrl(QUrl(linkStr))

    def info(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)

        msg.setText("What help? The app is very simple!!")
        msg.setWindowTitle("What Help?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.exec_()
        
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Warning', "Are you sure want to quit?",
                                               QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            if type(event) != bool:
                event.ignore()
