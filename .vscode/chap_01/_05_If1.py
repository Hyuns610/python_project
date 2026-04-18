# 사람의 나이에 따른 성인, 미성년 판별 프로그램 설계!

age = 20

# 조건문은 조건식이 True인 경우에 실행된다.
# 조건문은 조건식이 False인 경우에 실행되지 않는다.

# v1 : 비효율적으로 작성된 코드
if age >= 20:
  print("성인입니다.")

if age < 20:
  print("미성년입니다.")
  
# v2 : v1보다는 효율적인 구조
if age >= 20:
  print("성인입니다.")
elif age < 20:
  print("미성년입니다.")
  
# v3 : if, else 구조
if age >= 20:
  print("성인입니다.")
else: # if문의 맨 마지막에 위치
  print("미성년입니다.")