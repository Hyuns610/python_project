# 내장 함수 : print(), input(), int(), str()
# 사용자 정의 함수 : def를 이용해서 생성

# 내장 객체
# - 파이썬에서 사용하는 모든 데이터(int, str, float, double)
# - 컬렉션 객체 : 리스트, 튜플, 딕셔너리

# 사용자 정의 객체 : 클래스
# 클래스는 객체가 아니고, 객체를 만들기 위한 설계도이다.
# 클래스 내부에는 속성과 기능을 정의할 수 있다.
# 속성은 변수로 만들고, 기능은 함수로 만든다.
class Person():
  # 생성자 메서드
  # 객체가 만들어질 때 딱 한번 실행
  # 클래스 내부에 함수를 만들 때 self 무조건 매개변수로 넘겨줘야 한다.
  def __init__(self, age, name, hobby, home_town):
    self.age = age
    self.name = name
    self.hobby = hobby
    self.home_town = home_town
    
  # 객체의 출력 형식을 주소값이 아닌 커스텀 방식으로 출력이 가능
  # 개발자 디버깅 활동을 할 때 도움을 주는 함수
  def __str__(self):
    return f"age: {self.age}, name: {self.name}, hobby: {self.hobby}, home_town: {self.home_town}"

  def introduce(self):
    print("== 자기소개 시작 ==")
    print(f"나이 : {self.age}살")
    print(f"이름 : {self.name}")
    print(f"취미 : {self.hobby}")
    print(f"사는 곳 : {self.home_town}")
    print("== 자기소개 끝 ==")
  
# 사람 객체 생성
p1 = Person(10, "홍길동", "축구", "대전") # 객체 생성
print(p1)
print(p1.age)
print(p1.name)
print(p1.hobby)
print(p1.home_town)
p1.introduce()

# 객체 내부에 속성과 기능에 접근시에 . 을 통해 접근
p2 = Person(20, "홍길순", "탁구", "안산")
print(p2)
print(p2.age)
print(p2.name)
print(p2.hobby)
print(p2.home_town)
p2.introduce()

# p2.age = 21
p2.age += 1
p2.name = "홍순만"
p2.introduce()

print(p1)
print(p2)