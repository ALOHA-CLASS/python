
# 코딩을 제일 잘 가르치는 지역?

# 무한반복
# : 무조건 계속 반복하는 반복문
#   반드시, 종료조건 넣어주어야 한다.

# break
# : 현재 속한 반복문을 벗어나는 키워드

while True:
    city = input('코딩을 제일 잘 가르치는 지역?')
    # 종료조건
    if city == '영등포' or city == 'YDP':
        print('정답입니다.')
        break
    else:
        print('틀렸습니다.')