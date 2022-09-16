# WH2API::Webhook

## 목차

| 내용                       | slug                                  | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :------------------------- | :------------------------------------ | :-------: | :-----: | :--: | :--: |
| 1. [웹훅 목록 조회]        | /api/webhook/list                     |    GET    |    O    |  -   |  -   |
| 2. [웹훅 정보 수정]        | /api/webhook/{webhook_idx}/update     | 	POST  	 |    O    |  -   |  -   |
| 3. [웹훅 등록]             | /api/webhook/create                   |   POST    |    O    |  -   |  -   |
| 4. [웹훅 삭제]             | /api/webhook/{webhook_idx}/delete     |   POST    |    O    |  -   |  -   |
| 5. [웹훅 활성화]           | /api/webhook/{webhook_idx}/activate   |   POST    |    O    |  -   |  -   |
| 6. [웹훅 비활성화]         | /api/webhook/{webhook_idx}/deactivate |   POST    |    O    |  -   |  -   |
| 7. [웹훅 트리거 목록 조회] | /api/webhook/trigger/list             |   GET  	 |    O    |  -   |  -   |

- O\* - api 없이 콘트롤러에 직접 구현

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 웹훅 목록 조회 <a id="webhook-list"></a>

### `GET /api/webhook/list`

### permission

- `permission.do_global_setting`

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
  {
  "data": {
    "webhooks": [
      {
        "idx": "1",
        "name": "app",
        "url": "http://2.3.4.5/hook",
        "hooking_num": "12",
        "is_on": "1"
      },
      {
        "idx": "2",
        "name": "Render",
        "url": "http://11.22.33.44",
        "hooking_num": "4",
        "is_on": "1"
      }
    ]
  }
}
```

---

## 2. 웹훅 정보 수정 <a id="webhook-update"></a>

- 웹훅 1가지 정보만 선택해서 수정

### `POST /api/webhook/{webhook_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc                      |
| ----------- | :---: | :-----: | :------: | ------------------------- |
| webhook_idx | path  | integer |    O     |                           |
| column      | query | string  |    O     | webhook_name, webhook_url |
| old_val     | query | string  |    O     | 공백일 수는 있음          |
| new_val     | query | string  |    O     | 공백일 수는 있음          |

### response

```json
{
	"error": {
		"code": 200,
		"message": "웹훅 정보가 수정됐습니다."
	},
	"data": {
		"webhook_idx": 2
	}
}
```

---

## 3. 웹훅 등록 <a id="webhook-create"></a>

### `POST /api/webhook/create`

### permission

- `permission.do_global_setting`

### request

| param        | type  |  data  | required | desc |
| ------------ | :---: | :----: | :------: | ---- |
| webhook_name | query | string |    O     |      |
| webhook_url  | query | string |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "웹훅이 추가됐습니다."
	},
	"data": {
		"webhook" {
			"idx": "8",
			"name": "webhook-server",
			"url": "http://1.2.3.33:50/hook",
			"description": "",
			"triggers": "",
			"is_on": "1"
		}
	}
}
```

---

## 4. 웹훅 삭제 <a id="webhook-delete"></a>

### `POST /api/webhook/{webhook_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| webhook_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "웹훅이 삭제됐습니다."
	},
	"data": null
}
```

---

## 5. 웹훅 활성화 <a id="webhook-activate"></a>

### `POST /api/webhook/{webhook_idx}/activate`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| webhook_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "웹훅이 활성화됐습니다."
	},
	"data": null
}
```

---

## 6. 웹훅 비활성화 <a id="webhook-deactivate"></a>

### `POST /api/webhook/{webhook_idx}/deactivate`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| webhook_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "웹훅이 비활성화됐습니다."
	},
	"data": null
}
```

---

## 7. 웹훅 트리거 목록 조회 <a id="webhook-trigger-list"></a>

### `GET /api/webhook/trigger/list`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": null
}
```

---

## 끝

[이용자 목록 조회]: #webhook-list
[이용자 정보 수정]: #webhook-update
[이용자 등록]: #webhook-create
[이용자 삭제]: #webhook-delete
[이용자 활성화]: #webhook-activate
[이용자 비활성화]: #webhook-deactivate
[웹훅 트리거 목록 조회]: #webhook-trigger-list
