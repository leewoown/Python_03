import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QFile
from un_test import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.is_on = False


        self.ui.pushButton.clicked.connect(self.button_was_clicked)
        self.ui.pushButton_2.clicked.connect(self.button2_was_clicked)
        self.ui.pushButton_3.clicked.connect(self.button3_was_clicked)
        
    def button_was_clicked(self):
        self.ui.textEdit.append("첫 번째 버튼이 클릭되었습니다.")

    def button2_was_clicked(self):
        self.ui.textEdit.append("두 번째 버튼이 클릭되었습니다.")

    def button3_was_clicked(self):
        self.is_on = not self.is_on  
        if self.is_on : 
            self.ui.pushButton_3.setText("Clear")
            self.ui.textEdit.append("세 번째 버튼이 클릭되었습니다.")
        else :
           self.ui.pushButton_3.setText("Write")
           self.ui.textEdit.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())