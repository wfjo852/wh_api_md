# WH2API::Shot

## 목차

| 내용                             | slug                                                                                    | 서버 구현 | 웹 적용 |
| :------------------------------- | :-------------------------------------------------------------------------------------- | :-------: | :-----: |
| 1. [샷 등록]                     | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/create    |   POST    |    O    |
| 2. [샷 정보 수정]                | /api/project/{project_idx}/shot/{shot_idx}/update                                       |   POST    |    O    |
| 3. [샷 삭제]                     | /api/project/{project_idx}/shot/{shot_idx}/delete                                       |   POST    |    O    |
| 4. [샷 정보 조회]                | /api/project/{project_idx}/shot/{shot_idx}/read                                         |    GET    |    X    |
| 5. [샷 썸네일 업데이트]          | /api/project/{project_idx}/shot/{shot_idx}/thumbnail/update                             |   POST    |    O    |
| 6. [샷 목록 조회]                | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/list      |    GET    |    O    |
| 7. [샷 벌크 등록]                | /api/project/{project_idx}/shot/bulk/create                                             |   POST    |    O    |
| 8. [샷 벌크 목록 조회]           | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/bulk/list |    GET    |    O    |
| 9. [샷에 관련된 에셋 추가]       | /api/project/{project_idx}/shot/{shot_idx}/asset/add                                    |   POST    |    O    |
| 10. [샷에 관련된 에셋 벌크 추가] | /api/project/{project_idx}/shot/{shot_idx}/asset/bulk/add                               |   POST    |    X    |
| 11. [샷에 관련된 에셋 제거]      | /api/project/{project_idx}/shot/{shot_idx}/asset/remove                                 |   POST    |    O    |
| 12. [샷에 관련된 에셋 벌크 제거] | /api/project/{project_idx}/shot/{shot_idx}/asset/bulk/remove                            |   POST    |    X    |
| 14. [릴레이션 오버뷰 조회]       | /api/project/{project_idx}/episode/{episode_idx}/shot/asset/relation/overview/read      |    GET    |    O    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 샷 등록 <a id="project-shot-create"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/create`

### permission

- `permission.update_project`

### request

| param        | type  |  data   | required | desc |
| ------------ | :---: | :-----: | :------: | ---- |
| project_idx  | path  | integer |    O     |      |
| episode_idx  | path  | integer |    O     |      |
| sequence_idx | path  | integer |    O     |      |
| shot_order   | query |  float  |    X     |      |
| shot_name    | query | string  |    O     |      |
| attached     | query |  file   |    X     |      |
| description  | query | string  |    X     |      |
| status_idx   | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "샷이 등록됐습니다."
	},
	"data": {
		"shot_idx": "2103",
		"shot_name": "s0010_c0010",
		"shot_order": "114",
		"shot_thumbnail": null,
		"status_idx": "1",
		"project_idx": "1",
		"episode_idx": "1",
		"episode_name": "ep01",
		"sequence_idx": "1",
		"sequence_name": "s0010",
		"shot_status_name": "wip",
		"description": null,
		"location": null,
		"note": null,
		"length": null,
		"handle_in": null,
		"handle_out": null,
		"frame_in": null,
		"frame_out": null,
		"timecode_in": null,
		"timecode_out": null,
		"importance": "0",
		"difficulty": null,
		"original_path": null,
		"camera_clip": null,
		"camera_name": null,
		"lens_type": null,
		"focal_length": null,
		"grip": null,
		"camera_filter": null,
		"iso": null,
		"shutter_speed": null,
		"f_stop": null,
		"stereo_type": null,
		"stereo_iod": null,
		"stereo_converged_point": null,
		"stereo_rig": null,
		"camera_note": null
	}
}
```

---

## 2. 샷 정보 수정 <a id="project-shot-update"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/update`

### permission

- `permission.update_shot_and_task`

### request

| param    | type  |  data   | required | desc             |
| -------- | :---: | :-----: | :------: | ---------------- |
| shot_idx | path  | integer |    O     |                  |
| column   | query | string  |    O     |                  |
| old_val  | query | string  |    O     | 공백일 수는 있음 |
| new_val  | query | string  |    O     | 공백일 수는 있음 |

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

- episode name, sequence name, shot name, 모든 태스크들의 summary는 수정이 불가능하고 그외의 모든 컬럼은 수정이 가능합니다.
- 숫자만 들어갈 수 있는 컬럼은 Shots 헤더의 Length, Handle In, Handle Out, Frame In, Frame Out 컬럼입니다.

---

## 3. 샷 삭제 <a id="project-shot-delete"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/delete`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| shot_idx    | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "샷이 삭제됐습니다."
	},
	"data": null
}
```

---

## 4. 샷 정보 조회 <a id="project-shot"></a>

### `GET /api/project/{project_idx}/shot/{shot_idx}/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| shot_idx    | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"shot_idx": "4",
		"shot_name": "s0010_c0010",
		"shot_order": "1",
		"shot_thumbnail": null,
		"episode_idx": "1",
		"episode_name": "ep01",
		"sequence_idx": "1",
		"sequence_name": "s0010",
		"description": "> Comp : 1 GATE",
		"shot_status_name": "wip"
	}
}
```

---

## 5. 샷 썸네일 업데이트 <a id="project-shot-thumbnail"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/thumbnail/update`

### permission

- `permission.update_shot_and_task`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| shot_idx    | path  | integer |    O     |      |
| attached    | query |  file   |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "샷 썸네일이 등록됐습니다."
	},
	"data": {
		"shot_idx": 4,
		"shot_thumbnail": "http://localhost:81/2019/02/21/05ed16a5d80f3f4b.png"
	}
}
```

---

## 6. 샷 목록 조회 <a id="project-shot-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/list`

### permission

- `permission.read_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"shots": [
			{
				"shot_idx": "1",
				"name": "s0010_c0010",
				"shot_order": "1"
			},
			{
				"shot_idx": "2",
				"name": "s0010_c0020",
				"shot_order": "2"
			},
			{
				"shot_idx": "3",
				"name": "s0010_c0030",
				"shot_order": "3"
			}
		]
	}
}
```

---

## 7. 샷 벌크 등록 <a id="#pproject-shot-bulk-create"></a>

### `POST /api/project/{project_idx}/shot/bulk/create`

### permission

- `permission.update_project`

### request

| param            | type  |  data   | required | desc |
| ---------------- | :---: | :-----: | :------: | ---- |
| project_idx      | path  | integer |    O     |      |
| episode_idx      | query | integer |    O     |      |
| sequence_idx     | query | integer |    O     |      |
| shot_name[]      | query | string  |    O     |      |
| description[]    | query | string  |    O     |      |
| direction_note[] | query | string  |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에피소드가 삭제 되었습니다."
	},
	"data": {}
}
```

---

## 8. 샷 벌크 목록 조회 <a id="#project-shot-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/bulk/list`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"shots": [
			{
				"shot_name": "s0010_c0010",
				"shot_thumbnail": "",
				"description": "",
				"tasks": {
					"Lookdev": {
						"task_idx": "538",
						"duration_init": "0",
						"user_idx": "1",
						"user_name": "cccc"
					},
					"Photo": {
						"task_idx": "535",
						"duration_init": "0",
						"user_idx": "1",
						"user_name": "cccc"
					}
				}
			},
			{
				"shot_name": "s0010_c0020",
				"shot_thumbnail": "",
				"description": "",
				"tasks": {
					"Lookdev": {
						"task_idx": "538",
						"duration_init": "0",
						"user_idx": "1",
						"user_name": "cccc"
					},
					"Photo": {
						"task_idx": "535",
						"duration_init": "0",
						"user_idx": "1",
						"user_name": "cccc"
					}
				}
			}
		]
	}
}
```

---

## 9. 샷에 관련된 에셋 추가 <a id="shot-asset-add"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/asset/add`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| shot_idx    | path  | integer |    O     |      |
| asset_idx   | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋이 샷에 추가됐습니다."
	},
	"data": null
}
```

---

## 10. 샷에 관련된 에셋 벌크 추가 <a id="shot-asset-bulk-add"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/asset/bulk/add`

### permission

- `permission.update_project`

### request

| param       | type  |       data       | required | desc |
| ----------- | :---: | :--------------: | :------: | ---- |
| project_idx | path  |     integer      |    O     |      |
| shot_idx    | path  |     integer      |    O     |      |
| asset_idx[] | query | array of integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋이 샷에 추가됐습니다."
	},
	"data": null
}
```

---

## 11. 샷에 관련된 에셋 제거 <a id="shot-asset-remove"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/asset/remove`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| shot_idx    | path  | integer |    O     |      |
| asset_idx   | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋이 샷에서 제거됐습니다."
	},
	"data": null
}
```

---

## 12. 샷에 관련된 에셋 벌크 제거 <a id="shot-asset-bulk-remove"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/asset/bulk/remove`

### permission

- `permission.update_project`

### request

| param       | type  |       data       | required | desc |
| ----------- | :---: | :--------------: | :------: | ---- |
| project_idx | path  |     integer      |    O     |      |
| shot_idx    | path  |     integer      |    O     |      |
| asset_idx[] | query | array of integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "에셋이 샷에서 제거됐습니다."
	},
	"data": null
}
```

---

## 14. 릴레이션 오버뷰 조회 <a id="relation-overview-read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/shot/asset/relation/overview/read`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    O     |      |

### response

- 연관되어 있으면 org_text, dispolay_text를 모두 "O"로 내려주세요.
- 연관되어 있지 않으면 org_text, display_text를 모두 ""로 내려 주세요.

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"collapsible_columns": [
			{ "row": -2, "col": 7, "collapsible": true },
			{ "row": -2, "col": 14, "collapsible": true }
		],
		"nested_headers": [
			[
				"Sequence",
				"Sequence",
				"Shot",
				"Shot",
				"Thumbnail",
				"Description",
				"Direction Note",
				{ "label": "ch", "colspan": 7 },
				{ "label": "env", "colspan": 6 }
			],
			[
				"sequence_idx",
				"name",
				"-",
				"name",
				"-",
				"-",
				"-",
				"ch_Asset01",
				"ch_Asset02",
				"ch_Asset03",
				"ch_Asset04",
				"ch_Asset05",
				"ch_Asset06",
				"ch_Asset07",
				"env_Asset01",
				"env_Asset02",
				"env_Asset03",
				"env_Asset04",
				"end_Asset05",
				"env_Asset06"
			]
		],
		"overview": [
			{
				"sequence_idx": 1,
				"sequence_name": "s0010",
				"shot_idx": 1,
				"shot_name": "s0010_c0050",
				"shot_thumbnail": "",
				"description": "Bunny is stretching his body",
				"direction_note": "",
				"assets": {
					"ch": {
						"ch_asset01": {
							"asset_idx": 1,
							"org_text": "O",
							"display_text": "O"
						},
						"ch_asset02": {
							"asset_idx": 2,
							"org_text": "O",
							"display_text": "O"
						},
						"ch_asset03": {
							"asset_idx": 3,
							"org_text": "",
							"display_text": ""
						},
						"ch_asset04": {
							"asset_idx": 4,
							"org_text": "O",
							"display_text": "O"
						},
						"ch_asset05": {
							"asset_idx": 5,
							"org_text": "O",
							"display_text": "O"
						},
						"ch_asset06": {
							"asset_idx": 6,
							"org_text": "",
							"display_text": ""
						},
						"ch_asset07": {
							"asset_idx": 7,
							"org_text": "O",
							"display_text": "O"
						}
					},
					"env": {
						"env_asset01": {
							"asset_idx": 1,
							"org_text": "O",
							"display_text": "O"
						},
						"env_asset02": {
							"asset_idx": 2,
							"org_text": "O",
							"display_text": "O"
						},
						"env_asset03": {
							"asset_idx": 3,
							"org_text": "O",
							"display_text": "O"
						},
						"env_asset04": {
							"asset_idx": 4,
							"org_text": "O",
							"display_text": "O"
						},
						"env_asset05": {
							"asset_idx": 5,
							"org_text": "O",
							"display_text": "O"
						},
						"env_asset06": {
							"asset_idx": 6,
							"org_text": "O",
							"display_text": "O"
						}
					}
				}
			}
		],
		"setting_column": [
			{
				"data": "sequence_idx",
				"type": "numeric",
				"width": 50,
				"editor": false
			},
			{
				"data": "sequence_name",
				"type": "text",
				"readOnly": true,
				"width": 120,
				"editor": false
			},
			{ "data": "shot_idx", "type": "numeric", "width": 50, "editor": false },
			{
				"data": "shot_name",
				"type": "text",
				"readOnly": true,
				"width": 120,
				"editor": false
			},
			{
				"data": "shot_thumbnail",
				"renderer": "renderThumbnail",
				"width": 84,
				"editor": false
			},
			{
				"data": "description",
				"type": "text",
				"width": 190,
				"readOnly": true,
				"editor": false
			},
			{
				"data": "direction_note",
				"type": "text",
				"width": 190,
				"readOnly": true,
				"editor": false
			},
			{
				"data": "assets.ch.ch_asset01.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.ch.ch_asset02.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.ch.ch_asset03.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.ch.ch_asset04.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.ch.ch_asset05.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.ch.ch_asset06.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.ch.ch_asset07.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.env.env_asset01.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.env.env_asset02.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.env.env_asset03.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.env.env_asset04.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.env.env_asset05.display_text",
				"renderer": "renderRelation",
				"type": "text"
			},
			{
				"data": "assets.env.env_asset06.display_text",
				"renderer": "renderRelation",
				"type": "text"
			}
		]
	}
}
```

---

## 끝

[샷 등록]: #project-shot-create
[샷 정보 수정]: #project-shot-update
[샷 삭제]: #project-shot-delete
[샷 정보 조회]: #project-shot
[샷 썸네일 업데이트]: #project-shot-thumbnail
[샷 목록 조회]: #project-shot-list
[샷 벌크 등록]: #project-shot-bulk-create
[샷 벌크 목록 조회]: #project-shot-list
[샷에 관련된 에셋 추가]: #shot-asset-add
[샷에 관련된 에셋 벌크 추가]: #shot-asset-bulk-add
[샷에 관련된 에셋 제거]: #shot-asset-remove
[샷에 관련된 에셋 벌크 제거]: #shot-asset-bulk-remove
[샷에 관련된 에셋과 태스크 목록 조회]: #shot-asset-list
[릴레이션 오버뷰 조회]: #relation-overview-read
