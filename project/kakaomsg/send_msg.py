
import json
import requests
import save_token

# 저장된 토큰 정보를 읽어 옴
tokens = save_token.load_tokens(save_token.KAKAO_TOKEN_FILE)



# 텍스트 메시지 url
url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

# header 정보
headers = {
    'Authorzation' : 'Bearer ' + tokens['access_token']
}


temp = {
    'object_type' : 'text',
    'text' : '안녕 카카오~!',
    'link' : { 'web_url' : 'www.naver.com' }
}

data = {
    'template_object' : json.dumps( temp )
}


# 나에게 카카오 메시지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)