# WH2API::Setting

## 목차

| 내용                              | slug                                            | 서버 구현 | 웹 적용 |
| :-------------------------------- | :---------------------------------------------- | :-------: | :-----: |
| 1. [웜홀 설치 프로그램 목록 조회] | /api/setting/list                               |     X     |    X    |
| 2. [상태 코드 추가]               | /api/setting/status/create                      |   POST    |    O    |
| 3. [상태 코드 수정]               | /api/setting/status/{status_idx}/update         |   POST    |    O    |
| 4. [상태 코드 삭제]               | /api/setting/status/{status_idx}/delete         |   POST    |    O    |
| 5. [상태 코드 목록 조회]          | /api/setting/status/list                        |    GET    |    O    |
| 6. [포함 프로젝트 목록]           | /api/setting/status/{status_idx}/project/list   |    GET    |    O    |
| 7. [포함 프로젝트 변경]           | /api/setting/status/{status_idx}/project/update |   POST    |    O    |
| 8. [DB 유효성 체크]               | /api/setting/db/check                           |   POST    |    O    |
| 9. [웜홀 시스템 버전 보기]        | /api/setting/system/version/read                |    GET    |    O    |
| 10. [DB 버전 관련 밸리데이션 #1]  | /api/setting/db/version/case/1/validate         |   POST    |    O    |
| 11. [DB 버전 관련 밸리데이션 #2]  | /api/setting/db/version/case/2/validate         |   POST    |    O    |
| 12. [DB 버전 관련 밸리데이션 #3]  | /api/setting/db/version/case/3/validate         |   POST    |    O    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 웜홀 설치 프로그램 목록 조회 <a id="settting-list"></a>

### `GET /api/projects/list`

### permission

- `permission.read_setting`

### request

```javascript
{
}
```

### response

```json
{
	"wh_installers": [
		{
			"num": 43,
			"update_date": "2018.2.26 8:54:30",
			"patch_file": "wormhole_installer_v3.6.0.exe",
			"contents": "-bug fix fox xxxxx <br/>-but fix for xxxx",
			"download_date": "2018.2.26 8:54:30",
			"download_url": "/downloads/a.exe"
		},
		{
			"num": 42,
			"update_date": "2018.2.26 8:54:30",
			"patch_file": "wormhole_installer_v3.6.0.exe",
			"contents": "-bug fix fox xxxxx <br/>-but fix for xxxx",
			"download_date": "2018.2.26 8:54:30",
			"download_url": "/downloads/a.exe"
		},
		{
			"num": 41,
			"update_date": "2018.2.26 8:54:30",
			"patch_file": "wormhole_installer_v3.6.0.exe",
			"contents": "-bug fix fox xxxxx <br/>-but fix for xxxx",
			"download_date": "2018.2.26 8:54:30",
			"download_url": "/downloads/a.exe"
		},
		{
			"num": 40,
			"update_date": "2018.2.26 8:54:30",
			"patch_file": "wormhole_installer_v3.6.0.exe",
			"contents": "-bug fix fox xxxxx <br/>-but fix for xxxx",
			"download_date": "2018.2.26 8:54:30",
			"download_url": "/downloads/a.exe"
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

## 2. 상태 코드 추가 <a id="settting-status-create"></a>

### `POST /api/setting/status/create`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc             |
| ----------- | :---: | :-----: | :------: | ---------------- |
| status_name | query | string  |    O     |                  |
| color       | query | string  |    O     |                  |
| progress    | query | integer |    O     | 0 ~ 100 (진행률) |
| description | query | string  |          |                  |

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드가 추가됐습니다."
	},
	"data": {
		"status_idx": 9
	}
}
```

---

## 3. 상태 코드 수정 <a id="settting-status-update"></a>

### `POST /api/setting/status/{status_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param      | type  |  data   | required | desc                                       |
| ---------- | :---: | :-----: | :------: | ------------------------------------------ |
| status_idx | path  | integer |    O     |                                            |
| column     | query | string  |    O     | statrus_name, color, progress, description |
| old_val    | query | string  |    O     | 공백일 수는 있음                           |
| new_val    | query | string  |    O     | 공백일 수는 있음                           |

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드가 수정됐습니다."
	},
	"data": {
		"status_idx": 7,
		"status_name": "working"
	}
}
```

---

## 4. 상태 코드 삭제 <a id="settting-status-delete"></a>

### `POST /api/setting/status/{status_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param      | type |  data   | required | desc |
| ---------- | :--: | :-----: | :------: | ---- |
| status_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드가 삭제됐습니다."
	},
	"data": null
}
```

---

## 5. 상태 코드 목록 조회 <a id="settting-status-list"></a>

### `GET /api/setting/status/list`

### permission

- `permission.do_global_setting`

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
		"status_list": [
			{
				"status_idx": "1",
				"status_name": "wip",
				"color": "#888888",
				"progress": "100",
				"description": null,
				"project_list": [
					{
						"project_idx": "1",
						"name": "prjA"
					},
					{
						"project_idx": "2",
						"name": "Popo Cuca"
					}
				]
			},
			{
				"status_idx": "2",
				"status_name": "confirm",
				"color": "#888888",
				"progress": "100",
				"description": null,
				"project_list": [
					{
						"project_idx": "1",
						"name": "prjA"
					},
					{
						"project_idx": "2",
						"name": "Popo Cuca"
					}
				]
			},
			{
				"status_idx": "3",
				"status_name": "retake",
				"color": "#888888",
				"progress": "100",
				"description": null,
				"project_list": [
					{
						"project_idx": "1",
						"name": "prjA"
					},
					{
						"project_idx": "2",
						"name": "Popo Cuca"
					}
				]
			},
			{
				"status_idx": "4",
				"status_name": "pub",
				"color": "#888888",
				"progress": "100",
				"description": null,
				"project_list": [
					{
						"project_idx": "1",
						"name": "prjA"
					}
				]
			},
			{
				"status_idx": "5",
				"status_name": "final",
				"color": "#888888",
				"progress": "100",
				"description": null,
				"project_list": null
			}
		]
	}
}
```

## 6. 포함 프로젝트 목록 <a id="settting-status-project-list"></a>

- 시스템에 존재하는 모든 프로젝트가 리스팅되며, `status_idx`가 포함된/포함 안 된 프로젝트 인덱스가 주어진다.

### `GET /api/setting/status/{status_idx}/project/list`

### permission

- `permission.do_global_setting`

### request

| param      | type |  data   | required | desc |
| ---------- | :--: | :-----: | :------: | ---- |
| status_idx | path | integer |    O     |      |

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
			},
			{
				"name": "project 3333",
				"project_idx": "3"
			}
		],
		"status_idx_with_project": ["1"],
		"status_idx_without_project": ["2", "3"]
	}
}
```

---

## 7. 포함 프로젝트 변경 <a id="settting-status-project-update"></a>

### `POST /api/setting/status/{status_idx}/project/update`

### permission

- `permission.do_global_setting`

### request

| param                        | type  |       data       | required | desc |
| ---------------------------- | :---: | :--------------: | :------: | ---- |
| status_idx                   | path  |     integer      |    O     |      |
| project_idx_with_status[]    | query | array of integer |    O     |      |
| project_idx_without_status[] | query | array of integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "프로젝트가 변경 되었습니다."
	},
	"data": {
		"project_idx_with_status": [
			{
				"project_idx": 1,
				"name": "project01"
			},
			{
				"project_idx": 2,
				"name": "project02"
			}
		]
	}
}
```

---

## 8. DB 유효성 체크 <a id="db-check"></a>

### `POST /api/setting/db/check`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "시스템 체크를 했습니다."
	},
	"data": null
}
```

---

## 9. 웜홀 시스템 버전 보기 <a id="system-version-read"></a>

### `GET /api/setting/system/version/read`

### permission

- all

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version": "1.2.7",
		"updated_time": "2019-08-14 00:43:40"
	}
}
```

---

## 10. DB 버전 관련 밸리데이션 #1 <a id="db-version-case1-validate"></a>

### `POST /api/setting/db/version/case/1/validate`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "유효성 검증 작업을 했습니다."
	},
	"data": null
}
```

---

## 11. DB 버전 관련 밸리데이션 #2 <a id="db-version-case2-validate"></a>

### `POST /api/setting/db/version/case/2/validate`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "유효성 검증 작업을 했습니다."
	},
	"data": null
}
```

---

## 12. DB 버전 관련 밸리데이션 #3 <a id="db-version-case2-validate"></a>

### `POST /api/setting/db/version/case/3/validate`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "유효성 검증 작업을 했습니다."
	},
	"data": null
}
```

---

## 끝

[웜홀 설치 프로그램 목록 조회]: #settting-list
[상태 코드 추가]: #settting-status-create
[상태 코드 수정]: #settting-status-update
[상태 코드 삭제]: #settting-status-delete
[상태 코드 목록 조회]: #settting-status-list
[포함 프로젝트 목록]: #settting-status-project-list
[포함 프로젝트 변경]: #settting-status-project-update
[db 유효성 체크]: #db-check
[웜홀 시스템 버전 보기]: #system-version-read
[db 버전 관련 밸리데이션 #1]: #db-version-case1-validate
[db 버전 관련 밸리데이션 #2]: #db-version-case2-validate
[db 버전 관련 밸리데이션 #3]: #db-version-case3-validate
