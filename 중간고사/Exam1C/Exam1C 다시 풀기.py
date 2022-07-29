# 파일명 : Exam03 다시 풀기.py
# 프로그램 목적 및 기능: 딕셔너리를 이용해서 거리 테이블을 만들기
# 프로그램 작성자 : 신대홍(2022년 7월 2일)
# 최종 Update : Version 1.0.0, 2022년 7월 2일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/07/02     v1.0.0       최초작성

def  setKcity(d_ICD, C1, C2, Dist):         #키를 설정 
    d_ICD[(C1 ,C2)] = Dist

def getKCityDist(d_ICD, C1, C2):            #딕셔너리에서 키를 이용해서 값을 찾음
    if (C1, C2) in d_ICD:                   # C1, C2가 정방향, 역방향이든 상관없이 그 키가 포함되어있으면
        return d_ICD[(C1, C2)]              # 언제든지 찾을 수 있게, 2가지 경우를 모두 설정함
    elif (C2, C1) in d_ICD:
        return d_ICD[(C2, C1)]
    else:                                   # 위의 두 경우가 없다면 None처리 (c1 == c2 인 경우도 포함)
        return None

def printDTable(d_ICD): 
    keys = d_ICD.keys()                     # 키의 리스트를 만듦

    Column_width = 10
    L_city = []                             # 키를 담을 리스트를 만듦
    for key in keys:                        # keys 리스트 안의 키들을 하나하나씩 들고와서 대조
        (c1, c2) = key                      # 먼저 key를 이용해 c1, c2를 설정
        if c1 not in L_city:
            L_city.append(c1)               # 만약 리스트에 c1이 없다면 추가, 있으면 추가x
        elif c2 not in L_city:
            L_city.append(c2)               # c2가 없다면 추가
    Column_width = 10                       # 기본 자리수는 10자리로 설정
    # 표 양식
    print(" " * Column_width + "|", end='')
    for city in L_city:
        print("{:>10s}".format(city), end='') # 도시 출력
    print("\n" + "-" * Column_width + "+", end='')
    for citys in L_city:
        print("-" * Column_width, end='')   # 표 분리선 출력  
    print()
    for city1 in L_city:                    # 행마다 반복
        print("{:^10s}|".format(city1), end='') # city1(행 도시 이름)
        for city2 in L_city:                    # 열 방향 도시 
            dist = getKCityDist(d_ICD, city1, city2)    # city1, city2의 거리를 찾음
            if (dist == None) and (city1 == city2):     # 만약 dist가 None이고, 도시가 같으면 0 출력
                print("{:>10d}".format(int(0)), end='')
            elif (dist == None) and (city1 != city2):   # dist가 None, 그러나 도시가 다르면 unknown 출력
                print("{:>10s}".format("unknown"), end='')
            else:
                print("{:10d}".format(dist), end='')    # 그외는 정상출력
        print()                                     # 한 행 완료

def main():
    print("2022-1 컴사파 Exam1C 학번: 21912193, 성명: 신대홍") 

    d_ICD = dict() # == {} 

    Tuples_ICD = (("Seoul", "Daejon", 150), ("Daejon", "Daegu", 150), ("Seoul", "Daegu", 300),\
    ("Daegu", "Busan", 130), ("Seoul", "Busan", 430), ("Daegu", "Gwangju", 180),\
    ("Daejon", "Gwangju", 160), ("Seoul", "Gwangju", 310), ("Gwangju", "Busan", 210),\
    ("Daejon", "Busan", 280))                       #튜플 초기값들 

    print("S_ICD = ", Tuples_ICD)                   #튜플들 출력
    for icd in Tuples_ICD: 
        (c1, c2, d) = icd
        setKcity(d_ICD, c1, c2, d)                  #딕셔너리로 만듦

    print("\nInter_City_Distance_Table : ")         # 표 출력
    printDTable(d_ICD)

if __name__ == "__main__":
    main()