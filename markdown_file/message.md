# WH2API::Message

## 목차

| 내용                                 | slug                                                          |    서버 구현     | 웹 적용 | 웹훅 | 로그 |
|:-------------------------------------|:--------------------------------------------------------------|:----------------:|:-------:|:----:|:----:|
| 1. [채널 목록 조회]                  | /api/message/channel/list                                     |       GET        |    O    |  -   |  -   |
| 2. [멤버 조회]                       | ~~/api/message/user/list~~                                    | 참조<sup>1</sup> |    O    |  -   |  -   |
| 3. [멤버 검색]                       | ~~/api/message/user/search~~                                  | 참조<sup>1</sup> |    O    |  -   |  -   |
| 4. [채널 생성]                       | /api/message/channel/create                                   |       POST       |    O    |  -   |  -   |
| 5. [메시지 전송]                     | /api/message/channel/{channel_idx}/message/create             |       POST       |    O    |  -   |  -   |
| 6. [메시지 조회]                     | /api/message/channel/{channel_idx}/message/list               |       POST       |    O    |  -   |  -   |
| 7. [메시지 계속 조회]                | /api/message/channel/{channel_idx}/message/{message_idx}/list |       POST       |    O    |  -   |  -   |
| 8. [채널 탈퇴]                       | /api/message/channel/{channel_idx}/delete                     |       POST       |    O    |  -   |  -   |
| 9. [채널 참가 인원 조회]             | /api/message/channel/{channel_idx}/user/list                  |       GET        |    O    |  -   |  -   |
| 10. [그룹 채널 기본 설정 읽기]       | /api/message/channel/group/setting/read                       |       POST       |    O    |  -   |  -   |
| 11. [시스템 메시지 조회]             | /api/system_message/list                                      |       GET        |    X    |  -   |  -   |
| 12. [데스크탑 시스템 메시지 조회]    | /api/desktop/system_message/list                              |       GET        |    X    |  -   |  -   |
| 13. [시스템 메시지 삭제]             | /api/system_message/{system_message_idx}/delete               |       POST       |    O    |  -   |  -   |
| 14. [시스템 메시지 전체 삭제]        | /api/system_message/all/delete                                |       POST       |    O    |  -   |  -   |
| 15. [시스템 메시지 비활성화]         | /api/system_message/{system_message_idx}/deactivate           |       POST       |    X    |  -   |  -   |
| 16. [시스템 메시지 전체 비활성화]    | /api/system_message/all/deactivate                            |       POST       |    X    |  -   |  -   |
| 17. [시스템 메시지 활성화]           | /api/system_message/{system_message_idx}/activate             |       POST       |    X    |  -   |  -   |
| 18. [시스템 메시지 전체 활성화]      | /api/system_message/all/activate                              |       POST       |    X    |  -   |  -   |
| 19. [시스템 메시지 활성/비활성 토글] | /api/system_message/{system_message_idx}/activation/toggle    |       POST       |    X    |  -   |  -   |
| 20. [시스템 메시지 북마크 등록]      | /api/system_message/{system_message_idx}/favorite             |       POST       |    X    |  -   |  -   |
| 21. [시스템 메시지 북마크 해제]      | /api/system_message/{system_message_idx}/unfavorite           |       POST       |    X    |  -   |  -   |
| 22. [시스템 메시지 북마크 토글]      | /api/system_message/{system_message_idx}/favorite/toggle      |       POST       |    X    |  -   |  -   |

- 참조<sup>1</sup> - /api/user/list 이용 (user.md 참조)

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 메시지 채널 목록 조회 <a id="#message-list"></a>

- 본인 기준에서의 메시지 채널 목록을 조회하는 것임.

### `GET /api//message/channel/list`

### permission

- `permission.do_message`

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
		"system_unread_message": 1,
		"group_unread_message": 30,
		"group_channels": [
			{
				"channel_idx": "16",
				"name": "abc",
				"unread_message": 3
			},
			{
				"channel_idx": "17",
				"name": "def",
				"unread_message": 3
			}
		],
		"personal_unread_message": 30,
		"personal_channels": [
			{
				"channel_idx": "18",
				"name": "c4m",
				"unread_message": 3
			},
			{
				"channel_idx": "19",
				"name": "c5m",
				"unread_message": 3
			}
		]
	}
}
```

---

## 4. 메시지 채널 생성 <a id="#message-channel-create"></a>

### `POST /api/message/channel/create`

### permission

- `permission.do_message`

### request

| param      | type  |  data   |           required           | desc                                           |
|------------|:-----:|:-------:|:----------------------------:|------------------------------------------------|
| is_group   | query | integer |              O               | 0 - 개인 채널 / 1 - 그룹 채널                  |
| name       | query | string  | O (그룹 채널), X (개인 채널) | 채널 이름. 개인 채널인 경우는 서버에서 무시함. |
| user_idx[] | query | integer |              O               | 채널에 참여할 이용자(들)의 인덱스              |

- 개인 채널의 경우 추가할 이용자가 1명이더라도 `user_idx[]` 로 처리해서 보낸다.
- 그룹 채널인 경우 `user_idx[]`가 2개 이상이어야 채널이 생성된다.
- 개인 채널의 경우 `user_idx[]`가 1개일 때만 채널이 생성된다.

### response

```json
{
	"error": {
		"code": 200,
		"message": "채널이 생성됐습니다."
	},
	"data": {
		"channel_idx": 4
	}
}
```

---

## 5. 메시지 전송 <a id="#message-message-create"></a>

### `POST /api/message/channel/{channel_idx}/message/create`

### permission

- `permission.do_message`

### request

| param       | type  |  data   | required | desc                          |
|-------------|:-----:|:-------:|:--------:|-------------------------------|
| channel_idx | path  | integer |    O     | 채널 인덱스                   |
| is_group    | query | integer |    O     | 0 - 개인 채널 / 1 - 그룹 채널 |
| message     | query | string  |    O     | 전송하는 메시지 내용          |

- message는 기본적으로 태그는 필터링이 됨

### response

```json
{
	"error": {
		"code": 200,
		"message": "메시지가 전송됐습니다."
	},
	"data": {
		"message_idx": 4
	}
}
```

---

## 6. 메시지 조회 <a id="#message-message-read"></a>

- 채널에 처음 입장했을 때 표시되는 메시지 리스트를 위한 api

### `POST /api/message/channel/{channel_idx}/message/list`

### permission

- `permission.do_message`

### request

| param       | type |  data   | required | desc |
|-------------|:----:|:-------:|:--------:|------|
| channel_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"owner_user_idx": 1,
		"group_unread_message": 1,
		"personal_unread_message": 1,
		"system_unread_message": 1,
		"messages": [
			{
				"message_idx": "7",
				"message": "감자는 감자",
				"date": "2019-01-27 14:52:56",
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"message_idx": "8",
				"message": "햄버거는 햄버거",
				"date": "2019-01-27 14:53:01",
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			}
		]
	}
}
```

---

## 7. 메시지 계속 조회 <a id="#message-message-read-more"></a>

- 채널에서 더 오래된 메시지를 부를 때 필요한 api

### `POST /api/message/channel/{channel_idx}/message/{message_idx}/list`

### permission

- `permission.do_message`

### request

| param       | type |  data   | required | desc                                          |
|-------------|:----:|:-------:|:--------:|-----------------------------------------------|
| channel_idx | path | integer |    O     |                                               |
| message_idx | path | integer |    O     | 이 메시지 인덱스보다 오래된 메시지만 읽어들임 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"owner_user_idx": 1,
		"group_unread_message": 1,
		"personal_unread_message": 1,
		"system_unread_message": 1,
		"messages": [
			{
				"message_idx": "7",
				"message": "감자는 감자",
				"date": "2019-01-27 14:52:56",
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"message_idx": "8",
				"message": "햄버거는 햄버거",
				"date": "2019-01-27 14:53:01",
				"user_idx": "1",
				"user_id": "c2m",
				"user_name": "cccc",
				"user_thumbnail": ""
			}
		]
	}
}
```

---

## 8. 채널 탈퇴 <a id="#message-channel-delete"></a>

- 실제로 기록을 지워버리는 것이 아니라 채널에서 해당 이용자만 아카이빙하는 형태임.
- 나중에 채널 추가, 인원 별도 추가 등의 액션에 대해 유저 시나리오를 짜야 함.

### `POST /api/message/channel/{channel_idx}/delete`

### permission

- `permission.do_message`

### request

| param       | type  |  data   | required | desc                          |
|-------------|:-----:|:-------:|:--------:|-------------------------------|
| channel_idx | path  | integer |    O     | 채널 인덱스                   |
| is_group    | query | integer |    O     | 0 - 개인 채널 / 1 - 그룹 채널 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "채널에서 나왔습니다."
	},
	"data": {
		"channel_idx": 3
	}
}
```

---

## 9. 채널 참가 인원 조회 <a id="message-group-memeber-list"></a>

### `GET /api/message/channel/{channel_idx}/member/list`

### permission

- `permission.do_message`

### request

| param       | type |  data   | required | desc |
|-------------|:----:|:-------:|:--------:|------|
| channel_idx | path | integer |    O     |      |

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
				"user_idx": "1",
				"user_id": "c1m",
				"user_name": "cccc",
				"user_thumbnail": ""
			},
			{
				"user_idx": "2",
				"user_id": "c2m",
				"user_name": "aaa",
				"user_thumbnail": ""
			},
			{
				"user_idx": "3",
				"user_id": "c3m",
				"user_name": "ddd",
				"user_thumbnail": ""
			},
			{
				"user_idx": "4",
				"user_id": "c4m",
				"user_name": "abo",
				"user_thumbnail": ""
			}
		]
	}
}
```

---

## 10. 그룹 채널 기본 설정 읽기 <a id="group-channel-setting-read"></a>

- 기본적으로 테스크 디테일 모달에서 이용.
- 해당 샷/에셋을 작업하는 아티스트(테스크 디테일 모달의 progress 영역)가 기본으로 선택되도록 하기 위함.

### `POST /api/message/channel/group/setting/read`

### permission

- `permission.do_message`

### request

| param       | type  |  data   | required | desc          |
|-------------|:-----:|:-------:|:--------:|---------------|
| project_idx | query | integer |    O     |               |
| task_idx    | query | integer |    O     |               |
| kind        | query | string  |    O     | shot or asset |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"chnnel_name": "s0010_c0010_animation",
		"users": [
			{
				"user_idx": "1",
				"name": "cccc"
			},
			{
				"user_idx": "1",
				"name": "cccc"
			}
		],
		"selected_users": [1, 2, 3]
	}
}
```

---

## 11. 시스템 메시지 조회 <a id="system-message-list"></a>

### `GET /api/system_message/list`

### permission

- all

### request

| param | type | data | required | desc |
|-------|:----:|:----:|:--------:|------|
| X     |  X   |  X   |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"system_messages": [
			{
				"idx": "3",
				"type": {
					"idx": "3",
					"name": "Version Created"
				},
				"target": {
					"version": {
						"idx": "1",
						"name": "big_s0010_c0010_anim_v001"
					}
				},
				"location": {
					"project": {
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"is_on": "1",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					},
					"episode": {
						"idx": "1",
						"name": "Ep01",
						"description": "Demo_Bigbuck_Bunny_First",
						"is_on": "1",
						"order": "1"
					},
					"sequence": {
						"idx": "1",
						"name": "s0010",
						"description": "Opening Sequence",
						"is_on": "1",
						"sequence_order": "1",
						"order": "1"
					},
					"shot": {
						"idx": "1",
						"name": "s0010_c0010",
						"is_on": "1",
						"thumbnail": "http://localhost:81/2019/04/08/24591d492b5b4b16.jpg",
						"order": "1"
					},
					"tasktype": {
						"idx": "1",
						"name": "Animation5",
						"description": "for animation",
						"is_on": "1",
						"pos": "1",
						"color": "#DE4E4E",
						"kind": "shot"
					}
				},
				"url": "/version/1/detail",
				"description": "버전이 리뷰 대기 중",
				"created_time": "2021-03-31 01:33:49",
				"is_on": "1"
			},
			{
				"idx": "2",
				"type": {
					"idx": "2",
					"name": "Task Updated"
				},
				"target": {
					"tasktype": {
						"idx": "15",
						"name": "Texture",
						"description": "Texture",
						"is_on": "1",
						"pos": "4",
						"color": "#3f51b5",
						"kind": "asset"
					}
				},
				"location": {
					"project": {
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"is_on": "1",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					},
					"asset_category": {
						"idx": "1",
						"name": "char",
						"description": "character",
						"is_on": "1"
					},
					"asset": {
						"idx": "1",
						"name": "ch_bunny",
						"is_on": "1",
						"order": "1"
					}
				},
				"url": "/asset/task/1/detail",
				"description": "start_date 변경: 2021-04-10 → 2021-04-06",
				"created_time": "2021-03-31 01:33:01",
				"is_on": "2"
			}
		]
	}
}
```

---

## 12. 데스크탑 시스템 메시지 조회 <a id="desktop-system-message-list"></a>

### `GET /api/desktop/system_message/list`

### permission

- all

### request

| param          | type  |  data   | required | desc                                         |
|----------------|:-----:|:-------:|:--------:|----------------------------------------------|
| page           | query | integer |    X     | 생략 시 1                                    |
| is_on          | query | integer |    X     | 99 - all / 1 - 미확인 / 2 - 확인             |
| block_size     | query | integer |    X     | 생략 시 50개                                 |
| favorite_order | query | integer |    X     | 생략 시 1 - 우선순위로 표시 / 2 - 우선순위 x |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"system_messages": [
			{
				"idx": "3",
				"type": {
					"idx": "3",
					"name": "Version Created"
				},
				"target": {
					"version": {
						"idx": "1",
						"name": "big_s0010_c0010_anim_v001"
					}
				},
				"location": {
					"project": {
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"is_on": "1",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					},
					"episode": {
						"idx": "1",
						"name": "Ep01",
						"description": "Demo_Bigbuck_Bunny_First",
						"is_on": "1",
						"order": "1"
					},
					"sequence": {
						"idx": "1",
						"name": "s0010",
						"description": "Opening Sequence",
						"is_on": "1",
						"sequence_order": "1",
						"order": "1"
					},
					"shot": {
						"idx": "1",
						"name": "s0010_c0010",
						"is_on": "1",
						"thumbnail": "http://localhost:81/2019/04/08/24591d492b5b4b16.jpg",
						"order": "1"
					},
					"tasktype": {
						"idx": "1",
						"name": "Animation5",
						"description": "for animation",
						"is_on": "1",
						"pos": "1",
						"color": "#DE4E4E",
						"kind": "shot"
					}
				},
				"url": "/version/1/detail",
				"description": "버전이 리뷰 대기 중",
				"created_time": "2021-03-31 01:33:49",
				"is_on": "1",
				"is_favorite": "0"
			},
			{
				"idx": "2",
				"type": {
					"idx": "2",
					"name": "Task Updated"
				},
				"target": {
					"tasktype": {
						"idx": "15",
						"name": "Texture",
						"description": "Texture",
						"is_on": "1",
						"pos": "4",
						"color": "#3f51b5",
						"kind": "asset"
					}
				},
				"location": {
					"project": {
						"idx": "1",
						"name": "Demo_Bigbuck_Bunny",
						"description": "Demo_Bigbuck_Bunny",
						"is_on": "1",
						"start_date": "2018-12-11",
						"end_date": "2019-04-12"
					},
					"asset_category": {
						"idx": "1",
						"name": "char",
						"description": "character",
						"is_on": "1"
					},
					"asset": {
						"idx": "1",
						"name": "ch_bunny",
						"is_on": "1",
						"order": "1"
					}
				},
				"url": "/asset/task/1/detail",
				"description": "start_date 변경: 2021-04-10 → 2021-04-06",
				"created_time": "2021-03-31 01:33:01",
				"is_on": "2",
				"is_favorite": "1"
			}
		]
	}
}
```

---

## 13. 시스템 메시지 삭제 <a id="system-message-delete"></a>

### `POST /api/system_message/{system_message_idx}/delete`

### permission

- all

### request

| param              | type |  data   | required | desc |
|--------------------|:----:|:-------:|:--------:|------|
| system_message_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "삭제했습니다."
	},
	"data": null
}
```

---

## 14. 시스템 메시지 전체 삭제 <a id="system-message-all-delete"></a>

### `POST /api/system_message/all/delete`

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
		"message": "삭제했습니다."
	},
	"data": null
}
```

---

## 15. 시스템 메시지 비활성화 <a id="system-message-deactivate"></a>

### `POST /api/system_message/{system_message_idx}/deactivate`

### permission

- all

### request

| param              | type |  data   | required | desc |
|--------------------|:----:|:-------:|:--------:|------|
| system_message_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "비활성화했습니다."
	},
	"data": null
}
```

---

## 16. 시스템 메시지 전체 비활성화 <a id="system-message-all-deactivate"></a>

### `POST /api/system_message/all/deactivate`

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
		"message": "비활성화했습니다."
	},
	"data": null
}
```

---

## 17. 시스템 메시지 활성화 <a id="system-message-activate"></a>

### `POST /api/system_message/{system_message_idx}/activate`

### permission

- all

### request

| param              | type |  data   | required | desc |
|--------------------|:----:|:-------:|:--------:|------|
| system_message_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "활성화했습니다."
	},
	"data": null
}
```

---

## 18. 시스템 메시지 전체 활성화 <a id="system-message-all-activate"></a>

### `POST /api/system_message/all/activate`

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
		"message": "활성화했습니다."
	},
	"data": null
}
```

---

## 19. 시스템 메시지 활성/비활성 토글 <a id="system-message-activation-toggle"></a>

### `POST /api/system_message/all/activate`

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
		"message": "활성화했습니다."
	},
	"data": null
}
```

---

## 20. 시스템 메시지 북마크 등록 <a id="system-message-favorite"></a>

### `POST /api/system_message/{system_message_idx}/favorite`

### permission

- all

### request

| param              | type |  data   | required | desc |
|--------------------|:----:|:-------:|:--------:|------|
| system_message_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "북마크를 등록했습니다."
	},
	"data": null
}
```

---

## 21. 시스템 메시지 북마크 해제 <a id="system-message-unfavorite"></a>

### `POST /api/system_message/{system_message_idx}/unfavorite`

### permission

- all

### request

| param              | type |  data   | required | desc |
|--------------------|:----:|:-------:|:--------:|------|
| system_message_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "북마크를 해제했습니다."
	},
	"data": null
}
```

---

## 22. 시스템 메시지 북마크 토글 <a id="system-message-favorite-toggle"></a>

### `POST /api/system_message/{system_message_idx}/favorite/toggle`

### permission

- all

### request

| param              | type |  data   | required | desc |
|--------------------|:----:|:-------:|:--------:|------|
| system_message_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "북마크를 등록했습니다."
	},
	"data": null
}
```

---

## 끝

[채널 목록 조회]: #message-list
[멤버 조회]: #message-member-list
[멤버 검색]: #message-member-search
[채널 생성]: #message-channel-create
[메시지 전송]: #message-message-create
[메시지 조회]: #message-message-read
[메시지 계속 조회]: #message-message-read-more
[채널 탈퇴]: #message-channel-delete
[채널 참가 인원 조회]: #message-group-memeber-list
[그룹 채널 기본 설정 읽기]: #group-channel-setting-read
[시스템 메시지 조회]: #system-message-list
[시스템 메시지 조회]: #desktop-system-message-list
[시스템 메시지 삭제]: #system-message-delete
[시스템 메시지 전체 삭제]: #system-message-all-delete
[시스템 메시지 비활성화]: #system-message-deactivate
[시스템 메시지 전체 비활성화]: #system-message-all-deactivate
[시스템 메시지 활성화]: #system-message-activate
[시스템 메시지 전체 활성화]: #system-message-all-activate
[시스템 메시지 활성/비활성 토글]: #system-message-activation-toggle
[시스템 메시지 북마크 등록]: #system-message-favorite
[시스템 메시지 북마크 해글]: #system-message-unfavorite
[시스템 메시지 북마크 토글]: #system-message-favorite-toggle
