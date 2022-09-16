# WH2API::Publish

## 목차

| 내용                    | slug                                                | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :---------------------- | :-------------------------------------------------- | :-------: | :-----: | :----: | :--: |
| 1. [퍼블리시 설정 생성] | /api/{which}/task/{task_idx}/publish/setting/create |   POST    |  일부   |   -    |  -   |
| 2. [퍼블리시 설정 조회] | /api/publish/setting/read                           |   POST    |   O\*   |   -    |  -   |
| 3. [퍼블리시 생성]      | /api/{which}/task/publish/create                    |   POST    |   O\*   | hooked |  -   |

- O\* - 버전 툴에서 사용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 퍼블리시 설정 생성 <a id="publish-setting-create"></a>

### `POST /api/{which}/task/{task_idx}/publish/setting/create`

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
		"publish_key": "MUJaT1BDOEh5VGwwL2dhWVp4eWp6RlBIQzRFYjlmMkV3RElEUHhza3V5L1QrdHJ5bUNrcHRib3VHVzdOY2J0MTR0cnpzUnBYU0treFc2R2Q1Tk5od1RmL0k1NTlvMmt0MWJ3YVJaNnBTZkE9",
		"user_lang": "EN",
		"api_uri": "http://182.231.41.120"
	}
}
```

---

## 2. 퍼블리시 설정 조회 <a id="publish-setting-read"></a>

### `POST /api/publish/setting/read`

### permission

- `permission.do_version_and_publish`

### request

| param       | type  |  data  | required | desc |
| ----------- | :---: | :----: | :------: | ---- |
| publish_key | query | string |    O     |      |

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
		"path_form": "[Fileserver]/[Project]/shot/[Episode]/[Sequence]/[Shot]/pub/[Publish]",
		"path": "[Fileserver]/prjA/shot/ep01/s0090/s0010_c0010/pub/[Publish]",
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
				"name": "WIP (now)",
				"color": "#03a9f4",
				"progress": "30",
				"description": null,
				"selected": true
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
		"version_history": [
			{
				"version_idx": "473",
				"name": "s0010_c0010_matchmove_v0010"
			},
			{
				"version_idx": "472",
				"name": "big_buck_bunny_1080p_h264"
			}
		]
	}
}
```

---

## 3. 퍼블리시 생성 <a id="publish-create"></a>

### `POST /api/{which}/task/publish/create`

### Webhook

- event: publish
- action: create

### permission

- `permission.do_version_and_publish`

### request

| param              | type  |      data       |  required   | desc                                      |
| ------------------ | :---: | :-------------: | :---------: | ----------------------------------------- |
| which              | path  |     string      |      O      | asset or shot                             |
| publish_key        | query |     string      |      O      | user_idx, kind, task_idx 가 포함되어 있음 |
| project_idx        | query |     integer     |      O      |                                           |
| asset_category_idx | query |     integer     | 에셋일 때 O |                                           |
| asset_idx          | query |     integer     | 에셋일 때 O |                                           |
| episode_idx        | query |     integer     |  샷일 때 O  |                                           |
| sequence_idx       | query |     integer     |  샷일 때 O  |                                           |
| shot_idx           | query |     integer     |  샷일 때 O  |                                           |
| task_status_idx    | query |     integer     |      O      |                                           |
| version_status_idx | query |     integer     |      O      |                                           |
| description        | query |     string      |      X      |                                           |
| publish_name       | query |     string      |      O      |                                           |
| main_path          | query |     string      |      O      | 메인이 되는 파일 혹은 폴더의 풀패스       |
| attached[]         | query | array of string |      O      | 첨부 파일의 파일명                        |
| attached_path[]    | query | array of string |      O      | 첨부 파일의 오리지널 풀패스               |
| attached_folder[]  | query | array of string |      O      | 첨부 폴더의 오리지널 풀패스               |
| tag[]              | query | array of string |      O      | 태그. 형식은 배열이나 현재 1개만 받음     |

- 퍼블리시 때는 실제 파일을 웜홀 2 서버에 업로드하지 않는다.

### response

```json
{
	"error": {
		"code": 200,
		"message": "버전이 생성됐습니다."
	},
	"data": {
		"publish": {
			"idx": "5"
		}
	}
}
```

---

## 끝

[퍼블리시 설정 생성]: #publish-setting-create
[퍼블리시 설정 조회]: #publish-setting-read
[퍼블리시 생성]: #publish-create
