# WH2API::GNB

## 목차

| 내용                           | slug                 | 서버 구현 | 웹 적용 |
| :----------------------------- | :------------------- | :-------: | :-----: |
| 1. [GNB 정보 읽기]             | /api/gnb/read        |    GET    |    O    |
| 2. [프론트엔드 i18n 정보 읽기] | /api/i18n/front/read |    GET    |    O    |
| 3. [SSE 읽기]                  | /api/sse/read        |    GET    |   O\*   |

- O\* - SSE 로 구현

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. GNB 정보 읽기 <a id="gnb-read"></a>

### `GET /api/gnb/read`

### permission

- all authorized users

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    X     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"projects": [
			{
				"project_idx": "1",
				"name": "Demo_Bigbuck_Bunny",
				"url_thumbnail": "http://localhost:81/2019/04/08/2890e1bc7f14dd4c.jpg",
				"start_date": "2018-12-11",
				"end_date": "2019-04-12",
				"project_status": "1",
				"description": "Demo_Bigbuck_Bunny",
				"project_status_name": "Waiting",
				"is_finished": "0"
			}
		],
		"total_unread_message": "0"
	}
}
```

---

## 2. 프론트엔드 i18n 정보 읽기 <a id="i18n-front-read"></a>

### `GET /api/i18n/front/read`

### permission

- all authorized users

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"wh2": {
		"i18n-key-1": "번역 원문장 #1",
		"i18n-key-2": "번역 원문장 #2"
	}
}
```

---

## 3. SSE 읽기 <a id="sse-read"></a>

- SSE 방식으로 작동함 (header: text/event-stream)

### `GET /api/sse/read`

### permission

- all authorized users

### request

| param    | type |  data   | required | desc                                        |
| -------- | :--: | :-----: | :------: | ------------------------------------------- |
| reset    | path | integer |    X     | 1 - '프로젝트 리스트' 캐시 리프레시 원할 때 |
| location | path | string  |    X     | 클라이언트의 현재 로케이션                  |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"projects": [
			{
				"project_idx": "1",
				"name": "Demo_Bigbuck_Bunny",
				"url_thumbnail": "http://localhost:81/2019/04/08/2890e1bc7f14dd4c.jpg",
				"start_date": "2018-12-11",
				"end_date": "2019-04-12",
				"project_status": "1",
				"description": "Demo_Bigbuck_Bunny",
				"project_status_name": "Waiting",
				"is_finished": "0"
			}
		],
		"total_unread_message": "0"
	}
}
```

---

## 끝

[gnb 정보 읽기]: #gnb-read
[프론트엔드 i18n 정보 읽기]: #i18n-front-read
[sse 읽기]: #sse-read
