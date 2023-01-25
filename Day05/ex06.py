# 예외 정보
# as 키워드로 예외 정보를 확인할 수 있다
'''
    except 예외 클래스 as 변수명
    
    ex) 
      except XXXError as err:
        # err.args  : 예외 정보를 가진 변수
        #     - args[0] : 에러번호
        #     - args[1] : 에러 메시지
        # err       : __str__ 메소드에 의해 예외정보가 출력됨
'''
try:
    file = open('존재하지않는파일.txt')
    line = file.readline()
    print(line)
except OSError as err:
    print('예외 정보 : ', err.args)
    print('예외 정보 : ', err)
except:
    print('알 수 없는 예외 발생...')
else:
    print('정상적으로 파일을 읽어왔습니다.')