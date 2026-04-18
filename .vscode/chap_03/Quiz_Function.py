# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

def print_8_dan():
  dan = 8
  i = 1
  while i <= 9:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1


i = 1
while i <= 9:
  print(f"== {i}번쨰 구구단 8단 출력 ==")
  print_8_dan()
  i += 1