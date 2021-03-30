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
   %d %s  => %(number, str)
   {0} => .format("str")
 - 문자 개수 세기 count()
 - 문자 위치 알려주기 find() index()
 - 문자열 삽입 join(str) 문자열 str사이에 구분자 삽입
 - 공백제거 lstrip() rstrip() strip()
 - 문자열 바꾸기 replace()

3. 리스트 자료형
 - 리스트(List)
  arr = [ ] 
  arr = list()
  문자열처럼 인덱싱, 슬라이싱 가능
 - 리스트 더하기(+)
 - 리스트 반복하기(*)
 - 리스트 길이( len() )
 - 리스트 요소 (맨뒤에) 추가하기( arr.append(value) )
 - 리스트 요소 추가하기( arr.insert(0,9) )
 - 리스트 요소 삭제하기( del arr[0] )
 - 리스트 요소 삭제하기( arr.remove(value) 첫번째로 나오는 value 삭제 )
 - 리스트 마지막 요소 끄집어내기( arr.pop() )
 - 리스트 정렬( arr.sort() )
 - 리스트 뒤집기( arr.reverse() )
 - 리스트 위치 검색( arr.index(value) )
 - 리스트 요소 개수 세기( arr.count(value) value 값 개수 count )
 - 리스트 확장( arr1.extend(arr2) )
 
 4. 튜플 자료형
  - 튜플(tuple)
   tu1 = ()
   tu1 = (1,)
   tu1 = (1, 2, 3)
   tu1 = 1, 2, 3
   인덱싱, 슬라이싱 가능
  - 튜플은 요소 변경 및 삭제 불가능
  - 튜플 더하기(+)
  - 튜플 곱하기(*)
  - 튜플 길이( len() )
 
 5. 딕셔너리(=연관 배열, 해시) 자료형
  dict = {'name' : 'kjh',  ... }
  - 쌍 추가하기 dic['address'] = 'gangnam2'
  - 요소 삭제하기 del dic['address']
                  
 
   
   
 
 
 
 
 


