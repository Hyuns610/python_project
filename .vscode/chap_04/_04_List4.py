# 리스트 전용 내장 함수
nums = [5, 7, 3, 2, 6, 1, 8, 9, 10, 4]
print(nums)
print(f"원본 : {id(nums)}")

# 리스트 오름차순 정렬
# 정렬 함수 : sort()
# 원본 리스트를 훼손하여 정렬
nums.sort()
print(nums)
print(f"원본 : {id(nums)}")

# 정렬 함수 : sorted(list)
nums = [5, 7, 3, 2, 6, 1, 8, 9, 10, 4]
print(f"정렬 전 : {nums}")
print(f"원본 주소값 : {id(nums)}")

sorted_nums = sorted(nums)
print(f"정렬 후 : {sorted_nums}")
print(f"복사본 주소값 : {id(sorted_nums)}")

# sorted(nums, reverse=True) : 리스트 역순 정렬
sorted_nums = sorted(nums, reverse=True)
print(f"정렬 후 : {sorted_nums}")
print(f"복사본 주소값 : {id(sorted_nums)}")

# 리스트를 반대로 뒤집어 주는 함수 : reverse()
# 원본 리스트를 훼손하여 반대로 뒤집어줌
nums = [5, 7, 3, 2, 6, 1, 8, 9, 10, 4]
print(id(nums))

nums.reverse()
print(id(nums))
print(nums)

# 최대값, 최소값
lst = [30, 127, 5, 3, 100, 1]

"""
max_num = lst[0]
min_num = lst[0]

i = 0
while i < len(lst):
  if lst[i] > max_num:
    max_num = lst[i]
  elif lst[i] < min_num:
    min_num = lst[i]
  i += 1
  
print(f"max_num : {max_num}")
print(f"min_num : {min_num}")
"""

lst = [30, 127, 5, 3, 100, 1]
print(f"최대값 : {max(lst)}")
print(f"최소값 : {min(lst)}")

# 리스트 합 구하기
a = []
for i in range(1, 11):
  a.append(i)
  
s = 0
for val in a:
  s = s + val
  
print(f"합계 : {s}")

# sum 함수 도입
print(f"합계2 : {sum(a)}")
print(f"평균 : {sum(a) / len(a)}")