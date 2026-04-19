# 문제 - 리스트를 역순으로 출력해주세요.
# 조건 : 반복문, 리스트 전용 함수 사용가능

lst = [1, 2, 3, 4, 5]

# 출력: [5, 4, 3, 2, 1]
print(sorted(lst, reverse=True))


# 문제 - 리스트의 모든 요소값을 더해주세요.
# 조건 : while문 사용가능, 리스트 전용 함수 사용 가능

lst = [1, 2, 3, 4, 5]

# 정답 : 15
print(f"정답 : {sum(lst)}")


# 문제 - 리스트에서 최대값, 최소값을 구해 주세요.
# 조건 : while문 사용 가능, 리스트 전용함수 사용가능

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 최대값 : 9
print(f"최대값 : {max(lst)}")
# 최소값 : 1
print(f"최소값 : {min(lst)}")


# 문제 - 리스트에서 특정 값의 인덱스 찾아주세요.
# 조건
 # 1) 특정 값을 찾으면 해당 값의 인덱스를 출력
 # 2) 없는 경우 -1이 출력

# 예시
lst = [1, 2, 3, 4, 5]

def find_index(lst, a):
  if a in lst:
    return lst.index(a)
  else:
    return -1

print(find_index(lst, 3))  # 출력: 2
print(find_index(lst, 6))  # 출력: -1


# 문제 - 리스트에서 짝수와 홀수 분리해서 새로운 리스트를 만들어주세요.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for i in lst:
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)

print(even) # 출력: [2, 4, 6, 8, 10]
print(odd) # 출력: [1, 3, 5, 7, 9]
  