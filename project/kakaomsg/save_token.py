import json
import requests
import datetime
import os

# 카카오 토큰을 저장할 파일명(json)
KAKAO_TOKEN_FILE = './kakao_token.json'


# 토큰 저장
def save_tokens(filename, tokens):
    with open(filename, 'w') as fp:
        json.dump(tokens, fp)
        
        
# 토큰 조회
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)
        print(tokens)
        
    return tokens


# 토큰 갱신
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)
    
    url = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type'    : 'authorization_code',
        'client_id'     : '636004344b306ca0cc7283d41ffc4f1b',   # REST API 키
        'refresh_token' : tokens['refresh_token']
    }
    
    response = requests.post(url, data=data)
    
    # 요청 실패 시,
    if response.status_code != 200:
        print('오류가 발생하였습니다', response.json())
    # 요청 성공 시,
    else:
        token = response.json()
        print(token)
        # 기본 파일 백업
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = filename + "." + now
        os.rename(filename, backup_filename)    # 파일 이름 변경
        
        # 갱신된 토큰 저장
        token['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)
        
    return tokens

##########################


# 토큰 저장
# tokens = input('발급받은 토큰 정보 입력 : ')
# save_tokens(KAKAO_TOKEN_FILE, tokens)

# 토큰 갱신
# KAKAO_APP_KEY = '636004344b306ca0cc7283d41ffc4f1b'
# tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILE)
# save_tokens(KAKAO_TOKEN_FILE, tokens)

