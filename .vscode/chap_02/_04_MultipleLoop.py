# 이중 반복문

# i = 1
# while i <= 3:
#   print(f"i : {i}")  
#   j = 1
#   while j <= 3:
#     print("사랑해")
#     j += 1 
#   i += 1

# 다중 반복문
# i = 1
# while i <= 3:
#   print(f"i : {i}")  
#   j = 1
#   while j <= 3:
#     k = 1
#     while k <= 3:
#       print("사랑해")
#       k += 1
#     j += 1 
#   i += 1

# for문을 이용한 중첩 반복문
# for문에서 반복문 내부에 코드를 돌리기 위해서 사용한다면
# 변수를 생략하고 생략하는 대신 _(언더바)를 둘 수 있다.
for i in range(3):
  print(f"i : {i}")
  for _ in range(3):
    for _ in range(3):
      print("사랑해")