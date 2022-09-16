# WH2API::Setting

## 목차

| 내용                              | slug                                            | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
|:----------------------------------|:------------------------------------------------|:---------:|:-------:|:----:|:----:|
| 1. [웜홀 설치 프로그램 목록 조회] | /api/setting/list                               |     X     |    X    |  -   |  -   |
| 2. [상태 코드 추가]               | /api/setting/status/create                      |   POST    |    O    |  -   |  -   |
| 3. [상태 코드 수정]               | /api/setting/status/{status_idx}/update         |   POST    |    O    |  -   |  -   |
| 4. [상태 코드 삭제]               | /api/setting/status/{status_idx}/delete         |   POST    |    O    |  -   |  -   |
| 5. [상태 코드 목록 조회]          | /api/setting/status/list                        |    GET    |    O    |  -   |  -   |
| 6. [포함 프로젝트 목록]           | /api/setting/status/{status_idx}/project/list   |    GET    |    O    |  -   |  -   |
| 7. [포함 프로젝트 변경]           | /api/setting/status/{status_idx}/project/update |   POST    |    O    |  -   |  -   |
| 8. [DB 유효성 체크]               | /api/setting/db/check                           |   POST    |    O    |  -   |  -   |
| 9. [웜홀 시스템 버전 보기]        | /api/setting/system/version/read                |    GET    |    O    |  -   |  -   |
| 10. [DB 버전 관련 밸리데이션 #1]  | /api/setting/db/version/case/1/validate         |   POST    |    O    |  -   |  -   |
| 11. [DB 버전 관련 밸리데이션 #2]  | /api/setting/db/version/case/2/validate         |   POST    |    O    |  -   |  -   |
| 12. [DB 버전 관련 밸리데이션 #3]  | /api/setting/db/version/case/3/validate         |   POST    |    O    |  -   |  -   |
| 13. [작업내역 관련 밸리데이션]    | /api/setting/db/settlement/work_time/validate   |   POST    |    O    |  -   |  -   |
| 14. [커스텀 컬럼 마이그레이션 #1] | /api/setting/db/custom/migrate/1                |   POST    |    O    |  -   |  -   |
| 15. [커스텀 컬럼 마이그레이션 #2] | /api/setting/db/custom/migrate/2                |   POST    |    O    |  -   |  -   |
| 16. [커스텀 컬럼 마이그레이션 #3] | /api/setting/db/custom/migrate/3                |   POST    |    O    |  -   |  -   |
| 17. [커스텀 컬럼 마이그레이션 #4] | /api/setting/db/custom/migrate/4                |   POST    |    O    |  -   |  -   |
| 18. [커스텀 컬럼 재정렬]          | /api/setting/db/custom/order/validate           |   POST    |    O    |  -   |  -   |
| 19. [사용 중인 프로젝트 체크]     | /api/{which}/{which_idx}/used/check             |    GET    |    O    |  -   |  -   |
| 20. [라이센스 수정]               | /api/setting/license/update                     |   POST    |    O    |  -   |  -   |
| 21. [재로그인 안내]               | /api/setting/guide/credentials                  |    GET    |    O    |  -   |  -   |
| 22. [상태코드 밸리데이션]         | /api/setting/status/validate                    |   POST    |    O    |  -   |  -   |

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
|-------------|:-----:|:-------:|:--------:|------------------|
| status_name | query | string  |    O     |                  |
| color       | query | string  |    O     |                  |
| progress    | query | integer |    X     | 0 ~ 100 (진행률) |
| description | query | string  |    X     |                  |

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드가 추가됐습니다."
	},
	"data": {
		"status": {
			"idx": "17",
			"name": "wait-b-team",
			"description": "",
			"pos": "8",
			"color": "#333333",
			"progress": "50"
		}
	}
}
```

---

## 3. 상태 코드 수정 <a id="settting-status-update"></a>

### `POST /api/setting/status/{status_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param      | type  |  data   | required | desc                               |
|------------|:-----:|:-------:|:--------:|------------------------------------|
| status_idx | path  | integer |    O     |                                    |
| column     | query | string  |    O     | name, color, progress, description |
| old_val    | query | string  |    O     | 공백일 수는 있음                   |
| new_val    | query | string  |    O     | 공백일 수는 있음                   |

### response

```json
{
	"error": {
		"code": 200,
		"message": "상태 코드가 수정됐습니다."
	},
	"data": {
		"status": {
			"idx": "5",
			"name": "final",
			"description": null,
			"pos": "5.1",
			"color": "#607d8b",
			"progress": "100"
		}
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
|------------|:----:|:-------:|:--------:|------|
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
|-------|:----:|:----:|:--------:|------|
| X     |  X   |  X   |    X     | X    |

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
				"pos": "1",
				"name": "wip",
				"color": "#dbd8db",
				"progress": "5",
				"description": "123",
				"projects": [
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
				"idx": "2",
				"pos": "2",
				"name": "confirmm",
				"color": "#03a9f4",
				"progress": "30",
				"description": "44",
				"projects": [
					{
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					},
					{
						"idx": "2",
						"name": "Project A",
						"description": "for A",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					}
				]
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
|------------|:----:|:-------:|:--------:|------|
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

| param                     | type  |       data       | required | desc |
|---------------------------|:-----:|:----------------:|:--------:|------|
| status_idx                | path  |     integer      |    O     |      |
| project_idx_with_status[] | query | array of integer |    O     |      |
| add_project_name[]        | query | array of string  |    X     |      |

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
|-------|:----:|:----:|:--------:|------|
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
|-------|:----:|:----:|:--------:|------|
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
|-------|:----:|:----:|:--------:|------|
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
|-------|:----:|:----:|:--------:|------|
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
|-------|:----:|:----:|:--------:|------|
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

## 13. 작업내역 관련 밸리데이션 <a id="db-settlement-work_time-validate"></a>

### `POST /api/setting/db/settlement/work_time/validate`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
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

## 14. 커스텀 컬럼 마이그레이션 #1 <a id="db-custom-migrate-1"></a>

### `POST /api/setting/db/custom/migrate/1`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| x     |  x   |  x   |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"custom_tables": ["asset_custom", "episode_custom", "shot_custom"]
	}
}
```

---

## 15. 커스텀 컬럼 마이그레이션 #2 <a id="db-custom-migrate-2"></a>

### `POST /api/setting/db/custom/migrate/2`

### permission

- `permission.do_global_setting`

### request

| param          | type  |      data       | required | desc |
|----------------|:-----:|:---------------:|:--------:|------|
| custom_columns | query | array of string |    x     |      |

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

## 16. 커스텀 컬럼 마이그레이션 #3 <a id="db-custom-migrate-3"></a>

### `POST /api/setting/db/custom/migrate/3`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| x     |  x   |  x   |    x     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"pass": "ok"
	}
}
```

- pass가 "ok"일 경우에만 17번 api를 호출 함

---

## 17. 커스텀 컬럼 마이그레이션 #4 <a id="db-custom-migrate-4"></a>

### `POST /api/setting/db/custom/migrate/4`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| x     |  x   |  x   |    x     |      |

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

## 18. 커스텀 컬럼 재 정렬 <a id="db-custom-order-validate"></a>

### `POST /api/setting/db/custom/order/validate`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| x     |  x   |  x   |    x     | x    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "커스텀 컬럼을 성공적으로 정렬했습니다."
	},
	"data": null
}
```

## 19. 사용 중인 프로젝트 체크 <a id="used-check"></a>

### `GET /api/{which}/{which_idx}/used/check`

### permission

- `permission.do_global_setting`

### request

| param     | type |  data   | required | desc                  |
|-----------|:----:|:-------:|:--------:|-----------------------|
| which     | path | string  |    O     | 지원 엘리먼트: status |
| which_idx | path | integer |    O     |                       |

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
				"idx": "1",
				"name": "Demo Big Bunny"
			},
			{
				"idx": "2",
				"name": "Holly Molly"
			}
		]
	}
}
```

## 20. 라이센스 수정 <a id="license-update"></a>

### `POST /api/license/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data  | required | desc        |
|-------------|:-----:|:------:|:--------:|-------------|
| license_key | query | string |    O     | 라이센스 키 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "라이센스를 갱신했습니다."
	},
	"data": null
}
```

## 21. 재로그인 안내 <a id="guide-credentials"></a>

### `POST /api/setting/guide/credentials`

### permission

- all

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| x     |  x   |  x   |    x     | x    |

### response

```json
{
  "error": {
    "code": 401,
    "message": "Your authentification token is expired. Please check your credentials again."
  },
  "data": null
}
```

## 22. 상태코드 밸리데이션 <a id="status-validate"></a>

### `POST /api/setting/status/validate`

### permission

- all

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| x     |  x   |  x   |    x     | x    |

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
[커스텀 컬럼 마이그레이션 #1]: #db-custom-migrate-1
[커스텀 컬럼 마이그레이션 #2]: #db-custom-migrate-2
[커스텀 컬럼 마이그레이션 #3]: #db-custom-migrate-3
[커스텀 컬럼 마이그레이션 #4]: #db-custom-migrate-4
[커스텀 컬럼 재정렬]: #db-custom-order-validate
[사용 중인 프로젝트 체크]: #used-check
[라이센스 수정]: #license-update
[재로그인 안내]: #guide-credentials
[상태코드 밸리데이션]: #status-validate
