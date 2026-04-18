# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에 있는지 if문으로 체크 후, 있다면 삭제해주세요.
lst = ['월', '화', '수', '목', '금']
target = '화'
if target in lst:
  lst.remove(target)
else:
  print(f"{target}은 존재하지 않습니다.")
print(lst)

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 리스트에 있는 '금'을 안전하게 삭제하는 2가지 방법을 보여주세요.
lst = ['월', '화', '수', '목', '금']
target = '금'
# if target in lst:
#   lst.remove(target)

if target in lst:
  del lst[lst.index(target)]
print(lst)