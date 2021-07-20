# 2021-03-17
# DataTypes.py 
# 자료형

1. 숫자형
 - 정수형, 실수형(+지수 표현 방식) 
 - 8진수, 16진수
 - 사칙연산(+,-,*,/)
 - **(제곱 연산자)
 - //(몫 연산자)

2. 문자형
 - 문자열 사용 방법
  1) "문자열"
  2) '문자열'
  3) """문자열"""
  4) '''문자열'''
  
 - 문자열 더하기 
  ABC + DEF => ABCDEF
  ABC * 2 => ABCABC
  
 - 문자열길이 LEN(문자열) 
 - 인덱스는 0부터 시작, 뒤에서는 -1부터
 
 - 문자열 슬라이싱 str[0:4] str[1:] str[:3] str[:] str[5:-7]
 
 - 문자열중 문자1개를 바꿀수 없음, 슬라이싱으로 조합을 해야함
 
 - 문자열 포매팅 
   "%d %s" %(number, str)
  
 - format함수 포매팅 
   "{0} {1}" .format(number, str)
   "{number} {day}" .format(number=10, day=3)
   
 - 문자열 정렬
   {0:<10} 왼쪽정렬 {0:>10} 오른쪽정렬 {0:^10}가운데정렬 {0:=^10} 정렬 후 빈칸을 =으로 
   
 - f문자열 포매팅
   f'Hello {name}' name변수를 참조할수있음
  
 - 문자 개수 세기
   count('a') : 문자열 중 문자 a의 개수.
 - 문자 위치 알려주기(첫 위치) 
   find() : 존재하지않으면 -1 리턴
   index() : 존재하지않으면 오류발생
 - 문자열 삽입 '#'.join(str) 문자열 str사이에 '#' 삽입
 - 공백제거 lstrip() rstrip() strip()
 - 문자열 바꾸기 replace("~를", "~으로")
 - 문자열 나누기 split('구분자')  '구분자'를 기준으로 토큰 나누어 리스트로 리턴

3. 리스트 자료형
 - 리스트(List)
  arr = [ ] 
  arr = list()
  문자열처럼 인덱싱, 슬라이싱 가능
 - 리스트 더하기(+)
   [1, 2, 3] + [4, 5, 6] => [1, 2, 3, 4, 5, 6]
 - 리스트 반복하기(*)
   [1, 2, 3] * 3 => [1, 2, 3, 1, 2, 3, 1, 2, 3]
 - 리스트 길이 len() 
 - 리스트 요소 (맨뒤에) 추가하기 arr.append(value) 
 - 리스트 요소 추가하기 arr.insert(0,9) 
 - 리스트 요소 삭제하기 del arr[0] 
 - 리스트 요소 삭제하기 arr.remove(value) 첫번째로 나오는 value 삭제 
 - 리스트 마지막 요소 끄집어내기 arr.pop() 
 - 리스트 정렬 arr.sort() 
 - 리스트 뒤집기 arr.reverse() 
 - 리스트 위치 검색 arr.index(value) 
 - 리스트 요소 개수 세기 arr.count(value) value 값 개수 count 
 - 리스트 확장 arr1.extend(arr2) 
 
 4. 튜플 자료형
  - 튜플(tuple) 
   tu1 = ()
   tu1 = (1,)
   tu1 = (1, 2, 3)
   tu1 = 1, 2, 3
   인덱싱, 슬라이싱 가능
  - 튜플은 요소 변경 및 삭제 불가능
  - 튜플 더하기(+) tu1 + tu2
  - 튜플 곱하기(*) tu3 * 3
  - 튜플 길이 len() 
 
 5. 딕셔너리(=연관 배열, 해시) 자료형
  dict = {'name' : 'kjh',  ... }
  - 쌍 추가하기 dic['address'] = 'gangnam2'
  - 요소 삭제하기 del dic['address']
  - Key 리스트 만들기 dict.keys()
  - Value 리스트 만들기 dict.values()
  - Key,Value 리스트 얻기 dict.items()
  - Value 얻기 dict[key] dict.get(key)
  - Key로 안에 있는지 조사하기 'name' in dict => True or False
  
 6. 집합 자료형
  { 1, 2, 3 }
  set([1, 2, 3]) => {1, 2, 3}
  set("Hello") => {'H', 'e', 'l', 'l', 'o'}
  - 중복을 허용하지 않음
  - 순서가 없음
  - 교집합(&) set1 & set2 
  - 합집합(|) set1 | set2
  - 차집합(-) set1 - set2, set1.difference(s2)
  - 값 추가하기 set.add(value)
  - 값 여러 개 추가하기 set.update(value1, value2)
  - 값 제거하기 set.remove(value3)
  
 7. 불 자료형
  True, False (대소문자 구분)
  
 
 8. 변수
  a = [1, 2, 3]
  b = a
  a is b => True, 같은 주소를 가르키는 변수
  
  복사 방법
  1) 리스트 전체 [:]를 사용해서 복사
  2) copy 모듈사용
   from copy import copy
   b = copy(a)
   
  
  
   
   
 
 
 
 
 


