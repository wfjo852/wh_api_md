# WH2API::Tool

## 목차

| 내용                              | slug                      | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :-------------------------------- | :------------------------ | :-------: | :-----: | :--: | :--: |
| 1. [WH2Tool 버전 정보 조회]       | /api/tool/version/{os}    |    GET    |   O\*   |  -   |  -   |
| 2. [WH2Tool 업데이트 리스트 조회] | /api/tool/list            |    GET    |   O\*   |  -   |  -   |
| 3. [WH2Tool 업데이트 다운로드]    | /api/tool/download/{path} |    GET    |   O\*   |  -   |  -   |

- O\* - WH2Tool에서 사용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. WH2Tool 버전 정보 조회 <a id="wh2tool-version-read"></a>

### `GET /api/tool/version/{os}`

### permission

- `permission.do_version_and_publish`

### request

| param | type |  data  | required | desc |
| ----- | :--: | :----: | :------: | ---- |
| os    | path | string |    O     | 임시 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version": "1.0.1",
		"user_lang": "EN",
		"api_uri": "http://182.231.41.120"
	}
}
```

---

## 2. WH2Tool 업데이트 리스트 조회 <a id="wh2tool-version-list"></a>

### `GET /api/tool/list`

### permission

- `permission.do_version_and_publish`

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
		"list": [
			{
				"version": "1.0.1",
				"path": "/update/1.0.1/mac_osx_node_modules.zip",
				"size": 123875125
			},
			{
				"version": "1.0.1",
				"path": "/update/1.0.1/mac_osx_wh2tool.zip",
				"size": 937250
			},
			{
				"version": "1.0.1",
				"path": "/update/1.0.1/win_32_node_modules.zip",
				"size": 125852327
			}
		],
		"user_lang": "EN",
		"api_uri": "http://182.231.41.120"
	}
}
```

---

## 3. WH2Tool 업데이트 다운로드 <a id="wh2tool-version-get"></a>

### `GET /api/tool/download/{path}`

### permission

- `permission.do_version_and_publish`

### request

| param | type |  data  | required | desc |
| ----- | :--: | :----: | :------: | ---- |
| path  | path | string |    O     | 임시 |

### response

file data

---

## 끝

[wh2tool 버전 정보 조회]: #wh2tool-version-read
[wh2tool 업데이트 리스트 조회]: #wh2tool-version-list

[WH2Tool 업데이트 다운로드] : #wh2tool-version-get
