# WH2API::ProgressOverview

## 목차

| 내용                                     | slug                                                                                                           | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------- | :-------: | :-----: | :--: | :--: |
| 1. [에피소드 진행 오버뷰 조회]           | /api/project/{project_idx}/episode/progress/overview/read                                                      |    GET    |    O    |  -   |  -   |
| 2. [에피소드 진행 오버뷰 설정 수정]      | /api/project/{project_idx}/episode/progress/overview/setting/update                                            |   POST    |    O    |  -   |  -   |
| 3. [시퀀스 진행 오버뷰 조회]             | /api/project/{project_idx}/episode/{episode_idx}/sequence/progress/overview/read                               |    GET    |    O    |  -   |  -   |
| 4. [시퀀스 진행 오버뷰 설정 수정]        | /api/project/{project_idx}/episode/{episode_idx}/sequence/progress/overview/setting/update                     |   POST    |    O    |  -   |  -   |
| 5. [샷 진행 오버뷰 조회]                 | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/progress/overview/read           |    GET    |    X    |  -   |  -   |
| 6. [샷 진행 오버뷰 설정 수정]            | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/progress/overview/setting/update |   POST    |    X    |  -   |  -   |
| 7. [에셋 카테고리 진행 오버뷰 조회]      | /api/project/{project_idx}/category/progress/overview/read                                                     |    GET    |    X    |  -   |  -   |
| 8. [에셋 카테고리 진행 오버뷰 설정 수정] | /api/project/{project_idx}/category/progress/overview/setting/update                                           |   POST    |    X    |  -   |  -   |
| 9. [에셋 진행 오버뷰 조회]               | /api/project/{project_idx}/category/{category_idx}/asset/progress/overview/read                                |    GET    |    X    |  -   |  -   |
| 10. [에셋 진행 오버뷰 설정 수정]         | /api/project/{project_idx}/category/{category_idx}/asset/progress/overview/setting/update                      |   POST    |    X    |  -   |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에피소드 진행 오버뷰 조회 <a id="episode-progress-overview-read"></a>

### `GET /api/project/{project_idx}/episode/progress/overview/read`

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
		"message": "성공"
	},
	"data": {
		"episodes": [
			{
				"idx": "1",
				"name": "Ep01",
				"description": "Demo_Bigbuck_Bunny_First",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"count": "30",
				"progress": "13.5",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			},
			{
				"idx": "1",
				"name": "Ep01",
				"description": "Demo_Bigbuck_Bunny_First",
				"tasktype_name": "Comp",
				"start_date": null,
				"end_date": null,
				"count": "30",
				"progress": "5.8",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			}
		],
		"config": {
			"hidden_columns": [5, 6],
			"columns": [
				{
					"title": "idx",
					"name": "idx",
					"data": "idx",
					"className": "idx dt-body-center",
					"searchable": false,
					"visible": false
				},
				{
					"title": "episode name",
					"name": "name",
					"data": "name",
					"className": "name dt-body-center",
					"visible": true
				},
				{
					"title": "description",
					"name": "description",
					"data": "description",
					"className": "description dt-body-center",
					"visible": true
				},
				{
					"title": "abc",
					"name": "c1",
					"data": "c1",
					"className": "c1 dt-body-center",
					"visible": true
				},
				{
					"title": "def",
					"name": "c2",
					"data": "c2",
					"className": "c2 dt-body-center",
					"visible": true
				},
				{
					"title": "qqq",
					"name": "c3",
					"data": "c3",
					"className": "c3 dt-body-center",
					"visible": false
				},
				{
					"title": "www",
					"name": "c4",
					"data": "c4",
					"className": "c4 dt-body-center",
					"visible": false
				},
				{
					"title": "tasktype",
					"name": "tasktype_name",
					"data": "tasktype_name",
					"className": "tasktype_name dt-body-center",
					"visible": true
				},
				{
					"title": "start date",
					"name": "start_date",
					"data": "start_date",
					"className": "start_date dt-body-center",
					"visible": true
				},
				{
					"title": "end date",
					"name": "end_date",
					"data": "end_date",
					"className": "end_date dt-body-center",
					"visible": true
				},
				{
					"title": "count",
					"name": "count",
					"data": "count",
					"className": "count dt-body-center",
					"visible": true
				},
				{
					"title": "progress",
					"name": "progress",
					"data": "progress",
					"className": "progress dt-body-center",
					"visible": true
				}
			],
			"rows_group": [
				"idx:name",
				"name:name",
				"description:name",
				"c1:name",
				"c2:name",
				"c3:name",
				"c4:name"
			],
			"editable_columns": [2, 3, 4, 5, 6],
			"editor_fields": [
				{
					"label": "description:",
					"name": "description"
				},
				{
					"label": "abc:",
					"name": "c1"
				},
				{
					"label": "def:",
					"name": "c2"
				},
				{
					"label": "qqq:",
					"name": "c3"
				},
				{
					"label": "www:",
					"name": "c4"
				}
			]
		},
		"tasktypes": [
			{
				"idx": "1",
				"name": "Animation",
				"color": "#DE4E4E"
			},
			{
				"idx": "3",
				"name": "Comp",
				"color": "#FFD906"
			}
		],
		"row_span_columns": [1, 2, 3, 4],
		"row_task_count": [
			[1, 3],
			[2, 2]
		]
	}
}
```

---

## 2. 에피소드 진행 오버뷰 설정 수정 <a id="episode-progress-overview-setting-update"></a>

### `POST /api/project/{project_idx}/episode/progress/overview/setting/update`

### permission

- `permission.read_shot_task_overview`

### request

| param         | type  |  data   | required | desc            |
| ------------- | :---: | :-----: | :------: | --------------- |
| project_idx   | path  | integer |    O     |                 |
| setting_name  | query | string  |    O     | 'hidden_column' |
| setting_value | query | string  |    O     |                 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "설정이 저장됐습니다."
	},
	"data": null
}
```

---

## 3. 시퀀스 진행 오버뷰 조회 <a id="sequence-progress-overview-read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/progress/overview/read`

### permission

- `permission.read_shot_task_overview`

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
		"message": "성공"
	},
	"data": {
		"sequences": [
			{
				"idx": "1",
				"name": "s0010",
				"description": "Opening Sequence",
				"tasktype_name": "Animation",
				"start_date": "2019-04-08",
				"end_date": "2019-05-01",
				"count": "13",
				"progress": "59.6"
			},
			{
				"idx": "1",
				"name": "s0010",
				"description": "Opening Sequence",
				"tasktype_name": "Comp",
				"start_date": null,
				"end_date": null,
				"count": "10",
				"progress": "31.0"
			},
			{
				"idx": "2",
				"name": "s0020",
				"description": "Fighting in the Jungle",
				"tasktype_name": "Animation",
				"start_date": "2019-04-08",
				"end_date": "2019-04-11",
				"count": "10",
				"progress": "54.0"
			},
			{
				"idx": "2",
				"name": "s0020",
				"description": "Fighting in the Jungle",
				"tasktype_name": "Comp",
				"start_date": null,
				"end_date": null,
				"count": "10",
				"progress": "37.5"
			}
		],
		"config": {
			"hidden_columns": [],
			"columns": [
				{
					"title": "idx",
					"name": "idx",
					"data": "idx",
					"className": "idx dt-body-center",
					"searchable": false,
					"visible": false
				},
				{
					"title": "sequence name",
					"name": "name",
					"data": "name",
					"className": "name dt-body-center",
					"visible": true
				},
				{
					"title": "description",
					"name": "description",
					"data": "description",
					"className": "description dt-body-center",
					"visible": true
				},
				{
					"title": "tasktype",
					"name": "tasktype_name",
					"data": "tasktype_name",
					"className": "tasktype_name dt-body-center",
					"visible": true
				},
				{
					"title": "start date",
					"name": "start_date",
					"data": "start_date",
					"className": "start_date dt-body-center",
					"visible": true
				},
				{
					"title": "end date",
					"name": "end_date",
					"data": "end_date",
					"className": "end_date dt-body-center",
					"visible": true
				},
				{
					"title": "count",
					"name": "count",
					"data": "count",
					"className": "count dt-body-center",
					"visible": true
				},
				{
					"title": "progress",
					"name": "progress",
					"data": "progress",
					"className": "progress dt-body-center",
					"visible": true
				}
			],
			"rows_group": ["idx:name", "name:name", "description:name"],
			"editable_columns": [2],
			"editor_fields": [
				{
					"label": "description:",
					"name": "description"
				}
			]
		},
		"tasktypes": [
			{
				"idx": "1",
				"name": "Animation",
				"color": "#DE4E4E"
			},
			{
				"idx": "3",
				"name": "Comp",
				"color": "#FFD906"
			},
			{
				"idx": "17",
				"name": "rendering",
				"color": "#f44336"
			},
			{
				"idx": "18",
				"name": "roto",
				"color": "#f44336"
			}
		],
		"row_span_columns": [1, 2, 3, 4],
		"row_task_count": [
			[1, 3],
			[2, 2]
		]
	}
}
```

---

## 4. 시퀀스 진행 오버뷰 설정 수정 <a id="sequence-progress-overview-setting-update"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/progress/overview/setting/update`

### permission

- `permission.read_shot_task_overview`

### request

| param         | type  |  data   | required | desc            |
| ------------- | :---: | :-----: | :------: | --------------- |
| project_idx   | path  | integer |    O     |                 |
| episode_idx   | path  | integer |    O     |                 |
| setting_name  | query | string  |    O     | 'hidden_column' |
| setting_value | query | string  |    O     |                 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "설정이 저장됐습니다."
	},
	"data": null
}
```

---

## 5. 샷 진행 오버뷰 조회 <a id="shot-progress-overview-read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/progress/overview/read`

### permission

- `permission.read_shot_task_overview`

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
				"idx": "1",
				"name": "s0010_c0010",
				"description": "river flows",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"status_name": "confirm",
				"artist_name": "Artist",
				"last_version": "big_s0010_c0010_anim_v001",
				"last_version_comment": "Confirm_check",
				"last_publish": "",
				"last_publish_comment": "",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			},
			{
				"idx": "1",
				"name": "s0010_c0010",
				"description": "river flows",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"status_name": "confirm",
				"artist_name": "Artist",
				"last_version": "big_s0010_c0010_anim_v001",
				"last_version_comment": "Confirm_check",
				"last_publish": "",
				"last_publish_comment": "",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			}
		],
		"config": {
			"hidden_columns": [5, 6],
			"columns": [
				{
					"title": "idx",
					"name": "idx",
					"data": "idx",
					"className": "idx dt-body-center",
					"searchable": false,
					"visible": false
				},
				{
					"title": "shot name",
					"name": "name",
					"data": "name",
					"className": "name dt-body-center",
					"visible": true
				},
				{
					"title": "description",
					"name": "description",
					"data": "description",
					"className": "description dt-body-center",
					"visible": true
				},
				{
					"title": "abc",
					"name": "c1",
					"data": "c1",
					"className": "c1 dt-body-center",
					"visible": true
				},
				{
					"title": "tasktype",
					"name": "tasktype",
					"data": "tasktype",
					"className": "tasktype dt-body-center",
					"visible": true
				},
				{
					"title": "start date",
					"name": "start_date",
					"data": "start_date",
					"className": "start_date dt-body-center",
					"visible": false
				},
				{
					"title": "end date",
					"name": "end_date",
					"data": "end_date",
					"className": "end_date dt-body-center",
					"visible": false
				},
				{
					"title": "status name",
					"name": "status_name",
					"data": "status_name",
					"className": "status_name dt-body-center",
					"visible": true
				},
				{
					"title": "artist name",
					"name": "artist_name",
					"data": "artist_name",
					"className": "artist_name dt-body-center",
					"visible": true
				},
				{
					"title": "last version",
					"name": "last_version",
					"data": "last_version",
					"className": "last_version dt-body-center",
					"visible": true
				},
				{
					"title": "last version comment",
					"name": "last_version_comment",
					"data": "last_version_comment",
					"className": "last_version_comment dt-body-center",
					"visible": true
				},
				{
					"title": "last publish",
					"name": "last_publish",
					"data": "last_publish",
					"className": "last_publish dt-body-center",
					"visible": true
				},
				{
					"title": "last publish comment",
					"name": "last_publish_comment",
					"data": "last_publish_comment",
					"className": "last_publish_comment dt-body-center",
					"visible": true
				}
			],
			"rows_group": ["idx:name", "name:name", "description:name", "c1:name"],
			"editable_columns": [2, 3, 4, 5, 6],
			"editor_fields": [
				{
					"label": "description:",
					"name": "description"
				},
				{
					"label": "abc:",
					"name": "c1"
				},
				{
					"label": "def:",
					"name": "c2"
				},
				{
					"label": "qqq:",
					"name": "c3"
				},
				{
					"label": "www:",
					"name": "c4"
				}
			]
		},
		"shot_statuses": [
			{
				"idx": "1",
				"name": "wip",
				"color": "#DE4E4E"
			}
		],
		"task_statuses": [
			{
				"idx": "1",
				"name": "wip",
				"color": "#DE4E4E"
			}
		],
		"tasktypes": [
			{
				"idx": "1",
				"name": "Animation",
				"color": "#DE4E4E"
			},
			{
				"idx": "3",
				"name": "Comp",
				"color": "#FFD906"
			}
		],
		"row_span_columns": [1, 2, 3, 4],
		"row_task_count": [
			[1, 3],
			[2, 2]
		]
	}
}
```

---

## 6. 샷 진행 오버뷰 설정 수정 <a id="shot-progress-overview-setting-update"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/progress/overview/setting/update`

### permission

- `permission.read_asset_task_overview`

### request

| param         | type  |  data   | required | desc            |
| ------------- | :---: | :-----: | :------: | --------------- |
| project_idx   | path  | integer |    O     |                 |
| episode_idx   | path  | integer |    O     |                 |
| sequence_idx  | path  | integer |    O     |                 |
| setting_name  | query | string  |    O     | 'hidden_column' |
| setting_value | query | string  |    O     |                 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "설정이 저장됐습니다."
	},
	"data": null
}
```

---

## 7. 에셋 카테고리 진행 오버뷰 조회 <a id="category-progress-overview-read"></a>

### `GET /api/project/{project_idx}/category/progress/overview/read`

### permission

- `permission.read_asset_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"categories": [
			{
				"idx": "1",
				"name": "category_name",
				"description": "Demo_Bigbuck_Bunny_First",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"progress": "13.5",
				"artist": "c2m",
				"status_name": "wip",
				"progress": "3.3",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			},
			{
				"idx": "1",
				"name": "category_name",
				"description": "Demo_Bigbuck_Bunny_First",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"progress": "13.5",
				"artist": "c2m",
				"status_name": "wip",
				"progress": "3.3",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			}
		],
		"config": {
			"hidden_columns": [5, 6],
			"columns": [
				{
					"title": "idx",
					"name": "idx",
					"data": "idx",
					"className": "idx dt-body-center",
					"searchable": false,
					"visible": false
				},
				{
					"title": "category name",
					"name": "name",
					"data": "name",
					"className": "name dt-body-center",
					"visible": true
				},
				{
					"title": "description",
					"name": "description",
					"data": "description",
					"className": "description dt-body-center",
					"visible": true
				},
				{
					"title": "abc",
					"name": "c1",
					"data": "c1",
					"className": "c1 dt-body-center",
					"visible": true
				},
				{
					"title": "def",
					"name": "c2",
					"data": "c2",
					"className": "c2 dt-body-center",
					"visible": true
				},
				{
					"title": "qqq",
					"name": "c3",
					"data": "c3",
					"className": "c3 dt-body-center",
					"visible": false
				},
				{
					"title": "www",
					"name": "c4",
					"data": "c4",
					"className": "c4 dt-body-center",
					"visible": false
				},
				{
					"title": "tasktype",
					"name": "tasktype_name",
					"data": "tasktype_name",
					"className": "tasktype_name dt-body-center",
					"visible": true
				},
				{
					"title": "start date",
					"name": "start_date",
					"data": "start_date",
					"className": "start_date dt-body-center",
					"visible": true
				},
				{
					"title": "end date",
					"name": "end_date",
					"data": "end_date",
					"className": "end_date dt-body-center",
					"visible": true
				},
				{
					"title": "count",
					"name": "count",
					"data": "count",
					"className": "count dt-body-center",
					"visible": true
				},
				{
					"title": "progress",
					"name": "progress",
					"data": "progress",
					"className": "progress dt-body-center",
					"visible": true
				}
			],
			"rows_group": [
				"idx:name",
				"name:name",
				"description:name",
				"c1:name",
				"c2:name",
				"c3:name",
				"c4:name"
			],
			"editable_columns": [2, 3, 4, 5, 6],
			"editor_fields": [
				{
					"label": "description:",
					"name": "description"
				},
				{
					"label": "abc:",
					"name": "c1"
				},
				{
					"label": "def:",
					"name": "c2"
				},
				{
					"label": "qqq:",
					"name": "c3"
				},
				{
					"label": "www:",
					"name": "c4"
				}
			]
		},
		"tasktypes": [
			{
				"idx": "1",
				"name": "Animation",
				"color": "#DE4E4E"
			},
			{
				"idx": "3",
				"name": "Comp",
				"color": "#FFD906"
			}
		],
		"row_span_columns": [1, 2, 3, 4],
		"row_task_count": [
			[1, 3],
			[2, 2]
		]
	}
}
```

---

## 8. 에셋 카테고리 진행 오버뷰 설정 수정 <a id="category-progress-overview-setting-update"></a>

### `POST /api/project/{project_idx}/category/progress/overview/setting/update`

### permission

- `permission.read_asset_task_overview`

### request

| param         | type  |  data   | required | desc            |
| ------------- | :---: | :-----: | :------: | --------------- |
| project_idx   | path  | integer |    O     |                 |
| setting_name  | query | string  |    O     | 'hidden_column' |
| setting_value | query | string  |    O     |                 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "설정이 저장됐습니다."
	},
	"data": null
}
```

---

## 9. 에셋 진행 오버뷰 조회 <a id="asset-progress-overview-read"></a>

### `GET /api/project/{project_idx}/category/{category_idx}/asset/progress/overview/read`

### permission

- `permission.read_asset_task_overview`

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
				"idx": "1",
				"name": "ch_bunny",
				"thumbnail": "/abc.png",
				"description": "Hero character",
				"asset_status": "wip",
				"used": "",
				"reference_path": "",
				"hdri_path": "",
				"source_path": "",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"artist": "c2m",
				"task_status": "wip",
				"last_version": "",
				"last_comment": "컨펌해 주세요",
				"last_publish": "",
				"last_publish_comment": "",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			},
			{
				"idx": "1",
				"name": "ch_bunny",
				"thumbnail": "/abc.png",
				"description": "Hero character",
				"asset_status": "wip",
				"used": "",
				"reference_path": "",
				"hdri_path": "",
				"source_path": "",
				"tasktype_name": "Animation",
				"start_date": "2019-04-05",
				"end_date": "2019-05-01",
				"artist": "c2m",
				"task_status": "wip",
				"last_version": "",
				"last_comment": "컨펌해 주세요",
				"last_publish": "",
				"last_publish_comment": "",
				"c1": null,
				"c2": null,
				"c3": null,
				"c4": null
			}
		],
		"config": {
			"hidden_columns": [5, 6],
			"columns": [
				{
					"title": "idx",
					"name": "idx",
					"data": "idx",
					"className": "idx dt-body-center",
					"searchable": false,
					"visible": false
				},
				{
					"title": "asset name",
					"name": "name",
					"data": "name",
					"className": "name dt-body-center",
					"visible": true
				},
				{
					"title": "description",
					"name": "description",
					"data": "description",
					"className": "description dt-body-center",
					"visible": true
				},
				{
					"title": "asset status",
					"name": "asset status",
					"data": "asset status",
					"className": "asset-status dt-body-center",
					"visible": true
				},
				{
					"title": "used",
					"name": "used",
					"data": "used",
					"className": "used dt-body-center",
					"visible": true
				},
				{
					"title": "reference path",
					"name": "reference_path",
					"data": "reference_path",
					"className": "reference_path dt-body-center",
					"visible": false
				},
				{
					"title": "hdri path",
					"name": "hdri_path",
					"data": "hdri_path",
					"className": "hdri-path dt-body-center",
					"visible": false
				},
				{
					"title": "source path",
					"name": "source_path",
					"data": "source_path",
					"className": "source_path dt-body-center",
					"visible": true
				},
				{
					"title": "tasktype",
					"name": "tasktype_name",
					"data": "tasktype_name",
					"className": "tasktype_name dt-body-center",
					"visible": true
				},
				{
					"title": "start date",
					"name": "start_date",
					"data": "start_date",
					"className": "start_date dt-body-center",
					"visible": true
				},
				{
					"title": "end date",
					"name": "end_date",
					"data": "end_date",
					"className": "end_date dt-body-center",
					"visible": true
				},
				{
					"title": "artist",
					"name": "artist",
					"data": "artist",
					"className": "artist dt-body-center",
					"visible": true
				},
				{
					"title": "task status",
					"name": "task status",
					"data": "task status",
					"className": "task-status dt-body-center",
					"visible": true
				}
			],
			"rows_group": [
				"idx:name",
				"name:name",
				"description:name",
				"c1:name",
				"c2:name",
				"c3:name",
				"c4:name"
			],
			"editable_columns": [2, 3, 4, 5, 6],
			"editor_fields": [
				{
					"label": "description:",
					"name": "description"
				},
				{
					"label": "abc:",
					"name": "c1"
				},
				{
					"label": "def:",
					"name": "c2"
				},
				{
					"label": "qqq:",
					"name": "c3"
				},
				{
					"label": "www:",
					"name": "c4"
				}
			]
		},
		"asset_statuses": [
			{
				"idx": "1",
				"name": "wip",
				"color": "#DE4E4E"
			}
		],
		"task_statuses": [
			{
				"idx": "1",
				"name": "wip",
				"color": "#DE4E4E"
			}
		],
		"tasktypes": [
			{
				"idx": "1",
				"name": "Animation",
				"color": "#DE4E4E"
			},
			{
				"idx": "3",
				"name": "Comp",
				"color": "#FFD906"
			}
		],
		"row_span_columns": [1, 2, 3, 4],
		"row_task_count": [
			[1, 3],
			[2, 2]
		]
	}
}
```

---

## 8. 에셋 카테고리 진행 오버뷰 설정 수정 <a id="asset-progress-overview-setting-update"></a>

### `POST /api/project/{project_idx}/category/{category_idx}/asset/progress/overview/setting/update`

### permission

- `permission.read_asset_task_overview`

### request

| param         | type  |  data   | required | desc            |
| ------------- | :---: | :-----: | :------: | --------------- |
| project_idx   | path  | integer |    O     |                 |
| category_idx  | path  | integer |    O     |                 |
| setting_name  | query | string  |    O     | 'hidden_column' |
| setting_value | query | string  |    O     |                 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "설정이 저장됐습니다."
	},
	"data": null
}
```

---

## 끝

[에피소드 진행 오버뷰 조회]: #episode-progress-overview-read
[에피소드 진행 오버뷰 설정 수정]: #episode-progress-overview-setting-update
[시퀀스 진행 오버뷰 조회]: #sequence-progress-overview-read
[시퀀스 진행 오버뷰 설정 수정]: #sequence-progress-overview-setting-update
[샷 진행 오버뷰 조회]: #shot-progress-overview-read
[에셋 카테고리 진행 오버뷰 조회]: #category-progress-overview-read
[에셋 카테고리 진행 오버뷰 설정 수정]: #category-progress-overview-setting-update
[에셋 진행 오버뷰 조회]: #asset-progress-overview-read
[에셋 진행 오버뷰 설정 수정]: #asset-progress-overview-setting-update
