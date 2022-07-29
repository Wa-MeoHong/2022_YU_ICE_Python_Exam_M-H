# 파일명 : Exam1A_21912193_신대홍.py
# 프로그램 목적 및 기능: 지정된 개수의 실수를 입력 후, 최대, 최소, 평균, 분산
#                   , 표준편차와 merge sort를 구현
# 프로그램 작성자 : 신대홍(2022년 4월 16일)
# 최종 Update : Version 1.0.0, 2022년 4월 16일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/16     v1.0.0       최초작성

from math import * #제곱근(루트)구할때 필요 

def inputFloatData(num_data): #리스트 입력
    L = []
    x = list(map(float, input("input 10 float Data : ").split())) # 입력받은 데이터를 쪼갬
    for i in range(0, num_data): #그중 딱 선 입력된 10개만 리스트에 추가 
        L.append(x[i])
    return L #리스트 반환
#-------------------------------------------------------------------------------------------   
def printList(name, L): #입력된 리스트 출력
    print(name, "=")
    for i in L:
        print("%6.2lf" %(i), end = "") #end로 한줄안에 입력하게 함
    print()
#-------------------------------------------------------------------------------------------
def getStatistics(L): #최대, 최소, 평균, 분산, 표준편차 계산
    max_index = 0
    min_index = 0
    MAX_List = L[0]
    MIN_List = L[0]
    for i in range(0, len(L)):
        if (MAX_List < L[i]):
            max_index = i
            MAX_List = L[i]
        if (MIN_List > L[i]):
            min_index = i
            MIN_List = L[i]
    
    MAX_L = MAX_List
    MIN_L = MIN_List
    AVG_L = sum(L)/len(L)
    
    V_sum = 0 #분산 덧셈
    for i in L:
        V_sum += (i-AVG_L)**2 #분산 = 편차의 제곱의 평균
    Var_L = V_sum / len(L)

    Std_L = sqrt(Var_L) #표준편차
    print("L_min = %3.2lf, L_max = %3.2lf, L_avg = %3.2lf, L_var = %3.2lf, L_std = %3.2lf"\
        %(MIN_L, MAX_L, AVG_L, Var_L, Std_L))
#-------------------------------------------------------------------------------------------
def mergeSort(L): #병합정렬 함수
    if len(L) < 2:
        return L[:] #2개 이하면 그냥 출력
    else:
        middle = len(L) // 2 #중간지점(나눌부분)찾음
        L_left = mergeSort(L[:middle]) #처음엔 가장 작은 부분(왼쪽 2개)부터 시작해서 점점 늘어감
        L_right = mergeSort(L[middle:])
    return merge(L_left, L_right) #정렬 시작
#
def merge(L_left, L_right):  #병합 정렬 하기 위한 함수
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right) #왼, 오른쪽 리스트의 길이
    
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]: 
            L_res.append(L_left[i]) #만약 왼쪽 리스트에 있는 것이 작다면 왼쪽리스트에 있는 걸 추가 
            i += 1 
        else:
            L_res.append(L_right[j]) #아니면 오른쪽
            j += 1 

    while (i < len_left): 
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res
#------------------------------------------------------------------------------------
def main(): #메인 함수 출력
    print("2022-1 컴사파 Exam1A 학번 : 21912193, 성명 : 신대홍 ")
    ListA = inputFloatData(10) #데이터 입력
    printList("L_data", ListA) #리스트 출력
    getStatistics(ListA) # 정보 구하기
    LA_Sorted = mergeSort(ListA) #정렬 하기
    printList("L_sorted", LA_Sorted) #정렬한 리스트 출력
#------------------------------------------------------------------------------------
if __name__ == "__main__":
    main() #메인함수 출력