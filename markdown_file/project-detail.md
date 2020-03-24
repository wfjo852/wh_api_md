# WH2API::ProjectDetail

- `project.md` 와 일부 합칠 예정

## 목차

| 내용                                 | slug                                                | 서버 구현 | 웹 적용 |
| :----------------------------------- | :-------------------------------------------------- | :-------: | :-----: |
| 1. [태스크타입 할당 조회]            | /api/project/{project_idx}/tasktype/{which}/list    |    GET    |    O    |
| 2. [태스크타입 재할당]               | /api/project/{project_idx}/tasktype/{which}/update  |   POST    |    O    |
| 3. [프로젝트 내 상태 코드 할당 조회] | /api/project/{project_idx}/status/allocation/list   |    GET    |    O    |
| 4. [프로젝트 내 상태 코드 재할당]    | /api/project/{project_idx}/status/allocation/update |   POST    |    O    |
| 5. [이용자 할당 조회]                | /api/project/{project_idx}/user/allocation/list     |    GET    |    O    |
| 6. [이용자 재할당]                   | /api/project/{project_idx}/user/allocation/update   |   POST    |    O    |
| 7. [샷/에셋 커스텀 컬럼 목록 조회]   | /api/project/{project_idx}/{which}/custom/list      |    GET    |    O    |
| 8. [샷/에셋 커스텀 컬럼 정보 수정]   | /api/project/{project_idx}/{which}/custom/update    |   POST    |    O    |

- 참조<sup>1</sup> - /api/project/{project_idx}/episode/list[/{detail}] (project-shot-overview.md 참조)

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 태스크타입 할당 조회 <a id="project-tasktype-list"></a>

### `GET /api/project/{project_idx}/tasktype/{which}/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc          |
| ----------- | :--: | :-----: | :------: | ------------- |
| project_idx | path | integer |    O     |               |
| which       | path | string  |    O     | asset or shot |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"tasktypes": [
			{
				"tasktype_idx": "12",
				"tasktype_name": "render",
				"color": "#888888",
				"description": "asset render"
			},
			{
				"tasktype_idx": "13",
				"tasktype_name": "coloring",
				"color": "#888888",
				"description": "asset coloring"
			},
			{
				"tasktype_idx": "14",
				"tasktype_name": "Rigging",
				"color": "#888888",
				"description": "리깅"
			}
		],
		"tasktype_idx_with_project": ["12", "13"]
	}
}
```

---

## 2. 태스크타입 재할당 <a id="project-tasktype-update"></a>

### `POST /api/project/{project_idx}/tasktype/{which}/update`

### permission

- `permission.update_project`

### request

| param          | type  |  data   | required | desc |
| -------------- | :---: | :-----: | :------: | ---- |
| project_idx    | path  | integer |    O     |      |
| which          | path  | string  |    O     |      |
| tasktype_idx[] | query | integer |    O     |      |

- 파라미터로 넘어온 tasktype_idx 만 프로젝트에 할당하고, 포함되지 않은 것은 모두 할당에서 제외함.

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크 타입을 할당했습니다."
	},
	"data": null
}
```

---

## 3. 프로젝트 내 상태 코드 목록 조회 <a id="project-status-list"></a>

### `GET /api/project/{project_idx}/detail/status/list`

### permission

- `permission.read_project`

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
		"statuses": [
			{
				"status_idx": 1,
				"name": "Final",
				"color": "#DE4E4E",
				"progress": "100%"
			},
			{
				"status_idx": 2,
				"name": "Hold",
				"color": "#F5A623",
				"progress": "90%"
			},
			{
				"status_idx": 3,
				"name": "ing",
				"color": "#FFD906",
				"progress": "80%"
			}
		],
		"shot_asset_idx_with_project": [1, 2, 3], // status_idx
		"task_idx_with_project": [1, 2, 3], // status_idx
		"version_idx_with_project": [1, 2, 3] // status_idx
	}
}
```

---

## 4. 프로젝트 내 상태 코드 재할당 <a id="project-status-update"></a>

### `POST /api/project/{project_idx}/status/allocation/update`

### permission

- `permission.update_project`

### request

| param            | type  |  data   | required | desc                      |
| ---------------- | :---: | :-----: | :------: | ------------------------- |
| project_idx      | path  | integer |    O     |                           |
| shot_asset_idx[] | query | integer |    O     | 실제 값은 모두 status_idx |
| task_idx[]       | query | integer |    O     | 실제 값은 모두 status_idx |
| version_idx[]    | query | integer |    O     | 실제 값은 모두 status_idx |

### response

```json
{
	"error": {
		"code": 200,
		"message": "해당 상태 코드를 재할당했습니다."
	},
	"data": null
}
```

---

## 5. 이용자 할당 조회 <a id="project-user-list"></a>

### `GET /api/project/{project_idx}/user/allocation/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

```json
{{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "users": [
      {
        "user_idx": "1",
        "user_id": "c2m",
        "user_name": "cccc",
        "user_thumbnail": "http://localhost:81/2019/02/15/c0738fbd241feb2a.jpg",
        "email": "c2m@c2m.com",
        "name": "artist"
      },
      {
        "user_idx": "2",
        "user_id": "c3m",
        "user_name": "111-222-3333",
        "user_thumbnail": "",
        "email": "c3m@c2.com",
        "name": "artist"
      },
      {
        "user_idx": "3",
        "user_id": "spito",
        "user_name": "002-11-21-2",
        "user_thumbnail": "",
        "email": "cmcm@munger.com",
        "name": "artist"
      }
    ],
    "user_idx_with_project": ["1","2"]
  }
}
```

---

## 6. 이용자 재할당 <a id="project-user-update"></a>

### `POST /api/project/{project_idx}/user/allocation/update`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| user_idx[]  | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "이용자를 재할당했습니다."
	},
	"data": null
}
```

---

## 7. 샷/에셋 커스텀 컬럼 목록 조회 <a id="project-custom-list"></a>

### `GET /api/project/{project_idx}/{which}/custom/list`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc          |
| ----------- | :--: | :-----: | :------: | ------------- |
| project_idx | path | integer |    O     |               |
| which       | path | string  |    O     | shot or asset |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"custom_columns": [
			{
				"column_name": "c1",
				"show_name": "AA BB",
				"description": "",
				"is_on": "1"
			},
			{
				"column_name": "c2",
				"show_name": "Memo #1",
				"description": "",
				"is_on": "1"
			},
			{
				"column_name": "c3",
				"show_name": "Dr Koo",
				"description": "",
				"is_on": "1"
			},
			{
				"column_name": "c4",
				"show_name": "Ani-team",
				"description": "",
				"is_on": "1"
			},
			{
				"column_name": "c5",
				"show_name": "Tilt Temp",
				"description": "",
				"is_on": "1"
			},
			{
				"column_name": "c6",
				"show_name": "Column6",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c7",
				"show_name": "Column7",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c8",
				"show_name": "Column8",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c9",
				"show_name": "Column9",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c10",
				"show_name": "Column10",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c11",
				"show_name": "Column11",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c12",
				"show_name": "Column12",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c13",
				"show_name": "Column13",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c14",
				"show_name": "Column14",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c15",
				"show_name": "Column15",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c16",
				"show_name": "Column16",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c17",
				"show_name": "Column17",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c18",
				"show_name": "Column18",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c19",
				"show_name": "Column19",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c20",
				"show_name": "Column20",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c21",
				"show_name": "Column21",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c22",
				"show_name": "Column22",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c23",
				"show_name": "Column23",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c24",
				"show_name": "Column24",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c25",
				"show_name": "Column25",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c26",
				"show_name": "Column26",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c27",
				"show_name": "Column27",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c28",
				"show_name": "Column28",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c29",
				"show_name": "Column29",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c30",
				"show_name": "Column30",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c31",
				"show_name": "Column31",
				"description": "",
				"is_on": "0"
			},
			{
				"column_name": "c32",
				"show_name": "Column32",
				"description": "",
				"is_on": "0"
			}
		]
	}
}
```

## 8. 샷/에셋 커스텀 컬럼 정보 수정 <a id="project-custom-update"></a>

### `POST /api/project/{project_idx}/{which}/custom/update`

### permission

- `permission.update_project`

### request

| param         | type  |       data       | required | desc                         |
| ------------- | :---: | :--------------: | :------: | ---------------------------- |
| project_idx   | path  |     integer      |    O     |                              |
| which         | path  |      string      |    O     | shot or asset                |
| column_name[] | query | array of string  |    O     | c1, c2 ~ c31, c32            |
| show_name[]   | query | array of string  |    O     |                              |
| description[] | query | array of string  |    O     |                              |
| is_on[]       | query | array of integer |    O     | 1 - 이용 / 0 - 이용하지 않음 |

### response (작성 중)

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"column_names": ["c1", "c2"]
	}
}
```

---

## 끝

[태스크타입 할당 조회]: #project-tasktype-list
[태스크타입 재할당]: #project-tasktype-update
[프로젝트 내 상태 코드 할당 조회]: #project-status-list
[프로젝트 내 상태 코드 재할당]: #project-status-update
[이용자 할당 조회]: #project-user-list
[이용자 재할당]: #project-user-update
[샷/에셋 커스텀 컬럼 목록 조회]: #project-custom-list
[샷/에셋 커스텀 컬럼 정보 수정]: #project-custom-update
