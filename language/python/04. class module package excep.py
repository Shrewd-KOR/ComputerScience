 1. 클래스
 
 2. 모듈
  import 모듈명
  from 모듈명 import 함수명 => 모듈명.함수명이 아니라 함수명만으로 호출이 가능
  from 모듈명 import *
  
  __name__ 변수 => 직접 모듈팡리을 실행할 경우 __main__이 할당되지만 다른 모듈에서 import할 경우에는 모듈 이름 값이 할당된다
  
  3. 패키지
  
  4. 예외 처리
  try:
    ...
  except:
    ...
  else:
    ...
  finally:
    ...
  
  5. 내장 함수
   abs() 절대값
   all() 요소가 모두 참이면 True 아니면 False
   any() 요소중 하나라도 참이면 True, 아니면 False
   chr() 유니코드값을 전달받아 해당하는 문자 출력
   dir() 객체가 가지고 있는 변수나 함수를 보여준다
   divmod(a,b) a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
   enumerate() 인덱스 값을 포함하는 enumerate 객체 리턴
   eval('1+2') => 3 문자열을 실행한 결과값을 리턴
   filter()
   hex()
   oct()
   int()
   isinstance()
   list()
   map()
   ord() 유니코드값 리턴
   pow()
   round() 반올림
   sorted() 
   str()
   sum()
   tuple()
   zip()
    
  6. 라이브러리
   sys
   pickle
   os 
   shutil
   glob
   tempfile
   time
   calendar
   random
   webbrowser
   
    
  
