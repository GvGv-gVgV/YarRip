import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt6 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Рисование')

        self.do_paint = False
        self.pushButton.clicked.connect(self.draw_flag)

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        r = randint(20, 150)
        x = randint(0, self.width() - r)
        y = randint(0, self.height() - r)
        qp.drawEllipse(QPaintF(x,y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())