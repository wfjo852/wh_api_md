# WH2API::Asset

## 목차

| 내용                                     | slug                                                                  | 서버 구현 | 웹 적용 |
| :--------------------------------------- | :-------------------------------------------------------------------- | :-------: | :-----: |
| 1. [에셋 등록]                           | /api/project/{project_idx}/category/{category_idx}/asset/create       |   POST    |    O    |
| 2. [에셋 정보 수정]                      | /api/project/asset/{asset_idx}/update                                 |   POST    |    O    |
| 3. [에셋 삭제]                           | /api/project/{project_idx}/asset/{asset_idx}/delete                   |   POST    |    O    |
| 4. [에셋 썸네일 업데이트]                | /api/project/{project_idx}/asset/{asset_idx}/thumbnail/update         |   POST    |    O    |
| 5. [에셋 벌크 등록]                      | /api/project/{project_idx}/asset/bulk/create                          |   POST    |    O    |
| 6. [에셋 벌크 목록 조회]                 | /api/project/{project_idx}/category/{category_idx}/asset/bulk/list    |    GET    |    O    |
| 7. [에셋에 관련된 샷과 태스크 목록 조회] | /api/project/{project_idx}/asset/{asset_idx}/shot/list[/with/setting] |   X GET   |    X    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에셋 등록 <a id="project-asset-create"></a>

### `POST /api/project/{project_idx}/category/{category_idx}/asset/create`

### permission

- `permission.update_project`

### request

| param           | type  |  data   | required | desc |
| --------------- | :---: | :-----: | :------: | ---- |
| project_idx     | path  | integer |    O     |      |
| category_idx    | path  | integer |    O     |      |
| asset_order     | query |  float  |    X     |      |
| asset_name      | query | string  |    O     |      |
| asset_thumbnail | query |  file   |    X     |      |
| description     | query | string  |    X     |      |
| status_idx      | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋이 등록되었습니다."
	},
	"data": {
		"shot_idx": "2104"
	}
}
```

---

## 2. 에셋 정보 수정 <a id="project-asset-update"></a>

### `POST /api/project/asset/{asset_idx}/update`

### permission

- `permission.update_asset_and_task`

### request

| param     | type  |  data   | required | desc             |
| --------- | :---: | :-----: | :------: | ---------------- |
| asset_idx | path  | integer |    O     |                  |
| column    | query | string  |    O     |                  |
| old_val   | query | string  |    O     | 공백일 수는 있음 |
| new_val   | query | string  |    O     | 공백일 수는 있음 |

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

## 3. 에셋 삭제 (/api/project/asset/{asset_idx}/delete) <a id="project-asset-delete"></a>

### `POST /api/project/asset/{asset_idx}/delete`

### permission

- `permission.update_project`

### request

| param     | type |  data   | required | desc |
| --------- | :--: | :-----: | :------: | ---- |
| asset_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋 정보가 삭제됐습니다."
	},
	"data": null
}
```

---

## 4. 에셋 썸네일 업데이트 <a id="project-asset-thumbnail"></a>

### `POST /api/project/{project_idx}/asset/{asset_idx}/thumbnail/update`

### permission

- `permission.update_asset_and_task`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| asset_idx   | path  | integer |    O     |      |
| attached    | query |  file   |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋 썸네일이 등록됐습니다."
	},
	"data": {
		"shot_idx": 4,
		"shot_thumbnail": "http://localhost:81/2019/02/21/05ed16a5d80f3f4b.png"
	}
}
```

---

## 5. 에셋 벌크 등록 <a id="project-asset-bulk-create"></a>

- 사용 예: http://localhost/project/1/asset/add

### `POST /api/project/{project_idx}/asset/bulk/create`

### permission

- `permission.update_project`

### request

- handsontable의 데이터를 보냅니다.

| param              | type  |  data   | required | desc |
| ------------------ | :---: | :-----: | :------: | ---- |
| project_idx        | path  | integer |    O     |      |
| asset_category_idx | query | integer |    O     |      |
| asset_name[]       | query | string  |    O     |      |
| description[]      | query | string  |    O     |      |

```json
{
	"assets": [
		{
			"name": "에셋네임1",
			"description": "에셋 설명입니다."
		},
		{
			"name": "에셋네임1",
			"description": "에셋 설명입니다."
		},
		{
			"name": "에셋네임1",
			"description": "에셋 설명입니다."
		}
	]
}
```

### response

```json
{
	"error": {
		"code": 200,
		"message": "Asset Data가 입력되었습니다."
	}
}
```

---

## 6. 에셋 벌크 목록 조회 (/api/project/{project_idx}/category/{category_idx}/asset/bulk/list) <a id="project-asset-bulk-list"></a>

- 사용 예: http://localhost/project/1/category/1/asset/task/add

### `GET /api/project/{project_idx}/category/{category_idx}/asset/bulk/list`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| category_idx | path | integer |    O     |      |

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
				"asset_name": "asn1",
				"asset_thumbnail": "",
				"description": "desc1",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					}
				}
			},
			{
				"asset_name": "asn2",
				"asset_thumbnail": "",
				"description": "desc2",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					}
				}
			},
			{
				"asset_name": "asn3",
				"asset_thumbnail": "",
				"description": "desc3",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					}
				}
			},
			{
				"asset_name": "asn4",
				"asset_thumbnail": "",
				"description": "desc4",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0",
						"user_idx": null,
						"user_name": null
					}
				}
			},
			{
				"asset_name": "Asset Name 0001",
				"asset_thumbnail": "",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0"
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0"
					}
				}
			},
			{
				"asset_name": "Asset Name 0002",
				"asset_thumbnail": "",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0"
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0"
					}
				}
			},
			{
				"asset_name": "Asset Name 0003",
				"asset_thumbnail": "",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0"
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0"
					}
				}
			},
			{
				"asset_name": "Asset Name 0004",
				"asset_thumbnail": "",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0"
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0"
					}
				}
			},
			{
				"asset_name": "Asset Name 0005",
				"asset_thumbnail": "",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"tasks": {
					"Lookdev": {
						"task_idx": null,
						"duration_init": "0"
					},
					"Photo": {
						"task_idx": null,
						"duration_init": "0"
					}
				}
			}
		]
	}
}
```

---

## 7. 에셋에 관련된 샷과 태스크 목록 조회 (/api/project/{project_idx}/asset/{asset_idx}/shot/list[/with/{setting}]) <a id="asset-shot-list"></a>

### `GET /api/project/{project_idx}/asset/{asset_idx}/shot/list[/with/{setting}`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc           |
| ----------- | :---: | :-----: | :------: | -------------- |
| project_idx | path  | integer |    O     |                |
| asset_idx   | path  | integer |    O     |                |
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
				"shot_idx": "1",
				"name": "s0010_c0010",
				"episode_name": "e01",
				"sequence_name": "s0010",
				"start_date": "2019-09-11",
				"end_date": "2019-09-15",
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
				"shot_idx": "2",
				"name": "s0010_c0020",
				"episode_name": "e01",
				"sequence_name": "s0010",
				"start_date": "2019-09-12",
				"end_date": "2019-09-17",
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
				"data": "episode_name",
				"type": "text",
				"width": 100,
				"editor": false
			},
			{
				"data": "sequence_name",
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
				"data": "start_date",
				"type": "date",
				"width": 100,
				"editor": false
			},
			{
				"data": "end_date",
				"type": "date",
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
			"Episode Name",
			"Sequence Name",
			"Shot Name",
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

[에셋 등록]: #project-asset-create
[에셋 정보 수정]: #project-asset-update
[에셋 삭제]: #project-asset-delete
[에셋 썸네일 업데이트]: #project-asset-thumbnail
[에셋 벌크 등록]: #project-asset-bulk-create
[에셋 벌크 목록 조회]: #project-asset-bulk-list
[에셋에 관련된 샷과 태스크 목록 조회]: #asset-shot-list
