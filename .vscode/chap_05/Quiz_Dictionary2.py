# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 
# update를 이용하여, 2월을 29일로 수정하고 4월, 5월의 정보도 추가
month_end_days = {'1월': 31, '2월': 28, '3월': 31}
month_end_days2 = {'2월': 29, '4월': 30, '5월': 31}
month_end_days.update(month_end_days2)
print(month_end_days)

# 문제 : 영수, 영희, 철수, 민수의 나이를 딕셔너리에 담고, 데이터를 넣은 순서대로 순회출력
ages = {"영수": 10, "영희": 20, "철수": 30, "민수": 40}
for name, age in ages.items():
  print(f"{name} : {age}살")