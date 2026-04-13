# 연산자 우선순위 : 사칙 > 비교 > 논리

print("== 사칙연산자 예시 ==")
print(10 + 10)
print(30 - 5)
print(30 * 5)
print(5 ** 3) # 제곱
print(10 / 3) # 나눈 몫
print(10 // 3) # 나눈 몫의 정수부분
print(10 % 3) # 나눈 나머지

print("== 비교연산자 예시 ==")
print(5 >= 3)
print(5 > 3)
print(3 <= 1)
print(3 < 1)
print(10 == 10) # 같다
print(10 != 10) # 같지 않다

print("== 논리연산자 예시 ==")
# 논리 연산자 우선순위 : not > and > or
# and -> 앞에서 먼저 false가 나오거나 true가 나오면 뒤에 연산은 하지 않는다. (최적화)
print(10 > 3 and 5 == 5) # 양쪽을 비교한 결과값이 둘 다 True인 경우 결과는 True이다.
print(10 < 3 and 5 == 5) # 양쪽을 비교한 결과값 중 하나라도 False인 경우 결과는 False이다.
print(5 != 5 or 3 < 1) # 양쪽을 비교한 결과값이 둘 다 False인 경우 결과는 False이다.
print(5 == 5 or 3 < 1) # 양쪽을 비교한 결과값 중 하나라도 True인 경우 결과는 True이다.

print(not True)
print(not(not True))
