# WH2API::TaskType

## 목차

| 내용                                      | slug                                        | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
|:------------------------------------------|:--------------------------------------------|:---------:|:-------:|:----:|:----:|
| 1. [태스크타입 목록 조회]                 | /api/tasktype/{which}/list                  |    GET    |    O    |  -   |  -   |
| 2. [태스크타입 등록]                      | /api/tasktype/create                        |   POST    |    O    |  -   |  -   |
| 3. [태스크타입 수정]                      | /api/tasktype/{tasktype_idx}/update         |   POST    |    O    |  -   |  -   |
| 4. [태스크타입 삭제]                      | /api/tasktype/{tasktype_idx}/delete         |   POST    |    O    |  -   |  -   |
| 5. [태스크타입의 포함 프로젝트 목록 조회] | /api/tasktype/{tasktype_idx}/project/list   |    GET    |    O    |  -   |  -   |
| 6. [태스크타입의 포함 프로젝트 변경]      | /api/tasktype/{tasktype_idx}/project/update |   POST    |    O    |  -   |  -   |

- TODO: url slug 에 /setting/ 을 넣는 것이 의미가 분명해질 듯함. 판단 필요.
- (cf. status) (혹은 반대로 status 등 쪽에 setting을 빼는 것도 검토.)

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 태스크타입 목록 조회 <a id="tasktype-list"></a>

### `GET /api/tasktype/{which}/list`

### permission

- `permission.do_global_setting`

### request

| param | type |  data  | required | desc               |
|-------|:----:|:------:|:--------:|--------------------|
| which | path | string |    O     | shot, asset, issue |

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
				"color": "#DE4E4E",
				"kind": "shot",
				"project_list": [
					{
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					}
				]
			},
			{
				"idx": "3",
				"name": "Comp",
				"description": "Composition",
				"color": "#FFD906",
				"kind": "shot",
				"project_list": [
					{
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					}
				]
			}
		]
	}
}
```

---

## 2. 태스크타입 등록 <a id="tasktype-create"></a>

### `POST /api/tasktype/create`

### permission

- `permission.do_global_setting`

### request

| param         | type  |  data  | required | desc                         |
|---------------|:-----:|:------:|:--------:|------------------------------|
| tasktype_name | query | string |    O     |                              |
| which         | query | string |    O     | 'shot' or 'asset' or 'issue' |
| color         | query | string |    O     |                              |
| description   | query | string |    X     |                              |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크타입이 추가됐습니다."
	},
	"data": {
		"task_idx": "8"
	}
}
```

---

## 3. 태스크타입 수정 <a id="tasktype-update"></a>

### `POST /api/tasktype/{tasktype_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param        | type  |  data   | required | desc             |
|--------------|:-----:|:-------:|:--------:|------------------|
| tasktype_idx | path  | integer |    O     |                  |
| column       | query | string  |    O     |                  |
| old_val      | query | string  |    O     | 공백일 수는 있음 |
| new_val      | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
	"error": {
		"message": "태스크타입이 수정됐습니다."
	},
	"data": {
		"tasktype" : {
				"idx": "1",
				"name": "Animation1",
				"description": "for animation",
				"color": "#DE4E4E",
				"kind": "shot"
			}
		}
	}
}
```

---

## 4. 태스크타입 삭제 <a id="tasktype-delete"></a>

### `POST /api/tasktype/{task_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param        | type |  data   | required | desc |
|--------------|:----:|:-------:|:--------:|------|
| tasktype_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크타입이 삭제됐습니다."
	},
	"data": null
}
```

## 5. 태스크타입의 포함 프로젝트 목록 <a id="tasktype-project-list"></a>

- 시스템에 존재하는 모든 프로젝트가 리스팅되며, `tasktype_idx`가 포함된/포함 안 된 프로젝트 인덱스가 주어진다.

### `GET /api/tasktype/{task_idx}/project/list`

### permission

- `permission.do_global_setting`

### request

| param        | type |  data   | required | desc |
|--------------|:----:|:-------:|:--------:|------|
| tasktype_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"projects": [
			{
				"name": "prjA",
				"project_idx": "1"
			},
			{
				"name": "Popo Cuca",
				"project_idx": "2"
			}
		],
		"project_idx_with_tasktype": ["1"],
		"project_idx_without_tasktype": ["2"]
	}
}
```

## 6. 태스크타입의 포함 프로젝트 변경 <a id="tasktype-project-update"></a>

### `POST /api/tasktype/{tasktype_idx}/project/update`

### permission

- `permission.do_global_setting`

### request

| param                       | type  |       data       | required | desc |
|-----------------------------|:-----:|:----------------:|:--------:|------|
| tasktype_idx                | path  |     integer      |    O     |      |
| project_idx_with_tasktype[] | query | array of integer |    O     |      |
| add_project_name[]          | query | array of string  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "참여 프로젝트가 변경됐습니다."
	},
	"data": {
		"project_idx_with_tasktype": [
			{
				"project_idx": 1,
				"name": "pr1"
			},
			{
				"project_idx": 2,
				"name": "pr2"
			}
		]
	}
}
```

---

## 끝

[태스크타입 목록 조회]: #tasktype-list
[태스크타입 등록]: #tasktype-create
[태스크타입 수정]: #tasktype-update
[태스크타입 삭제]: #tasktype-delete
[태스크타입의 포함 프로젝트 목록 조회]: #tasktype-project-list
[태스크타입의 포함 프로젝트 변경]: #tasktype-project-update
