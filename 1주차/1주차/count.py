from collections import Counter
f = open("C:/충북대학교/소프트웨어학과/2학년/1학기 수업/오픈소스기초프로젝트/1주차/mobydick.txt", encoding="utf-8")
#d드라이브가 없어 c드라이브 안에 넣고 진행
count = Counter(f.read().split())

print("단어 출현 횟수 :", count)