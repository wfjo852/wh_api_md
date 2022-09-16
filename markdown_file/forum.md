# WH2API::Forum

## 목차

| 내용                  | slug                                                                    | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :-------------------- | :---------------------------------------------------------------------- | :-------: | :-----: | :--: | :--: |
| 1. [게시글 목록 조회] | /api/forum/article/list[/page/{page}/search/{search}/keyword/{keyword}] |    GET    |   O\*   |  -   |  -   |
| 2. [게시글 등록]      | /api/forum/article/create                                               |   POST    |    O    |  -   |  -   |
| 3. [게시글 보기]      | /api/forum/article/{article_idx}/read[/{article_range}]                 |    GET    |   O\*   |  -   |  -   |
| 4. [게시글 수정]      | /api/forum/article/{article_idx}/update                                 |   POST    |    O    |  -   |  -   |
| 5. [게시글 삭제]      | /api/forum/article/{article_idx}/delete                                 |   POST    |    O    |  -   |  -   |
| 6. [공지글 등록]      | /api/forum/article/{article_idx}/pin                                    |   POST    |    O    |  -   |  -   |
| 7. [공지글 해지]      | /api/forum/article/{article_idx}/unpin                                  |   POST    |    O    |  -   |  -   |
| 8. [댓글 등록]        | /api/forum/comment/create                                               |   POST    |    O    |  -   |  -   |
| 9. [댓글 삭제]        | /api/forum/comment/{comment_idx}/delete                                 |   POST    |    O    |  -   |  -   |

- O\* - 뷰에 직접 구현

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 게시글 목록 조회 <a id="forum-article-list"></a>

### `GET /api/forum/article/list`

### permission

- `permission.read_article`

### request

| param   | type |  data   | required | desc                                    |
| ------- | :--: | :-----: | :------: | --------------------------------------- |
| page    | path | integer |    X     | 페이지 번호                             |
| search  | path | string  |    X     | 검색 필드: subject, contents, user_name |
| keyword | path | string  |    X     | 검색어                                  |

- keyword(검색어)는 반드시 search(검색 필드)가 존재해야 제대로 작동한다.

### response

```json
{
	"error": {
		"code": 200,
		"message": "Success"
	},
	"data": {
		"articles": [
			{
				"idx": "71",
				"subject": "Test Article",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
				},
				"is_notice": "0",
				"created_time": "2020-07-31 16:00:06",
				"views": "1"
			},
			{
				"idx": "70",
				"subject": "Test Article2",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
				},
				"is_notice": "0",
				"created_time": "2020-07-31 15:56:02",
				"views": "0"
			},
			{
				"idx": "5",
				"subject": "Example Article",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
				},
				"is_notice": "0",
				"created_time": "2020-07-29 16:03:21",
				"views": "30"
			}
		],
		"paging": {
			"cur_page": 1,
			"first_page": 1,
			"last_page": 1,
			"total_page": 1,
			"block_per_page": 5
		},
		"search": "subject",
		"keyword": "article"
	}
}
```

---

## 2. 게시글 등록 <a id="forum-article-create"></a>

### `POST /api/forum/article/create`

### permission

- `permission.update_article`

### request

| param      | type  |  data   | required | desc   |
| ---------- | :---: | :-----: | :------: | ------ |
| subject    | query | string  |    O     |        |
| contents   | query | string  |    O     |        |
| attached[] | query |  file   |    X     |        |
| is_notice  | query | integer |    O     | 0 or 1 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "글이 등록됐습니다."
	},
	"data": {
		"article": {
			"idx": "55",
			"subject": "Example Article",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
			},
			"is_notice": "0",
			"created_time": "2020-07-30 17:48:44",
			"views": "0"
		}
	}
}
```

---

## 3. 게시글 보기 <a id="forum-article-read"></a>

### `GET /api/forum/article/{article_idx}/read/{article_only}`

### permission

- `permission.read_article`

### request

| param         | type |  data   | required | desc                        |
| ------------- | :--: | :-----: | :------: | --------------------------- |
| article_idx   | path | integer |    O     |                             |
| article_range | path | string  |    X     | 값: article_only or minimum |

### response

```json
{
	"error": {
		"code": 200,
		"message": "Success"
	},
	"data": {
		"article": {
			"idx": "5",
			"subject": "Example Article",
			"contents": "Example Article Contents",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
			},
			"is_notice": "0",
			"created_time": "2020-07-29 16:03:21",
			"views": "2",
			"me_created": true,
			"attachments": [
				{
					"idx": "5",
					"name": "test-img.jpg",
					"url": "http://localhost:81/2020/07/29/3f74997229c00db9.jpg",
					"thumbnail": "",
					"mime_type": ["image", "jpeg"]
				}
			]
		},
		"comments": [
			{
				"idx": "7",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
				},
				"created_time": "2020-07-29 16:03:32",
				"comment": "This is Comment",
				"can_delete": 1
			},
			{
				"idx": "8",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
				},
				"created_time": "2020-07-29 16:03:39",
				"comment": "Example Comment",
				"can_delete": 1
			}
		]
	}
}
```

---

## 4. 게시글 수정 <a id="forum-article-update"></a>

### `POST /api/forum/article/{article_idx}/update`

### permission

- `permission.update_article`: 본인 것만 수정
- `permission.do_other_article`: 다른 사람 것도 수정

### request

| param       | type  |  data   | required | desc   |
| ----------- | :---: | :-----: | :------: | ------ |
| article_idx | path  | integer |    O     |        |
| subject     | query | string  |    O     |        |
| contents    | query | string  |    O     |        |
| is_notice   | query | integer |    X     | 0 or 1 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "글이 수정됐습니다."
	},
	"data": {
		"article": {
			"idx": "55",
			"subject": "Example Article",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
			},
			"is_notice": "0",
			"created_time": "2020-07-30 17:48:44",
			"views": "1"
		}
	}
}
```

---

## 5. 게시글 삭제 <a id="forum-article-delete"></a>

### `POST /api/forum/article/{article_idx}/delete`

### permission

- `permission.update_article`: 본인 것만 삭제
- `permission.do_other_article`: 다른 사람 것도 삭제

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| article_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "게시글이 삭제됐습니다."
	},
	"data": null
}
```

---

## 6. 공지글 등록 <a id="forum-article-pin"></a>

### `POST /api/forum/article/{article_idx}/pin`

### permission

- `permission.do_other_article`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| article_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "공지글로 등록되었습니다."
	},
	"data": null
}
```

---

## 7. 공지글 해지 <a id="forum-article-unpin"></a>

### `POST /api/forum/article/{article_idx}/unpin`

### permission

- `permission.do_other_article`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| article_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "공지글에서 해지됐습니다."
	},
	"data": null
}
```

---

## 8. 댓글 등록 <a id="forum-comment-create"></a>

### `POST /api/forum/comment/create`

### permission

- `permission.update_comment`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| article_idx | query | integer |    O     |      |
| comment     | query | string  |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "The Comment is added."
	},
	"data": {
		"comment": {
			"idx": 33,
			"comment": "Example Comment",
			"created_time": "2020-07-31 17:30:33",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
			},
			"article": {
				"idx": "71",
				"subject": "Example Article",
				"user": {
					"idx": "1",
					"name": "C2Monster",
					"id": "c2m",
					"email": "contact@c2monster.com",
					"thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png"
				},
				"is_notice": "0",
				"created_time": "2020-07-31 16:00:06",
				"views": "32"
			}
		}
	}
}
```

---

## 9. 댓글 삭제 <a id="forum-comment-delete"></a>

### `POST /api/forum/comment/{comment_idx}/delete`

### prermission

- `permission.update_comment`: 본인 댓글만 삭제
- `permission.do_other_article`: 모든 댓글 삭제

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| comment_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "The Comment is removed."
	},
	"data": null
}
```

---

## 끝

[게시글 목록 조회]: #forum-article-list
[게시글 등록]: #forum-article-create
[게시글 보기]: #forum-article-read
[게시글 수정]: #forum-article-update
[게시글 삭제]: #forum-article-delete
[공지글 등록]: #forum-article-pin
[공지글 해지]: #forum-article-unpin
[댓글 등록]: #forum-comment-create
[댓글 삭제]: #forum-comment-delete
