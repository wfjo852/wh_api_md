# WH2API::Version

## 목차

| 내용                             | slug                                                                   | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :------------------------------- | :--------------------------------------------------------------------- | :-------: | :-----: | :----: | :--: |
| 1. [버전 설정 생성]              | /api/{which}/task/{task_idx}/version/setting/create                    |   POST    |  일부   |   -    |  -   |
| 2. [버전 설정 조회]              | /api/version/setting/read                                              |   POST    |   O\*   |   -    |  -   |
| 3. [ftp 서버 목록 조회]          | /api/version/ftpserver/list                                            |   POST    |   O\*   |   -    |  -   |
| 4. [ftp 서버 목록 수정]          | /api/version/ftpserver/update                                          |   POST    |   O\*   |   -    |  -   |
| 5. [버전 생성]                   | /api/{which}/task/version/create                                       |   POST    |   O\*   | hooked |  O   |
| 6. [버전 상태 코드 수정]         | /api/project/{project_idx}/version/{version_idx}/status/update         |   POST    |    O    |   -    |  -   |
| 7. [패스트 버전 설정 생성]       | /api/project/{project_idx}/version/bulk/setting/create                 |   POST    |    O    |   -    |  -   |
| 8. [패스트 버전 설정 조회]       | /api/version/bulk/setting/read                                         |   POST    |    X    |   -    |  -   |
| 9. [패스트 버전 데이터 검사하기] | /api/version/bulk/validate                                             |  X POST   |    X    |   -    |  -   |
| 10. [버전 벌크 생성]             | /api/{which}/task/version/bulk/create                                  |   POST    |    X    | hooked |  O   |
| 11. [샷의 마지막 버전 정보 조회] | /api/project/{project_idx}/shot/{shot_idx}/version/last/read           |    GET    |    X    |   -    |  -   |
| 12. [버전 메인 리뷰어 패스]      | /api/project/{project_idx}/version/{version_idx}/reviewer/pass         |   POST    |    O    | hooked |  O   |
| 13. [버전 목록 조회]             | /api/project/{project_idx}/{which}/task/{task_idx}/version/list        |    GET    |    X    |   -    |  -   |
| 14. [참조 리뷰어 목록 조회]      | /api/project/{project_idx}/version/{version_idx}/reviewer/cc/list      |    GET    |    O    |   -    |  -   |
| 15. [참조 리뷰어 목록 수정]      | /api/project/{project_idx}/version/{version_idx}/reviewer/cc/update    |   POST    |    O    | hooked |  O   |
| 16. [버전 정보 조회]             | /api/version/{version_idx}/read                                        |   X GET   |    X    |   -    |  -   |
| 17. [버전 정보 수정]             | /api/project/{project_idx}/version/{version_idx}/update                |   POST    |    X    | hooked |  O   |
| 18. [버전 파일 리스트]           | /api/project/{project_idx}/version/from/{from}/to/{to}/attachment/list |    GET    |    O    |   -    |  -   |
| 19. [버전 파일 개수 조회]        | /api/project/{project_idx}/version/attachment/count/{yyyy}/{mm}/list   |    GET    |    O    |   -    |  -   |
| 20. [버전 파일 벌크 정보 수정]   | /api/version/attachment/bulk/update                                    |   POST    |    O    |   -    |  -   |
| 21. [버전 벌크 삭제]             | /api/version/bulk/delete                                               |   POST    |    O    |   -    |  -   |
| 22. [버전의 blob 조회]           | /api/version/{version_idx}/blob/read                                   |    GET    |    O    |   -    |  -   |

## 목차 V2

| 내용                     | slug                               | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :----------------------- | :--------------------------------- | :-------: | :-----: | :----: | :--: |
| A1. [버전 추가]          | /api/versions/create               |   POST    |    O    |   -    |  -   |
| A2. [버전 첨부파일 추가] | /api/version_attachments/create    |   POST    |    O    |   -    |  -   |
| A3. [버전 추가 완료]     | /api/versions/{version_idx}/finish |   POST    |    O    | hooked |  O   |
| A4. [버전 벌크 삭제]     | /api/versions/bulk/delete          |   POST    |    O    |   -    |  -   |

- O\* - 버전 툴, 패스트 버전 툴에서 사용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 버전 설정 생성 <a id="version-setting-create"></a>

### `POST /api/{which}/task/{task_idx}/version/setting/create`

### Webhook

- event: version
- action: create

### permission

- `permission.do_version_and_publish`

### request

| param    | type |  data   | required | desc              |
| -------- | :--: | :-----: | :------: | ----------------- |
| which    | path | string  |    O     | `shot` or `asset` |
| task_idx | path | integer |    O     |                   |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version_key": "MUJaT1BDOEh5VGwwL2dhWVp4eWp6RlBIQzRFYjlmMkV3RElEUHhza3V5L1QrdHJ5bUNrcHRib3VHVzdOY2J0MTR0cnpzUnBYU0treFc2R2Q1Tk5od1RmL0k1NTlvMmt0MWJ3YVJaNnBTZkE9",
		"user_lang": "EN",
		"api_uri": "http://182.231.41.120"
	}
}
```

---

## 2. 버전 설정 조회 <a id="version-setting-read"></a>

### `POST /api/version/setting/read`

### permission

- `permission.do_version_and_publish`

### request

| param       | type  |  data  | required | desc |
| ----------- | :---: | :----: | :------: | ---- |
| version_key | query | string |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"user_idx": "1",
		"kind": "2",
		"project_name": "abc",
		"project_idx": "1",
		"episode_name": "e01",
		"episode_idx": "1",
		"sequence_name": "s0010",
		"sequence_idx": "1",
		"shot_name": "c0010",
		"shot_idx": "1",
		"tasktype_name": "Animation",
		"task_idx": "4",
		"fileserver_windows": "/aa/dd/folder",
		"fileserver_osx": "/aa/dd/folder",
		"fileserver_linux": "/aa/dd/folder",
		"path_form": "[Fileserver]/[Project]/shot/[Episode]/[Sequence]/[Shot]/version/[User]/[Today]/[Version]",
		"path": "[Fileserver]/prjA/shot/ep01/s0090/s0010_c0010/version/cccc/2019-03-18/[Version]",
		"task_status": [
			{
				"status_idx": "1",
				"name": "Waiting (now)",
				"color": "#dbd8db",
				"progress": "5",
				"description": null
			},
			{
				"status_idx": "2",
				"name": "WIP",
				"color": "#03a9f4",
				"progress": "30",
				"description": null
			},
			{
				"status_idx": "3",
				"name": "Done",
				"color": "#f44336",
				"progress": "10",
				"description": null
			}
		],
		"version_status": [
			{
				"status_idx": "1",
				"name": "Waiting",
				"color": "#dbd8db",
				"progress": "5",
				"description": null
			},
			{
				"status_idx": "2",
				"name": "WIP",
				"color": "#03a9f4",
				"progress": "30",
				"description": null
			},
			{
				"status_idx": "3",
				"name": "Done",
				"color": "#f44336",
				"progress": "10",
				"description": null
			}
		],
		"reviewer_main": [
			{
				"user_idx": "1",
				"name": "KIM"
			},
			{
				"user_idx": "2",
				"name": "HONG"
			},
			{
				"user_idx": "3",
				"name": "James"
			}
		],
		"reviewer_cc": [
			{
				"user_idx": "1",
				"name": "KIM"
			},
			{
				"user_idx": "2",
				"name": "HONG"
			},
			{
				"user_idx": "4",
				"name": "Lee"
			}
		]
	}
}
```

---

## 3. ftp 서버 목록 조회 <a id="ftpserver-list"></a>

### `POST /api/version/ftpserver/list`

### permission

- `permission.do_version_and_publish`

### request

| param       | type  |  data  | required | desc |
| ----------- | :---: | :----: | :------: | ---- |
| version_key | query | string |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"ftpserver_list": [
			{
				"checking": "true",
				"ip": "115.93.255.205",
				"protocol": "ftp",
				"port": "21",
				"account": "outsourcing",
				"pw": "2018jya",
				"path": "/outsourcing/drp_test"
			},
			{
				"checking": "false",
				"ip": "112.118.229.111",
				"protocol": "ftp",
				"port": "21",
				"account": "abcd",
				"pw": "aoqiw",
				"path": "/doqi/woq"
			}
		]
	}
}
```

---

## 4. ftp 서버 목록 수정 <a id="ftpserver-update"></a>

### `POST /api/version/ftpserver/update`

### permission

- `permission.do_version_and_publish`

### request

| param       | type  |  data  | required | desc |
| ----------- | :---: | :----: | :------: | ---- |
| version_key | query | string |    O     |      |
| checking[]  | query | string |    O     |      |
| ip[]        | query | string |    O     |      |
| protocol[]  | query | string |    O     |      |
| port[]      | query | string |    O     |      |
| account[]   | query | string |    O     |      |
| pw[]        | query | string |    O     |      |
| path[]      | query | string |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "서버 목록이 갱신됐습니다."
	},
	"data": null
}
```

---

## 5. 버전 생성 <a id="version-create"></a>

### `POST /api/{which}/task/version/create`

### permission

- `permission.do_version_and_publish`

### request

| param              | type  |       data       |  required   | desc                                      |
| ------------------ | :---: | :--------------: | :---------: | ----------------------------------------- |
| which              | path  |      string      |      O      | asset or shot                             |
| version_key        | query |      string      |      O      | user_idx, kind, task_idx 가 포함되어 있음 |
| project_idx        | query |     integer      |      O      |                                           |
| asset_category_idx | query |     integer      | 에셋일 때 O |                                           |
| asset_idx          | query |     integer      | 에셋일 때 O |                                           |
| episode_idx        | query |     integer      |  샷일 때 O  |                                           |
| sequence_idx       | query |     integer      |  샷일 때 O  |                                           |
| shot_idx           | query |     integer      |  샷일 때 O  |                                           |
| version_name       | query |      string      |      O      |                                           |
| task_status_idx    | query |     integer      |      O      |                                           |
| version_status_idx | query |     integer      |      O      |                                           |
| description        | query |      string      |      X      |                                           |
| hour_spent         | query |      float       |      O      | 버전을 올리는 데 걸린 시간(hour)          |
| reviewer_user_idx  | query |     integer      |      O      | 메인 리뷰어 user_idx                      |
| cc_user_idx[]      | query | array of integer |      X      | 참조 리뷰어 user_idx                      |
| main_path          | query |      string      |      O      | 메인이 되는 파일 혹은 폴더의 풀패스       |
| attached[]         | query |  array of file   |      O      | 첨부 파일                                 |
| attached_path[]    | query | array of string  |      O      | 첨부 파일의 오리지널 풀패스               |
| attached_folder[]  | query | array of string  |      O      | 첨부 폴더의 오리지널 풀패스               |
| metadata[]         | query | array of string  |      X      | 첨부 파일의 메타데이터 (json)             |
| thumbnail          | query |       file       |      X      | 메인 파일의 썸네일                        |

- attached[] 와 attached_path[], metadata[]의 갯수는 동일해야 함

### response

```json
{
	"error": {
		"code": 200,
		"message": "버전이 생성됐습니다."
	},
	"data": {
		"version": {
			"kind": "shot",
			"idx": "5",
			"name": "s0010_c0010_matchmove_v0010
		}
	}
}
```

---

## 6. 버전 상태 코드 수정 <a id="version-status-update"></a>

### `POST /api/project/{project_idx}/version/{version_idx}/status/update`

### permission

- `permission.do_task_and_version_status`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| version_idx | path  | integer |    O     |      |
| status_idx  | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "버전의 상태 코드가 변경됐습니다."
	},
	"data": {
		"status_idx": "1",
		"status_name": "wip",
		"assigned": true
	}
}
```

---

## 7. 패스트 버전 설정 생성 <a id="version-bulk-setting-create"></a>

### `POST /api/project/{project_idx}/version/bulk/setting/create`

### permission

- `permission.do_other_version_and_publish`

### request

| param       | type  |  data   | required | desc                      |
| ----------- | :---: | :-----: | :------: | ------------------------- |
| project_idx | path  | integer |    O     |                           |
| episode_idx | query | integer |    O     | kind == 'asset' 인 경우 0 |
| kind        | query | string  |    O     | 'shot' or 'asset'         |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version_key": "MUJaT1BDOEh5VGwwL2dhWVp4eWp6RlBIQzRFYjlmMkV3RElEUHhza3V5L1QrdHJ5bUNrcHRib3VHVzdOY2J0MTR0cnpzUnBYU0treFc2R2Q1Tk5od1RmL0k1NTlvMmt0MWJ3YVJaNnBTZkE9",
		"user_lang": "EN",
		"api_uri": "http://182.231.41.120"
	}
}
```

---

## 8. 패스트 버전 설정 조회 <a id="version-bulk-setting-read"></a>

### `POST /api/version/bulk/setting/read`

### permission

- `permission.do_other_version_and_publish`

### request

| param       | type  |  data  | required | desc |
| ----------- | :---: | :----: | :------: | ---- |
| version_key | query | string |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"user_idx": "1",
		"kind": "2",
		"project_name": "abc",
		"project_idx": "1",
		"episode_name": "ep1", // kind = 2 (샷)인 경우에만
		"episode_idx": "2", // kind = 2 (샷)인 경우에만
		"fileserver_windows": "/aa/dd/folder",
		"fileserver_osx": "/aa/dd/folder",
		"fileserver_linux": "/aa/dd/folder",
		"path_form": "[Fileserver]/[Project]/shot/[Episode]/[Sequence]/[Shot]/version/[User]/[Today]/[Version]",
		"task_status": [
			{
				"status_idx": "1",
				"name": "Waiting",
				"color": "#dbd8db",
				"progress": "5",
				"description": null
			},
			{
				"status_idx": "2",
				"name": "WIP",
				"color": "#03a9f4",
				"progress": "30",
				"description": null
			},
			{
				"status_idx": "3",
				"name": "Done",
				"color": "#f44336",
				"progress": "10",
				"description": null
			}
		],
		"version_status": [
			{
				"status_idx": "1",
				"name": "Waiting",
				"color": "#dbd8db",
				"progress": "5",
				"description": null
			},
			{
				"status_idx": "2",
				"name": "WIP",
				"color": "#03a9f4",
				"progress": "30",
				"description": null
			},
			{
				"status_idx": "3",
				"name": "Done",
				"color": "#f44336",
				"progress": "10",
				"description": null
			}
		],
		"reviewer_main": [
			{
				"user_idx": "1",
				"name": "KIM"
			},
			{
				"user_idx": "2",
				"name": "HONG"
			},
			{
				"user_idx": "3",
				"name": "James"
			}
		],
		"reviewer_cc": [
			{
				"user_idx": "1",
				"name": "C2MonsterAA"
			},
			{
				"user_idx": "2",
				"name": "Artist"
			}
		]
	}
}
```

---

## 9. 패스트 버전 데이터 검사하기 <a id="version-bulk-validate"></a>

### `POST /api/version/bulk/validate`

### permission

- `permission.do_other_version_and_publish`

### request

| param           | type  |      data       |  required   | desc              |
| --------------- | :---: | :-------------: | :---------: | ----------------- |
| version_key     | query |     string      |      O      |                   |
| kind            | query |     string      |      O      | 'shot' or 'asset' |
| project_idx     | query |     integer     |      O      | 프로젝트 인덱스   |
| episode_idx     | query |     integer     |  샷일 때 O  | 에피소드 인덱스   |
| sequence_name[] | query | array of string |  샷일 때 O  | 시퀀스 이름       |
| shot_name[]     | query | array of string |  샷일 때 O  | 샷 이름           |
| category_name[] | query | array of string | 에셋일 때 O | 카테고리 이름     |
| asset_name[]    | query | array of string | 에셋일 때 O | 에셋 이름         |
| task_name[]     | query | array of string |      O      |                   |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"result": false,
		"validated_rows": [
			{
				"row": 1,
				"version_key": "asdasdasdas"
			},
			{
				"row": 3,
				"version_key": "asdasdasdas"
			},
			{
				"row": 4,
				"version_key": "asdasdasdas"
			}
		],
		"not_validated_rows": [2],
		"not_assigned_rows": [5, 6]
	}
}
```

- `data.result`의 열(rows)은 `0`부터 시작함.

  - `validated_rows`: 각종 인덱스와 이름에 대당하는 태스크가 존재하고 이용자에게 할당된 열 (즉, 작업할 수 있는 열)
  - `not_validated_rows`: 태스크의 정보가 없는 열
  - `not_assigned_rows`: 태스크는 존재하나 이용자에게 할당되지 않은 열

- `data.result` 값은 성공하면 `true`, 실패하면 `false`

---

## 10. 버전 벌크 생성 <a id="version-bulk-create"></a>

### `POST /api/{which}/task/version/bulk/create`

### Webhook

- event: version
- action: bulk create

### permission

- `permission.do_version_and_publish`

### request

| param                 | type  |       data       |  required   | desc                                      |
| --------------------- | :---: | :--------------: | :---------: | ----------------------------------------- |
| which                 | path  |      string      |      O      | asset or shot                             |
| version_key           | query |      string      |      O      | user_idx, kind, task_idx 가 포함되어 있음 |
| project_idx           | query |     integer      |      O      |                                           |
| asset_category_name[] | query | array of string  | 에셋일 때 O |                                           |
| asset_name[]          | query | array of string  | 에셋일 때 O |                                           |
| episode_idx           | query |     integer      |  샷일 때 O  |                                           |
| sequence_name[]       | query | array of string  |  샷일 때 O  |                                           |
| shot_name[]           | query | array of string  |  샷일 때 O  |                                           |
| task_name[]           | query | array of string  |      O      |                                           |
| version_name[]        | query | array of string  |      O      |                                           |
| task_status_idx       | query |     integer      |      O      | 변경할 태스크 상태                        |
| version_status_idx    | query |     integer      |      O      | 변경할 버전 상태                          |
| description[]         | query | array of string  |      X      |                                           |
| hour_spent            | query |      float       |      O      | 버전을 올리는 데 걸린 시간(hour)          |
| reviewer_user_idx     | query |     integer      |      O      | 메인 리뷰어 user_idx                      |
| cc_user_idx[]         | query | array of integer |      X      | 참조 리뷰어 user_idx                      |
| attached[]            | query |  array of file   |      O      | 첨부 파일                                 |
| attached_path[]       | query | array of string  |      O      | 첨부 파일의 오리지널 풀패스               |
| metadata[]            | query | array of string  |      X      | 첨부 파일의 메타데이터 (json)             |
| thumbnail[]           | query |  array of file   |      X      | 첨부 파일의 썸네일                        |

- asset_category_name[], asset_name[], sequence_name[], shot_name[], task_name[], version_name[], description[], main_path[], attached[], attached_path[] 갯수가 모두 동일해야 함

### response

```json
{
	"error": {
		"code": 200,
		"message": "버전이 생성됐습니다."
	},
	"data": {
		"versions": [
			{
				"kind": "shot",
				"idx": "19",
				"name": "s0010_c0010_Ani_v0010"
			},
			{
				"kind": "shot",
				"idx": "20",
				"name": "s0010_c0010_Color_v0030"
			}
		]
	}
}
```

---

## 11. 샷의 마지막 버전 정보 조회 <a id="shot-last-version-read"></a>

### `GET /api/project/{project_idx}/shot/{shot_idx}/version/last/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| shot_idx    | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "Success"
	},
	"data": {
		"project_idx": "1",
		"project_name": "Demo_Bigbuck_Bunny",
		"episode_idx": "1",
		"episode_name": "Ep01",
		"sequence_idx": "1",
		"sequence_name": "s0010",
		"shot_idx": "1",
		"shot_name": "s0010_c0010",
		"task_name": "Animation",
		"task_idx": "4",
		"version_idx": "1",
		"version_name": "big_s0010_c0010_anim_v001",
		"local_file_path": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0010_anim_v001.mp4",
		"created_time": "2019-04-08 17:30:59",
		"user_idx": "2",
		"user_name": "Artist",
		"version_status_name": "retake",
		"shot_status_name": "wip"
	}
}
```

---

## 12. 버전 메인 리뷰어 패스 <a id="version-reviewer-pass"></a>

### `POST /api/project/{project_idx}/version/{version_idx}/reviewer/pass`

### Webhook

- event: version
- action: reviewer pass

### permission

- `permission.update_reviewer`

### request

| param          | type  |  data   | required | desc |
| -------------- | :---: | :-----: | :------: | ---- |
| project_idx    | path  | integer |    O     |      |
| version_idx    | path  | integer |    O     |      |
| from_user_idx  | query | integer |    O     |      |
| to_user_idx    | query | integer |    O     |      |
| from_user_name | query | string  |    X     |      |
| to_user_name   | query | string  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "메인 리뷰어가 변경됐습니다."
	},
	"data": {
		"version_idx": 16,
		"main_reviewer": {
			"idx": "1",
			"name": "Supervisor",
			"id": "c4m",
			"email": ""
		},
		"cc_reviewers": [
			{
				"idx": "2",
				"name": "Artist",
				"id": "c3m",
				"email": ""
			},
			{
				"idx": "4",
				"name": "Administrator",
				"id": "c5m",
				"email": ""
			}
		]
	}
}
```

---

## 13. 버전 목록 조회 <a id="version-list"></a>

### `GET /api/project/{project_idx}/{which}/task/{task_idx}/version/list`

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| which       | path | string  |    O     |      |
| task_idx    | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "Success"
	},
	"data": {
		"versions": [
			{
				"idx": "1",
				"name": "big_s0010_c0010_anim_v001",
				"description": "Confirm_check",
				"hour_spent": "2"
			}
		]
	}
}
```

---

## 14. 참조 리뷰어 목록 조회 <a id="reviewer-cc-list"></a>

### `GET /api/project/{project_idx}/version/{version_idx}/reviewer/cc/list`

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| version_idx | path | integer |    O     |      |

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
				"idx": "1",
				"name": "charles"
			},
			{
				"idx": "2",
				"name": "tom"
			},
			{
				"idx": "3",
				"name": "superv"
			},
			{
				"idx": "4",
				"name": "kim"
			}
		],
		"cc_reviewers": ["2", "3"],
		"cc_not_reviewers": ["4"]
	}
}
```

---

## 15. 참조 리뷰어 목록 수정 <a id="reviewer-cc-update"></a>

### `POST /api/project/{project_idx}/version/{version_idx}/reviewer/cc/update`

### Webhook

- event: version
- action: cc update

### permission

- `permission.do_version_and_publish`

### request

| param       | type  |       data       | required | desc |
| ----------- | :---: | :--------------: | :------: | ---- |
| project_idx | path  |     integer      |    O     |      |
| version_idx | path  |     integer      |    O     |      |
| user_idx[]  | query | array of integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version_idx": 16,
		"cc_reviewers": [
			{
				"idx": "2",
				"name": "Artist"
			}
		]
	}
}
```

---

## 16. 버전 정보 조회 <a id="version-read"></a>

### `GET /api/version/{version_idx}/read`

### Webhook

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| version_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version": {
			"idx": "1",
			"name": "big_s0010_c0010_anim_v001",
			"description": "Confirm_check",
			"kind": "shot",
			"project": {
				"idx": "1",
				"name": "Demo_Bigbuck_Bunny",
				"description": "Demo_Bigbuck_Bunny",
				"start_date": "2018-12-11",
				"end_date": "2019-04-12"
			},
			"episode": {
				"idx": "1",
				"name": "Ep01",
				"description": "Demo_Bigbuck_Bunny_First"
			},
			"sequence": {
				"idx": "1",
				"name": "s0010",
				"description": "Opening Sequence"
			},
			"shot": {
				"idx": "1",
				"name": "s0010_c0010"
			},
			"task": {
				"idx": "4",
				"start_date": "2019-04-05",
				"end_date": "2019-04-11"
			},
			"user": {
				"idx": "2",
				"name": "Artist",
				"id": "c3m",
				"email": "artist@c2monster.com",
				"thumbnail": "http://localhost:81/2019/04/08/dc3295a0a38e89e9.png"
			},
			"main_reviewer": {
				"idx": "4",
				"name": "Supervisor",
				"id": "c4m",
				"email": "",
				"thumbnail": "http://localhost:81/2019/04/08/d63b00a6934f6b55.png"
			},
			"cc_reviewers": [
				{
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
				},
				{
					"idx": "2",
					"name": "Artist",
					"id": "c3m",
					"email": "artist@c2monster.com",
					"thumbnail": "http://localhost:81/2019/04/08/dc3295a0a38e89e9.png"
				}
			],
			"url": "http://localhost/project/1/version/1/detail",
			"attachments": [
				{
					"idx": "1",
					"name": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0010_anim_v001.mp4",
					"url": "http://localhost:81/2019/04/08/816982d46b930845.mp4",
					"mime_type": ["video", "mp4"],
					"is_main": "1"
				}
			]
		}
	}
}
```

---

## 17. 버전 정보 수정 <a id="version-update"></a>

### `POST /api/project/{project_idx}/version/{version_idx}/update`

### Webhook

- event: version
- action: update

### permission

- `permission.do_version_and_publish`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| version_idx | path  | integer |    O     |      |
| column      | query | string  |    O     |      |
| new_val     | query | string  |    O     |      |
| old_val     | query | string  |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "Version information is edited."
	},
	"data": {
		"version": {
			"kind": "shot",
			"idx": 1,
			"column": "artist",
			"value": "Artist",
			"status": {
				"idx": 1
			}
		}
	}
}
```

---

## 18. 버전 파일 리스트 <a id="version-attachment-list"></a>

### `GET /api/project/{project_idx}/version/from/{from}/to/{to}/attachment/list`

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| from        | path | string  |    O     |      |
| to          | path | string  |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"attachments": [
			{
				"idx": "17",
				"name": "big_s0010_c0020_animation_v001.mp4",
				"path": "/Users/bumyeol/Documents/wormhole_sample_video/big_s0010_c0020_animation_v001.mov",
				"version": {
					"idx": "16",
					"name": "big_s0010_c0010_animation_v001",
					"thumbnail": "http://localhost:81/2021/02/23/033755189346e9d1.png",
					"kind": "shot"
				},
				"shot_asset": {
					"idx": "1",
					"name": "s0010_c0010"
				},
				"task": {
					"idx": "1",
					"name": "Comp"
				}
			}
		]
	}
}
```

---

## 19. 버전 파일 개수 조회 <a id="version-attachment-count-list"></a>

### `GET /api/project/{project_idx}/version/attachment/count/{yyyy}/{mm}/list`

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc        |
| ----------- | :--: | :-----: | :------: | ----------- |
| project_idx | path | integer |    O     |             |
| yyyy        | path | string  |    O     | year (YYYY) |
| mm          | path | string  |    O     | month (MM)  |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"attachments_per_date": [
			{ "date": "2020-07-16", "count": "22", "prev_no_more": false },
			{ "date": "2020-07-21", "count": "31" },
			{ "date": "2020-07-22", "count": "4" },
			{ "date": "2020-07-24", "count": "9" },
			{ "date": "2020-07-29", "count": "30", "next_no_more": false }
		],
		"move": {
			"prev": { "year": "2020", "month": "03" },
			"next": { "year": "2020", "month": "08" }
		}
	}
}
```

---

## 20. 버전 파일 벌크 정보 수정 <a id="version-attachment-bulk-update"></a>

### `POST /api/version/attachment/bulk/update`

### permission

- `permission.do_version_and_publish`

### request

| param                    | type  |       data       | required | desc                    |
| ------------------------ | :---: | :--------------: | :------: | ----------------------- |
| version_idx[]            | query | array of integer |    O     |                         |
| version_attachment_idx[] | query | array of integer |    O     |                         |
| column[]                 | query | array of string  |    O     | 버전 파일의 수정할 항목 |
| old_val[]                | query | array of string  |    O     |                         |
| new_val[]                | query | array of string  |    O     |                         |

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

## 21. 버전 벌크 삭제 <a id="version-bulk-delete"></a>

### `POST /api/version/bulk/delete`

### permission

- `permission.do_version_and_publish`

### request

| param         | type  | data  | required | desc |
| ------------- | :---: | :---: | :------: | ---- |
| version_idxes | query | array |    O     |      |

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

## 22. 버전 blob 조회<a id="version-blob-read"></a>

### `GET /api/version/{version_idx}/blob/read`

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| version_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"version_idx": "43",
		"kind": "asset",
		"name": "c100_lung_modeling sheet_v2",
		"thumbnail": "/2021/03/12/b8c3f77d2c993be1.png",
		"status_idx": "5",
		"status_name": "final",
		"version_attachment_idx": "51",
		"file_url": "http://localhost:81/2021/03/12/7a816ac33cc3d47f.jpg",
		"name_original": "\\\\mserver\\MF\\01_plan\\03_Artwork\\01_ch\\c100_lung\\2 sheet\\c100_lung_modeling sheet_v2.jpg",
		"metadata": {
			"frames": 3,
			"fps": 24,
			"duration": 0.125
		},
		"blob": "...."
	}
}
```

---

## A1. 버전 추가 <a id="versions-create"></a>

### `POST /api/versions/create`

### permission

- `permission.do_version_and_publish`

### request

| param              | type  |       data       |  required   | desc                                      |
| ------------------ | :---: | :--------------: | :---------: | ----------------------------------------- |
| which              | query |      string      |      O      | `asset` or `shot`                         |
| version_key        | query |      string      |      O      | user_idx, kind, task_idx 가 포함되어 있음 |
| version_name       | query |      string      |      O      |                                           |
| task_status_idx    | query |     integer      |      O      |                                           |
| version_status_idx | query |     integer      |      O      |                                           |
| description        | query |      string      |      X      |                                           |
| hour_spent         | query |      float       |      O      | 버전을 올리는 데 걸린 시간(hour)          |
| reviewer_user_idx  | query |     integer      |      O      | 메인 리뷰어 user_idx                      |
| cc_user_idx[]      | query | array of integer |      X      | 참조 리뷰어 user_idx                      |
| thumbnail          | query |       file       |      X      | 버전 썸네일                               |

- attached[] 와 attached_path[], metadata[]의 갯수는 동일해야 함

### response

```json
{
	"error": {
		"code": 200,
		"message": "버전이 생성됐습니다."
	},
	"data": {
		"version": {
			"kind": "shot",
			"idx": "5",
			"name": "s0010_c0010_matchmove_v0010
		}
	}
}
```

---

## A2. 버전 첨부파일 추가 <a id="version-attachments-create"></a>

### `POST /api/version_attachments/create`

### permission

- `permission.do_version_and_publish`

### request

| param                | type  |  data   |  required  | desc                          |
| -------------------- | :---: | :-----: | :--------: | ----------------------------- |
| version_key          | path  | string  |     O      | 버전 생성할 때 받은 버전 키   |
| version_idx          | path  | integer |     O      |                               |
| is_main              | query | integer |     O      | 버전의 메인이면 1, 아니면 0   |
| is_file              | query | integer |     O      | 파일이면 1, 아니면(폴더면F) 0 |
| attached             | query |  file   | 파일이면 O | 첨부파일                      |
| attached_path        | query | string  | 파일이면 O | 첨부파일의 원본 경로          |
| attached_folder      | query | string  |  폴더면 O  | 첨부파일 대신 폴더만 입력     |
| metadata[]           | query |  json   |     X      | 첨부파일의 메타데이터         |
| file                 | query |  file   | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowChunkNumber      | query | integer | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowChunkSize        | query | integer | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowCurrentChunkSize | query | integer | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowTotalSize        | query | integer | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowIdentifier       | query | string  | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowFilename         | query | string  | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowRelativePath     | query | string  | 파일이면 O | 청크 업로드를 위한 필수 정보  |
| flowTotalChunks      | query | integer | 파일이면 O | 청크 업로드를 위한 필수 정보  |

### response (청크 업로드 진행 중)

```json
{
	"error": {
		"code": 202,
		"message": "청크 업로드를 진행 중입니다."
	},
	"data": null
}
```

### response

```json
{
	"error": {
		"code": 200,
		"message": "파일이 업로드됐습니다."
	},
	"data": {
		"version": {
			"idx": 5,
			"attachment": {
				"idx": 55
			}
		}
	}
}
```

---

## A3. 버전 추가 완료 <a id="versions-finish"></a>

### `POST /api/versions/{version_idx}/finish`

### permission

- `permission.do_version_and_publish`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| version_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "완료"
	},
	"data": null
}
```

---

## A4. 버전 벌크 삭제 <a id="versions-bulk-delete"></a>

### `POST /api/versions/bulk/delete`

### permission

- `permission.do_version_and_publish`

### request

| param         | type  |       data       | required | desc |
| ------------- | :---: | :--------------: | :------: | ---- |
| version_idx[] | query | array of integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "완료"
	},
	"data": null
}
```

---

## 끝

---

[버전 설정 생성]: #version-setting-create
[버전 설정 조회]: #version-setting-read
[ftp 서버 목록 조회]: #ftpserver-list
[ftp 서버 목록 수정]: #ftpserver-update
[버전 생성]: #version-create
[버전 상태 코드 수정]: #version-status-update
[패스트 버전 설정 생성]: #version-bulk-setting-create
[패스트 버전 설정 조회]: #version-bulk-setting-read
[패스트 버전 데이터 검사하기]: #version-bulk-validate
[버전 벌크 생성]: #version-bulk-create
[샷의 마지막 버전 정보 조회]: #shot-last-version-read
[버전 메인 리뷰어 패스]: #version-reviewer-pass
[버전 목록 조회]: #version-list
[참조 리뷰어 목록 조회]: #reviewer-cc-list
[참조 리뷰어 목록 수정]: #reviewer-cc-update
[버전 정보 조회]: #version-read
[버전 정보 수정]: #version-update
[버전 파일 리스트]: #version-attachment-list
[버전 파일 개수 조회]: #version-attachment-count-list
[버전 파일 벌크 정보 수정]: #version-attachment-bulk-update
[버전 벌크 삭제]: #version-bulk-delete
[버전의 blob 조회]: #version-blob-read
[버전 추가]: #versions-create
[버전 첨부파일 추가]: #version-attachments-create
[버전 추가 완료]: #versions-finish
[버전 벌크 삭제]: #versions-bulk-delete
