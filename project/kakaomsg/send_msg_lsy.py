import json
import requests
import save_token

tokens = save_token.load_tokens(save_token.KAKAO_TOKEN_FILE)

#json문자열의 작은따옴표 를 큰따옴표로 변환
json_str = tokens.replace("'","\"")

#json 문자열을 딕셔너리 변환
tokens = json.loads(json_str)

#print(tokens)
print(tokens['access_token'])

#텍스트 메시지 url
url = 'http://kapi.kakao.com/v2/api/talk/memo/default/send'

#header 정보
# Authorization 인증정보 담는 헤더

headers = {
    'Authorization' : 'Bearer ' + tokens['access_token']
    
}

  
temp = {
    'object_type' : 'text',
    'text' : '안녕 카카오',
    'link' : { 'web_url' : 'www.naver.com' }
    
    }