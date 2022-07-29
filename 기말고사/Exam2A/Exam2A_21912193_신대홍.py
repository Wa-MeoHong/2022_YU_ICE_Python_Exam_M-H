# 파일명 : Exam2A_21912193_신대홍.py
# 프로그램 목적 및 기능: Excel 파일을 읽어와서 학생의 성적 평균, 과목평균을 
#           Pandas를 이용해 계산하고 xlsx파일로 작성하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 6월 11일)
# 최종 Update : Version 1.0.0, 2022년 6월 11일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/06/11     v1.0.0       최초작성

import pandas as pd #판다스 모듈 호출

df = pd.read_excel("ExamA_student_scores_21912193_신대홍.xlsx")
#엑셀에서 데이터를 읽어와 df생성

print("df_with_avg = ") # 읽어온 초기 데이터를 먼저 출력
avgs_Student = df.loc[:, ['Kor', 'Eng', 'Math', 'Sci']].mean(1)
#df.loc을 통해 계산하고 싶은 열의 데이터들을 가져왔음
# 각 학생의 평균 성적을 계산함. 
df['Avg'] = avgs_Student #학생 평균 성적 행을 추가

print(df,"\n") # 데이터 프레임 출력

avgs_Class = df.loc[:, ['Kor', 'Eng', 'Math', 'Sci', 'Avg']].mean()
#열의 평균 (과목당 평균, 학생평균성적의 평균)

df.sort_values('Avg', ascending=False, inplace=True) 
#학생 평균성적을 기준으로 내림차순 정렬 후, 저장(inplace)
# sort_values(기준열, 오름/내림, 저장)

df.loc[len(df)] = avgs_Class #과목 평균, 평균 성적의 평균을 추가
df.at[len(df)-1, 'st_name'] = 'Per_class_Avg' #과목 평균 열의 이름을 추가
df = df.fillna(' ') #Nan 값을 모두 공백으로 조정

print("df_sorted_with_Avg = ") # 통계가 끝난 데이터 출력
print(df,"\n") #출력
print("Writing df to excel File") #엑셀 파일로 작성

with pd.ExcelWriter("ExamA_processed_scores_21912193_신대홍.xlsx") as excel_writer:
    df.to_excel(excel_writer) #작성
