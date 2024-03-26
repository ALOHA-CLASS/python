'''
    주소록 프로그램 만들기
    [기능]
    1. 새로운 주소 등록하기
    2. 기존 주소 삭제하기
    3. 기존 주소 수정하기
    4. 특정 주소 검색하기
    5. 전체 주소 출력하기
    6. 주소록 정보를  파일로 관리하기
    
    * 객체
    - Person 객체
    - Address Book 객체
    
    * 주소록 정보
    - AddressBook.csv 파일로 정리
    - 이름, 전화번호, 주소 정보를 저장
    ex)
    김조은, 010-1234-1234, 서울시 영등포구
    김조은, 010-1234-1234, 서울시 영등포구
    김조은, 010-1234-1234, 서울시 영등포구
    
    * 함수
    file_reader()           : AddressBook.csv 파일 읽기
    file_generator()        : AddressBook.csv 파일 생성
    menu()                  : 메뉴 소개 및 입력
    exit()                  : 프로그램 종료
    run()                   : 프로그램 실행
    insert()                : 추가
    update()                : 수정
    search()                : 검색
    print_all()             : 전체 출력
    
    __init__()              : 생성자 - 주소록 리스트, 파일 객체 초기화

'''

import sys
'''
    sys 모듈
    : 인터프리터가 제공하는 변수와 함수를 
      직접 제어할 수 있게 해주는 모듈
      sys.exit()      : 프로그램 종료 
'''

# 사람
class Person:
    # 변수 - 이름, 전화번호, 주소
    # 메소드 - 정보 확인
    # 변수      : name, phone, addr
    # 메소드    : info()
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr
        
    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))

# 주소록
class AddressBook:
    # 변수 : 주소 리스트 - address_list
    # 메소드
    '''
        file_reader()           : AddressBook.csv 파일 읽기
        file_generator()        : AddressBook.csv 파일 생성
        menu()                  : 메뉴 소개 및 입력
        exit()                  : 프로그램 종료
        run()                   : 프로그램 실행
        insert()                : 추가
        update()                : 수정
        search()                : 검색
        print_all()             : 전체 출력
    '''
    
    # 생성자
    def __init__(self):
        self.address_list = []
        self.file_reader()
        
    # 파일 읽기
    def file_reader(self):
        # 예외 처리
        # 에러 ? 프로그램 코드의 문법적인 문제
        # 예외 ? 프로그램이 샐행 이후에 발생하는 문제
        #        - 파일이 존재하지 않는 경우
        try:
            # 예외 발생 가능성이 있는 코드
            file = open('AddressBook.csv', 'rt', encoding='UTF-8')
        except:
            # 예외 발생 시, 실행할 코드
            print('AddressBook.csv 파일이 없습니다.')
        else:
            # 예외 미발생 시, 성공적으로 파일 입력 
            while True:
                buffer = file.readline()    # 한 줄씩 데이터를 읽어온다
                print('읽어온 데이터...')
                print( len(buffer) )
                
                if not buffer:
                    break
                # 김조은, 010-1234-1234, 서울시 영등포구
                # split() --> ['김조은', '010-1234-1234', '서울시 영등포구\n']
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                # rstrip(문자)  : 지정한 문자를 문자열에 오른쪽에서 제거
                addr = buffer.split(',')[2].rstrip('\n')
                # Person 객체 생성
                person = Person(name, phone, addr)
                # 가져온 연락처 정보를 주소 목록에 추가
                self.address_list.append( person )
                
            print('AddressBook.csv 파일을 읽어왔습니다.')
            file.close()
        
    # 파일 생성
    def file_generate(self):
        try:
            file = open('AddressBook.csv', 'wt', encoding='UTF-8')
        except:
            print('AddressBook.csv 파일을 생성할 수 없습니다.')
        else:
            # address_list 를 반복하여, 모든 연락처 정보를 .csv 파일에 출력
            for person in self.address_list:
                file.write('{}, {}, {}\n'.format( person.name, person.phone, person.addr) )

            file.close()

    # 메뉴
    def menu():
        print('-' * 30)
        print('1. 주소 등록하기')
        print('2. 주소 삭제하기')
        print('3. 주소 수정하기')
        print('4. 주소 검색하기')
        print('5. 모든 주소 출력하기')
        print('0. 프로그램 종료')
        print('-' * 30)
        choice = int( input('메뉴 번호 : ') )
        return choice   
    
    # 프로그렘 종료
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()
        
    # 프로그램 실행
    def run(self):
        while True:
            choice = AddressBook.menu()             # 입력한 메뉴번호
            if choice == 0: self.exit()             # 종료
            elif choice == 1:   self.insert()       # 추가
            elif choice == 2:   self.delete()       # 삭제
            elif choice == 3:   self.update()       # 수정
            elif choice == 4:   self.search()       # 검색
            elif choice == 5:   self.print_all()    # 전체출력
            else: print('(0~5) 사이의 메뉴번호를 입력해주세요...')
            
    # 주소록 추가
    def insert(self):
        print('==== 새 연락처 추가 ====')
        name = input('등록할 이름 : ')
        phone = input('등록할 전화번호 : ')
        addr = input('등록할 주소 : ')
        if name and phone and addr : 
            # 입력한 주소 정보를 Person 객체를 생성하여,
            # address_list 에 추가한다
            person = Person(name, phone, addr)
            self.address_list.append( person )
            self.file_generate()
            print('새 연락처가 정상적으로 등록되었습니다.')
        else:
            print('누락된 입력값이 있어 등록되지 않았습니다.')

    # 주소록 삭제
    def delete(self):
        print('=== 기존 얀락처 삭제 ===')
        name = input('삭제할 이름 : ')
        if not name:
            print('이름이 입력되지 않아 삭제를 취소합니다.')
            return
        # 삭제 여부
        deleted = False
        
        for i, person in enumerate( self.address_list ):
            # 입력한 이름이 연락처 목록에 존재하명,
            if name == self.address_list[i].name:
                phone = self.address_list[i].phone
                print('검색한 전화번호가 "{}" 입니다.'.format(phone))
                if input('삭제할까요? (Y/N)').upper() == 'N': 
                    continue
                
                # pop(index) : index 의 요소를 삭제
                self.address_list.pop(i)
                delete = True
                print('{} 의 정보를 삭제하였습니다.'.format(name))
                self.file_generate()
                break
            if not deleted:
                print('{} 의 정보가 삭제되지 않았습니다.'.format(name))
                
    # 주소록 수정
    def update(self):
        print('=== 기존 연락처 수정 ===') 
        name = input('수정할 이름 :')
        if not name:
            print('이름이 입력되지 않아 수정을 취소합니다.')
            return
        # 수정 여부
        updated = False
        for i, person in  enumerate(self.address_list):
            if name == self.address_list[i].name:
                phone = self.address_list[i].phone
                print('검색할 전환번호가 "{}" 입니다.'.format(phone))
                if input('수정할까요? (Y/N)').upper() == 'N':
                    continue

                new_name = input('변경할 이름 : ')
                new_phone = input('변경할 전화번호 : ')
                new_addr = input('변경할 주소 : ')

                if new_name:
                    self.address_list[i].name = new_name

                if new_phone:
                    self.address_list[i].phone = new_phone

                if new_addr:
                    self.address_list[i].addr = new_addr
                    
                update = True
                print('주소록이 수정되었습니다.')
                print('수정된 주소록의 정보')
                self.address_list[i].info()
                self.file_generate()
                break
            
            if not updated:
                print('{} 의 정보가 수정되지 않았습니다.'.format(name))
                
    # 검색하기
    def search(self):
        # 리스트에서 찾아서 연락처 정보를 츨력
        name = input('검색할 이름 : ')
        if not name:
            print('이름이 입력되지 않아 조회할 수 없습니다.')
            return

        print('=== 조회된 연락처 정보 ===')
        searched = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print('=== 조회된 연락처 정보 ===')
                print( person.info() )
                
        if not searched:
            print('조회된 연락처가 없습니다.')
                
    # 주소록 전체 출력
    def print_all(self):
        print('==== 전체 연락처 출력 ====')
        for person in self.address_list:
            person.info
            
        list_count = len(self.address_list)
        print('총 {} 개의 연락처가 있습니다.'.format(list_count))

    # class AddressBook 끝      
    
# AddressBook 객체 생성
my_app = AddressBook()

# 프로그램 실행 - run()
my_app.run()
                                
                        

        
    
        