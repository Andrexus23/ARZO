from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def initUi(self, ui):
        self.ui = ui
        self.ui.setupUi(self)
        self.show()
