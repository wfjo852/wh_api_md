# WH2API::Version

## 목차

| 내용                             | slug                                                           | 서버 구현 | 웹 적용 |
| :------------------------------- | :------------------------------------------------------------- | :-------: | :-----: |
| 1. [버전 설정 생성]              | /api/{which}/task/{task_idx}/version/setting/create            |   POST    |  일부   |
| 2. [버전 설정 조회]              | /api/version/setting/read                                      |   POST    |   O\*   |
| 3. [ftp 서버 목록 조회]          | /api/version/ftpserver/list                                    |   POST    |   O\*   |
| 4. [ftp 서버 목록 수정]          | /api/version/ftpserver/update                                  |   POST    |   O\*   |
| 5. [버전 생성]                   | /api/{which}/task/version/create                               |   POST    |   O\*   |
| 6. [버전 상태 코드 수정]         | /api/project/{project_idx}/version/{version_idx}/status/update |   POST    |    O    |
| 7. [패스트 버전 설정 생성]       | /api/project/{project_idx}/version/bulk/setting/create         |   POST    |    O    |
| 8. [패스트 버전 설정 조회]       | /api/version/bulk/setting/read                                 |   POST    |    X    |
| 9. [패스트 버전 데이터 검사하기] | /api/version/bulk/validate                                     |   POST    |    X    |
| 10. [버전 벌크 생성]             | /api/{which}/task/version/bulk/create                          |   POST    |    X    |
| 11. [샷의 마지막 버전 정보 조회] | /api/project/{project_idx}/shot/{shot_idx}/version/last/read   |    GET    |    X    |
| 12. [버전 메인 리뷰어 패스]      | /api/project/{project_idx}/version/{version_idx}/reviewer/pass |   POST    |    O    |

- O\* - 버전 툴, 패스트 버전 툴에서 사용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 버전 설정 생성 <a id="version-setting-create"></a>

### `POST /api/{which}/task/{task_idx}/version/setting/create`

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
				"name": "Waiting (now)"
			},
			{
				"status_idx": "2",
				"name": "WIP"
			},
			{
				"status_idx": "3",
				"name": "Done"
			}
		],
		"version_status": [
			{
				"status_idx": "1",
				"name": "Waiting"
			},
			{
				"status_idx": "2",
				"name": "WIP"
			},
			{
				"status_idx": "3",
				"name": "Done"
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

- 참고로 `task_status` 목록 중 현재 태스크의 상태 코드에는 `name`에 "(now)"라는 문구를 추가해서 내려옴

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
| reviewer_user_idx  | query |     integer      |      O      |                                           |
| cc_user_idx[]      | query | array of integer |      X      |                                           |
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
		"version_idx": "5"
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
		"status_name": "wip"
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
				"name": "Waiting"
			},
			{
				"status_idx": "2",
				"name": "WIP"
			},
			{
				"status_idx": "3",
				"name": "Done"
			}
		],
		"version_status": [
			{
				"status_idx": "1",
				"name": "Waiting"
			},
			{
				"status_idx": "2",
				"name": "WIP"
			},
			{
				"status_idx": "3",
				"name": "Done"
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
		"validated_rows": [1, 3, 4, 5],
		"not_validated_rows": [2],
		"not_assigned_rows": [7, 8]
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

### permission

- `permission.do_version_and_publish`

### request

| param                 | type  |      data       |  required   | desc                                      |
| --------------------- | :---: | :-------------: | :---------: | ----------------------------------------- |
| which                 | path  |     string      |      O      | asset or shot                             |
| version_key           | query |     string      |      O      | user_idx, kind, task_idx 가 포함되어 있음 |
| project_idx           | query |     integer     |      O      |                                           |
| asset_category_name[] | query | array of string | 에셋일 때 O |                                           |
| asset_name[]          | query | array of string | 에셋일 때 O |                                           |
| episode_idx           | query |     integer     |  샷일 때 O  |                                           |
| sequence_name[]       | query | array of string |  샷일 때 O  |                                           |
| shot_name[]           | query | array of string |  샷일 때 O  |                                           |
| task_name[]           | query | array of string |      O      |                                           |
| version_name[]        | query | array of string |      O      |                                           |
| task_status_idx       | query |     integer     |      O      | 변경할 태스크 상태                        |
| version_status_idx    | query |     integer     |      O      | 변경할 버전 상태                          |
| description[]         | query | array of string |      X      |                                           |
| hour_spent            | query |      float      |      O      | 버전을 올리는 데 걸린 시간(hour)          |
| reviewer_user_idx     | query |     integer     |      O      | 메인 리뷰어 user_idx                      |
| attached[]            | query |  array of file  |      O      | 첨부 파일                                 |
| attached_path[]       | query | array of string |      O      | 첨부 파일의 오리지널 풀패스               |
| metadata[]            | query | array of string |      X      | 첨부 파일의 메타데이터 (json)             |
| thumbnail[]           | query |  array of file  |      X      | 첨부 파일의 썸네일                        |

- asset_category_name[], asset_name[], sequence_name[], shot_name[], task_name[], version_name[], description[], main_path[], attached[], attached_path[] 갯수가 모두 동일해야 함

### response

```json
{
	"error": {
		"code": 200,
		"message": "버전이 생성됐습니다."
	},
	"data": null
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

### permission

- `permission.update_reviewer`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| project_idx   | path  | integer |    O     |      |
| version_idx   | path  | integer |    O     |      |
| from_user_idx | query | integer |    O     |      |
| to_user_idx   | query | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "메인 리뷰어가 변경됐습니다."
	},
	"data": {
		"user_idx": "1",
		"user_name": "Supervisor"
	}
}
```

---

## 끝

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
