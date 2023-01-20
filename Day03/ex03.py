from secure import *

# 사용자 정보를 마스킹하기

name = '김휴먼'
no = '800422-1234567'
phone = '010-1234-5678'

print( name )
print( no )
print( phone )
print()

print( secure_name(name) )
print( secure_no(no) )
print( secure_phone(phone) )