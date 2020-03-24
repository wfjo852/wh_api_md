# WH2API::Sequence

- `project.md` 와 일부 합칠 예정

## 목차

| 내용                  | slug                                                                            | 서버 구현 | 웹 적용 |
| :-------------------- | :------------------------------------------------------------------------------ | :-------: | :-----: |
| 1. [시퀀스 등록]      | /api/project/{project_idx}/episode/{episode_idx}/sequence/create                |   POST    |    O    |
| 2. [시퀀스 정보 수정] | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/update |   POST    |    O    |
| 3. [시퀀스 삭제]      | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/delete |   POST    |    O    |
| 4. [시퀀스 활성화]    | /api/project/{project_idx}/sequence/{sequence_idx}/activate                     |   POST    |    O    |
| 5. [시퀀스 비활성화]  | /api/project/{project_idx}/sequence/{sequence_idx}/deactivate                   |   POST    |    O    |
| 6. [시퀀스 목록 조회] | /api/project/{project_idx}/episode/{episode_idx}/sequence/list                  |    GET    |    O    |

- 참조<sup>1</sup> - /api/project/{project_idx}/episode/list[/{detail}] (project-shot-overview.md 참조)

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 시퀀스 등록 <a id="project-sequence-create"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/create`

### permission

- `permission.update_project`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| project_idx   | path  | integer |    O     |      |
| episode_idx   | path  | string  |    O     |      |
| sequence_name | query | string  |    O     |      |
| description   | query | string  |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "시퀀스가 생성 되었습니다."
	},
	"data": {
		"sequence_idx": 7
	}
}
```

---

## 2. 시퀀스 수정 <a id="#project-sequence-update"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/update`

### permission

- `permission.update_project`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| project_idx   | path  | integer |    O     |      |
| episode_idx   | path  | integer |    O     |      |
| sequence_idx  | path  | integer |    O     |      |
| sequence_name | query | string  |    O     |      |
| description   | query | string  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "시퀀스 정보가 수정됐습니다."
	},
	"data": null
}
```

---

## 3. 시퀀스 삭제 <a id="#project-sequence-delete"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/delete`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| project_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "시퀀스가 삭제 되었습니다."
	},
	"data": {}
}
```

---

## 4. 시퀀스 활성화 <a id="project-shot-sequence-activate"></a>

### `POST /api/project/{project_idx}/sequence/{sequence_idx}/activate`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "시퀀스가 활성화 되었습니다."
	},
	"data": null
}
```

---

## 5. 시퀀스 비활성화 <a id="project-shot-sequence-deactivate"></a>

### `POST /api/project/{project_idx}/sequence/{sequence_idx}/deactivate`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "시퀀스가 비활성화 되었습니다."
	},
	"data": null
}
```

---

## 6. 시퀀스 목록 조회 <a id="project-sequence-list"></a>

### `GET /api/project/project/{project_idx}/episode/{episode_idx}/sequence/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"sequences": [
			{
				"sequence_idx": "1",
				"name": "s0010",
				"sequence_order": "1",
				"description": "설명"
			},
			{
				"sequence_idx": "2",
				"name": "s0020",
				"sequence_order": "2",
				"description": "설명"
			},
			{
				"sequence_idx": "3",
				"name": "s0030",
				"sequence_order": "3",
				"description": "설명"
			}
		]
	}
}
```

---

## 끝

[시퀀스 등록]: #project-sequence-create
[시퀀스 정보 수정]: #project-sequence-update
[시퀀스 삭제]: #project-sequence-delete
[시퀀스 활성화]: #project-shot-sequence-activate
[시퀀스 비활성화]: #project-shot-sequence-deactivate
[시퀀스 목록 조회]: #project-sequence-list
