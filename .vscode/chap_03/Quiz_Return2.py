# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.

def is_prime_number(num):
  # 1은 소수가 아니고, 1이하의 값은 처리하지 않는다.
  if num <= 1:
    return False
  
  # 2는 소수이기 때문에 바로 True
  if num == 2:
    return True
  
  # 짝수는 소수가 아니기 때문에 바로 False
  if num % 2 == 0:
    return False
  
  for i in range(3, num):
    if num % i == 0:
      return False
  return True
  

print("3은 소수입니다 : {}".format(is_prime_number(3)))
print("4는 소수입니다 : {}".format(is_prime_number(4)))
print("1000은 소수입니다 : {}".format(is_prime_number(1000)))