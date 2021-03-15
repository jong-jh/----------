# def std_weight(height,gender):
#     if gender=="M":
#         return height*height*22
#     else:
#         return height*height*21

# height=175
# gender = "M"
# weight=round(std_weight(height/100,gender),2)
# print("키{}, 성별 {}, 몸무게 {}".format(height,gender,weight))

# scores={"math":0,"english":50,"coding":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(3),sep=":")
# for num in range(1,21):
#     print("num : "+str(num).zfill(3)) #0을 채워주는 함수
# answer=input("press the anykey : ")
# print("your key is : "+answer+".")

# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# print("{0:_<+10}".format(500))
# print("{0:,}".format(10000000000000))
# print("{0:.2f}".format(5/3)) #소수점 셋째자리에서 반올림

# score_file=open("score.txt","w",encoding="utf-8")
# print("math : 0",file=score_file)
# print("english : 50",file=score_file)
# score_file.close()

# score_file=open("score.txt","a",encoding="utf8")
# score_file.write("\nscience : 80")
# score_file.write("\ncoding : 80")

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# while True:
#     line =score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

#pickle
# import pickle
# profile_file=open("profile.pickle","wb")
# profile={"name":"jong", "age":23,"hobby":["soccer","piano"]}
# print(profile)
# pickle.dump(profile,profile_file)#profile에 있는 정보를 file에 저장
# profile_file.close()

# import pickle
# profile_file=open("profile.pickle","rb")
# profile=pickle.load(profile_file)#파일에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle
# #close() 함수 없이 파일 쓰고 읽는 법
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8")as study_file:
#     study_file.write("파이선 공부 중")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())
for i in range(1,51):
    with open("{}주차.txt".format(i),"w",encoding="utf8") as report_file:
        report_file.write("부서 : \n이름: \n업무 요약:")
