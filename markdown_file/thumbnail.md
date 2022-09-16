# WH2API::Thumbnail

## 목차

| 내용                          | slug                                                                        | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :---------------------------- | :-------------------------------------------------------------------------- | :-------: | :-----: | :--: | :--: |
| 1. [샷 썸네일 벌크 임시 등록] | /api/project/{project_idx}/episode/{episode_idx}/shot/thumbnail/bulk/create |   POST    |    O    |  -   |  -   |
| 2. [샷 썸네일 벌크 목록 조회] | /api/project/{project_idx}/episode/{episode_idx}/shot/thumbnail/bulk/list   |    GET    |    O    |  -   |  -   |
| 3. [샷 썸네일 벌크 적용]      | /api/project/{project_idx}/episode/{episode_idx}/shot/thumbnail/bulk/update |   POST    |    O    |  -   |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 샷 썸네일 벌크 임시 등록 <a id="shot-thumbnail-bulk-create"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/shot/thumbnail/bulk/create`

### permission

- `permission.update_shot_and_task`

### request

| param       | type  |     data      | required | desc |
| ----------- | :---: | :-----------: | :------: | ---- |
| project_idx | path  |    integer    |    O     |      |
| episode_idx | path  |    integer    |    O     |      |
| attached[]  | query | array of file |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"num_of_uploaded_files": 7
	}
}
```

- 파일명 형식은 {sequence_name}+{shot_name}.EXT
- TODO: 파일명 형식이 맞지 않아 업로드 되지 않은 갯수를 `response`에 보여줄지 판단 필요

---

## 2. 샷 썸네일 벌크 목록 조회 <a id="shot-thumbnail-bulk-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/shot/thumbnail/bulk/list`

### permission

- `permission.update_shot_and_task`

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
		"shots": [
			{
				"sequence_idx": "1",
				"sequence_name": "s0010",
				"shot_idx": "1",
				"shot_name": "c0010",
				"shot_thumbnail_original": "s0010+s0010_c0010.jpg",
				"shot_thumbnail_uploaded": "http://localhost:81/2019/02/21/05ed16a5d80f3f4b.png"
			},
			{
				"sequence_idx": "1",
				"sequence_name": "s0010",
				"shot_idx": "1",
				"shot_name": "c0020",
				"shot_thumbnail_original": "s0010+s0010_c0020.jpg",
				"shot_thumbnail_uploaded": "http://localhost:81/2019/02/21/9234jkflse012.png"
			}
		]
	}
}
```

---

## 3. 샷 썸네일 벌크 적용 <a id="shot-thumbnail-bulk-update"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/shot/thumbnail/bulk/update`

### permission

- `permission.update_shot_and_task`

### request

| param            | type  |       data       | required | desc |
| ---------------- | :---: | :--------------: | :------: | ---- |
| project_idx      | path  |     integer      |    O     |      |
| episode_idx      | path  |     integer      |    O     |      |
| shot_thumbnail[] | query | array of string  |    O     |      |
| sequence_idx[]   | query | array of integer |    O     |      |
| shot_idx[]       | query | array of integer |    O     |      |

- `shot_thumbnail[]`, `sequence_idx[]`, `shot_idx[]` 의 개수는 서로 같아야 함
- `shot_thumbnail`은 [샷 썸네일 벌크 목록 조회]에서 받은 shot_thumbnail_uploaded 를 보내면 됨

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

## 끝

[샷 썸네일 벌크 임시 등록]: #shot-thumbnail-bulk-create
[샷 썸네일 벌크 목록 조회]: #shot-thumbnail-bulk-list
[샷 썸네일 벌크 적용]: #shot-thumbnail-bulk-update
