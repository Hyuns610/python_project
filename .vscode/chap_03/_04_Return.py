# 리턴 : 함수 실행 결과값

def plus(a, b):
  return a + b

def minus(a, b):
  return a - b

def multiply(a, b):
  return a * b

# 어떤 연산의 행위는 결과를 남긴다
rs = plus(10, 20)
print(f"plus rs : {rs}")

rs = minus(30, 5)
print(f"minus rs : {rs}")

print(f"multiply rs : {multiply(5, 10)}")

# v1
# def is_adult_age(age):
#   if age >= 20:
#     return True
#   return False

# v2
# 함수는 리턴을 만나면 그 즉시 종료된다
# def is_adult_age(age):
#   if age >= 20:
#     return True
#   return False

# v3
def is_adult_age(age):
  return age >= 20

age = 20
print(f"{age}살은 성인 나이인가요? : {is_adult_age(age)}")

age = 10
print(f"{age}살은 성인 나이인가요? : {is_adult_age(age)}")