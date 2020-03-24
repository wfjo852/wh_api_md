# WH2API::task

## 목차

| 내용                                      | slug                                                                           | 서버 구현 | 웹 적용 |
| :---------------------------------------- | :----------------------------------------------------------------------------- | :-------: | :-----: |
| 1. [에셋 태스크 등록]                     | /api/project/{project_idx}/asset/{asset_idx}/task/create                       |   POST    |    O    |
| 2. [에셋 태스크 삭제]                     | /api/project/{project_idx}/asset/task/{task_idx}/delete                        |   POST    |    O    |
| 3. [에셋 태스크 정보 수정]                | /api/project/{project_idx}/asset/task/{task_idx}/update                        |   POST    |    O    |
| 4. [샷 태스크 등록]                       | /api/project/{project_idx}/shot/{shot_idx}/task/create                         |   POST    |    O    |
| 5. [샷 태스크 삭제]                       | /api/project/{project_idx}/shot/task/{task_idx}/delete                         |   POST    |    O    |
| 6. [샷 태스크 정보 수정]                  | /api/project/{project_idx}/shot/task/{task_idx}/update                         |   POST    |    O    |
| 7. [샷/에셋 태스크 상태 코드 수정 수정]   | /api/project/{project_idx}/{which}/task/{task_idx}/status/update               |   POST    |    O    |
| 8. [샷/에셋 태스크 업무 시작]             | /api/project/{project_idx}/{which}/task/{task_idx}/start                       |   POST    |    O    |
| 9. [샷/에셋 태스크 업무 정지]             | /api/project/{project_idx}/{which}/task/{task_idx}/stop                        |   POST    |    O    |
| 10. [샷 태스크의 에셋 릴레이션 목록 조회] | /api/project/{project_idx}/shot/task/{task_idx}/relation/read[/with/{setting}] |    GET    |    O    |

- O\* - 3, 4번 동시 적용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에셋 태스크 등록 <a id="project-asset-task-create"></a>

### `POST /api/project/{project_idx}/asset/{asset_idx}/task/create`

### permission

- `permission.update_asset_and_task`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| project_idx   | path  | integer |    O     |      |
| asset_idx     | path  | integer |    O     |      |
| tasktype_name | query | string  |    O     |      |
| status_idx    | query | integer |    X     |      |
| description   | query | string  |    X     |      |
| user_idx      | query | integer |    X     |      |
| start_date    | query | string  |    X     |      |
| end_date      | query | string  |    X     |      |
| duration      | query | double  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 등록 되었습니다."
	},
	"data": {
		"task_idx": 1
	}
}
```

---

## 2. 에셋 태스크 삭제 <a id="project-asset-task-delete"></a>

### `POST /api/project/{project_idx}/asset/task/{task_idx}/delete`

### permission

- `permission.update_asset_and_task`

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
		"message": "태스크가 삭제됐습니다."
	},
	"data": null
}
```

---

## 3. 에셋 태스크 정보 수정 <a id="project-asset-task-update"></a>

- 에셋 태스크 1개의 1가지 정보만 선택해서 수정
- 사용 예)
  - http://localhost/project/1/category/1/asset/task/add
  - task의 duration_init 값을 수정합니다.

### `POST /api/project/{project_idx}/asset/task/{task_idx}/update`

### permission

- `permission.update_asset_and_task`

### request

| param    | type  |  data   | required | desc             |
| -------- | :---: | :-----: | :------: | ---------------- |
| task_idx | path  | integer |    O     |                  |
| column   | query | string  |    O     |                  |
| old_val  | query | string  |    O     | 공백일 수는 있음 |
| new_val  | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 배치 되었습니다."
	},
	"data": null
}
```

---

## 4. 샷 태스크 등록 <a id="project-shot-task-create"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/task/create`

### permission

- `permission.update_shot_and_task`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| project_idx   | path  | integer |    O     |      |
| shot_idx      | path  | integer |    O     |      |
| tasktype_name | query | string  |    O     |      |
| status_idx    | query | integer |    X     |      |
| description   | query | string  |    X     |      |
| user_idx      | query | integer |    X     |      |
| start_date    | query | string  |    X     |      |
| end_date      | query | string  |    X     |      |
| duration      | query | double  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 등록 되었습니다."
	},
	"data": {
		"task_idx": 1
	}
}
```

---

## 5. 샷 태스크 삭제 <a id="project-shot-task-delete"></a>

### `POST /api/project/{project_idx}/shot/task/{task_idx}/delete`

### permission

- `permission.update_shot_and_task`

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
		"message": "태스크가 삭제됐습니다."
	},
	"data": null
}
```

---

## 6. 샷 태스크 정보 수정 <a id="project-shot-task-update"></a>

### `POST /api/project/{project_idx}/shot/task/{task_idx}/update`

### permission

- `permission.update_shot_and_task`

### request

| param    | type  |  data   | required | desc             |
| -------- | :---: | :-----: | :------: | ---------------- |
| task_idx | path  | integer |    O     |                  |
| column   | query | string  |    O     |                  |
| old_val  | query | string  |    O     | 공백일 수는 있음 |
| new_val  | query | string  |    O     | 공백일 수는 있음 |

- 이용자 정보를 없애려면 ''(공백)을 보냄

### response

```json
{
	"error": {
		"code": 200,
		"message": "샷 정보가 수정됐습니다."
	},
	"data": null
}
```

---

## 7. 샷/에셋 태스크 상태 코드 수정 <a id="task-status-update"></a>

### `POST /api/project/{project_idx}/{which}/task/{task_idx}/status/update`

### permission

- `permission.do_task_and_version_status`

### request

| param       | type  |  data   | required | desc          |
| ----------- | :---: | :-----: | :------: | ------------- |
| project_idx | path  | integer |    O     |               |
| task_idx    | path  | integer |    O     |               |
| which       | path  | string  |    O     | asset or shot |
| status_idx  | query | integer |    O     |               |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크 상태가 변경됐습니다."
	},
	"data": {
		"status_idx": "1",
		"status_name": "wip"
	}
}
```

---

## 8. 샷/에셋 태스크 업무 시작 <a id="task-start"></a>

### `POST /api/project/{project_idx}/{which}/task/{task_idx}/start`

### permission

- `permission.do_task_and_version_status`

### request

| param       | type |  data   | required | desc          |
| ----------- | :--: | :-----: | :------: | ------------- |
| project_idx | path | integer |    O     |               |
| task_idx    | path | integer |    O     |               |
| which       | path | string  |    O     | asset or shot |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 시작됐습니다."
	},
	"data": null
}
```

---

## 9. 샷/에셋 태스크 업무 정지 <a id="task-stop"></a>

### `POST /api/project/{project_idx}/{which}/task/{task_idx}/stop`

### permission

- `permission.do_task_and_version_status`

### request

| param       | type |  data   | required | desc          |
| ----------- | :--: | :-----: | :------: | ------------- |
| project_idx | path | integer |    O     |               |
| task_idx    | path | integer |    O     |               |
| which       | path | string  |    O     | asset or shot |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 정지됐습니다."
	},
	"data": null
}
```

---

## 10. 샷 태스크의 에셋 릴레이션 목록 조회 <a id="shot-task-relation-read"></a>

### `GET /api/project/{project_idx}/shot/task/{task_idx}/relation/read[/with/{setting}]`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc           |
| ----------- | :---: | :-----: | :------: | -------------- |
| project_idx | path  | integer |    O     |                |
| task_idx    | path  | integer |    O     |                |
| setting     | query | string  |    X     | 값은 'setting' |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"assets": [
			{
				"asset_idx": "1",
				"name": "ch_bunny",
				"asset_category_name": "char",
				"tasks": {
					"Modeling": {
						"task_idx": "7",
						"status_name": "wip",
						"status_color": "#dbd8db",
						"status_idx": "1"
					},
					"Texture": {
						"task_idx": null,
						"status_name": null,
						"status_color": null,
						"status_idx": null
					},
					"Concept": {
						"task_idx": null,
						"status_name": null,
						"status_color": null,
						"status_idx": null
					}
				}
			},
			{
				"asset_idx": "2",
				"name": "ch_bird",
				"asset_category_name": "char"
			},
			{
				"tasks": {
					"Modeling": {
						"task_idx": "2",
						"status_name": "wip",
						"status_color": "#dbd8db",
						"status_idx": "1"
					},
					"Texture": {
						"task_idx": "1",
						"status_name": "wip",
						"status_color": "#dbd8db",
						"status_idx": "1"
					},
					"Concept": {
						"task_idx": "6",
						"status_name": "confirm",
						"status_color": "#03a9f4",
						"status_idx": "2"
					}
				}
			}
		],
		"setting_column": [
			{
				"data": "asset_category_name",
				"type": "text",
				"width": 100,
				"editor": false
			},
			{
				"data": "name",
				"type": "text",
				"width": 100,
				"editor": false
			},
			{
				"data": "tasks.Modeling.status_name",
				"type": "text",
				"width": 80,
				"editor": false
			},
			{
				"data": "tasks.Texture.status_name",
				"type": "text",
				"width": 80,
				"editor": false
			},
			{
				"data": "tasks.Concept.status_name",
				"type": "text",
				"width": 80,
				"editor": false
			}
		],
		"headers": [
			"Asset Category",
			"Asset Name",
			"Modeling",
			"Texture",
			"Concept"
		]
	}
}
```

- `setting_column`과 `header`는 `/with/setting`으로 접근할 때만 표시됨

---

## 끝

[에셋 태스크 등록]: #project-asset-task-create
[에셋 태스크 삭제]: #project-asset-task-delete
[에셋 태스크 정보 수정]: #project-asset-task-update
[샷 태스크 등록]: #project-shot-task-create
[샷 태스크 삭제]: #project-shot-task-delete
[샷 태스크 정보 수정]: project-shot-task-update
[샷/에셋 태스크 상태 코드 수정]: #task-status-update
[샷/에셋 태스크 업무 시작]: #task-start
[샷/에셋 태스크 업무 정지]: #task-stop
[샷 태스크의 에셋 릴레이션 목록 조회]: #shot-task-relation-read
