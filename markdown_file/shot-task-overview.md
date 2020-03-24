# WH2API::ShotTaskOverview

## 목차

| 내용                                            | slug                                                                      | 서버 구현 | 웹 적용 |
| :---------------------------------------------- | :------------------------------------------------------------------------ | :-------: | :-----: |
| 1. [샷 태스크오버뷰의 모든 태스크 조회]         | /api/project/{project_idx}/shot/task/list                                 |    GET    |    O    |
| 2. [샷 태스크오버뷰의 태스크 안 모든 속성 조회] | /api/project/{project_idx}/shot/task/property/list                        |    GET    |    O    |
| 3. [샷 태스크오버뷰의 설정 컬럼 (샷) 조회]      | /api/project/{project_idx}/shot/column/shot/list                          |    GET    |    -    |
| 4. [샷 태스크오버뷰의 설정 컬럼 (카메라) 조회]  | /api/project/{project_idx}/shot/column/camera/list                        |    GET    |    -    |
| 5. [샷 태스크오버뷰의 설정 컬럼 (태스크) 조회]  | /api/project/{project_idx}/shot/column/task/list                          |    GET    |    -    |
| 6. [샷 태스크오버뷰의 설정 컬럼 4개 동시 조회]  | /api/project/{project_idx}/shot/column/list                               |    GET    |   O\*   |
| 7. [샷 태스크오버뷰 조회]                       | /api/project/{project_idx}/shot/task/overview/read                        |    GET    |    O    |
|                                                 | /api/project/{project_idx}/episode/{episode_idx}/shot/task/overview/read  |    GET    |    O    |
| 8. [샷 태스크오버뷰 세팅 정보 항목별 조회]      | /api/project/{project_idx}/shot/task/overview/setting/{setting_name}/read |    GET    |    X    |
| 9. [샷 태스크오버뷰 세팅 정보 동시 조회]        | /api/project/{project_idx}/shot/task/overview/setting/read                |    GET    |    O    |
| 10. [샷 태스크오버뷰 세팅 정보 수정]            | /api/project/{project_idx}/shot/task/overview/setting/update              |   POST    |    X    |

- O\* - 3, 4, 5번 동시 적용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 샷 태스크오버뷰의 모든 태스크 조회 <a id="project-shot-task-list"></a>

### `GET /api/project/{project_idx}/shot/task/list`

### permission

- `permission.read_shot_task_overview`

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
				"name": "Simulation"
			}
		]
	}
}
```

---

## 2. 샷 태스크오버뷰의 태스크 안 모든 속성 조회 <a id="project-shot-task-property-list"></a>

### `GET /api/project/{project_idx}/shot/task/property/list`

### permission

- `permission.read_shot_task_overview`

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

## 3. 샷 태스크오버뷰의 설정 컬럼 (샷) 조회 <a id="project-shot-column-shot-list"></a>

### `GET /api/project/{project_idx}/shot/column/shot/list`

### permission

- `permission.read_shot_task_overview`

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
				"column": "shot_status_name",
				"name": "Status",
				"visible": true
			},
			{
				"column": "location",
				"name": "Location",
				"visible": true
			},
			{
				"column": "note",
				"name": "Direction Note",
				"visible": true
			},
			{
				"column": "length",
				"name": "Length",
				"visible": true
			},
			{
				"column": "handle_in",
				"name": "Handle In",
				"visible": true
			},
			{
				"column": "handle_out",
				"name": "Handle Out",
				"visible": true
			},
			{
				"column": "frame_in",
				"name": "Frame In",
				"visible": true
			},
			{
				"column": "frame_out",
				"name": "Frame Out",
				"visible": true
			},
			{
				"column": "importance",
				"name": "Importance",
				"visible": true
			},
			{
				"column": "difficulty",
				"name": "Level",
				"visible": true
			},
			{
				"column": "original_path",
				"name": "Original Edit Path",
				"visible": true
			}
		]
	}
}
```

---

## 4. 샷 태스크오버뷰의 설정 컬럼 (카메라) 조회 <a id="project-shot-column-camera-list"></a>

### `GET /api/project/{project_idx}/shot/column/camera/list`

### permission

- `permission.read_shot_task_overview`

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
		"camera_column": [
			{
				"column": "camera_clip",
				"name": "Camera Clip",
				"visible": true
			},
			{
				"column": "camera_name",
				"name": "Camera Name",
				"visible": true
			},
			{
				"column": "lens_type",
				"name": "Lens Type",
				"visible": true
			},
			{
				"column": "focal_length",
				"name": "Focal Length",
				"visible": true
			},
			{
				"column": "grip",
				"name": "Grip",
				"visible": true
			},
			{
				"column": "camera_filter",
				"name": "Filter",
				"visible": true
			},
			{
				"column": "iso",
				"name": "ISO",
				"visible": true
			},
			{
				"column": "shutter_speed",
				"name": "Shutter Speed",
				"visible": true
			},
			{
				"column": "f_stop",
				"name": "F-Stop",
				"visible": true
			},
			{
				"column": "stereo_type",
				"name": "Stereo Type",
				"visible": true
			},
			{
				"column": "stereo_iod",
				"name": "Stereo IOD",
				"visible": true
			},
			{
				"column": "stereo_rig",
				"name": "Stereo Rig",
				"visible": true
			},
			{
				"column": "stereo_dof",
				"name": "Stereo DOF",
				"visible": true
			},
			{
				"column": "camera_note",
				"name": "Note",
				"visible": true
			}
		]
	}
}
```

---

## 5. 샷 태스크오버뷰의 설정 컬럼 (태스크) 조회 <a id="project-shot-column-task-list"></a>

### `GET /api/project/{project_idx}/shot/column/task/list`

### permission

- `permission.read_shot_task_overview`

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

## 6. 샷 태스크오버뷰의 설정 컬럼 4개 동시 조회 <a id="project-shot-column-list"></a>

### `GET /api/project/{project_idx}/shot/column/list`

### permission

- `permission.read_shot_task_overview`

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
				"column": "shot_status",
				"name": "Status",
				"visible": true
			},
			{
				"column": "location",
				"name": "Location",
				"visible": true
			},
			{
				"column": "note",
				"name": "Direction Note",
				"visible": true
			},
			{
				"column": "length",
				"name": "Length",
				"visible": true
			},
			{
				"column": "handle_in",
				"name": "Handle In",
				"visible": true
			},
			{
				"column": "handle_out",
				"name": "Handle Out",
				"visible": true
			},
			{
				"column": "frame_in",
				"name": "Frame In",
				"visible": true
			},
			{
				"column": "frame_out",
				"name": "Frame Out",
				"visible": true
			},
			{
				"column": "importance",
				"name": "Importance",
				"visible": true
			},
			{
				"column": "difficulty",
				"name": "Level",
				"visible": true
			},
			{
				"column": "original_path",
				"name": "Original Edit Path",
				"visible": true
			}
		],
		"camera_column": [
			{
				"column": "camera_clip",
				"name": "Camera Clip",
				"visible": true
			},
			{
				"column": "camera_name",
				"name": "Camera Name",
				"visible": true
			},
			{
				"column": "lens_type",
				"name": "Lens Type",
				"visible": true
			},
			{
				"column": "focal_length",
				"name": "Focal Length",
				"visible": true
			},
			{
				"column": "grip",
				"name": "Grip",
				"visible": true
			},
			{
				"column": "camera_filter",
				"name": "Filter",
				"visible": true
			},
			{
				"column": "iso",
				"name": "ISO",
				"visible": true
			},
			{
				"column": "shutter_speed",
				"name": "Shutter Speed",
				"visible": true
			},
			{
				"column": "f_stop",
				"name": "F-Stop",
				"visible": true
			},
			{
				"column": "stereo_type",
				"name": "Stereo Type",
				"visible": true
			},
			{
				"column": "stereo_iod",
				"name": "Stereo IOD",
				"visible": true
			},
			{
				"column": "stereo_rig",
				"name": "Stereo Rig",
				"visible": true
			},
			{
				"column": "stereo_dof",
				"name": "Stereo DOF",
				"visible": true
			},
			{
				"column": "camera_note",
				"name": "Note",
				"visible": true
			}
		],
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

## 7. 샷 태스크오버뷰 조회 <a id="project-shot-task-overview-read"></a>

- /api/project/{project_idx}/shot/task/overview/read
- /api/project/{project_idx}/episode/{episode_idx}/shot/task/overview/read

### `GET /api/project/{project_idx}/shot/task/overview/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| episode_idx | path  | integer |    X     |      |
| search_type | query | string  |    X     |      |
| keyword     | query | string  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"project_name": "Demo_Bigbuck_Bunny",
		"episode_name": "Ep1",
		"overview": [
			{
				"shot_idx": "4",
				"shot_name": "s0010_c0010",
				"shot_order": "1",
				"shot_thumbnail": null,
				"episode_idx": "1",
				"episode_name": "ep01",
				"sequence_idx": "1",
				"sequence_name": "s0010",
				"description": "> Comp : 1 GATE \ud569\uc131 / \ube44 \ucd94\uac00",
				"shot_status_name": "wip",
				"location": "\ucc3b\uc9d1",
				"note": "\uc194\ub8e8\uc158 \ub17c\uc758 \ud544\uc694",
				"length": "220",
				"handle_in": "3",
				"handle_out": "3",
				"frame_in": "438",
				"frame_out": "644",
				"timecode_in": "2:41:41:21",
				"timecode_out": "2:41:43:06",
				"importance": "1",
				"difficulty": "S",
				"original_path": "E:\uffe6Park_doc\uffe6wormhole\uffe6Test_shot\uffe601.plates0010_c0010_plate_v001.mp4",
				"camera_clip": "A201_L011_0706SK",
				"camera_name": "RED",
				"lens_type": null,
				"focal_length": "18mm",
				"grip": null,
				"camera_filter": "ND-8",
				"iso": "200",
				"shutter_speed": "1/48",
				"f_stop": "f 1.4",
				"stereo_type": "convergence",
				"stereo_iod": null,
				"stereo_converged_point": "1.2m",
				"stereo_rig": "\uc9c1\uad50\ub9ac\uadf8",
				"camera_note": "\uce74\uba54\ub77c \ub178\ud2b8",
				"tasks": {
					"Animation": {
						"tasktype_idx": "1",
						"tasktype_name": "Animation",
						"tasktype_color": "#DE4E4E",
						"user_id": "c2m",
						"artist": "cccc",
						"pub": null,
						"start_date": "2019-01-01",
						"end_date": "2019-01-31",
						"duration": "0",
						"description": null,
						"task_status_name": "wip",
						"is_on": 1
					}
				}
			}
		],
		"setting_column": [
			{
				"data": "shot_idx",
				"type": "numeric",
				"width": 50,
				"editor": false
			},
			{
				"data": "shot_order",
				"type": "text",
				"width": 50,
				"editor": false
			},
			{
				"data": "episode_name",
				"type": "text",
				"width": 120,
				"editor": false
			},
			{
				"data": "sequence_name",
				"type": "text",
				"width": 120,
				"editor": false
			},
			{
				"data": "shot_name",
				"type": "text",
				"width": 180,
				"editor": false
			},
			{
				"data": "shot_thumbnail",
				"renderer": "renderShotThumbnail",
				"width": 84
			},
			{
				"data": "description",
				"type": "text",
				"width": 190
			},
			{
				"data": "shot_status_name",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["wip", "confirm", "retake", "pub", "final"],
				"renderer": "renderStatus",
				"width": 120
			},
			{
				"data": "location",
				"type": "text",
				"width": 120
			},
			{
				"data": "note",
				"type": "text",
				"width": 160
			},
			{
				"data": "length",
				"renderer": "renderLength",
				"type": "text",
				"width": 85
			},
			{
				"data": "handle_in",
				"type": "text",
				"width": 95
			},
			{
				"data": "handle_out",
				"type": "text",
				"width": 95
			},
			{
				"data": "frame_in",
				"type": "text",
				"width": 90
			},
			{
				"data": "frame_out",
				"type": "text",
				"width": 90
			},
			{
				"data": "timecode_in",
				"type": "text",
				"width": 130
			},
			{
				"data": "timecode_out",
				"type": "text",
				"width": 130
			},
			{
				"data": "importance",
				"type": "text",
				"width": 110
			},
			{
				"data": "difficulty",
				"type": "text",
				"width": 80
			},
			{
				"data": "original_path",
				"type": "text",
				"width": 430
			},
			{
				"data": "camera_clip",
				"type": "text",
				"width": 150
			},
			{
				"data": "camera_name",
				"type": "text",
				"width": 125
			},
			{
				"data": "lens_type",
				"type": "text",
				"width": 125
			},
			{
				"data": "focal_length",
				"type": "text",
				"width": 130
			},
			{
				"data": "grip",
				"type": "text"
			},
			{
				"data": "camera_filter",
				"type": "text"
			},
			{
				"data": "iso",
				"type": "text"
			},
			{
				"data": "shutter_speed",
				"type": "text",
				"width": 150
			},
			{
				"data": "f_stop",
				"type": "text",
				"width": 150
			},
			{
				"data": "stereo_type",
				"type": "text",
				"width": 120
			},
			{
				"data": "stereo_iod",
				"type": "text",
				"width": 100
			},
			{
				"data": "stereo_converged_point",
				"type": "text",
				"width": 180
			},
			{
				"data": "stereo_rig",
				"type": "text",
				"width": 100
			},
			{
				"data": "stereo_dof",
				"type": "text",
				"width": 100
			},
			{
				"data": "camera_note",
				"type": "text",
				"width": 100
			},
			{
				"data": "tasks.Animation.summary",
				"renderer": "renderSummary",
				"readOnly": true,
				"width": 120
			},
			{
				"data": "tasks.Animation.task_status_name",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["wip", "confirm", "pub", "final"],
				"renderer": "renderStatus",
				"width": 120
			},
			{
				"data": "tasks.Animation.description",
				"type": "text",
				"width": 120
			},
			{
				"data": "tasks.Animation.pub",
				"type": "text",
				"editor": false,
				"width": 120
			},
			{
				"data": "tasks.Animation.artist",
				"type": "dropdown",
				"allowInvalid": false,
				"source": ["cccc", "111-222-3333", "002-11-21-2"],
				"width": 120
			},
			{
				"data": "tasks.Animation.start_date",
				"renderer": "renderStartDate",
				"type": "date",
				"dateFormat": "YYYY-MM-DD",
				"width": 120
			},
			{
				"data": "tasks.Animation.end_date",
				"renderer": "renderEndDate",
				"type": "date",
				"dateFormat": "YYYY-MM-DD",
				"width": 120
			},
			{
				"data": "tasks.Animation.duration",
				"renderer": "renderDuration",
				"type": "text",
				"width": 100
			}
		],
		"collapsible_columns": [
			{
				"row": -2,
				"col": 4,
				"collapsible": true
			},
			{
				"row": -2,
				"col": 20,
				"collapsible": true
			},
			{
				"row": -2,
				"col": 35,
				"collapsible": true
			}
		],
		"nested_headers": [
			[
				"Idx",
				"Order",
				"Episode",
				"Sequence",
				{
					"label": "Shots",
					"colspan": 16
				},
				{
					"label": "Camera",
					"colspan": 15
				},
				{
					"label": "Animation",
					"colspan": 8
				}
			],
			[
				"-",
				"-",
				"Name",
				"Name",
				"Shot Name",
				"Thumbnail",
				"Description",
				"Status",
				"Location",
				"Direction Note",
				"Length",
				"Handle In",
				"Handle Out",
				"Frame In",
				"Frame Out",
				"Timecode In",
				"Timecode Out",
				"Importance",
				"Level",
				"Original Edit Path",
				"Camera Clip",
				"Camera Name",
				"Lens Type",
				"Focal Length",
				"Grip",
				"Filter",
				"ISO",
				"Shutter Speed",
				"F-Stop",
				"Stereo Type",
				"Stereo IOD",
				"Stereo Converged Point",
				"Stereo Rig",
				"Stereo DOF",
				"Note",
				"Summary",
				"Status",
				"Description",
				"Pub",
				"Artist",
				"Start Date",
				"End Date",
				"Duration"
			]
		]
	}
}
```

- 모든 태스크들에 있는 duration 값은 샷의 '태스크 할당'에서 입력하는 값(실수)을 가져옴
  - http://localhost/project/abc/shot/task/add (샷의 태스크 할당)
  - 태스크 할당에서 입력한 값에 소수점이 있을 경우 올림해서 정수로 표기함
- 태스크 헤더에는 태스크의 color가 표기되어야 함

---

## 8. 샷 태스크오버뷰 세팅 정보 항목별 조회 <a id="project-shot-task-overview-setting-column-read"></a>

### `GET /api/project/{project_idx}/shot/task/overview/setting/{setting_name}/read`

### permission

- `permission.read_shot_task_overview`

### request

| param        | type  |  data   | required | desc                                                                                      |
| ------------ | :---: | :-----: | :------: | ----------------------------------------------------------------------------------------- |
| project_idx  | path  | integer |    O     |                                                                                           |
| setting_name | query | string  |    O     | shot_column, camera_column, shot_custom_column, shot_task_column, task_shot, summary_shot |

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

## 9. 샷 태스크오버뷰 세팅 정보 동시 조회 <a id="project-shot-task-overview-setting-read"></a>

### `GET /api/project/{project_idx}/shot/task/overview/setting/read`

### permission

- `permission.read_shot_task_overview`

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

## 10. 샷 태스크오버뷰 세팅 정보 수정 <a id="project-shot-task-overview-setting-update"></a>

### `POST /api/project/{project_idx}/shot/task/overview/setting/update`

### permission

- `permission.read_shot_task_overview`

### request

| param         | type  |  data   | required | desc                                                                                      |
| ------------- | :---: | :-----: | :------: | ----------------------------------------------------------------------------------------- |
| project_idx   | path  | integer |    O     |                                                                                           |
| setting_name  | query | string  |    O     | shot_column, camera_column, shot_custom_column, shot_task_column, task_shot, summary_shot |
| setting_value | query | string  |    O     |                                                                                           |

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

[샷 태스크오버뷰의 모든 태스크 조회]: #project-shot-task-list
[샷 태스크오버뷰의 태스크 안 모든 속성 조회]: #project-shot-task-property-list
[샷 태스크오버뷰의 설정 컬럼 (샷) 조회]: #project-shot-column-shot-list
[샷 태스크오버뷰의 설정 컬럼 (카메라) 조회]: #project-shot-column-camera-list
[샷 태스크오버뷰의 설정 컬럼 (태스크) 조회]: #project-shot-column-task-list
[샷 태스크오버뷰의 설정 컬럼 4개 동시 조회]: #project-shot-column-list
[샷 태스크오버뷰 조회]: #project-shot-task-overview-read
[샷 태스크오버뷰 세팅 정보 항목별 조회]: #project-shot-task-overview-setting-column-read
[샷 태스크오버뷰 세팅 정보 동시 조회]: #project-shot-task-overview-setting-read
[샷 태스크오버뷰 세팅 정보 수정]: #project-shot-task-overview-setting-update
