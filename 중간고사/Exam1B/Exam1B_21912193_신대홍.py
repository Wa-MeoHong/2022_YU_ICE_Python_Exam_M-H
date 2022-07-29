# 파일명 : Exam1B_21912193_신대홍.py
# 프로그램 목적 및 기능: 다각형을 입력받아 꼭지점의 개수를 알아낸 후, 터틀 그래픽으로 표시
# 프로그램 작성자 : 신대홍(2022년 4월 16일)
# 최종 Update : Version 1.0.0, 2022년 4월 16일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/16     v1.0.0       최초작성

import turtle as t
from math import *

def  getNUmVertices(polygon_name): #꼭지점 개수 
    if (polygon_name == "triangle"): #삼각형
        return 3
    elif (polygon_name == "square"): #사각형
        return 4
    elif (polygon_name == "pentagon"): #오각형
        return 5
    elif (polygon_name == "hexagon"): #육각형
        return 6 
    elif (polygon_name == "heptagon"): #칠각형
        return 7
    elif (polygon_name == "octagon"): #팔각형
        return 8

def DrawPolygon (numVer, x, y, length, color):
    PI = 3.14159265358979 #각도를 구하기 위해 라디안으로 계산할 때 필요
    ROUND = 360 #360도를 상수로 지정해봄

    t.width(3)  #그리는 선분의 너비를 3으로 
    t.up()  #선을 그리지 않는 상태(펜을 위로 든 상태)
    t.goto(x, y)  #입력한 좌표로 이동, 후에 좌표를 출력
    t.write(t.pos())
    t.dot(10,"blue")  #좌표 표시용으로 점을 하나 찍는다
    j = (180 - (ROUND / numVer))/2 # 맨위 꼭지점으로 이동 후, 예시에 맞게 조정하기 위해
    # 내각의 절반을 구함
    radian = PI/180 * j # 라디안으로 변경
    height = (length/2)*tan(radian) #계산에 필요함
    hyp = sqrt(pow((length/2),2)+pow(height,2)) #중심위치에서 꼭짓점까지의 거리 구함

    if (numVer == 4 ): #만약 사각형일경우
        a = length/2 # 위에거 다무시하고, 길이의 절반만큼 x, y를 이동
        t.goto(x - a, y + a)
        t.lt(90 + (ROUND/ numVer)/2) # 이동후, 왼쪽위 45도를 바라본다.
    else:
        t.goto(x, y + hyp) # 나머지는 '중심 - 꼭지점까지 거리'(hyp)만큼  y좌표 이동후
        t.lt(90) #북쪽 바라보기
        
    t.lt(180 - j) #그후, 시작하기전 먼저 먼저 턴을 해줌
    t.write(t.position()) #위치 기록
    t.dot(10,"red")
    t.pencolor(color)
    t.down()  #이제부터 펜을 아래로 놓아 그릴 준비 

    for i in range(0,numVer):
        t.forward(length) #앞으로 가면서 그림
        t.lt(ROUND / numVer) #외각만큼 턴함
    t.up()
    t.home() #끝나고 홈으로 돌아감(좌표, 보는 방향 초기화)

def main():
    t.setup(600, 400) #터틀 창 크기 조절
    t.title("2022-1 컴사파 Exam1B 학번 : 21912193, 성명: 신대홍") #터틀 창 제목
    t.shape("classic") #거북이 모양 = 클래식 화살표
    shapes = [
        ("triangle", -200, 75, 100, "red"), ("square", 0, 75, 50, "blue"),\
        ("pentagon", 200, 75, 50, "green"), ("hexagon", -200, -75, 50, "green"),\
        ("heptagon", 0, -75, 50, "red"), ("octagon", 200, -75, 50, "blue")
    ] #다각형 초기값, 위치, 선색깔

    for shape in shapes: # 출력
        sh, cx, cy, length, color = shape[0], int(shape[1]), int(shape[2]), int(shape[3]), shape[4]
        num_vertices = getNUmVertices(sh) #꼭짓점 개수 구하기
        DrawPolygon(num_vertices, cx, cy, length, color)
    t.mainloop() #끝나고 창이 안꺼지게 함

if __name__ == "__main__":
    main()