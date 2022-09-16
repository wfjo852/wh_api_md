# WH2API::Plugin

## 목차

| 내용                          | slug                     | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
|:------------------------------|:-------------------------|:---------:|:-------:|:----:|:----:|
| 1. 마야 플러그인 파일 목록    | /api/plugin/maya/list    |    GET    |    O    |  -   |  -   |
| 2. whtools 플러그인 파일 목록 | /api/plugin/whtools/list |    GET    |    O    |  -   |  -   |

---

## 1. 마야 플러그인 파일 목록 <a id="plugin-maya-list"></a>

### `GET /api/plugin/maya/list`

### permission

- all

### request

| param | type  |  data  | required | desc          |
|-------|:-----:|:------:|:--------:|---------------|
| base  | query | string |    x     | 하위 폴더경로 |

- 예) 모든 리스트

  - base=/
  - 혹은 base 미전달

- 예) 특정 폴더 조회
  - base=/tools (tools폴더 내 파일 출력. 하위폴더 포함)

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"files": [
			{
				"src": "/marker/Wh2main.ui",
				"url": "http://localhost/plugin/maya/marker/wh2main",
				"size": 57772
			},
			{
				"src": "/marker/Wh2msg.ui",
				"url": "http://localhost/plugin/maya/marker/wh2msg",
				"size": 5495
			}
		]
	}
}
```

---

## 2. whtools 플러그인 파일 목록 <a id="plugin-whtools-list"></a>

### `GET /api/plugin/whtools/list`

### permission

- all

### request

| param | type  |  data  | required | desc          |
|-------|:-----:|:------:|:--------:|---------------|
| base  | query | string |    x     | 하위 폴더경로 |

- 예) 모든 리스트

  - base=/
  - 혹은 base 미전달

- 예) 특정 폴더 조회
  - base=/tools (tools폴더 내 파일 출력. 하위폴더 포함)

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "files": [
            {
                "src": "/progressFrame.py",
                "url": "http://localhost/plugin/whtools/progressframe",
                "size": 6008
            },
            {
                "src": "/customUI/CustomFrame.py",
                "url": "http://localhost/plugin/whtools/customui/customframe",
                "size": 3817
            },
            {
                "src": "/customUI/DropFrame.py",
                "url": "http://localhost/plugin/whtools/customui/dropframe",
                "size": 7452
            }
        ]
    }
}
```

---

## 끝

[마야 플러그인 파일 목록]: #plugin-maya-list
[whtools 플러그인 파일 목록]: #plugin-whtools-list
