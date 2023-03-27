from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

#디자인 파일 경로
UI_PATH = "07.GUI/login.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)
        
        # 버튼 클릭 이벤트 주는 방법
        # self.객체이름.clicked.connect(self.실행할함수이름)
        self.login_btn.clicked.connect(self.login_start) #메서드
        
    def login_start(self):
        input_id = self.id.text()
        input_pw = self.pw.text()
        print(f'입력한 아이디는 : {input_id}')
        print(f'입력한 패스워드는 : {input_pw}')
        
QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())