# 문제 : 입력받은 정수의 모든 약수를 출력하는 함수를 구현해주세요.

def print_divisors(num):
  i = 1
  while i <= num:
    if num % i == 0:
      print(i)
    i += 1
  # 구현

print_divisors(1000)
''' 출력
1
2
4
5
8
10
20
25
40
50
100
125
200
250
500
1000
'''