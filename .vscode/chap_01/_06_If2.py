# 조건문은 복수개의 정답을 가져서는 안 된다!

age = 50
age_grade = -1

if age < 10:
  age_grade = 0
  
if age >= 10 and age < 20: # 나이가 10살 이상이고 20살 미만이다.
  age_grade = 10 # 10대
  
if age >= 20 and age < 30: # 나이가 10살 이상이고 20살 미만이다.
  age_grade = 20 # 20대
  
if age >= 30 and age < 40: # 나이가 10살 이상이고 20살 미만이다.
  age_grade = 30 # 30대
  
if age_grade == -1:
  print("50대 이상입니다.")
elif age_grade == 0:
  print("10살 미만 아동입니다.")
else:
  print(f"{age_grade}대 입니다.")