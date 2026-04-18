nums = [10, 20, 30, 40, 50]

# 1. 리스트 요소값 접근
# 리스트의 요소값은 index로 접근이 가능
print(nums[0])
print(nums[1])
print(nums[2])
# print(nums[5]) # list index out of range

# 리스트 요소값 추가
# append() : 요소값 추가(추가된 요소값은 맨 뒤에 위치)
nums.append(60)
print(nums)

nums.append(70)
print(nums)

# 리스트 요소값 삭제1 : remove(val)
# 동일안 요소값이 두 개 이상 존재하는 경우, 해당 요소값의 첫 번째 위치한 값이 제거
nums = [10, 20, 30, 40, 50, 30]
nums.remove(30)
print(nums)

nums.remove(30)
print(nums)

# nums.remove(30) # list.remove(x): x not in list
# print(nums)

# 리스트 요소값 삭제2 : del list[index]
nums = [10, 20, 30, 40, 50]
del nums[2]
print(nums)

del nums[2]
print(nums)

# 리스트 요소값 수정
nums = [10, 20, 30, 40, 50]
print(f"수정 전 : {nums}")

nums[2] = 300
print(f"수정 후 : {nums}")

# 리스트 요소값 길이
nums = [10, 20, 30, 40, 50]
# len : length의 약자
print(f"리스트 길이 확인 : {len(nums)}")

# 리스트 요소값의 위치 확인 : index(val)
nums = [10, 20, 30, 40, 50]
print(f"find index : {nums.index(40)}")

# print(f"find index : {nums.index(60)}") -> 없는 값은 조회 불가능