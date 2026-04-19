# 컴프리헨션 : 직관적으로 리스트를 생성하는 방법
# 원본은 기반으로 한 복사본을 생성

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)

# 기본 문법
# [표현값 for 변수 in 반복가능객체 if 조건문]
# if문 사용 안할 시 생략 가능 

# 문제1 : 리스트 요소값의 2를 곱한 결과를 출력
# 정답 : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 정답1
"""
i = 0
while i < len(a):
  a[i] *= 2
  i += 1
print(a)
"""

# 정답2
"""
for i in range(len(a)):
  a[i] *= 2
print(a)
"""

# 정답3
rs = [v * 2 for v in a]
print(rs)


# 문제2 : 주어진 리스트에서 짝수값만 걸러낸 리스트 반환
# 정답 : [2, 4, 6, 8, 10]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rs = []

# 정답1
'''
i = 0
while i < len(a):
  if a[i] % 2 == 0:
    rs.append(a[i])
  i += 1
print(rs)
'''

# 정답2
'''
for i in range(len(a)):
  if a[i] % 2 == 0:
    rs.append(a[i])
print(rs)
'''
'''
for v in a:
  if v % 2 == 0:
    rs.append(v)
print(rs)
'''

# 정답3
rs = [v for v in a if v % 2 == 0]
print(rs)

# 문제3 : 주어진 리스트에서 짝수이면서 3의 배수인 수의 합을 반환
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
s = 0

'''
for v in a:
  if v % 2 == 0 and v % 3 == 0:
    s += v
print(f"합 : {s}")
'''

'''
for i in range(len(a)):
  if a[i] % 2 == 0 and a[i] % 3 == 0:
    s += a[i]
print(f"합 : {s}")
'''

rs = [v for v in a if v % 2 == 0 and v % 3 == 0]
print(f"합 : {sum(rs)}")

# 문제4 : 문자열 리스트에서 요소값을 대문자로 변환
# 대문자(uppercase) -> upper()
# 소문자(lowercase) -> lower()

fruits = ['apple', 'banana', 'mango', 'watermelon']

rs = [fruit.upper() for fruit in fruits]
print(rs)

for fruit in rs:
  print(fruit)
  
# 문제5 : 모든 정수를 문자열로 변환
numbers = [1, 2, 3, 4, 5]

rs = []
for v in numbers:
  rs.append(str(v))
print(rs)

rs = [str(v) for v in numbers]
print(rs)

# 문제6 : 문자열에서 숫자만 추출해서 반환
text = "abcd1234ef56ghe"

'''
for i in text:
  print(i, end=" ")
'''

# isdigit : 문자열 내부에서 숫자만 추출
'''
rs = []
for char in text:
  if char.isdigit():
    print(char)
    rs.append(int(char))
print(rs)
'''

rs = [int(char) for char in text if char.isdigit()]
print(rs)