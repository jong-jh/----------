num=int(input("숫자를 입력하세요 : "))

for i in range(1,num+1): #divide 1 to num
    if num%i==0: # if remainder is 0, i is factor
        print(i,end=' ') #출력 후 띄어쓰기.