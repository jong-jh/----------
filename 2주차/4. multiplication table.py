s='=========================================================='
menu='구구단'
print(s.center(80,' ')) #밑줄 출력 #80칸 공간 확보 및 가운데 정렬
print(menu.center(80,' '))
print(s.center(80,' ')) #밑줄 출력
for i in range(1,10): # i increase  1 to 9
    for j in range(1,10): #1부터 9까지 j값 증가,  j increase  1 to 9 
        #2중 for 문으로 j값이 9까지 커진 뒤 i값이 1 커짐
        print("{}*{} ={:2}".format(j,i,i*j),end='  ')
    print()#구구단의 한 행이 다 출력된 뒤 줄 바꿈.