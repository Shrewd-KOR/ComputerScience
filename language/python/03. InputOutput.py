 1. 파이썬 함수 구조
  def 함수명(매개변수):
     <수행>
      
 2. 다중 매개변수 입력값 함수 구조
  def add_many(*args):
     <수행>
 
 3. 함수의 결과값은 오직 1개
  return을 두번 호출할 수 없음 

 4. 매개변수 초기값 설정하기
  def say_myself(name, old, man=True):
     <수행>
  초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓도록
  
 5. 함수 안에서 함수 밖 변수를 접근하는 방법
  global a => 외부 a변수 접근
  
 6. lambda 함수 생성 예약어
  add = lambda a, b: a+b
  
 7. 사용자 입출력
  input() 입력되는 모든 것을 문자열로 취급
  input("입력하세요: ")
  
  print() "로 둘러싸인 문자열은 +연산과 동일, 문자열 띄어쓰기는 콤마로 한다
  
  print(i, end=' ') 개행이 아닌 띄어쓰기를 끝 문자로 출력
  
 8. 파일 입출력
  f = open("name.txt",'w')
  f.close()
  
  readline() readlines() read()
  write()
 
 
  
  
