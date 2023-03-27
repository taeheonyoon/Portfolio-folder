from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import pyautogui

# 디자인 파일 경로
UI_PATH = "07.GUI/macro.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

        # 버튼 클릭 이벤트 주는 방법
        # self.객체이름.clicked.connect(self.실행할함수이름)
        self.move_btn.clicked.connect(self.move_start)
    
    def move_start(self):
        try:
            xcor = float(self.xcor.text())
            ycor = float(self.ycor.text())
            print(f'입력한 x좌표는 : {xcor}')
            print(f'입력한 y좌표는 : {ycor}')
            pyautogui.moveTo(xcor, ycor, 2)
        except:
            pass    

QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())