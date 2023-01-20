# 파일 저장 경로
path = 'C:/KHM/PYTHON/python/Day03/'

# rt : 읽기모드 + 텍스트모드
# 읽기모드 : r (read)
# 파일유형 : t (text)
file = open(path + 'hello.txt', 'rt', encoding='UTF-8')

while True:
    # str = file.read(10)       # 파일로부터 10글자씩 읽어온다.
    str = file.readline()       # 파일로부터 한 줄 씩 읽어온다.
    if not str:
        break
    print(str, end='')

# 파일 닫기 - 메모리 해제    
file.close()     
