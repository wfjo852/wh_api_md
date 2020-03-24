# WH2API::Project

## 목차

| 내용                                       | slug                                              | 서버 구현 | 웹 적용 |
| :----------------------------------------- | :------------------------------------------------ | :-------: | :-----: |
| 1. [프로젝트 목록 조회]                    | /api/project/list                                 |    GET    |    O    |
| 2. [프로젝트 생성]                         | /api/project/create                               |   POST    |    O    |
| 3. [프로젝트 정보 조회]                    | /api/project/{project_idx}/read                   |    GET    |    O    |
| 4. [프로젝트 상세 정보 조회]               | /api/project/{project_idx}/detail/read            |    GET    |    O    |
| 5. [프로젝트 정보 수정]                    | /api/project/{project_idx}/update                 |   POST    |    O    |
| 6. [프로젝트 경로 정보 수정]               | /api/project/{project_idx}/path/update            |   POST    |    O    |
| 7. [프로젝트 삭제]                         | /api/project/{project_idx}/delete                 |   POST    |    O    |
| 8. [프로젝트 상태 코드 목록 조회]          | /api/project/status/list                          |    O\*    |    X    |
| 9. [프로젝트에 할당된 상태 코드 목록 조회] | /api/project/{project_idx}/{in_which}/status/list |    GET    |    O    |

- O\* - api 없이 콘트롤러에 직접 구현

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 프로젝트 목록 조회 <a id="project-list"></a>

### `GET /api/project/list`

### permission

- `permission.read_project`

### request

| param              | type  |  data   | required | desc                                         |
| ------------------ | :---: | :-----: | :------: | -------------------------------------------- |
| including_finished | query | integer |    X     | 1                                            |
| page               | query | integer |    X     |                                              |
| all                | query | integer |    X     | 1 (페이징 처리 없이 한번에 모든 리스트 받기) |

### response

```json
{
	"projects": [
		{
			"project_idx": 1,
			"name": "Demo_BigBuck",
			"url_thumbnail": "http://128.0.1.234/assets/images/thumbnail/project/big/default.light.svg",
			"start_date": "2018-01-02",
			"end_date": "2018-08-08",
			"project_status": "1",
			"project_status_name": "Waiting",
			"is_finished": 0
		},
		{
			"project_idx": 2,
			"name": "Super Duper Power",
			"url_thumbnail": "http://128.0.1.234/assets/images/thumbnail/project/big/default.light.svg",
			"start_date": "2018-01-02",
			"end_date": "2018-08-08",
			"project_status": "1",
			"project_status_name": "Waiting",
			"is_finished": 0
		}
	],
	"paging": {
		"cur_page": 1,
		"start_page": 1,
		"last_page": 1,
		"total_page": 1
	}
}
```

---

## 2. 프로젝트 생성 <a id="project-create"></a>

### `POST /api/project/create`

### request

| param          | type  |  data   | required | desc                                     |
| -------------- | :---: | :-----: | :------: | ---------------------------------------- |
| project_name   | query | string  |    O     |                                          |
| description    | query | string  |    X     |                                          |
| start_date     | query |  date   |    X     | YYYY-MM-DD                               |
| end_date       | query |  date   |    X     | YYYY-MM-DD                               |
| project_status | query | integer |    O     | 1: 준비 중, 2: 작업 중, 3: 완료, 4: 홀드 |
| attached       | query |  file   |    X     | 썸네일 파일 (1개)                        |

### response

```json
{
	"error": {
		"code": 200,
		"message": "프로젝트가 생성됐습니다."
	},
	"data": {
		"project_idx": 1,
		"slug": "tv-series-new-1"
	}
}
```

---

## 3. 프로젝트 정보 조회 <a id="project-read"></a>

### `GET /api/project/{project_idx}/read`

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
		"project": {
			"project_idx": 1,
			"name": "Project Name",
			"url_thumbnail": "http://abc.jpg",
			"start_date": "2018-01-02",
			"end_date": "2018-08-08",
			"project_status": "1",
			"project_status_name": "Waiting",
			"description": "설명입니다."
		}
	}
}
```

---

## 4. 프로젝트 상세 정보 조회 <a id="project-detail-info"></a>

### `GET /api/project/{project_idx}/detail/read`

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
		"project": {
			"project_idx": "1",
			"name": "Demo_BigBuck",
			"slug": "prja",
			"project_thumbnail": "http://localhost:81/2019/03/19/daf3a19580c2d02e.jpg",
			"description": "Demo_BigBuck",
			"start_date": "2019-03-04",
			"end_date": "2019-03-29",
			"project_status": "2",
			"project_status_name": "Working"
		},
		"allocation": [
			{
				"type": "tasktype_asset",
				"allocated": "2",
				"total": "3"
			},
			{
				"type": "tasktype_shot",
				"allocated": "8",
				"total": "8"
			},
			{
				"type": "status",
				"allocated": "6",
				"total": "8"
			},
			{
				"type": "user",
				"allocated": "6",
				"total": "7"
			}
		],
		"path": {
			"asset": {
				"version": "[Fileserver]/[Project]/asset/[Category]/[Asset]/version/[User]/[Today]/[Version]",
				"publish": "[Fileserver]/[Project]/asset/[Category]/[Asset]/pub/[Publish]",
				"last_publish": "[Fileserver]/[Project]/asset/[Category]/[Asset]/pub/last"
			},
			"shot": {
				"version": "[Fileserver]/[Project]/shot/[Episode]/[Sequence]/[Shot]/version/[User]/[Today]/[Version]",
				"publish": "[Fileserver]/[Project]/shot/[Episode]/[Sequence]/[Shot]/pub/[Publish]",
				"last_publish": "[Fileserver]/[Project]/shot/[Episode]/[Sequence]/[Shot]/pub/last"
			}
		}
	}
}
```

---

## 5. 프로젝트 정보 수정 <a id="project-update"></a>

### `POST /api/project/{project_idx}/update`

### permission

- `permission.update_project`

### request

| param          | type  |  data   | required | desc                                     |
| -------------- | :---: | :-----: | :------: | ---------------------------------------- |
| project_idx    | path  | integer |    O     |                                          |
| project_name   | query | string  |    O     |                                          |
| description    | query | string  |    O     |                                          |
| start_date     | query | string  |    O     |                                          |
| end_date       | query | string  |    O     |                                          |
| project_status | query | integer |    O     | 1: 준비 중, 2: 작업 중, 3: 완료, 4: 홀드 |
| attached       | query |  file   |    X     | 썸네일 파일 (1개)                        |

### response

```json
{
	"error": {
		"code": 200,
		"message": "프로젝트 정보가 수정됐습니다."
	},
	"data": {
		"project_idx": 1,
		"project_thumbnail": "abc.jpg"
	}
}
```

---

## 6. 프로젝트 경로 정보 수정 <a id="project-path-update"></a>

- 경로에 쓰이는 변수들
  - [Fileserver]
  - [Project]
  - [Category]
  - [Asset]
  - [Publish]
  - [Episode]
  - [Sequence]
  - [Shot]
  - [Version]
  - [User]
  - [Today] : YYYY-MM-DD

### `POST /api/project/{project_idx}/path/update`

### permission

- `permission.update_project`

### request

| param              | type  |  data   | required | desc |
| ------------------ | :---: | :-----: | :------: | ---- |
| project_idx        | path  | integer |    O     |      |
| asset_version      | query | string  |    O     |      |
| asset_publish      | query | string  |    O     |      |
| asset_last_publish | query | string  |    O     |      |
| shot_version       | query | string  |    O     |      |
| shot_publish       | query | string  |    O     |      |
| shot_last_publish  | query | string  |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "프로젝트 정보가 수정됐습니다."
	},
	"data": {
		"project_idx": 1
	}
}
```

---

## 7. 프로젝트 삭제 <a id="project-delete"></a>

### `POST /api/project/{project_idx}/delete`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "프로젝트가 삭제됐습니다."
	},
	"data": null
}
```

---

## 8. 프로젝트 상태 코드 목록 조회 <a id="project-status-list"></a>

- 프로젝트 상태 코드는 고정으로 서비스 내부적으로만 이용하기로 함

| project_status |   name   |  color  |
| :------------: | :------: | :-----: |
|       0        | Archived |  #999   |
|       1        | Waiting  | #FBAC49 |
|       2        | Working  | #4990fb |
|       3        | Finished | #1f8c2f |
|       4        | Holding  | #c93f3f |

### `GET /api/status/list`

### permission

- `permission.read_project`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

- 현재 프로젝트 상태 코드는 4개로 픽스이고, 추가/수정/삭제를 할 수 없음.
- 즉, 만약 바꿔야 한다면, 코드를 수정해야 함. (BaseProject 클래스의 getStatusList() 메소드)

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": "project_status": [
    {
      "idx" : 1,
      "name": "Waiting",
      "color": "#FBAC49"
    },
    {
      "idx" : 2,
      "name": "Working",
      "color": "#4990fb"
    },
    {
      "idx" : 3,
      "name": "Finished",
      "color": "#1f8c2f"
    },
    {
      "idx" : 4,
      "name": "Holding",
      "color": "#c93f3f"
    },
  ]
}
```

---

## 9. 프로젝트에 할당된 상태 코드 목록 조회 <a id="project-which-status-list"></a>

### `GET /api/project/{project_idx}/{in_which}/status/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc                                               |
| ----------- | :--: | :-----: | :------: | -------------------------------------------------- |
| project_idx | path | integer |    O     |                                                    |
| in_which    | path | string  |    O     | episode / sequence / shot / asset / task / version |

- `in_which` 에 들어가는 문자열에 따라 필요한 상태 목록을 조회할 수 있다.
  - 예: {`project_idx = 1`}의 `shot` 상태 코드 조회: `/api/project/1/shot/status/list`
  - 예: {`project_idx = 3`}의 `version` 상태 코드 조회: `/api/project/1/version/status/list`

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드 목록이 조회 되었습니다."
	},
	"data": {
		"episode": [
			{
				"idx": 1,
				"name": "status 1"
			},
			{
				"idx": 2,
				"name": "status 2"
			},
			{
				"idx": 3,
				"name": "status 3"
			}
		]
	}
}
```

---

## 끝

[프로젝트 목록 조회]: #project-list
[프로젝트 생성]: #project-create
[프로젝트 정보 조회]: #project-read
[프로젝트 상세 정보 조회]: #project-detail-info
[프로젝트 정보 수정]: #project-update
[프로젝트 경로 정보 수정]: #project-path-update
[프로젝트 삭제]: #project-delete
[프로젝트 상태 코드 목록 조회]: #project-status-list
[프로젝트에 할당된 상태 코드 목록 조회]: #project-which-status-list
