# print() : 출력문
# input() : 입력문

''' -> 여러줄 주석
a = input() # 입력받은 데이터를 a 변수에 넣어준다.
print(f"a : {a}")

b = input()
print(f"b : {b}")
'''

# input을 통해 입력받은 데이터는 모두 문자열이다.
a = input() # 10 -> '10'
b = input() # 20 -> '20'
print(a + b)

# 입력받은 데이터를 실제로 더해서 출력하고 싶은 경우
# int() : 문장을 숫자로 변경이 가능하다.
print(f"a + b = {int(a) + int(b)}")

# 입력 받자마자 해당 데이터를 정수값으로 형변환
x = int(input())
y = int(input())
print(f"x + y = {x + y}")

print("데이터를 두 개 입력해주세요.")
# print("첫 번째 데이터 : ", end="") end = "" --> 줄바꿈 하지 않겠다.
a = int(input("첫 번째 데이터 : "))
b = int(input("두 번째 데이터 : "))
print(f"a * b = {a * b}")