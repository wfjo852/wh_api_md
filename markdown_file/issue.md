# WH2API::Issue

## 목차

| 내용                           | slug                                                                          | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :----------------------------- | :---------------------------------------------------------------------------- | :-------: | :-----: | :----: | :--: |
| 1. [이슈 조회]                 | /api/project/{project_idx}/issue/{issue_idx}/read                             |    GET    |    O    |   -    |  -   |
| 2. [이슈 등록]                 | /api/project/{project_idx}/issue/create                                       |   POST    |    O    | hooked |  -   |
| 3. [이슈 수정]                 | /api/project/{project_idx}/issue/{issue_idx}/update                           |   POST    |    O    | hooked |  -   |
| 4. [이슈 태그 조회]            | /api/project/{project_idx}/issue/tag/list                                     |    GET    |    O    |   -    |  -   |
| 5. [이슈 코멘트 등록]          | /api/project/{project_idx}/issue/{issue_idx}/comment/create                   |   POST    |    X    | hooked |  -   |
| 6. [이슈 리플라이 등록]        | /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/create     |   POST    |    X    | hooked |  -   |
| 7. [이슈 삭제]                 | /api/project/{project_idx}/issue/{issue_idx}/delete                           |   POST    |    O    |   -    |  -   |
| 8. [이슈 코멘트/리플라이 삭제] | /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/delete     |   POST    |    X    |   -    |  -   |
| 9. [이슈 코멘트 북마크 등록]   | /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/favorite   |   POST    |    X    |   -    |  -   |
| 10. [이슈 코멘트 북마크 해제]  | /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/unfavorite |   POST    |    X    |   -    |  -   |
| 11. [이슈 상태 코드 수정]      | /api/project/{project_idx}/issue/{issue_idx}/status/update                    |   POST    |    X    | hooked |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 이슈 조회 <a id="issue-read"></a>

### `GET /api/project/{project_idx}/issue/{issue_idx}/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| issue_idx   | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"issue": {
			"project": {
				"idx": "1",
				"name": "Demo_Bigbuck_Bunny",
				"description": "Demo_Bigbuck_Bunny",
				"start_date": "2018-12-11",
				"end_date": "2019-04-12"
			},
			"subject": "abc abc",
			"contents": "contents ... long contents",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
			},
			"assignees": [
				{
					"idx": "2",
					"name": "Artist",
					"id": "c3m",
					"email": "artist@c2monster.com",
					"thumbnail": "http://localhost:81/2019/04/08/dc3295a0a38e89e9.png"
				}
			],
			"start_date": "2020-06-24",
			"end_date": "2020-07-31",
			"priority": "3"
		},
		"tasktypes": [
			{
				"idx": "19",
				"name": "i.Animation",
				"selected": true
			},
			{
				"idx": "20",
				"name": "i.Render"
			},
			{
				"idx": "21",
				"name": "i.Comp"
			},
			{
				"idx": "22",
				"name": "i.Lookdev"
			}
		],
		"statuses": [
			{
				"idx": "1",
				"name": "wip",
				"selected": true
			},
			{
				"idx": "2",
				"name": "confirm"
			},
			{
				"idx": "3",
				"name": "retake"
			},
			{
				"idx": "4",
				"name": "pub"
			},
			{
				"idx": "5",
				"name": "final"
			}
		],
		"tags": [
			{
				"idx": "1",
				"name": "test",
				"selected": true
			},
			{
				"idx": "2",
				"name": "wow",
				"selected": true
			},
			{
				"idx": "3",
				"name": "2020-09-10",
				"selected": true
			},
			{
				"idx": "7",
				"name": "team1"
			}
		]
	}
}
```

---

## 2. 이슈 등록 <a id="issue-create"></a>

### `POST /api/project/{project_idx}/issue/create`

### Webhook

- event: issue
- action: create

### permission

- `permission.read_shot_task_overview`

### request

| param        | type  |       data       | required | desc          |
| ------------ | :---: | :--------------: | :------: | ------------- |
| project_idx  | path  |     integer      |    O     |               |
| subject      | query |      string      |    O     |               |
| contents     | query |      string      |    O     |               |
| attached[]   | query |  array of file   |    X     |               |
| assignee[]   | query | array of integer |    O     | 1명 이상 필수 |
| status_idx   | query |     integer      |    O     |               |
| tasktype_idx | query |     integer      |    O     |               |
| start_date   | query |       date       |    X     | YYYY-MM-DD    |
| end_date     | query |       date       |    X     | YYYY-MM-DD    |
| tag[]        | query | array of string  |    X     |               |
| priority     | query |     integer      |    O     | 1 ~ 5         |

### response

```json
{
	"error": {
		"code": 200,
		"message": "이슈를 저장했습니다."
	},
	"data": null
}
```

---

## 2. 이슈 수정 <a id="issue-update"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/update`

### Webhook

- event: issue
- action: update

### permission

- `permission.read_shot_task_overview`

### request

| param        | type  |       data       | required | desc          |
| ------------ | :---: | :--------------: | :------: | ------------- |
| project_idx  | path  |     integer      |    O     |               |
| issue_idx    | path  |     integer      |    O     |               |
| subject      | query |      string      |    O     |               |
| contents     | query |      string      |    O     |               |
| attached[]   | query |  array of file   |    X     |               |
| assignee[]   | query | array of integer |    O     | 1명 이상 필수 |
| status_idx   | query |     integer      |    O     |               |
| tasktype_idx | query |     integer      |    O     |               |
| start_date   | query |       date       |    X     | YYYY-MM-DD    |
| end_date     | query |       date       |    X     | YYYY-MM-DD    |
| tag[]        | query | array of string  |    X     |               |
| priority     | query |     integer      |    O     | 1 ~ 5         |

### response

```json
{
	"error": {
		"code": 200,
		"message": "이슈를 저장했습니다."
	},
	"data": null
}
```

---

## 4. 이슈 태그 조회 <a id="issue-tag-list"></a>

### `GET /api/project/{project_idx}/issue/tag/list`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태그를 조회 했습니다."
	},
	"data": {
		"tags": [
			{
				"idx": "12",
				"name": "tag 1"
			},
			{
				"idx": "13",
				"name": "tag 2"
			}
		]
	}
}
```

---

## 5. 이슈 코멘트 등록 <a id="comment-create"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/comment/create`

### Webhook

- event: issue comment
- action: create

### permission

- `permission.read_shot_task_overview`

### request

| param            | type  |     data      | required | desc                                    |
| ---------------- | :---: | :-----------: | :------: | --------------------------------------- |
| project_idx      | path  |    integer    |    O     |                                         |
| issue_idx        | path  |    integer    |    O     |                                         |
| contents         | query |    string     |    O     |                                         |
| last_comment_idx | query |    integer    |    X     | 현재 이슈에 달린 마지막 코멘트의 인덱스 |
| favorite         | query |    integer    |    O     | 북마크할 경우 1, 아니면 0               |
| attached[]       | query | array of file |    X     |                                         |

### response

```json
{
	"error": {
		"code": 200,
		"message": "코멘트가 등록됐습니다."
	},
	"data": {
		"comments": [
			{
				"idx": "2",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
				},
				"contents": "2nd 코멘트",
				"created_time": "2020-07-02 15:45:47",
				"is_favorite": false,
				"attached": [
					{
						"idx": "1",
						"url": "http://localhost:81//2020/07/02/d02a8432604334d0.png",
						"name": "KakaoTalk_Photo_2020-05-19-13-54-03.png",
						"thumbnail": "/assets/images/thumbnail/shot/small/default.light.svg",
						"file_format": "image"
					},
					{
						"idx": "2",
						"url": "http://localhost:81//2020/07/02/76418dc6b350b257.txt",
						"name": "wh2api_python_사용api.txt",
						"thumbnail": "/assets/images/thumbnail/file/big/default.light.svg",
						"file_format": "text"
					}
				],
				"replies": [
					{
						"idx": "3",
						"user": {
							"idx": "1",
							"name": "C2Monster",
							"id": "c2m",
							"email": "contact@c2monster.com",
							"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
						},
						"contents": "wow it's reply",
						"created_time": "2020-07-02 16:00:37",
						"is_favorite": false
					}
				]
			}
		]
	}
}
```

---

## 6. 이슈 리플라이 등록 <a id="reply-create"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/create`

### Webhook

- event: issue comment
- action: create

### permission

- `permission.read_shot_task_overview`

### request

| param            | type  |     data      | required | desc                                        |
| ---------------- | :---: | :-----------: | :------: | ------------------------------------------- |
| project_idx      | path  |    integer    |    O     |                                             |
| issue_idx        | path  |    integer    |    O     |                                             |
| comment_idx      | query |    integer    |    O     |                                             |
| last_comment_idx | query |    integer    |    X     | 현재 코멘트에 달린 마지막 리플라이의 인덱스 |
| contents         | query |    string     |    O     |                                             |
| attached[]       | query | array of file |    X     |                                             |

### response

```json

```

---

## 7. 이슈 삭제 <a id="issue-delete"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/delete`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| issue_idx   | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "이슈가 삭제됐습니다."
	},
	"data": null
}
```

---

## 8. 이슈 코멘트/리플라이 삭제 <a id="comment-delete"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/delete`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| issue_idx   | path | integer |    O     |      |
| comment_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "코멘트가 삭제됐습니다."
	},
	"data": null
}
```

---

## 9. 이슈 코멘트 북마크 등록 <a id="comment-favorite"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/favorite`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| issue_idx   | path | integer |    O     |      |
| comment_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "북마크가 등록됐습니다."
	},
	"data": null
}
```

---

## 10. 이슈 코멘트 북마크 해제 <a id="comment-unfavorite"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/comment/{comment_idx}/unfavorite`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| issue_idx   | path | integer |    O     |      |
| comment_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "북마크가 해제됐습니다."
	},
	"data": null
}
```

---

## 11. 이슈 상태 코드 수정 <a id="issue-status-update"></a>

### `POST /api/project/{project_idx}/issue/{issue_idx}/status/update`

### Webhook

- event: issue
- action: status update

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| issue_idx   | path  | integer |    O     |      |
| status_idx  | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드가 수정됐습니다."
	},
	"data": null
}
```

---

## 끝

[이슈 조회]: #issue-read
[이슈 등록]: #issue-create
[이슈 수정]: #issue-update
[이슈 태그 조회]: #issue-tag-list
[이슈 코멘트 등록]: #comment-create
[이슈 리플라이 등록]: #reply-create
[이슈 삭제]: #issue-delete
[이슈 코멘트/리플라이 삭제]: #comment-delete
[이슈 코멘트 북마크 등록]: #comment-favorite
[이슈 코멘트 북마크 해제]: #comment-unfavorite
[이슈 상태 코드 수정]: #issue-status-update
