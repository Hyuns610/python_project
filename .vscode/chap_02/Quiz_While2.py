# 문제 - 1부터 1000 사이의 수 중에서 3의 배수만 출력해주세요.(개념 : while, if, %)

i = -1
while i <= 1000:
  if i % 3 == 0:
    print(i)
  i += 1

# 문제 : 1부터 100까지의 수 중에서 짝수이고 3의 배수가 아닌 수의 합을 출력해주세요.

i = 1
result = 0
while i <= 100:
  if i % 2 == 0 and i % 3 != 0:
    result += i
  i += 1
print(result)

# n과 m 사이의 수 중 k의 배수 출력
n = 10
m = 30
k = 3

while n <= m:
  if n % k == 0:
    print(n)
  n += 1