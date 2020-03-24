# WH2API::Message

## 목차

| 내용                           | slug                                                          |    서버 구현     | 웹 적용 |
| :----------------------------- | :------------------------------------------------------------ | :--------------: | :-----: |
| 1. [채널 목록 조회]            | /api/message/channel/list                                     |       GET        |    O    |
| 2. [멤버 조회]                 | ~~/api/message/user/list~~                                    | 참조<sup>1</sup> |    O    |
| 3. [멤버 검색]                 | ~~/api/message/user/search~~                                  | 참조<sup>1</sup> |    O    |
| 4. [채널 생성]                 | /api/message/channel/create                                   |       POST       |    O    |
| 5. [메시지 전송]               | /api/message/channel/{channel_idx}/message/create             |       POST       |    O    |
| 6. [메시지 조회]               | /api/message/channel/{channel_idx}/message/list               |       POST       |    O    |
| 7. [메시지 계속 조회]          | /api/message/channel/{channel_idx}/message/{message_idx}/list |       POST       |    O    |
| 8. [채널 탈퇴]                 | /api/message/channel/{channel_idx}/delete                     |       POST       |    O    |
| 9. [시스템 메시지 조회]        | /api/message/system/message/list                              |       POST       |    O    |
| 10. [시스템 메시지 계속 조회]  | /api/message/system/message/{message_idx}/list                |       POST       |    O    |
| 11. [채널 참가 인원 조회]      | /api/message/channel/{channel_idx}/user/list                  |       GET        |    O    |
| 12. [그룹 채널 기본 설정 읽기] | /api/message/channel/group/setting/read                       |       POST       |    O    |
| 13. [시스템 메시지 조회]       | /api/system/message/read                                      |      X GET       |    X    |

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
| ----- | :--: | :--: | :------: | ---- |
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
| ---------- | :---: | :-----: | :--------------------------: | ---------------------------------------------- |
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
| ----------- | :---: | :-----: | :------: | ----------------------------- |
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
| ----------- | :--: | :-----: | :------: | ---- |
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
| ----------- | :--: | :-----: | :------: | --------------------------------------------- |
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
| ----------- | :---: | :-----: | :------: | ----------------------------- |
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

## 9. 시스템 메시지 조회 <a id="#message-system-read"></a>

### `POST /api/message/system/message/list`

### permission

- `permission.do_message`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

- 이용자와 직접 관련 있는 메시지는 `user_idx` ~ `user_thumbnail` 값이 존재함. 이용자 썸네일을 표시함.
- 이용자를 특정할 수 없는 메시지는 `user_idx` ~ `user_thumbnail` 이 null 임. 기본 시스템 아이콘을 표시함.

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"messages": [
			{
				"message_idx": "1",
				"message": "hello, world.",
				"date": "2018-11-15 08:43:38",
				"user_idx": null,
				"user_id": null,
				"user_name": null,
				"user_thumbnail": null
			},
			{
				"message_idx": "2",
				"message": "wow",
				"date": "2010-03-10 08:43:38",
				"user_idx": "2",
				"user_id": "c3m",
				"user_name": "111-222-3333",
				"user_thumbnail": ""
			}
		]
	}
}
```

## 10. 시스템 메시지 계속 조회 <a id="#message-system-read-more"></a>

### `POST /api/message/system/message/{message_idx}/list`

### permission

- `permission.do_message`

### request

| param       | type |  data   | required | desc                                            |
| ----------- | :--: | :-----: | :------: | ----------------------------------------------- |
| message_idx | path | integer |    O     | 이 메시지 인덱스보다 오래된 메시지만 불러오도록 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"messages": [
			{
				"message_idx": "7",
				"message": "감자는 감자",
				"date": "2019-01-27 14:52:56"
			},
			{
				"message_idx": "8",
				"message": "햄버거는 햄버거",
				"date": "2019-01-27 14:53:01"
			}
		]
	}
}
```

## 11. 채널 참가 인원 조회 <a id="message-group-memeber-list"></a>

### `GET /api/message/channel/{channel_idx}/member/list`

### permission

- `permission.do_message`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
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

## 12. 그룹 채널 기본 설정 읽기 <a id="group-channel-setting-read"></a>

- 기본적으로 테스크 디테일 모달에서 이용.
- 해당 샷/에셋을 작업하는 아티스트(테스크 디테일 모달의 progress 영역)가 기본으로 선택되도록 하기 위함.

### `POST /api/message/channel/group/setting/read`

### permission

- `permission.do_message`

### request

| param       | type  |  data   | required | desc          |
| ----------- | :---: | :-----: | :------: | ------------- |
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

## 13. 시스템 메시지 조회 <a id="system-message-read"></a>

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
  "data" : [
    {
      "Work Type":"shot",
      "Project":"Big_Buck_Bunny",
      "Work Name":"s0010_c0010",
      "Task Name": "Comp",
      "User": "C2M",
      "Message": "[Task Name] [Start Date]~[End Date]",
      "Request time": "2019/12/17 18:29"
    },
    {
      "Work Type":"shot",
      "Project":"Big_Buck_Bunny",
      "Work Name":"s0010_c0010",
      "Task Name": "Comp",
      "User": "C2M",
      "Message": "[Task Name] [Start Date]~[End Date]",
      "Request time": "2019/12/17 18:29"
    },
    {
      "Work Type":"shot",
      "Project":"Big_Buck_Bunny",
      "Work Name":"s0010_c0010",
      "Task Name": "Comp",
      "User": "C2M",
      "Message": "[Task Name] [Start Date]~[End Date]",
      "Request time": "2019/12/17 18:29"
    },
    {
      "Work Type":"shot",
      "Project":"Big_Buck_Bunny",
      "Work Name":"s0010_c0010",
      "Task Name": "Comp",
      "User": "C2M",
      "Message": "[Task Name] [Start Date]~[End Date]",
      "Request time": "2019/12/17 18:29"
    }
  ]
}

## 끝

[채널 목록 조회]: #message-list
[멤버 조회]: #message-member-list
[멤버 검색]: #message-member-search
[채널 생성]: #message-channel-create
[메시지 전송]: #message-message-create
[메시지 조회]: #message-message-read
[메시지 계속 조회]: #message-message-read-more
[채널 탈퇴]: #message-channel-delete
[시스템 메시지 조회]: #message-system-read
[시스템 메시지 계속 조회]: #message-system-read-more
[채널 참가 인원 조회]: #message-group-memeber-list
[그룹 채널 기본 설정 읽기]: #group-channel-setting-read
```
