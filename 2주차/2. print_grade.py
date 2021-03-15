stdnum=int(input("학번을 입력해 주세요: ")) #convert Integer type
print()
stdname=input("이름을 입력해 주세요: ")
print()
kor_Grade=int(input("국어 성적을 입력해 주세요: "))#convert Integer type
eng_Grade=int(input("영어 성적을 입력해 주세요: "))#convert Integer type
math_Grade=int(input("수학 성적을 입력해 주세요: "))#convert Integer type
C_Grade=int(input("C언어 성적을 입력해 주세요: "))#convert Integer type

total_Grade=kor_Grade+eng_Grade+math_Grade+C_Grade#sum of total grade
ave_Grade=round(total_Grade/4,2)#average of total grade

if(ave_Grade>=90): #평균 성적에 따른 학점 부여
    hakjum='A'
elif(ave_Grade>=80):
    hakjum='B'
elif(ave_Grade>=70):
    hakjum='C'
elif(ave_Grade>=60):
    hakjum='D'
else:
    hakjum='F'
    
print(stdname,"의 총점은 ",total_Grade,"이고 평균은",ave_Grade,end="")
print("이며 학점은 ",hakjum,"입니다")