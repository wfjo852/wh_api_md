#-*- coding:utf-8 -*-

import requests
import hashlib
import base64
import json

# 웜홀 API URI 세팅
wh_url = "http://localhost" # 웜홀2 서버 URL (프로토콜 포함)
api_pathname = "/api/user/auth" # 웜홀2 API 상세
api_url = wh_url + api_pathname

# 파라미터 확인
userid = "c2m"
userpw = "c2m"
origin_server = wh_url
outside = "0"

# 비밀번호 추가 세팅 - 이용자가 입력한 비밀번호를 sha256 해시 후 base64 인코딩 함
userpw = userpw.encode("utf-8")
userpw_hashed = hashlib.sha256(userpw).hexdigest()
userpw_hashed = userpw_hashed.encode("utf-8")
userpw_encoded = base64.b64encode(userpw_hashed)

# 파라미터 세팅
data = {"userid": userid, "userpw": userpw_encoded, "origin_server": origin_server, "outside": outside}

# API 호출
result = requests.post(api_url, data=data)

# 결과 확인 / 토큰 획득
result_json = json.loads(result.text)
if result_json["error"]["code"] == 200:
    whtoken = result_json["data"]["token"]
else:
    print ("error")
    # 토큰 획득 실패한 경우




# 웜홀 API URI 세팅
wh_url = "http://192.168.0.15" # 웜홀2 서버 URL (프로토콜 포함)
api_pathname = "/api/project/list" # 웜홀2 API 상세
api_url = wh_url + api_pathname

# 파라미터 세팅
#whtoken = "eyaoiasddkaso.asodkaosd.asodoasdoas" # 로그인 API 를 통해 얻은 token 값
cookies = {"whtoken": whtoken}

# API 호출
# - 이 API는 별도의 파라미터가 필요 없기 때문에 쿠키만 세팅
# - 만약 별도의 파라미터가 필요하면 data 혹은 param 을 이용하여 파라미터를 추가
cookies = {"whtoken": whtoken}
result = requests.get(api_url, cookies=cookies)

# 결과 확인
result_json = json.loads(result.text)
for x in result_json["data"]["projects"]:
    print(x['name'])

