# WH2API::Episode

- `project.md` 와 일부 합칠 예정

## 목차

| 내용                    | slug                                                        | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :---------------------- | :---------------------------------------------------------- | :-------: | :-----: | :----: | :--: |
| 1. [에피소드 목록 조회] | /api/project/{project_idx}/episode/list[/{detail}]          |    GET    |    O    |   -    |  -   |
| 2. [에피소드 등록]      | /api/project/{project_idx}/episode/create                   |   POST    |    O    | hooked |  O   |
| 3. [에피소드 정보 수정] | /api/project/{project_idx}/episode/{episode_idx}/update     |   POST    |    O    |   -    |  O   |
| 4. [에피소드 삭제]      | /api/project/{project_idx}/episode/{episode_idx}/delete     |   POST    |    O    |   -    |  O   |
| 5. [에피소드 활성화]    | /api/project/{project_idx}/episode/{episode_idx}/activate   |   POST    |    O    |   -    |  -   |
| 6. [에피소드 비활성화]  | /api/project/{project_idx}/episode/{episode_idx}/deactivate |   POST    |    O    |   -    |  -   |
| 7. [에피소드 검증]      | /api/episode/validate                                       |  X POST   |    X    |   -    |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에피소드 목록 조회 <a id="project-episode-list"></a>

### `GET /api/project/{project_idx}/episode/list[/{detail}]`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

#### 기본인 경우

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"episodes": [
			{
				"idx": "1",
				"name": "ep01",
				"description": "ep01",
				"order": "1"
			},
			{
				"idx": "2",
				"name": "ep02",
				"description": "ep01",
				"order": "2"
			}
		]
	}
}
```

#### /detail 인 경우

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"episodes": [
			{
				"idx": "1",
				"name": "ep01",
				"episode_order": "1",
				"description": "에피소드1화",
				"shot_count": "113",
				"is_on": "1",
				"duration_count": "2138",
				"progress": "10000%",
				"task": {
					"total": "389",
					"assigned_users": "3"
				},
				"sequences": [
					{
						"idx": "1",
						"name": "s0010",
						"description": "C2Monster 사무실 대화장면",
						"shot_count": "256",
						"duration_count": "1356",
						"progress": "10000%",
						"task": {
							"total": "256",
							"assigned_users": "3"
						}
					},
					{
						"idx": "2",
						"name": "s0020",
						"description": "C2monster 사무실 앞 ",
						"shot_count": "156",
						"duration_count": "892",
						"progress": "10000%",
						"task": {
							"total": "156",
							"assigned_users": "3"
						}
					},
					{
						"idx": "3",
						"name": "s0030",
						"description": "엘레베이터 앞 ",
						"shot_count": "128",
						"duration_count": "716",
						"progress": "10000%",
						"task": {
							"total": "128",
							"assigned_users": "3"
						}
					}
				]
			},
			{
				"idx": "2",
				"name": "ep02",
				"episode_order": "2",
				"description": "에피소드2화",
				"shot_count": "1986",
				"is_on": "1",
				"duration_count": "826",
				"progress": "10000%",
				"task": {
					"total": "151",
					"assigned_users": "3"
				},
				"sequences": [
					{
						"idx": "4",
						"name": "s0010",
						"description": "계단 대화",
						"shot_count": "0",
						"duration_count": 0,
						"progress": 0,
						"task": {
							"total": "0",
							"assigned_users": "0"
						}
					},
					{
						"idx": "5",
						"name": "s0020",
						"description": "옥상 대사씬",
						"shot_count": "0",
						"duration_count": 0,
						"progress": 0,
						"task": {
							"total": "0",
							"assigned_users": "0"
						}
					}
				]
			}
		]
	}
}
```

---

## 2. 에피소드 등록 <a id="project-episode-create"></a>

### `POST /api/project/{project_idx}/episode/create`

### Webhook

- event: episode
- action: create

### permission

- `permission.update_project`

### request

| param        | type  |  data   | required | desc |
| ------------ | :---: | :-----: | :------: | ---- |
| project_idx  | path  | integer |    O     |      |
| episode_name | query | string  |    O     |      |
| description  | query | string  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에피소드가 생성 되었습니다."
	},
	"data": {
		"episode": {
			"idx": "3"
		}
	}
}
```

---

## 3. 에피소드 수정 <a id="#project-episode-update"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/update`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc             |
| ----------- | :---: | :-----: | :------: | ---------------- |
| project_idx | path  | integer |    O     |                  |
| episode_idx | path  | integer |    O     |                  |
| column      | query | string  |    O     |                  |
| old_val     | query | string  |    O     | 공백일 수는 있음 |
| new_val     | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에피소드 정보가 수정됐습니다."
	},
	"data": {
		"episode": {
			"idx": "4",
			"column": "description",
			"value": "until 4"
		}
	}
}
```

---

## 4. 에피소드 삭제 <a id="#project-episode-delete"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/delete`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에피소드가 삭제됐습니다."
	},
	"data": null
}
```

---

## 5. 에피소드 활성화 <a id="project-shot-episode-activate"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/activate`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에피소드가 활성화 되었습니다."
	},
	"data": null
}
```

---

## 6. 에피소드 비활성화 <a id="project-shot-episode-deactivate"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/deactivate`

### permission

- `permission.update_project`

### request

| param    | type |  data   | required | desc |
| -------- | :--: | :-----: | :------: | ---- |
| team_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에피소드가 비활성화됐습니다."
	},
	"data": null
}
```

---

## 7. 에피소드 검증 <a id="episode-validate"></a>

### `POST /api/episode/validate`

### permission

- `permission.update_project`

### request

| param        | type |  data  | required | desc |
| ------------ | :--: | :----: | :------: | ---- |
| project_name | path | string |    O     |      |
| episode_name | path | string |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"episode": {
			"idx": 7,
			"name": "ep01",
			"description": ""
		}
	}
}
```

---

## 끝

[에피소드 목록 조회]: #project-episode-list
[에피소드 등록]: #project-episode-create
[에피소드 정보 수정]: #project-episode-update
[에피소드 삭제]: #project-episode-delete
[에피소드 활성화]: #project-shot-episode-activate
[에피소드 비활성화]: #project-shot-episode-deactivate
[에피소드 검증]: #episode-validate
