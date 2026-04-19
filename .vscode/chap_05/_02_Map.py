# input()

# input 을 통해서 입력받는 데이터는 모두 문자열이다.
# strip() : 양 옆의 발생한 공백을 제거한다. (중간에 발생한 공백 제거 x)
# split() : 특정 문자를 기준으로 입력받은 데이터를 나눈다.
# split() 만 사용하는 경우에 띄어쓰기를 기준으로 문자열을 나눈다. (띄어쓰기 몇 개여도 나누어줌)

'''
# 매번 아래와 같이 작업은 매번 형변환을 해줘야 하기 때문에 비효율적이다.
print("숫자 하나를 입력해주세요 : ", end="")
a = input().strip().split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
print(a[0] + a[1])
'''


# map : 입력받은 데이터를 map객체로 변환
print("숫자를 입력해주세요 : ", end="")
# int(), str(), list()
a = list(map(int, input().strip().split()))
print(a)
print(f"sum : {sum(a)}")