import re       # 정규표현식 라이브러리

# for 반복문
# for 변수 in (리스트, 튜플 등 컬렉션):
li = [1,2,3,4,5]

for n in li:
    print(n, end=' ')
    
    
# 문자열을 입력받아서 비밀번호를 확인하는
# 프로그램을 작성하시오.
# 비빌번호 조건 : 숫자와 문자가 모두 포함
print()
pwd = input('비밀번호 :')

ch_count = 0        # 문자의 개수
num_count = 0       # 숫자의 개수

# pwd 라는 문자열을 한 글자씩 가져와서 바복
for ch in pwd:
    # isalpha()       : 해당 문자가 알파벳/한글 이면 True, 아니면 False
    #                    (파이썬 v3.xx - 알파벳/한글 모두 True)
    # isnumeric()     : 해당 문자가 숫자 이면 True, 아니면 False
    # if ch.isalpha():
        # ch_count += 1
    # 정규표현식
    format = re.compile(r'[a-zA-Z]')        
    if format.match(ch):
        ch_count += 1
    if ch.isnumeric():
        num_count += 1
        
if (ch_count > 0 and num_count > 0):
    print('사용 가능한 비밀번호입니다.')
else:
    print('사용 불가한 비밀번호입니다.')
    