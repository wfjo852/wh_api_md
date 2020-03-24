# WH2API::Track

## 목차

| 내용                            | slug                                                                                          | 서버 구현 | 웹 적용 |
| :------------------------------ | :-------------------------------------------------------------------------------------------- | :-------: | :-----: |
| 1. [트랙 버전 목록 조회]        | /api/project/{project_idx}/track/version/read[/{last}]                                        |    GET    |    O    |
|                                 | /api/project/{project_idx}/track/from/{from}/to/{to}/version/read[/{last}]                    |    GET    |    O    |
| 2. [트랙 샷 태스크 목록 조회]   | /api/project/{project_idx}/track/shot/task/read                                               |    GET    |    O    |
|                                 | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/track/shot/task/read |    GET    |    O    |
| 3. [트랙 에셋 태스크 목록 조회] | /api/project/{project_idx}/track/asset/task/read                                              |    GET    |    O    |
|                                 | /api/project/{project_idx}/category/{category_idx}/track/asset/task/read                      |    GET    |    O    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 트랙 버전 목록 조회 <a id="track-version-list"></a>

### `GET /api/project/{project_idx}/track/version/read[/{last}]`

### `GET /api/project/{project_idx}/track/from/{from}/to/{to}/version/read[/{last}]`

### permission

- `permission.do_track`

### request

| param       | type |  data   | required | desc       |
| ----------- | :--: | :-----: | :------: | ---------- |
| project_idx | path | integer |    O     |            |
| last        | path | integer |    X     |            |
| from        | path |  date   |    X     | YYYY-MM-DD |
| to          | path |  date   |    X     | YYYY-MM-DD |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"track": [
			{
				"idx": 1,
				"thumbnail": "/assets/images/common/shot_img02.jpg",
				"shot_asset_name": "s0010_c0010",
				"task_name": "comp",
				"task_status": "Waiting",
				"task_is_on": 1,
				"version_name": "s0010_c0010_comp_v002.mp4",
				"version_status": "retake",
				"comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
				"artist": "박종호",
				"reviewer": "김상인",
				"pass_to": "이진영",
				"review_comment": "",
				"request_time": "2018-12-19 17:39:20",
				"answer_time": ""
			},
			{
				"idx": 2,
				"thumbnail": "/assets/images/common/shot_img02.jpg",
				"shot_asset_name": "s0010_c0010",
				"task_name": "comp",
				"task_status": "Waiting",
				"task_is_on": 1,
				"version_name": "s0010_c0010_comp_v002.mp4",
				"version_status": "retake",
				"comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
				"artist": "박종호",
				"reviewer": "김상인",
				"pass_to": "이진영",
				"review_comment": "",
				"request_time": "2018-12-19 17:39:20",
				"answer_time": ""
			},
			{
				"idx": 3,
				"thumbnail": "/assets/images/common/shot_img02.jpg",
				"shot_asset_name": "s0010_c0010",
				"task_name": "comp",
				"task_status": "Waiting",
				"task_is_on": 1,
				"version_name": "s0010_c0010_comp_v002.mp4",
				"version_status": "retake",
				"comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
				"artist": "박종호",
				"reviewer": "김상인",
				"pass_to": "이진영",
				"review_comment": "",
				"request_time": "2018-12-19 17:39:20",
				"answer_time": ""
			}
		]
	}
}
```

---

## 2. 트랙 샷 태스크 목록 조회 <a id="track-shot-task-list"></a>

### `GET /api/project/{project_idx}/track/shot/task/read`

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/track/shot/task/read`

### permission

- `permission.do_track`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    X     |      |
| sequence_idx | path | integer |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"track": [
			{
				"shot_idx": 1,
				"snapshot": "/assets/images/common/shot_img02.jpg",
				"episode": "Episode 0001",
				"sequence": "sequence Name 0001",
				"shot": "Shot Name 0001",
				"task": "comp",
				"artist": "Artist 001",
				"status": "Retake",
				"start_date": "2018/11/13",
				"end_date": "2018/12/13",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"last_review_version": "",
				"last_publish_version": "",
				"is_on": 1
			},
			{
				"shot_idx": 2,
				"snapshot": "/assets/images/common/shot_img02.jpg",
				"episode": "Episode 0001",
				"sequence": "sequence Name 0001",
				"shot": "Shot Name 0001",
				"task": "comp",
				"artist": "Artist 001",
				"status": "Retake",
				"start_date": "2018/11/13",
				"end_date": "2018/12/13",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"last_review_version": "",
				"last_publish_version": "",
				"is_on": 1
			},
			{
				"shot_idx": 3,
				"snapshot": "/assets/images/common/shot_img02.jpg",
				"episode": "Episode 0001",
				"sequence": "sequence Name 0001",
				"shot": "Shot Name 0001",
				"task": "comp",
				"artist": "Artist 001",
				"status": "Retake",
				"start_date": "2018/11/13",
				"end_date": "2018/12/13",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"last_review_version": "",
				"last_publish_version": "",
				"is_on": 1
			}
		]
	}
}
```

## 3. 트랙 에셋 태스크 목록 조회 <a id="track-asset-task-list"></a>

### `GET /api/project/{project_idx}/track/asset/task/read`

### `GET /api/project/{project_idx}/category/{category_idx}/track/asset/task/read`

### permission

- `permission.do_track`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| category_idx | path | integer |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"track": [
			{
				"asset_idx": 1,
				"snapshot": "/assets/images/common/shot_img02.jpg",
				"asset_category": "Prod",
				"asset": "Asset Name 001",
				"task": "comp",
				"artist": "Artist 001",
				"status": "Publish",
				"start_date": "2018/11/13",
				"end_date": "2018/12/13",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"last_review_version": "",
				"last_publish_version": "",
				"is_on": 1
			},
			{
				"asset_idx": 2,
				"snapshot": "/assets/images/common/shot_img02.jpg",
				"asset_category": "Prod",
				"asset": "Asset Name 001",
				"task": "comp",
				"artist": "Artist 001",
				"status": "Publish",
				"start_date": "2018/11/13",
				"end_date": "2018/12/13",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"last_review_version": "",
				"last_publish_version": "",
				"is_on": 1
			},
			{
				"asset_idx": 3,
				"snapshot": "/assets/images/common/shot_img02.jpg",
				"asset_category": "Prod",
				"asset": "Asset Name 001",
				"task": "comp",
				"artist": "Artist 001",
				"status": "Publish",
				"start_date": "2018/11/13",
				"end_date": "2018/12/13",
				"description": "Lorem ipsum dolor sit amet, consectetur.",
				"last_review_version": "",
				"last_publish_version": "",
				"is_on": 1
			}
		]
	}
}
```

---

## 끝

[트랙 버전 목록 조회]: #track-version-list
[트랙 버전 목록 조회]: #track-version-list
[트랙 샷 태스크 목록 조회]: #track-shot-task-list
[트랙 샷 태스크 목록 조회]: #track-shot-task-list
[트랙 에셋 태스크 목록 조회]: #track-asset-task-list
[트랙 에셋 태스크 목록 조회]: #track-asset-task-list
