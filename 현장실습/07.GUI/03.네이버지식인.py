from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import pyautogui
import requests
from bs4 import BeautifulSoup
import openpyxl

# 디자인 파일 경로
UI_PATH = "07.GUI/naver_kin.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

        # 버튼 클릭 이벤트 주는 방법
        # self.객체이름.clicked.connect(self.실행할함수이름)
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.close_btn.clicked.connect(self.close)
    
    def start(self):
        input_keyword = self.keyword.text()
        input_page = int(self.page.text())
        self.result = []
        
        for i in range(1, input_page + 1):
            self.textBrowser.append(f'{i} 페이지 크롤링 중...')
            QApplication.processEvents() #UI 업데이트
            
            response = requests.get(f"https://kin.naver.com/search/list.naver?query={input_keyword}&page={i}")
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            questions = soup.select(".basic1 > li")
            
            for i, question in enumerate(questions, 1):
                anchor = question.select_one("dt > a")
                title = anchor.text
                link = anchor['href']
                date = question.select_one(".txt_inline").text
                content = question.select_one(".txt_inline +dd").text
                
                print(i, title, link, date, content, end='\n')
                self.textBrowser.append(f'{title} {link} {date} {content}')
                QApplication.processEvents() #UI 업데이트
                self.result.append([title, link, date, content])
   
    def reset(self):
        self.keyword.setText('')
        self.page.setText('')
        self.textBrowser.setText('')
    
    def save(self):
        keyword = self.keyword.text()
        # 엑셀 파일 생성
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = self.keyword.text()
        
        ws.append(['제목', '링크', '날짜', '내용'])
        for res in self.result:
            ws.append(res)
        wb.save(f'{keyword}.xlsx')
   
    def close(self):
        sys.exit()
        
QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())