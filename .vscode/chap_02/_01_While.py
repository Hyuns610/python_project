# 반복문
# 1 ~ 10까지 출력

# while : ~할 때 동안 계속
# 반복문은 조건식이 True이면 실행
# False인 경우 종료 된다.
i = 1 # 시작값
while i <= 10: # 끝값
  print(i)
  i += 1 # 보폭 : 보폭을 작성하지 않으면 반복문의 조건식 계속 참이라 무한루프에 갇힌다.
  
print(f"i : {i}") # 11번 실행
  
print("== 내림차순 출력 ==")
i = 10
while i >= 1:
  print(i)
  i -= 1

print(f"i : {i}")