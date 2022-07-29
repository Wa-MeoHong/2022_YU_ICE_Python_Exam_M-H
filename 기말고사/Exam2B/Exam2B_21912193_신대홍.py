# 파일명 : Exam2B_21912193_신대홍.py
# 프로그램 목적 및 기능: tkinter 라이브러리를 이용한 USD -> KRW 환전 프로그램
# 프로그램 작성자 : 신대홍(2022년 6월 11일)
# 최종 Update : Version 1.0.0, 2022년 6월 11일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/06/11     v1.0.0       최초작성

from tkinter import * # tkinter 라이브러리 호출

class USD_KRW_Calculator: # 클래스 생성
    def __init__(self, master): # 초기 화면 설정
        frame = Frame(master) #컨테이너 위젯, 윈도우 창을 생성 함
        frame.pack() # 위젯을 압축배치함 (위젯의 크기에 맞게 윈도우창을 조절)

        Inframe = LabelFrame(frame, text='USD_KRW Exchange Calculator') # 외부프레임 생성
        Inframe.pack(padx=50) #외부공백을 좌우로 50을 주었다. 

        self.EXRatio_var = DoubleVar() #실수형 입력 변수 생성
        
        Label(Inframe, text='Exchange Ratio (1 USD => x KRW)').grid(row=0,column=0) # 라벨 생성 (입력 칸 바로 옆에 생성)
        Entry(Inframe, textvariable=self.EXRatio_var, justify=RIGHT).grid(row=0,column=1)
        # 입력칸 생성, text를 입력하면 EXRatio_var에 실수형으로 담긴다.
        self.EXRatio_var.set(1245.23) # 환율을 set으로 고정

        self.USD_var = DoubleVar() # 실수형을 입력할 변수를 만듦
        Label(Inframe, text='US Doller').grid(row=1,column=0) # 라벨 생성 (입력 칸 바로 옆에 생성)
        Entry(Inframe, textvariable=self.USD_var, justify=RIGHT).grid(row=1,column=1) 
        # 입력칸 생성, text를 입력하면 USD_var에 실수형으로 담긴다.

        self.KRW_var = DoubleVar() # 마일 입력을 위한 실수형 입력 변수 생성
        Label(Inframe, text='Korean Won').grid(row=2,column=0) # 라벨 Mile 생성
        Entry(Inframe, textvariable=self.KRW_var, justify=RIGHT).grid(row=2,column=1) #km와 똑같이 입력 칸 생성

        button1 = Button(Inframe, text='US Dollar -> Kr Won', bg="Green", command= self.convert_USD_KRW)
         #아래칸에 버튼1번 생성 (USD -> KRW 기능 수행)

        button1.grid(row=3, column=0) # 버튼1 위치 
        button2 = Button(Inframe, text='Kr Won -> US Dollar',bg="yellow",  command= self.convert_KRW_USD)
         # 버튼 2 생성 (KRW -> USD 기능 수행)
        button2.grid(row=3, column=1) # 버튼2 위치

    def convert_USD_KRW(self): # USD -> KRW 수행하는 함수, 1 USD = 1245.23 KRW
        USD = self.USD_var.get()
        KRW = USD * 1245.23 # 달러를 원으로 변환
        self.KRW_var.set(round(KRW, 2)) # 유효숫자 3자리로 표현
    
    def convert_KRW_USD(self): # KRW -> USD 수행하는 함수, 1 USD = 1245.23 KRW
        KRW = self.KRW_var.get()
        USD = KRW / 1245.23  # 원을 달러로 변환
        self.USD_var.set(round(USD, 2)) # 유효숫자 2자리로 표현

def main():
    window = Tk() # 윈도우 창 생성
    window.wm_title('2022-1 컴사파 Exam2B 21912193 신대홍') # 창 타이틀 설정
    app = USD_KRW_Calculator(window) # 창 출력
    window.mainloop() # 꺼지지 않게 함

if __name__ == "__main__": #메인함수 출력
    main()
