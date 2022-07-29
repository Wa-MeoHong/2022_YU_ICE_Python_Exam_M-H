# 파일명 : Exam2D_21912193_신대홍.py
# 프로그램 목적 및 기능: 실수 자료형 리스트에 대한 병합정렬, 퀵정렬 성능비교
# 프로그램 작성자 : 신대홍(2022년 6월 11일)
# 최종 Update : Version 1.0.0, 2022년 6월 11일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/06/11     v1.0.0       최초작성

from random import *
import time

def genBigRandList(BigR, SIZE): # 랜덤한 난수 발생 함수
    i = 0
    while i < SIZE:
        BigR.append((i - SIZE/2)/100) # i를 BigR리스트에 넣어준 후, i를 증가
        i += 1
    shuffle(BigR)               #셔플
#

def printListSample(L_BigRand, LINE_SIZE, Print_Lines): #난수 리스트 출력 
    SIZE = len(L_BigRand)

    if (SIZE <= 50): #만약 리스트의 개수가 50개 이하인 경우는 그냥 10개씩 출력하게함
        for k in range(0, SIZE // LINE_SIZE + 1):
            for j in range(0, LINE_SIZE): 
                if ((10*k + j) == SIZE):    # 만약 배열을 출력할 때 배열에 끝에 도달했다면
                    break #바로 중지
                print("%10.2lf" %(L_BigRand[k*10+j]), end = "") 
            print()
    else: #만약 아니라면
        for k in range(0, Print_Lines) :    # 처음 Print_Lines만큼을 먼저 출력
            for j in range(0, LINE_SIZE):
                print("%10.2lf" %(L_BigRand[k*10+j]), end = "")
            print()
        count = SIZE - (Print_Lines * LINE_SIZE) 
        print("\t . . . . . .")             # . . . 을 출력
        for k in range(0, Print_Lines) :    #마지막 Print_Lines만큼 출력
            for j in range(0, LINE_SIZE): 
                print("%10.2lf" %(L_BigRand[count+k*10+j]), end = "")
            print()
#
# 병합 정렬 (Merge Sort)
def merge(L_left, L_right):                 #병합 정렬 하기 위한 함수
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right) #왼, 오른쪽 리스트의 길이
    
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]: 
            L_res.append(L_left[i])         #만약 왼쪽 리스트에 있는 것이 작다면 왼쪽리스트에 있는 걸 추가 
            i += 1 
        else:
            L_res.append(L_right[j])        #아니면 오른쪽
            j += 1 

    while (i < len_left):                   # 나머지 요소를 추가해준다. 
        L_res.append(L_left[i])             # 왼쪽요소 추가
        i += 1
    while (j < len_right):                  # 오른쪽 요소도 추가 해준다.
        L_res.append(L_right[j])
        j += 1
    return L_res                            #이제 반환
#
def mergeSort(L):                           #병합정렬 함수
    if len(L) < 2:
        return L[:]                         #2개 이하면 그냥 출력
    else:
        middle = len(L) // 2                #중간지점(나눌부분)찾음
        L_left = mergeSort(L[:middle])      #처음엔 가장 작은 부분(왼쪽 2개)부터 시작해서 점점 늘어감
        L_right = mergeSort(L[middle:]) 
    return merge(L_left, L_right)           #정렬 시작
#

# 퀵정렬 (Quick Sort)
def Partition(L, L_left, L_right, P_I): # P_I의 좌측엔 P_I의 값보다 작은값, 우측엔 더 큰값으로 만드는 함수
    P_V = L[P_I] #먼저 P_I의 값을 L의 가장 우측으로 밀어버리고, 그 맨 우측의 값을 인덱스P_I의 위치에 옮긴다.
    L[P_I] = L[L_right]
    L[L_right] = P_V
    # SWAP 끝

    newPI = L_left # 새로운 P_I를 저장

    for i in range(L_left, L_right): # 범위 내에서
        if(L[i] <= P_V):            # P_V = L[P_I]의 값보다 작다면
            temp = L[i]             # 값 교환이 일어남. (작으면 왼쪽으로 이동함.)
            L[i] = L[newPI]
            L[newPI] = temp
            newPI += 1              # Swap이 일어난 후, newPI가 갱신된다. 
    
    P_V = L[L_right] #newPI를 모두 갱신된 후에는 맨 우측으로 옮겨놓았던 P_I의 값을 다시 제자리로 보냄
    L[L_right] = L[newPI]
    L[newPI] = P_V

    return newPI #모든 작업이 끝난후 반환한다.
#
def Quick_Sorting(L, L_left, L_right): #퀵정렬 본함수
    if (L_left >= L_right): #만약 Left와 Right가 같거나 Left가 더 커진다면
        return              # 다시 돌아간다. 
    else:
                    #P_I = Pivot_Index (기준 인덱스 번호, 주로 Left, Right의 중간) 
        P_I = (L_left + L_right) // 2 #인덱스번호는 정수이므로 //를 통해 내림연산을 해준다.

    New_P_I = Partition(L, L_left, L_right, P_I)

    if(L_left < (New_P_I - 1)):
        Quick_Sorting(L, L_left, New_P_I-1)
    if((New_P_I + 1) < L_right):
        Quick_Sorting(L, New_P_I+1, L_right)
#
def QuickSort(L):   #퀵정렬 초기 시작함수
    L_SIZE = len(L)
    Quick_Sorting(L, 0, L_SIZE-1)

L = []

def main():
    print("2022-1 컴사파 Exam2D 학번 : 21912193, 이름: 신대홍") # 확인용 이름

    SIZE_List = [100000, 500000, 1000000, 5000000]
    print("\nComparisons of Sorting Algorithms") 
    for L_SIZE in SIZE_List:
       
        print("\nCreating random list of size (%d)" % (L_SIZE))
        if (L_SIZE == 0):
            break
        genBigRandList(L, L_SIZE)   # 입력한 갯수만큼 랜덤한 수 생성(중복은 없다)

        #Testing Merge Sort 
        shuffle(L)
        print("\nBefore Merge Sort of L :") #정렬 전 출력
        printListSample(L, 10, 3) 
        t1 = time.time()                # 정렬 전 시간 측정
        L_sorted = mergeSort(L)         # 병합정렬 진행 후 반환 받음
        t2 = time.time()                # 정렬 후 시간 측정
        print("\nAfter Merge Sort of L . . .") # 정렬 후 출력
        printListSample(L_sorted, 10, 3) # 출력
        time_elapsed = t2- t1              # 걸린 시간 구함
        print("Merge Sorting of list (size= {0:d}) {1:.6f} sec".format(L_SIZE, float(time_elapsed))) #럴린 시간 출력

        #Testing Quick Sort 퀵정렬
        shuffle(L)
        print("\nBefore Quick Sort of L :") # 정렬 전 출력
        printListSample(L, 10, 3) # 
        t1 = time.time()
        QuickSort(L)            # 퀵정렬
        t2 = time.time()
        print("\nAfter Quick Sort of L . . .") #L_res 과 L은 같은 리스트이므로 L_res를 정렬 후 출력
        printListSample(L, 10, 3)
        time_elapsed = t2- t1   #걸린 시간 구함
        print("Quick Sorting of list (size= {0:d}) {1:.6f} sec".format(L_SIZE, float(time_elapsed))) #걸린 시간 출력

#
if __name__ == "__main__": #메인함수 출력
    main()
