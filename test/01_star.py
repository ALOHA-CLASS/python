
'''
별찍기 

N : 5
*
**
***
****
*****
'''
N = input('N : ')
N = int(N)

# ------
# i : 0
# j : 0
# ------
# i : 1
# j : 0 1
# ------
# i : 2
# j : 0 1 2
# ------
# i : 3
# j : 0 1 2 3
# ------
# i : 4
# j : 0 1 2 3 4
# ------

for i in range(0, N):
    for j in range(0, i+1):
        print('*', end='')
    print()



'''
N : 5
    *           # i : 1 - 빈칸4, *1     
   ***          # i : 2 - 빈칸3, *3
  *****         # i : 3 - 빈칸2, *5
 *******        # i : 4 - 빈칸1, *7
*********       # i : 5 - 빈칸0, *9
'''
for i in range(1, N+1):
    for j in range(N-i):    # (N-i) : 5-1 : 4
        print(' ', end='')
    for j in range(1, i*2):
        print('*', end='')     
    print()
    

