# 컬랙션 객체
# 리스트, 튜플, 딕셔너리

# 튜플 이란

# mutable(가변) | immutable(불가변)
# 리스트는 기본적으로 가변 데이터이다.
# 리스트는 기본적으로 CRUD가 가능하다.
# C(Create), R(Read), U(Update), D(Delete)
a = [1, 2, 3, 4, 5]
print(type(a)) # list
print(a)
a[2] = 10
print(a)
del a[2]
print(a)

# 튜플
# 튜플은 C(Create), R(Read)만 지원한다.
# 튜플은 불가변 객체이다.
a = (1, 2, 3, 4, 5)
print(type(a)) # tuple
print(a)
print(a[1])
# a.append(10)
# a[1] = 10
# a.remove(3)
# del a[3]
print(a)