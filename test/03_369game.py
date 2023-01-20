'''
    1부터 100까지 수를 반복하여 출력하면서,
    수가 3 또는 6 또는 9 인 경우 그 개수만큼 별(*)을 출력하는 프로그램을 완성하시오.
'''

# 1~100 까지 반복
for i in range(1, 101):
    ten = int( i / 10 )
    one = int( i % 10 )
    
    ten369 = ( ten == 3 or ten == 6 or ten == 9 )
    one369 = ( one == 3 or one == 6 or one == 9 )
    
    if ten369 and one369:
        print("**")
    elif ten369 or one369:
        print("*")
    else:
        print(i)
        
        
        