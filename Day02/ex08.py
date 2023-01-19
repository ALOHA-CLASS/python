#  중첩 반복문
#  : 반복문 안에 또 하나의 반복문을 작성
# i : 2~9
# j : 1~9
# 구구단 출력하기
print()
for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i, j, i*j))
    print()
    
    
'''
2 x 1 = 2
2 x 2 = 
...
2 x 8 = 16
2 x 9 = 18
(개행)
3 x 1 = 3
3 x 2 = 6
...
3 x 8 = 24
3 x 9 = 27
...
9 x 9 = 81

i x j = i*j
'''