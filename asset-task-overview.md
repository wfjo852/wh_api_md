# WH2API::AssetTaskOverview

## 목차

| 내용                                              | slug                                                                        | 서버 구현 | 웹 적용 |
| :------------------------------------------------ | :-------------------------------------------------------------------------- | :-------: | :-----: |
| 1. [에셋 태스크오버뷰의 모든 태스크 조회]         | /api/project/{project_idx}/asset/task/list                                  |    GET    |    O    |
| 2. [에셋 태스크오버뷰의 태스크 안 모든 속성 조회] | /api/project/{project_idx}/asset/task/property/list                         |    GET    |    O    |
| 3. [에셋 태스크오버뷰의 설정 컬럼 (에셋) 조회]    | /api/project/{project_idx}/asset/column/asset/list                          |     -     |    -    |
| 4. [에셋 태스크오버뷰의 설정 컬럼 (태스크) 조회]  | /api/project/{project_idx}/asset/column/task/list                           |     -     |    -    |
| 5. [에셋 태스크오버뷰의 설정 컬럼 3개 동시 조회]  | /api/project/{project_idx}/asset/column/list                                |    GET    |    O    |
| 6. [에셋 태스크오버뷰 조회]                       | /api/project/{project_idx}/asset/task/overview/read                         |    GET    |    O    |
|                                                   | /api/project/{project_idx}/category/{category_idx}/asset/task/overview/read |    GET    |    O    |
| 7. [에셋 태스크오버뷰 세팅 정보 항목별 조회]      | /api/project/{project_idx}/asset/task/overview/setting/{setting_name}/read  |    GET    |    X    |
| 8. [에셋 태스크오버뷰 세팅 정보 동시 조회]        | /api/project/{project_idx}/asset/task/overview/setting/read                 |    GET    |    O    |
| 9. [에셋 태스크오버뷰 세팅 정보 수정]             | /api/project/{project_idx}/asset/task/overview/setting/update               |   POST    |    O    |

- O\* - 3, 4번 동시 적용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에셋 태스크오버뷰의 모든 태스크 조회 <a id="project-asset-task-list"></a>

### `GET /api/project/{project_idx}/asset/task/list`

### permission

- `permission.read_asset_task_overview`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"task_list_in_project": [
			{
				"idx": "1",
				"name": "Animation"
			},
			{
				"idx": "2",
				"name": "Rendering"
			},
			{
				"idx": "3",
				"name": "Comp"
			}
		]
	}
}
```

---

## 2. 에셋 태스크오버뷰의 태스크 안 모든 속성 조회 <a id="project-asset-task-property-list"></a>

### `GET /api/project/{project_idx}/asset/task/property/list`

### permission

- `permission.read_asset_task_overview`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"property_per_task": [
			{
				"idx": "1",
				"name": "Status"
			},
			{
				"idx": "2",
				"name": "Description"
			},
			{
				"idx": "3",
				"name": "Publication"
			}
		]
	}
}
```

---

## 3. 에셋 태스크오버뷰의 설정 컬럼 (에셋) 조회 <a id="project-asset-column-asset-list"></a>

### `GET /api//project/{project_idx}/asset/column/asset/list`

### permission

- `permission.read_asset_task_overview`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"shot_column": [
			{
				"column": "description",
				"name": "Description",
				"visible": true
			},
			{
				"column": "asset_status",
				"name": "Status",
				"visible": true
			},
			{
				"column": "reference_path",
				"name": "Reference Path",
				"visible": true
			},
			{
				"column": "hdri_path",
				"name": "HDRI Path",
				"visible": true
			},
			{
				"column": "source_path",
				"name": "Source Path",
				"visible": true
			}
		]
	}
}
```

---

## 4. 에셋 태스크오버뷰의 설정 컬럼 (태스크) 조회 <a id="project-asset-column-task-list"></a>

### `GET /api//project/{project_idx}/asset/column/task/list`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"task_column": [
			{
				"column": "task_status",
				"name": "Status",
				"visible": true
			},
			{
				"column": "description",
				"name": "Description",
				"visible": true
			},
			{
				"column": "publish",
				"name": "Publish",
				"visible": true
			},
			{
				"column": "artist",
				"name": "Artist",
				"visible": true
			},
			{
				"column": "start_date",
				"name": "Start Date",
				"visible": true
			},
			{
				"column": "end_date",
				"name": "End Date",
				"visible": true
			},
			{
				"column": "duration",
				"name": "Duration",
				"visible": true
			}
		]
	}
}
```

---

## 5. 에셋 태스크오버뷰의 설정 컬럼 3개 동시 조회 <a id="project-asset-column-list"></a>

### `GET /api//project/{project_idx}/asset/column/list`

### permission

- `permission.read_asset_task_overview`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"shot_column": [
			{
				"column": "description",
				"name": "Description",
				"visible": true
			},
			{
				"column": "asset_status_name",
				"name": "Status",
				"visible": true
			},
			{
				"column": "reference_path",
				"name": "Reference Path",
				"visible": true
			},
			{
				"column": "hdri_path",
				"name": "HDRI Path",
				"visible": true
			},
			{
				"column": "source_path",
				"name": "Source Path",
				"visible": true
			}
		],
		"task_column": [
			{
				"idx": 1,
				"column": "task_status_name",
				"name": "Status",
				"visible": true
			},
			{
				"idx": 2,
				"column": "description",
				"name": "Description",
				"visible": true
			},
			{
				"idx": 3,
				"column": "pub",
				"name": "Pub",
				"visible": true
			},
			{
				"idx": 4,
				"column": "artist",
				"name": "Artist",
				"visible": true
			},
			{
				"idx": 5,
				"column": "start_date",
				"name": "Start Date",
				"visible": true
			},
			{
				"idx": 6,
				"column": "end_date",
				"name": "End Date",
				"visible": true
			},
			{
				"idx": 7,
				"column": "duration",
				"name": "Duration",
				"visible": true
			}
		]
	}
}
```

---

## 6. 에셋 태스크오버뷰 조회 (/api//project/{project_idx}/asset/task/overview/read) <a id="project-asset-task-overview-read"></a>

### `GET /api//project/{project_idx}/asset/task/overview/read`

### `GET /api/project/{project_idx}/category/{category_idx}/asset/task/overview/read`

### permission

- `permission.read_asset_task_overview`

### request

| param        | type  |  data   | required | desc |
| ------------ | :---: | :-----: | :------: | ---- |
| category_idx | query | integer |    X     |      |
| search_type  | query | string  |    X     |      |
| keyword      | query | string  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"project_name": "Demo_Bigbuck_Bunny",
		"category_name": "Animal",
		"overview": [
			{
				"asset_idx": "4",
				"asset_order": 1,
				"category_name": "Category 1",
				"asset_name": "AssetName 0001",
				"asset_thumbnail": "ddd.jpg",
				"description": "설명입니다.",
				"asset_status_name": "Waiting",
				"reference_path": "",
				"hdri_path": "",
				"source_path": "",
				"animation_summary": "Waiting, Artist 0001, V.002, 1", //aniStatus, aniArtist, aniPublish의 값을 합쳐놓은 요약
				"animation_status": "Waiting",
				"animation_desc": "Lorem ipsum dolor sit amet,",
				"animation_publish": "V.002",
				"animation_artist": "artist 0001",
				"animation_start_date": "2018-01-02",
				"animation_end_date": "2018-08-08",
				"rendering_summary": "ing, Artist 0002, V.003, 1",
				"rendering_status": "ing",
				"renderting_description": "ing",
				"rendering_publish": "V.003",
				"rendering_artist": "Artist 0002",
				"rendering_start_date": "2018-01-02",
				"rendering_end_date": "2018-01-02",
				"comp_summary": "",
				"comp_status": "Waiting",
				"comp_publish": "V.001",
				"comp_artist": "Artist 0005",
				"comp_start_date": "2018-01-02",
				"comp_end_date": "2018-08-08"
			}
		],
		"setting_column": [
			{
				"data": "asset_idx",
				"type": "numeric",
				"width": 50,
				"editor": false
			},
			{
				"data": "asset_order",
				"type": "text",
				"width": 20,
				"editor": false
			},
			{
				"data": "category_name",
				"type": "text",
				"width": 100,
				"editor": false
			},
			{
				"data": "asset_name",
				"type": "text",
				"width": 180,
				"editor": false
			},
			{
				"data": "asset_thumbnail",
				"renderer": "renderAssetThumbnail",
				"type": "text",
				"width": 180,
				"editor": false
			},
			{
				"data": "description",
				"type": "text",
				"width": 536
			},
			{
				"data": "asset_status_name",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["wip", "confirm", "retake", "pub", "final"],
				"renderer": "renderStatus",
				"width": 120
			},
			{
				"data": "reference_path",
				"type": "text",
				"width": 250
			},
			{
				"data": "reference_path",
				"type": "text",
				"width": 250
			},
			{
				"data": "hdri_path",
				"type": "text",
				"width": 250
			},
			{
				"data": "source_path",
				"type": "text",
				"width": 250
			},
			{
				"data": "animation_summary",
				"type": "text",
				"width": 250,
				"renderer": "renderAnimationSummary"
			},
			{
				"data": "animation_status",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["wip", "confirm", "retake", "pub", "final"],
				"renderer": "renderStatus",
				"width": 120
			},
			{
				"data": "animation_desc",
				"type": "text"
			},
			{
				"data": "animation_publish",
				"type": "text"
			},
			{
				"data": "animation_artist",
				"type": "dropdown",
				"allowInvalid": false,
				"source": [
					"사람이름1",
					"사람이름2",
					"사람이름3",
					"사람이름4",
					"사람이름5"
				]
			},
			{
				"data": "animation_start_date",
				"type": "date",
				"dateFormat": "dateType"
			},
			{
				"data": "animation_end_date",
				"type": "date",
				"dateFormat": "dateType"
			},
			{
				"data": "rendering_summary",
				"type": "text",
				"width": 250,
				"renderer": "renderAnimationSummary"
			},
			{
				"data": "rendering_status",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["wip", "confirm", "retake", "pub", "final"],
				"renderer": "renderStatus",
				"width": 120
			},
			{
				"data": "rendering_desc",
				"type": "text"
			},
			{
				"data": "rendering_publish",
				"type": "text"
			},
			{
				"data": "rendering_artist",
				"type": "dropdown",
				"allowInvalid": false,
				"source": [
					"사람이름1",
					"사람이름2",
					"사람이름3",
					"사람이름4",
					"사람이름5"
				]
			},
			{
				"data": "rendering_start_date",
				"type": "date",
				"dateFormat": "dateType"
			},
			{
				"data": "rendering_end_date",
				"type": "date",
				"dateFormat": "dateType"
			},
			{
				"data": "comp_summary",
				"type": "text",
				"width": 250,
				"renderer": "renderAnimationSummary"
			},
			{
				"data": "comp_status",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["wip", "confirm", "retake", "pub", "final"],
				"renderer": "renderStatus",
				"width": 120
			},
			{
				"data": "comp_desc",
				"type": "text"
			},
			{
				"data": "comp_publish",
				"type": "text"
			},
			{
				"data": "comp_artist",
				"type": "dropdown",
				"allowInvalid": false,
				"source": [
					"사람이름1",
					"사람이름2",
					"사람이름3",
					"사람이름4",
					"사람이름5"
				]
			},
			{
				"data": "comp_start_date",
				"type": "date",
				"dateFormat": "dateType"
			},
			{
				"data": "comp_end_date",
				"type": "date",
				"dateFormat": "dateType"
			}
		],
		"collapsible_columns": [
			{
				"row": -2,
				"col": 1,
				"collapsible": true
			},
			{
				"row": -2,
				"col": 8,
				"collapsible": true
			},
			{
				"row": -2,
				"col": 15,
				"collapsible": true
			},
			{
				"row": -2,
				"col": 22,
				"collapsible": true
			}
		],
		"nested_headers": [
			[
				"CutOrder",
				"Category",
				{
					"label": "Assets",
					"colspan": 7
				},
				{
					"label": "Animation",
					"colspan": 7
				},
				{
					"label": "Rendering",
					"colspan": 7
				}
			],
			[
				"",
				"Category Name",
				"Asset Name",
				"Snapshot",
				"Description",
				"Status",
				"Reference Path",
				"HDRI Path",
				"Source Path",
				"Summary",
				"Status",
				"Description",
				"Publish",
				"Artist",
				"Start Date",
				"End date",
				"Summary",
				"Status",
				"Description",
				"Publish",
				"Artist",
				"Start Date",
				"End date",
				"Summary",
				"Status",
				"Description",
				"Publish",
				"Artist",
				"Start Date",
				"End date"
			]
		]
	}
}
```

- 모든 태스크들에 있는 duration 값은 샷의 '태스크 할당'에서 입력하는 값(실수)을 가져옴
  _ http://localhost/project/abc/shot/task/add (샷의 태스크 할당)
  _ 태스크 할당에서 입력한 값에 소수점이 있을 경우 올림해서 정수로 표기함
- 태스크 헤더에는 태스크의 color가 표기되어야 함

---

## 7. 에셋 태스크오버뷰 세팅 정보 항목별 조회 <a id="project-asset-task-overview-setting-column-read"></a>

### `GET /api/project/{project_idx}/asset/task/overview/setting/{setting_name}/read`

### permission

- `permission.read_asset_task_overview`

### request

| param        | type  |  data   | required | desc                                                                            |
| ------------ | :---: | :-----: | :------: | ------------------------------------------------------------------------------- |
| project_idx  | path  | integer |    O     |                                                                                 |
| setting_name | query | string  |    O     | asset_column, asset_custom_column, asset_task_column, task_asset, summary_asset |

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

- 어떤 세팅값인지에 따라 `data`의 내용이 다르게 내려옴

---

## 8. 에셋 태스크오버뷰 세팅 정보 동시 조회 <a id="project-asset-task-overview-setting-read"></a>

### `GET /api/project/{project_idx}/asset/task/overview/setting/read`

### permission

- `permission.read_asset_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

- `setting_name` 값이 `all` 인 경우에는 6개의 모든 값을 다 묶어서 조회함.

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

- 어떤 세팅값인지에 따라 `data`의 내용이 다르게 내려옴

---

## 9. 에셋 태스크오버뷰 세팅 정보 수정 <a id="project-asset-task-overview-setting-update"></a>

### `POST /api/project/{project_idx}/asset/task/overview/setting/update`

### permission

- `permission.read_shot_task_overview`

### request

| param         | type  |  data   | required | desc                                                                            |
| ------------- | :---: | :-----: | :------: | ------------------------------------------------------------------------------- |
| project_idx   | path  | integer |    O     |                                                                                 |
| setting_name  | query | string  |    O     | asset_column, asset_custom_column, asset_task_column, task_asset, summary_asset |
| setting_value | query | string  |    O     |                                                                                 |

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

[에셋 태스크오버뷰의 모든 태스크 조회]: #project-asset-task-list
[에셋 태스크오버뷰의 태스크 안 모든 속성 조회]: #project-asset-task-property-list
[에셋 태스크오버뷰의 설정 컬럼 (에셋) 조회]: #project-asset-column-asset-list
[에셋 태스크오버뷰의 설정 컬럼 (태스크) 조회]: #project-asset-column-task-list
[에셋 태스크오버뷰의 설정 컬럼 3개 동시 조회]: #project-asset-column-list
[에셋 태스크오버뷰 조회]: #project-asset-task-overview-read
[에셋 태스크오버뷰 세팅 정보 항목별 조회]: #project-asset-task-overview-setting-column-read
[에셋 태스크오버뷰 세팅 정보 동시 조회]: #project-asset-task-overview-setting-read
[에셋 태스크오버뷰 세팅 정보 수정]: #project-asset-task-overview-setting-update
