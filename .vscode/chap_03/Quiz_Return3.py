# 문제 : 1부터 1000사이에 존재하는 소수들의 개수를 출력해주세요.

# cnt = 0
# i = 1
# while i <= 1000:
#     i_is_prime_number = True
    
#     if i <= 1:
#       i_is_prime_number = False
      
#     elif i <= 2:
#       i_is_prime_number = True
      
#     elif i % 2 == 0:
#       i_is_prime_number = False
      
#     if i_is_prime_number:
#       for j in range(3, i):
#         if i % j == 0:
#           i_is_prime_number = False
#           break
        
#     if i_is_prime_number:
#       cnt += 1
      
#     i += 1

def is_prime_number(num):
  # 1은 소수가 아니고, 1이하의 값은 처리하지 않는다.
  if num <= 1:
    return False
  
  # 2는 소수이기 때문에 바로 True
  elif num == 2:
    return True
  
  # 짝수는 소수가 아니기 때문에 바로 False
  elif num % 2 == 0:
    return False
  
  for i in range(3, num):
    if num % i == 0:
      return False
  return True
    

def is_prime_number_count(num):
  cnt = 0
  for i in range(1, num + 1):
    if is_prime_number(i):
      cnt += 1
  
  return cnt

num = 1000
print(f"1부터 {num}사이에 존재하는 소수들의 개수 : {is_prime_number_count(num)}")