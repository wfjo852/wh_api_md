# WH2API::Opinion

## 목차

| 내용                | slug                                                                         | 서버 구현 | 웹 적용 |
| :------------------ | :--------------------------------------------------------------------------- | :-------: | :-----: |
| 1. [의견 조회]      | /api/project/{project_idx}/version/{version_idx}/opinion/list                |    GET    |    O    |
| 2. [의견 계속 조회] | /api/project/{project_idx}/version/{version_idx}/opinion/{oppinion_idx}/list |    GET    |    O    |
| 3. [의견 추가]      | /api/project/{project_idx}/version/{version_idx}/opinion/create              |   POST    |    O    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 의견 목록 조회 <a id="task-detail-opinion-list"></a>

### `GET /api/project/{project_idx}/version/{version_idx}/opinion/list`

### permission

- `permission.read_opinion`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| task_idx    | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"opinions": [
			{
				"opinion_idx": "1",
				"opinion": "hello, world!",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"opinion_idx": "2",
				"opinion": "hello, world!",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"opinion_idx": "3",
				"opinion": "hello, world!",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": "",
				"attached": [
					{
						"url": "http://182.231.41.120:81/2019/03/11/11184591339fd8aa.xlsx",
						"name": "이미지 작업 해야 할 리소스 리스트.xlsx",
						"is_annotation": "0"
					},
					{
						"url": "http://182.231.41.120:81/2019/03/11/381f31fb47a52536.png",
						"name": "asset-overview.png",
						"is_annotation": "0"
					}
				]
			},
			{
				"opinion_idx": "4",
				"opinion": "hey",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			}
		]
	}
}
```

---

## 2. 의견 목록 계속 조회 <a id="task-detail-opinion-list-more"></a>

### `GET /api/project/{project_idx}/task/{task_idx}/version/{version_idx}/opinion/{opinion_idx}/list`

### permission

- `permission.read_opinion`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| task_idx    | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"opinions": [
			{
				"opinion_idx": "1",
				"opinion": "hello, world!",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"opinion_idx": "2",
				"opinion": "hello, world!",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"opinion_idx": "3",
				"opinion": "hello, world!",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": "",
				"attached": [
					{
						"url": "http://182.231.41.120:81/2019/03/11/11184591339fd8aa.xlsx",
						"name": "이미지 작업 해야 할 리소스 리스트.xlsx",
						"is_annotation": "1"
					},
					{
						"url": "http://182.231.41.120:81/2019/03/11/381f31fb47a52536.png",
						"name": "asset-overview.png",
						"is_annotation": "0"
					}
				]
			},
			{
				"opinion_idx": "4",
				"opinion": "hey",
				"date": null,
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			}
		]
	}
}
```

---

## 3. 의견 추가 <a id="task-detail-opinion-create"></a>

### `POST /api/project/{project_idx}/version/{version_idx}/opinion/create`

### permission

- `permission.create_opinion`

### request

| param           | type  |       data       | required | desc                              |
| --------------- | :---: | :--------------: | :------: | --------------------------------- |
| project_idx     | path  |     integer      |    O     |                                   |
| version_idx     | path  |     integer      |    O     |                                   |
| opinion         | query |      string      |    O     |                                   |
| attached[]      | query |  array of file   |    X     |                                   |
| is_annotation[] | query | array of integer |    X     | 1 - 어노테이션 / 0 - 일반 업로드  |
| location        | query |      string      |    O     | 'overview', 'mytask', 'track' ... |

- attached[] 와 is_annotation[] 순서, 갯수는 같아야 함.

```json
{
	"error": {
		"code": 200,
		"message": "의견이 등록 되었습니다."
	},
	"data": null
}
```

---

## 끝

[의견 조회]: #task-detail-opinion-list
[의견 계속 조회]: #task-detail-opinion-list-more
[의견 추가]: #task-detail-opinion-create
