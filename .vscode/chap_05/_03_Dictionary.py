# 딕셔너리

# 리스트의 한계점
ages = [10, 20, 30]
print(ages[0]) # 철수
print(ages[1]) # 민수
print(ages[2]) # 짱구

ages.append(40) # 맹구
print(ages[3])

del ages[2] # 짱구 나이 삭제
print(ages[2])

# 리스트 순회
# enumerate() : 리스트의 index, value를 동시에 가져올 수 있다.
ages = [10, 20, 30, 40, 50]

# print(list(enumerate(ages)))
for index, value in enumerate(ages):
  print(f"{index} : {value}")
  
# 딕셔너리
# key, value 한 쌍을 이루는 자료구조이다.
ages = {
  "철수": 10,
  "민수": 20,
  "짱구": 30,
  "맹구": 40
}

print(ages)

# 딕셔너리는 key를 통해 데이터의 접근 가능하다.
print(ages["철수"])
print(ages["민수"])
print(ages["짱구"])
print(ages["맹구"])

print("== 짱구 나이 삭제 ==")
del ages["짱구"]
print(ages)

print("== 민수 나이 수정 ==")
ages["민수"] = 21
print(ages)

print("== 딕셔너리 데이터 추가 ==")
# 딕셔너리의 해당 key가 존재하지 않으면 데이터 추가 된다.
ages["유리"] = 27
print(ages)

print("== 딕셔너리 반복 v1 ==")
for name in ages:
  age = ages[name]
  print(f"{name} : {age}살")
  
print("== 딕셔너리 반복 v2 : keys() ==")
# key 들로 이루어진 리스트 생성
print(ages.keys())
for name in ages.keys():
  age = ages[name]
  print(f"{name} : {age}살")
  
print("== 딕셔너리 반복 v3 values() ==")
# value 들로 이루어진 리스트 생성
print(ages.values())
for age in ages.values():
  print(f"나이 : {age}살")
  
print("== 딕셔너리 반복 v4 : items() ==")
print(ages.items())
for name, age in ages.items():
  print(f"{name} : {age}살")