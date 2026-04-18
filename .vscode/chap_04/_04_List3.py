nums = [10, 20, 30, 40, 50]

# 반복문을 이용한 순회 방법
print("== while문을 이용한 리스트 순회 ==")
i = 0
while i < len(nums):
  print(nums[i])
  i += 1
  
print("== for문을 이용한 리스트 순회 ==")
# v1
for val in nums:
  print(val)
  
# v2
for i in range(len(nums)):
  print(nums[i])
  
# v3 : 역순 출력
for i in range(len(nums) -1, -1, -1):
  print(nums[i])