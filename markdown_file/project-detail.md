# WH2API::ProjectDetail

- `project.md` 와 일부 합칠 예정

## 목차

| 내용                                                             | slug                                                            | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
|:-----------------------------------------------------------------|:----------------------------------------------------------------|:---------:|:-------:|:----:|:----:|
| 1. [태스크타입 할당 목록 조회]                                   | /api/project/{project_idx}/tasktype/{which}/allocation/list     |    GET    |    O    |  -   |  -   |
| 2. [태스크타입 재할당]                                           | /api/project/{project_idx}/tasktype/{which}/allocation/update   |   POST    |    O    |  -   |  -   |
| 3. [상태 코드 할당 목록 조회]                                    | /api/project/{project_idx}/status/allocation/list               |    GET    |    O    |  -   |  -   |
| 4. [상태 코드 재할당]                                            | /api/project/{project_idx}/status/allocation/update             |   POST    |    O    |  -   |  -   |
| 5. [이용자 할당 조회]                                            | /api/project/{project_idx}/user/allocation/list                 |    GET    |    O    |  -   |  -   |
| 6. [이용자 재할당]                                               | /api/project/{project_idx}/user/allocation/update               |   POST    |    O    |  -   |  -   |
| 7. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 목록 조회] | /api/project/{project_idx}/{which}/custom/list                  |    GET    |    O    |  -   |  -   |
| 8. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 정보 수정] | /api/project/{project_idx}/{which}/custom/update                |   POST    |    O    |  -   |  -   |
| 9. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 생성]      | /api/project/{project_idx}/{which}/custom/create                |   POST    |    O    |  -   |  -   |
| 10. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 삭제]     | /api/project/{project_idx}/{which}/custom/delete                |   POST    |    O    |  -   |  -   |
| 11. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 활성화]        | /api/project/{project_idx}/{which}/custom/activate              |   POST    |    O    |  -   |  -   |
| 12. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 비활성화]      | /api/project/{project_idx}/{which}/custom/deactivate            |   POST    |    O    |  -   |  -   |
| 13. [에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 순서 변경]     | /api/project/{project_idx}/{which}/custom/order                 |   POST    |    O    |  -   |  -   |
| 14. [태스크타입 할당 순서 수정]                                  | /api/project/{project_idx}/status/tasktype/{which}/order/update |  X POST   |    X    |  -   |  -   |
| 15. [상태 코드 할당 순서 수정]                                   | /api/project/{project_idx}/status/allocation/order/update       |  X POST   |    X    |  -   |  -   |

- 참조<sup>1</sup> - /api/project/{project_idx}/episode/list[/{detail}] (project-shot-overview.md 참조)

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 태스크타입 할당 목록 조회 <a id="project-tasktype-list"></a>

### `GET /api/project/{project_idx}/tasktype/{which}/allocation/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc                   |
|-------------|:----:|:-------:|:--------:|------------------------|
| project_idx | path | integer |    O     |                        |
| which       | path | string  |    O     | asset or shot or issue |

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
				"idx": "1",
				"name": "Animation",
				"description": "for animation",
				"pos": "1",
				"color": "#DE4E4E",
				"kind": "shot",
				"next_tasktype_idxes": [1, 2]
			},
			{
				"idx": "3",
				"name": "Comp",
				"description": "",
				"pos": "2",
				"color": "#FFD906",
				"kind": "shot",
				"next_tasktype_idxes": [1, 2]
			}
		],
		"tasktype_idx_with_project": ["1", "3"]
	}
}
```

---

## 2. 태스크타입 재할당 <a id="project-tasktype-update"></a>

### `POST /api/project/{project_idx}/tasktype/{which}/allocation/update`

### permission

- `permission.update_project`

### request

| param                 | type  |       data       | required | desc                            |
|-----------------------|:-----:|:----------------:|:--------:|---------------------------------|
| project_idx           | path  |     integer      |    O     |                                 |
| which                 | path  |      string      |    O     |                                 |
| tasktype_idx[]        | query | array of integer |    O     |                                 |
| add_tasktype_name[]   | query | array of integer |    X     | 생성되는 아이템 이름            |
| pos[]                 | query |  array of float  |    O     | 위치값 (0 이상)                 |
| add_pos[]             | query |  array of float  |    X     | 생성되는 아이템 위치값 (0 이상) |
| next_tasktype_idxes[] | query | array of integer |    O     | #all[idx=999999999] 모두를 뜻함 |

- 파라미터로 넘어온 tasktype_idx 만 프로젝트에 할당하고, 포함되지 않은 것은 모두 할당에서 제외함.

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크타입을 할당했습니다."
	},
	"data": null
}
```

---

## 3. 상태 코드 할당 목록 조회 <a id="project-status-list"></a>

### `GET /api/project/{project_idx}/status/allocation/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc |
|-------------|:----:|:-------:|:--------:|------|
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
                "idx": "1",
                "name": "wip",
                "description": null,
                "is_on": "1",
                "pos": "1",
                "color": "#dbd8db",
                "progress": "5"
            },
            {
                "idx": "14",
                "name": "A_tests",
                "description": "1111111111222",
                "is_on": "1",
                "pos": "1",
                "color": "#4caf50",
                "progress": "50"
            },
            {
                "idx": "2",
                "name": "confirm",
                "description": null,
                "is_on": "1",
                "pos": "2",
                "color": "#03a9f4",
                "progress": "30"
            },
            {
                "idx": "3",
                "name": "retake",
                "description": null,
                "is_on": "1",
                "pos": "3",
                "color": "#f44336",
                "progress": "10"
            },
            {
                "idx": "4",
                "name": "pub",
                "description": null,
                "is_on": "1",
                "pos": "4",
                "color": "#ff9800",
                "progress": "90"
            },
            {
                "idx": "5",
                "name": "final",
                "description": null,
                "is_on": "1",
                "pos": "5",
                "color": "#607d8b",
                "progress": "100"
            },
            {
                "idx": "15",
                "name": "test1111333",
                "description": "",
                "is_on": "1",
                "pos": 99999,
                "color": "#f44336",
                "progress": "50"
            }
        ],
        "shot_idx_with_project": ["1", "14", "2", "3", "4", "5"],
        "asset_idx_with_project": ["1", "14", "2", "3", "4", "5"],
        "task_idx_with_project": ["1", "14", "2", "3", "4", "5"],
        "version_idx_with_project": ["1", "2", "3", "4", "5"],
        "issue_idx_with_project": ["1", "14", "2", "3", "4", "5"]
    }
}
```

---

## 4. 상태 코드 재할당 <a id="project-status-update"></a>

### `POST /api/project/{project_idx}/status/allocation/update`

### permission

- `permission.update_project`

### request

| param            | type  |       data       | required | desc                               |
|------------------|:-----:|:----------------:|:--------:|------------------------------------|
| project_idx      | path  |     integer      |    O     |                                    |
| shot_asset_idx[] | query | array of integer |    O     | 실제 값은 모두 status_idx          |
| task_idx[]       | query | array of integer |    O     | 실제 값은 모두 status_idx          |
| version_idx[]    | query | array of integer |    O     | 실제 값은 모두 status_idx          |
| issue_idx[]      | query | array of integer |    O     | 실제 값은 모두 status_idx          |
| status_idx[]     | query | array of integer |    O     | 위치값 수정을 위한 실제 status_idx |
| pos[]            | query |  array of float  |    O     | 위치값 (0 이상)                    |

- status_idx[] 와 pos[] 는 갯수가 맞아야 함

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
|-------------|:----:|:-------:|:--------:|------|
| project_idx | path | integer |    O     |      |

### response

```json
{
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
|-------------|:-----:|:-------:|:--------:|------|
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

## 7. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 목록 조회 <a id="project-custom-list"></a>

### `GET /api/project/{project_idx}/{which}/custom/list`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc                                           |
|-------------|:----:|:-------:|:--------:|------------------------------------------------|
| project_idx | path | integer |    O     |                                                |
| which       | path | string  |    O     | episode, sequence, shot, asset_category, asset |

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

## 8. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 정보 수정 <a id="project-custom-update"></a>

### `POST /api/project/{project_idx}/{which}/custom/update`

### permission

- `permission.update_project`

### request

| param       | type  |       data       | required | desc                                           |
|-------------|:-----:|:----------------:|:--------:|------------------------------------------------|
| project_idx | path  |     integer      |    O     |                                                |
| which       | path  |      string      |    O     | episode, sequence, shot, asset_category, asset |
| idxes[]     | query | array of integer |    O     |                                                |
| column[]    | query | array of string  |    O     |                                                |
| old_val[]   | query | array of string  |    O     |                                                |
| new_val[]   | query | array of string  |    O     |                                                |

### response (작성 중)

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

## 9. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 생성 <a id="project-custom-create"></a>

### `POST /api/project/{project_idx}/{which}/custom/create`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc                                           |
|-------------|:-----:|:-------:|:--------:|------------------------------------------------|
| project_idx | path  | integer |    O     |                                                |
| which       | path  | string  |    O     | episode, sequence, shot, asset_category, asset |
| show_name   | query | string  |    O     |                                                |
| description | query | string  |    O     |                                                |

### response (작성 중)

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

## 10. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 삭제 <a id="project-custom-delete"></a>

### `POST /api/project/{project_idx}/{which}/custom/delete`

### permission

- `permission.update_project`

### request

| param       | type  |   data   | required | desc                                           |
|-------------|:-----:|:--------:|:--------:|------------------------------------------------|
| project_idx | path  | integer  |    O     |                                                |
| which       | path  |  string  |    O     | episode, sequence, shot, asset_category, asset |
| custom_idx  | query | interger |    O     |                                                |

### response (작성 중)

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

---

## 11. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 활성화 <a id="project-custom-activate"></a>

### `POST /api/project/{project_idx}/{which}/custom/activate`

### permission

- `permission.update_project`

### request

| param       | type  |   data   | required | desc                                           |
|-------------|:-----:|:--------:|:--------:|------------------------------------------------|
| project_idx | path  | integer  |    O     |                                                |
| which       | path  |  string  |    O     | episode, sequence, shot, asset_category, asset |
| custom_idx  | query | interger |    O     |                                                |

### response (작성 중)

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

## 12. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 비활성화 <a id="project-custom-deactivate"></a>

### `POST /api/project/{project_idx}/{which}/custom/deactivate`

### permission

- `permission.update_project`

### request

| param       | type  |   data   | required | desc                                           |
|-------------|:-----:|:--------:|:--------:|------------------------------------------------|
| project_idx | path  | integer  |    O     |                                                |
| which       | path  |  string  |    O     | episode, sequence, shot, asset_category, asset |
| custom_idx  | query | interger |    O     |                                                |

### response (작성 중)

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

## 13. 에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 순서 변경 <a id="project-custom-order"></a>

### `POST /api/project/{project_idx}/{which}/custom/order`

### permission

- `permission.update_project`

### request

| param       | type  |   data   | required | desc                                                               |
|-------------|:-----:|:--------:|:--------:|--------------------------------------------------------------------|
| project_idx | path  | integer  |    O     |                                                                    |
| which       | path  |  string  |    O     | episode, sequence, shot, asset_category, asset                     |
| start       | query | interger |    O     | 이동할 행들의 첫번째 행의 위치 값 ex: 5번,6번 -> 2번으로 이동 시 5 |
| end         | query | interger |    O     | 행들이 이동 한 위치의 값 ex: 5번,6번 -> 2번으로 이동 시 2          |
| row_count   | query | interger |    O     | 이동하는 행들의 개수 ex: 5번,6번 행이 이동 시 2                    |

### response (작성 중)

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

[태스크타입 할당 목록 조회]: #project-tasktype-list
[태스크타입 재할당]: #project-tasktype-update
[상태 코드 할당 목록 조회]: #project-status-list
[상태 코드 재할당]: #project-status-update
[이용자 할당 조회]: #project-user-list
[이용자 재할당]: #project-user-update
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 목록 조회]: #project-custom-list
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 정보 수정]: #project-custom-update
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 생성]: #project-custom-create
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 삭제]: #project-custom-delete
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 활성화]: #project-custom-activate
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 비활성화]: #project-custom-deactivate
[에피소드/시퀀스/샷/에셋 카테고리/에셋 커스텀 컬럼 순서 변경]: #project-custom-order
