# 예 : 구구단 출력 프로그램을 만드는 팀에 합류
# 함수
# 함수는 정의해야만 사용이 가능하다.
# 함수를 정의했으면 호출해야만 함수를 사용할 수 있다.

# 함수 정의
# def(define)
def print_2_dan():
  dan = 2
  for i in range(1, 10):
    print(f"{dan} * {i} = {dan * i}")

# 함수 호출
# print_2_dan()
# print_2_dan()
# print_2_dan()

for i in range(1, 11):
  print(f"== {i}번 실행 ==")
  print_2_dan()
