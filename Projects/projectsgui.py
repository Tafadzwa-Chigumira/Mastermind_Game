import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QPalette, QPainter, QBrush


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt5 App")

        # Set background image
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(10, QBrush(QPixmap(r"C:\Users\tchig\Desktop\Pins\2d860508d57550bd4928abd8499e7063.jpg")))
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())