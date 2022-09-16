# WH2API::Ganntt

## 목차

| 내용                            | slug                                                                                                        | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------- | :-------: | :-----: | :--: | :--: |
| 1. [샷 에피소드 조회]           | /api/project/{project_idx}/episode/{episode_idx}/gantt/read                                                 |    GET    |    O    |  -   |  -   |
| 2. [샷 시퀀스 조회]             | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/gantt/read                         |    GET    |    O    |  -   |  -   |
| 3. [샷 태스크 조회]             | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/tasktype/{tasktype_idx}/gantt/read |    GET    |    O    |  -   |  -   |
| 4. [에셋 카테고리 조회]         | /api/project/{project_idx}/category/{category_idx}/gantt/read                                               |    GET    |    O    |  -   |  -   |
| 5. [에셋 태스크 조회]           | /api/project/{project_idx}/category/{category_idx}/tasktype/{tasktype_idx}/gantt/read                       |    GET    |    O    |  -   |  -   |
| 6. [샷 태스크 일정 정보 저장]   | /api/project/{project_idx}/gantt/shot/task/update                                                           |   POST    |    O    |  -   |  -   |
| 7. [에셋 태스크 일정 정보 저장] | /api/project/{project_idx}/gantt/asset/task/update                                                          |   POST    |    O    |  -   |  -   |

- O\* - 뷰에 직접 구현
- O\*\* - api 없이 콘트롤러에 직접 구현

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 샷 에피소드 조회 <a id="gantt-episode-read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/gantt/read`

### permission

- `permission.read_gantt`

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
		"panel_data": [
			{
				"sequence_idx": 1,
				"name": "s0010(시퀀스 이름)",
				"duration": 3
			},
			{
				"sequence_idx": 2,
				"name": "s0020(시퀀스 이름)",
				"duration": 4
			},
			{
				"sequence_idx": 3,
				"name": "s0020(시퀀스 이름)",
				"duration": 5
			}
		],
		"gantt_data": [
			{
				"sequence_idx": 1,
				"name": "s0010",
				"progress": 20,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"sequence_idx": 1,
				"name": "s0020",
				"progress": 30,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"sequence_idx": 1,
				"name": "s0030",
				"progress": 40,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			}
		]
	}
}
```

---

## 2. 샷 시퀀스 조회 <a id="gantt-sequence-read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/gantt/read`

### permission

- `permission.read_gantt`

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
		"panel_data": [
			{
				"shot_idx": 1,
				"name": "s0010_c0010(샷 이름)",
				"tasks": [
					{
						"task_idx": 1,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Animation"
					},
					{
						"task_idx": 2,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Comp"
					},
					{
						"task_idx": 3,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Render"
					}
				]
			}
		],
		"gantt_data": [
			{
				"shot_idx": 1,
				"task_idx": 1,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 20,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"shot_idx": 1,
				"task_idx": 2,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 30,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"shot_idx": 1,
				"task_idx": 3,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 40,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			}
		]
	}
}
```

---

## 3. 샷 태스크 조회 <a id="gantt-shot-task-read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/tasktype/{tasktype_idx}/gantt/read`

### permission

- `permission.read_gantt`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |
| tasktype_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"panel_data": [
			{
				"shot_idx": 1,
				"name": "s0010_c0010(샷 이름)",
				"tasks": [
					{
						"task_idx": 1,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Animation"
					},
					{
						"task_idx": 2,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Comp"
					},
					{
						"task_idx": 3,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Render"
					}
				]
			}
		],
		"gantt_data": [
			{
				"shot_idx": 1,
				"task_idx": 1,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 20,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"shot_idx": 1,
				"task_idx": 2,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 30,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"shot_idx": 1,
				"task_idx": 3,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 40,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			}
		]
	}
}
```

---

## 4. 에셋 카테고리 조회 <a id="gantt-category-read"></a>

### `GET /api/project/{project_idx}/category/{category_idx}/gantt/read`

### permission

- `permission.read_gantt`

### request

| param        | type |  data   | required | desc                            |
| ------------ | :--: | :-----: | :------: | ------------------------------- |
| project_idx  | path | integer |    O     |                                 |
| category_idx | path | integer |    O     | 모든 카테고리를 조회할 때는 `0` |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"panel_data": [
			{
				"asset_idx": 1,
				"name": "ch_bunny (카테고리이름)",
				"tasks": [
					{
						"task_idx": 1,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Modeling"
					},
					{
						"task_idx": 2,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Texture"
					}
				]
			}
		],
		"gantt_data": [
			{
				"asset_idx": 1,
				"task_idx": 1,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 20,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"asset_idx": 1,
				"task_idx": 2,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 30,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			}
		]
	}
}
```

---

## 5. 에셋 태스크 조회 <a id="gantt-asset-task-read"></a>

### `GET /api/project/{project_idx}/category/{category_idx}/tasktype/{tasktype_idx}/gantt/read`

### permission

- `permission.read_gantt`

### request

| param        | type |  data   | required | desc                            |
| ------------ | :--: | :-----: | :------: | ------------------------------- |
| project_idx  | path | integer |    O     |                                 |
| category_idx | path | integer |    O     | 모든 카테고리를 조회할 때는 `0` |
| tasktype_idx | path | integer |    O     |                                 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"panel_data": [
			{
				"asset_idx": 1,
				"name": "ch_bunny (카테고리이름)",
				"tasks": [
					{
						"task_idx": 1,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Modeling"
					},
					{
						"task_idx": 2,
						"duration": 3,
						"start_date": "2019-10-08",
						"end_date": "2019-10-11",
						"task_name": "Texture"
					}
				]
			}
		],
		"gantt_data": [
			{
				"asset_idx": 1,
				"task_idx": 1,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 20,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			},
			{
				"asset_idx": 1,
				"task_idx": 2,
				"artist_name": "아티스트 이름",
				"status_name": "status 이름",
				"status_color": "#ddeeff",
				"tasktype_color": "#aabbcc",
				"progress": 30,
				"start_date": "2019-10-08",
				"end_date": "2019-10-11"
			}
		]
	}
}
```

---

## 6. 샷 태스크 스케쥴 정보 저장 <a id="gantt-shot-task-update"</a>

### `POST /api/project/{project_idx}/gantt/shot/task/update`

### permission

- `permission.update_gantt`

### request

| param        | type  |       data       | required | desc       |
| ------------ | :---: | :--------------: | :------: | ---------- |
| project_idx  | path  |     integer      |    O     |            |
| task_idx[]   | query | array of integer |    O     |            |
| start_date[] | query |  array of date   |    O     | YYYY-MM-DD |
| end_date[]   | query |  array of date   |    O     | YYYY-MM-DD |

### response

```json
{
	"error": {
		"code": 200,
		"message": "일정이 수정됐습니다."
	},
	"data": null
}
```

- 듀레이션 값은 start와 end 날짜 값을 계산해서 디비에 넣어주세요.
- 제가 보내는 듀레이션값은 정확하지 않습니다.

---

## 7. 에셋 태스크 스케쥴 정보 저장 <a id="gantt-asset-task-update"></a>

### `POST /api/gantt/project/{project_idx}/gantt/asset/task/update`

### permission

- `permission.update_gantt`

### request

| param        | type  |       data       | required | desc       |
| ------------ | :---: | :--------------: | :------: | ---------- |
| project_idx  | path  |     integer      |    O     |            |
| task_idx[]   | query | array of integer |    O     |            |
| start_date[] | query |  array of date   |    O     | YYYY-MM-DD |
| end_date[]   | query |  array of date   |    O     | YYYY-MM-DD |

### response

```json
{
	"error": {
		"code": 200,
		"message": "스케쥴이 변경 되었습니다."
	},
	"data": {
		"message_idx": 4
	}
}
```

---

---

## 끝

[샷 에피소드 조회]: #gantt-episode-read
[샷 시퀀스 조회]: #gantt-sequence-read
[샷 태스크 조회]: #gantt-shot-task-read
[에셋 카테고리 조회]: #gantt-category-read
[에셋 태스크 조회]: #gantt-asset-task-read
[샷 태스크 일정 정보 저장]: #gantt-shot-task-update
[에셋 태스크 일정 정보 저장]: #gantt-asset-task-update
