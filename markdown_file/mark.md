# WH2API::Mark

## 목차

| 내용                                    | slug                                           | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
|:----------------------------------------|:-----------------------------------------------|:---------:|:-------:|:----:|:----:|
| 1. [마크 등록]                          | /api/mark/create                               |   POST    |   O\*   |  -   |  -   |
| 2. [마크 수정]                          | /api/mark/{mark_idx}/update                    |   POST    |   O\*   |  -   |  -   |
| 3. [마크 조회]                          | /api/mark/{mark_idx}/read                      |    GET    |   O\*   |  -   |  -   |
| 4. [마크 삭제]                          | /api/mark/{mark_idx}/delete                    |   POST    |   X\*   |  -   |  -   |
| 5. [마크 내 마크 추가]                  | /api/mark/{mark_idx}/mark/add                  |   POST    |   O\*   |  -   |  -   |
| 6. [마크 내 마크 최신 목록 조회]        | /api/mark/{mark_idx}/mark/list                 |    GET    |   O\*   |  -   |  -   |
| 7. [마크 내 레퍼런스 목록 조회]         | /api/mark/{mark_idx}/reference/list            |    GET    |   X\*   |  -   |  -   |
| 8. [레퍼런스를 사용하는 마크 목록 조회] | /api/mark/{child_mark_idx}/reference/mark/list |    GET    |   X\*   |  -   |  -   |

- X\* - Maya plugin에서 사용 (아직 미구현)
- O\* - Maya plugin에서 사용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)
- history_idx는 자동으로 증가된다.

---

## 1. 파일 등록 <a id="mark-create"></a>

### `POST /api/mark/create`

### permission

- `permission.update_mark`

### request

| param       | type  |  data   | required | desc                        |
|-------------|:-----:|:-------:|:--------:|-----------------------------|
| description | query | string  |    X     |                             |
| kind        | query | string  |    X     | 'shot' or 'asset'           |
| task_idx    | query | integer |    X     |                             |
| status_idx  | query | integer |    X     | 웜홀에서 사용하는 상태 코드 |
| file_path   | query | string  |    O     | 경로가 포함된 파일 이름Ï    |
| attached    | query |  file   |    X     | 썸네일 파일 (1개)           |

- 만약 task_idx 를 보내면 kind 를 무조건 보내야 함

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"mark": {
			"idx": "7"
		}
	}
}
```

---

## 2. 파일 수정 <a id="mark-update"></a>

### `POST /api/mark/{mark_idx}/update`

### permission

- `permission.update_mark`

### request

| param       | type  |  data   | required | desc                        |
|-------------|:-----:|:-------:|:--------:|-----------------------------|
| mark_idx    | path  | integer |    O     | 파일 추가 때 받은 인덱스    |
| description | query | string  |    X     |                             |
| kind        | query | string  |    X     | 'shot' or 'asset'           |
| task_idx    | query | integer |    X     |                             |
| status_idx  | query | integer |    X     | 웜홀에서 사용하는 상태 코드 |
| file_path   | query | string  |    O     |                             |
| attached    | query |  file   |    X     | 썸네일 파일 (1개)           |

- 만약 task_idx 를 보내면 kind 를 무조건 보내야 함

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"mark": {
			"idx": "7"
		}
	}
}
```

---

## 3. 마크 조회 <a id="mark-read"></a>

### `GET /api/mark/{mark_idx}/read`

### permission

- `permission.read_mark`

### request

| param    | type |  data   | required | desc |
|----------|:----:|:-------:|:--------:|------|
| mark_idx | path | integer |    O     |      |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "mark": {
            "idx": "11",
            "mark_idx": "7",
            "name": "test05-.mb",
            "kind": "shot",
            "user": null,
            "description": "asdzxcv",
            "status": null,
            "local_file_path": "C:/testscene/test05-.mb",
            "task": {
                "idx": "16",
                "name": "comp"
            },
            "shot": {
                "idx": "8",
                "name": "s0010_c0080"
            },
            "thumbnail": "http://localhost:81/2020/11/02/3589f11cf0ba2f94.jpg",
            "project": {
                "idx": "1",
                "name": "Demo_Bigbuck_Bunny"
            },
            "created_time": "2020-11-02 13:10:49"
        },
        "history": [
            {
                "idx": "9",
                "mark_idx": "7",
                "name": "test05-.mb",
                "kind": "shot",
                "user": {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                },
                "description": "ttest",
                "status": null,
                "local_file_path": "C:/testscene/test05-.mb",
                "task": {
                    "idx": "16",
                    "name": "comp"
                },
                "shot": {
                    "idx": "8",
                    "name": "s0010_c0080"
                },
                "thumbnail": "http://localhost:81/2020/10/27/624d9acac1fa4de1.jpg",
                "project": {
                    "idx": "1",
                    "name": "Demo_Bigbuck_Bunny"
                },
                "created_time": "2020-10-27 15:07:36"
            },
            {
                "idx": "8",
                "mark_idx": "7",
                "name": "test05-.mb",
                "kind": "shot",
                "user": {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                },
                "description": "task information update ( [shot] 16 )",
                "status": null,
                "local_file_path": "C:/testscene/test05-.mb",
                "task": {
                    "idx": "16",
                    "name": "comp"
                },
                "shot": {
                    "idx": "8",
                    "name": "s0010_c0080"
                },
                "thumbnail": "http://localhost:81/2020/10/27/7cf8753b10257e4e.jpg",
                "project": {
                    "idx": "1",
                    "name": "Demo_Bigbuck_Bunny"
                },
                "created_time": "2020-10-27 15:07:29"
            },
            {
                "idx": "7",
                "mark_idx": "0",
                "name": "test05-.mb",
                "kind": null,
                "user": {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                },
                "description": "Not found mark - recreate mark",
                "status": null,
                "local_file_path": "C:/testscene/test05-.mb",
                "task": {
                    "idx": null,
                    "name": null
                },
                "thumbnail": null,
                "project": {
                    "idx": null,
                    "name": null
                },
                "created_time": "2020-10-27 15:06:29"
            }
        ]
    }
}
```

---

## 4. 마크 삭제 <a id="mark-delete"></a>

### `POST /api/mark/{mark_idx}/delete`

### permission

- `permission.update_mark`

### request

| param    | type |  data   | required | desc |
|----------|:----:|:-------:|:--------:|------|
| mark_idx | path | integer |    O     |      |

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

## 5. 마크 내 마크 추가 <a id="mark-mark-add"></a>

### `POST /api/mark/{mark_idx}/mark/add`

### permission

- `permission.update_mark`

### request

| param             | type  |       data       | required | desc |
|-------------------|:-----:|:----------------:|:--------:|------|
| mark_idx          | path  |     integer      |    O     |      |
| child_mark_idx[]  | query | array of integer |    X     |      |
| child_file_path[] | query | array of string  |    X     |      |

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

## 6. 마크 내 마크 최신 목록 조회 <a id="mark-mark-list"></a>

### `GET /api/mark/{mark_idx}/mark/list`

### permission

- `permission.update_mark`

### request

| param    | type |  data   | required | desc |
|----------|:----:|:-------:|:--------:|------|
| mark_idx | path | integer |    O     |      |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "marks": [
            {
                "idx": "4",
                "mark_idx": "3",
                "name": "test03.mb",
                "description": "ert",
                "kind": "shot",
                "task": {
                    "idx": "5"
                },
                "local_file_path": "C:/testscene/test03.mb",
                "created_time": "2020-10-27 15:04:41",
                "user": {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                },
                "status": null
            },
            {
                "idx": "6",
                "mark_idx": "5",
                "name": "test04.mb",
                "description": "asdf",
                "kind": "shot",
                "task": {
                    "idx": "34"
                },
                "local_file_path": "C:/testscene/test04.mb",
                "created_time": "2020-10-27 15:05:04",
                "user": {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                },
                "status": null
            },
            {
                "idx": null,
                "local_file_path": "C:/pic/big_s0010_c0040_Animation_v001.jpg"
            }
        ]
    }
}
```

---

## 7. 마크 내 레퍼런스 목록 조회 <a id="mark-mark-list"></a>

### `GET /api/mark/{mark_idx}/reference/list`

### permission

- `permission.update_mark`

### request

| param    | type |  data   | required | desc |
|----------|:----:|:-------:|:--------:|------|
| mark_idx | path | integer |    O     |      |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "marks": [
            {
                "idx": null,
                "local_file_path": "big_s0010_c0040_Animation_v001.jpg"
            },
            {
                "root_idx": "3",
                "last_idx": "4",
                "current_idx": "3",
                "used_count": 2,
                "idx": "3",
                "mark_idx": "0",
                "name": "test03.mb",
                "kind": null,
                "user": {
                    "idx": "1",
                    "id": "c2m",
                    "name": "C2Monster",
                    "thumbnail": "/2019/04/08/c1f855a779d0543e.png"
                },
                "description": "Not found mark - recreate mark",
                "status": null,
                "local_file_path": "C:/testscene/test03.mb",
                "task": {
                    "idx": null,
                    "name": null
                },
                "thumbnail": null,
                "project": {
                    "idx": null,
                    "name": null
                },
                "created_time": "2020-10-27 15:04:19"
            },
            {
                "root_idx": "5",
                "last_idx": "6",
                "current_idx": "5",
                "used_count": 1,
                "idx": "5",
                "mark_idx": "0",
                "name": "test04.mb",
                "kind": null,
                "user": {
                    "idx": "1",
                    "id": "c2m",
                    "name": "C2Monster",
                    "thumbnail": "/2019/04/08/c1f855a779d0543e.png"
                },
                "description": "Not found mark - recreate mark",
                "status": null,
                "local_file_path": "C:/testscene/test04.mb",
                "task": {
                    "idx": null,
                    "name": null
                },
                "thumbnail": null,
                "project": {
                    "idx": null,
                    "name": null
                },
                "created_time": "2020-10-27 15:05:01"
            }
        ]
    }
}
```
## 8. 레퍼런스를 사용하는 마크 목록 조회 <a id="mark-mark-list"></a>

### `GET /api/mark/{child_mark_idx}/reference/mark/list`

### permission

- `permission.update_mark`

### request

| param    | type |  data   | required | desc |
|----------|:----:|:-------:|:--------:|------|
| mark_idx | path | integer |    O     |      |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "marks": [
            {
                "idx": "6",
                "mark_idx": "5",
                "name": "test04.mb",
                "description": "asdf",
                "kind": "shot",
                "task": {
                    "idx": "34"
                },
                "local_file_path": "C:/testscene/test04.mb",
                "created_time": "2020-10-27 15:05:04",
                "user": {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                },
                "status": null,
                "project": {
                    "idx": "1",
                    "name": "Demo_Bigbuck_Bunny"
                },
                "reference_count": 1,
                "history": [
                    [
                        {
                            "idx": "5",
                            "mark_idx": "0",
                            "name": "test04.mb",
                            "kind": null,
                            "user": {
                                "idx": "1",
                                "name": "C2Monster",
                                "id": "c2m",
                                "email": "contact@c2monster.com",
                                "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                            },
                            "description": "Not found mark - recreate mark",
                            "status": null,
                            "local_file_path": "C:/testscene/test04.mb",
                            "task": {
                                "idx": null,
                                "name": null
                            },
                            "thumbnail": null,
                            "project": {
                                "idx": null,
                                "name": null
                            },
                            "created_time": "2020-10-27 15:05:01"
                        }
                    ]
                ]
            },
            {
                "idx": "11",
                "mark_idx": "7",
                "name": "test05-.mb",
                "description": "asdzxcv",
                "kind": "shot",
                "task": {
                    "idx": "16"
                },
                "local_file_path": "C:/testscene/test05-.mb",
                "created_time": "2020-11-02 13:10:49",
                "user": null,
                "status": null,
                "project": {
                    "idx": "1",
                    "name": "Demo_Bigbuck_Bunny"
                },
                "reference_count": 3,
                "history": [
                    [
                        {
                            "idx": "9",
                            "mark_idx": "7",
                            "name": "test05-.mb",
                            "kind": "shot",
                            "user": {
                                "idx": "1",
                                "name": "C2Monster",
                                "id": "c2m",
                                "email": "contact@c2monster.com",
                                "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                            },
                            "description": "ttest",
                            "status": null,
                            "local_file_path": "C:/testscene/test05-.mb",
                            "task": {
                                "idx": "16",
                                "name": "comp"
                            },
                            "shot": {
                                "idx": "8",
                                "name": "s0010_c0080"
                            },
                            "thumbnail": "http://localhost:81/2020/10/27/624d9acac1fa4de1.jpg",
                            "project": {
                                "idx": "1",
                                "name": "Demo_Bigbuck_Bunny"
                            },
                            "created_time": "2020-10-27 15:07:36"
                        },
                        {
                            "idx": "8",
                            "mark_idx": "7",
                            "name": "test05-.mb",
                            "kind": "shot",
                            "user": {
                                "idx": "1",
                                "name": "C2Monster",
                                "id": "c2m",
                                "email": "contact@c2monster.com",
                                "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                            },
                            "description": "task information update ( [shot] 16 )",
                            "status": null,
                            "local_file_path": "C:/testscene/test05-.mb",
                            "task": {
                                "idx": "16",
                                "name": "comp"
                            },
                            "shot": {
                                "idx": "8",
                                "name": "s0010_c0080"
                            },
                            "thumbnail": "http://localhost:81/2020/10/27/7cf8753b10257e4e.jpg",
                            "project": {
                                "idx": "1",
                                "name": "Demo_Bigbuck_Bunny"
                            },
                            "created_time": "2020-10-27 15:07:29"
                        },
                        {
                            "idx": "7",
                            "mark_idx": "0",
                            "name": "test05-.mb",
                            "kind": null,
                            "user": {
                                "idx": "1",
                                "name": "C2Monster",
                                "id": "c2m",
                                "email": "contact@c2monster.com",
                                "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
                            },
                            "description": "Not found mark - recreate mark",
                            "status": null,
                            "local_file_path": "C:/testscene/test05-.mb",
                            "task": {
                                "idx": null,
                                "name": null
                            },
                            "thumbnail": null,
                            "project": {
                                "idx": null,
                                "name": null
                            },
                            "created_time": "2020-10-27 15:06:29"
                        }
                    ]
                ]
            }
        ]
    }
}

## 끝

[마크 등록]: #mark-create
[마크 수정]: #mark-update
[마크 조회]: #mark-read
[마크 삭제]: #mark-delete
[마크 내 마크 추가]: #mark-mark-add
[마크 내 마크 목록 조회]: #mark-mark-list
