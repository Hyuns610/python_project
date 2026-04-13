# 변수 선언, 변수에다가 값을 할당
# 변수 초기화
# 변수 : 값을 저장하는 공간
# 변수에는 오직 값을 하나만 저장 가능하다.
# = : 대입연산자
x = 10
print(f"x : {x}")

x = 20
print(f"x : {x}")

x = x + 30
print(f"x : {x}")

# a = 10
# b = 10
# c = 10

# a, b, c 변수에 10을 동시에 할당
a = b = c = 10
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")

# 여러 변수에 값을 할당
x, y, z = 10, 20, 30
print(f"x : {x}")
print(f"y : {y}")
print(f"z : {z}")

# 변수는 변수에 어떤 값을 넣느냐에 따라 변수의 타입이 정해진다.
a1 = 1000
print(f"a1 : {a1}")
print(type(a1)) # a1 변수의 타입을 확인
# a1의 데이터 타입은 'int' 이다.

a2 = "안녕"
print(f"a2 : {a2}")
print(type(a2)) # a2의 데이터 타입은 'str' 이다.

a3 = 3.14
print(f"a3 : {a3}")
print(type(a3)) # a3의 데이터 타입은 'float' 이다.
# float은 실수형 데이터 타입이다.