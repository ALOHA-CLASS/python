
import json
import requests
import save_token

# 저장된 토큰 정보를 읽어 옴
tokens = save_token.load_tokens(save_token.KAKAO_TOKEN_FILE)

# json 문자열의  '(작은따옴표)를 "(큰따옴표)로 변환
json_str = tokens.replace("'", "\"")

# json 문자열을 딕셔너리 변환
tokens = json.loads(json_str)

# print(tokens)
print(tokens['access_token'])


# 텍스트 메시지 url
# 카카오톡 나에게 보내기 URL
url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

# header 정보
# Authorization : 인증정보를 담는 헤더
headers = {
    'Authorization' : 'Bearer ' + tokens['access_token']
}


temp = {
    'object_type' : 'feed',     # text, feed
    # 'text' : '안녕하세요~!',
    # URL 은 Kakao Developer > 내 애플리케이션 > 앱 설정 > 플랫폼 > Web 에
    # 등록된 도메인만 사용가능합니다.
    "content" : {
        "title" : "피카츄~!",
        "description" : "라이츄 파이리 꼬부기",
        "image_url": "https://upload.wikimedia.org/wikipedia/ko/thumb/a/a6/Pok%C3%A9mon_Pikachu_art.png/200px-Pok%C3%A9mon_Pikachu_art.png",
        "image_width": 640,
        "image_height": 640,
        'link' : { 
            "web_url" : 'https://wwwaloha.oopy.io',          # PC 카톡의 URL
            "mobile_web_url" : 'https://wwwaloha.oopy.io'    # 모바일 URL
        }
        
    }
}

data = {
    'template_object' : json.dumps( temp )
}


# 나에게 카카오 메시지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)