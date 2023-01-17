s = "안녕하세요"

# 문자열 선택 연산자    : [index]
# 인덱싱
# index 는 0 부터 시작하는 순서번호
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 슬라이싱
# [시작index : 끝index]
print(s[0:2])       # 안녕
print(s[2:])        # 하세요
print(s[:2])        # 안녕


# 안녕하세요            : index(0~4)
# print(s[100])         : 인덱스 범위 바깥의 범호를 입력한 예외

# 문자열의 길이 - len
print("문자열의 길이 : " + str( len(s) ))
