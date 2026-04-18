dan = 3
i = 1
while True:
  if i == 4:
    i += 1
    continue # 다음 실행 될 코드를 스킵
  
  print(f"{dan} * {i} = {dan * i}")
  
  if i == 10:
    break # 반복문 안에서만 사용이 가능, 반복문을 탈출(멈출 때) 사용한다.
  
  i += 1