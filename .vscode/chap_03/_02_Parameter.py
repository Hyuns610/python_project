# 예 : 구구단 프로그램 만드는 팀에 합류
# 

def print_dan(dan, limit): # 매개변수(parameter)
  print(f"== {dan}단 ==")
  i = 1
  while i <= limit:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1
    
print_dan(4, 3) # 인자값(arguments)
print_dan(8, 5)
print_dan(12, 10)