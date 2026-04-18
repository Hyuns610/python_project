# 컬렉션 객체 : 리스트, 튜플, 딕셔너리

'''
nums = [] # 리스트 객체 하나 생성
print(id(nums))

nums2 = []
print(id(nums2))

nums3 = []
print(id(nums3))
'''

nums = [1, 2, 3, 4, 5] # 리스트 객체 초기화
print(nums)
print(id(nums))

nums2 = nums # 객체 하나 공유
print(nums2)
print(id(nums2))