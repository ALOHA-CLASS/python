'''
    정수 하나를 입력받아,
    1부터 입력받은 수까지의 합계를 구하는 프로그램을 작성하시오.
    (입력예시) N : 10
    (출력예시) 합계 : 55
'''

N = input("정수 : ")
N = int(N)
sum = 0

for i in range(1, N+1):
    sum += i
    
print('합계 : {}'.format(sum))


'''
java

Scanner sc = new Scanner(System.in);
int N = sc.nextInt();
int sum = 0;
for( int i = 1 ; i <= N ; i++) {
    sum += i;
}
System.out.println(sum);


'''

