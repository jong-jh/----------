# try:

#     print("나누기 전용 계산기")
#     num1=int(input("첫 번째 숫자를 입력 : "))
#     num2=int(input("첫 번째 숫자를 입력 : "))

#     print("{}/{}={}".format(num1,num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:
#    print("오류가 발생하였습니다.")

# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1=int(input("first num: "))
#     num2=int(input("second num: "))
#     if num1>=10 or num2>=10:
#         raise BigNumberError("한 자리 수만 입력 부탁")
#     print("{}/{}={}".format(num1,num2,int(num1/num2)))
# except BigNumberError as err:
#     print(err)
class lownum(Exception):
    def __init__(self):
        print("양의 자리 숫자를 입력해주세요")

class SoldOutError(Exception):
    pass