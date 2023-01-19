
# 시퀀스 연산자
# - 순서가 있는 컬렉션에서 사용하는 연산자
# + : 컬렉션을 연결하는 연산자
# * : 표현식을 반복하는 연산자
a = [1,2,3]
b = [4,5,6]
c = a + b
print('c : {}'.format(c))

d = '*' * 10
print('d : {}'.format(d))

# 멤버쉽 연산자
# - 어떤 값이 지정한 컬렉션에 포함되어 있는지 여부를 반환하는 연산자
# a in C        : 컬렉션 C의 요소에 a 가 포함되면 True, 아니면 False
# a not in C    : 컬렉션 C의 요소에 a 가 포함되지 않으면 True, 아니면 False
x = 3 in a
y = 10 in a
z = 100 not in b
print('x : {}'.format(x))
print('y : {}'.format(y))
print('z : {}'.format(z))


# 조건 연산자
# x if 조건식 else y
# - 조건식의 결과가 참이면 x 를, 거짓이면 y 를 반환하는 연산자

m = 100
n = 200
result = m if (m - n) > 0 else n
print('result : {}'.format(result))

