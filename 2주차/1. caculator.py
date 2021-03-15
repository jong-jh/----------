num_1=input("첫번째 숫자를 입력하세요 : ")
print()
num_2=input("두번째 숫자를 입력하세요 : ")
print()
c=input("연산자를 입력하세요 : ")

if(c in '+'): #if '+' is in c, true
    print(num_1,c,num_2,"=",int(num_1)+int(num_2))#input으로 입력을 받으면 문자열로 받기 때문에 convert Integer type
elif(c in '-'):#if '-' is in c
    print(num_1,c,num_2,"=",int(num_1)-int(num_2))
elif(c in '*'):#if '*' is in c
    print(num_1,c,num_2,"=",int(num_1)*int(num_2))
elif(c in '//'):#if '//' is in c
    print(num_1,c,num_2,"=",int(num_1)//int(num_2))