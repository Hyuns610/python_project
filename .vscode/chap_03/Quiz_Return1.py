# 문제 : 입력받은 정수의 모든 약수의 합을 리턴하는 함수를 구현해주세요.

def get_divisors_sum(num):
  s = 0
  i = 1
     
  ''' 구현 '''
  while i <= num:
    if num % i == 0:
      s += i
    i += 1
  return s

s = get_divisors_sum(1000)

print("정수 1000의 약수의 합 : {}".format(s))
# 출력 => 정수 1000의 약수의 합 : 2340