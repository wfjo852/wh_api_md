# WH2API::Team

## 목차

| 내용                            | slug                            | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :------------------------------ | :------------------------------ | :-------: | :-----: | :--: | :--: |
| 1. [팀 목록 조회]               | /api/team/list                  |    GET    |    O    |  -   |  -   |
| 2. [팀 등록]                    | /api/team/create                |   POST    |    O    |  -   |  -   |
| 3. [팀 정보 엑셀 내보내기]      | /api/team/export                |     X     |    X    |  -   |  -   |
| 4. [팀 참여 가능한 이용자 목록] | /api/team/{team_idx}/user/list  |    GET    |    O    |  -   |  -   |
| 5. [팀 활성화]                  | /api/team/{team_idx}/activate   |   POST    |    O    |  -   |  -   |
| 6. [팀 비활성화]                | /api/team/{team_idx}/deactivate |   POST    |    O    |  -   |  -   |
| 7. [팀 삭제]                    | /api/team/{team_idx}/delete     |   POST    |    O    |  -   |  -   |
| 8. [팀 정보 수정]               | /api/team/{team_idx}/update     |   POST    |    O    |  -   |  -   |
| 9. [팀 구성원 변경하기]         | /api/team/{team_idx}/user/add   |   POST    |    O    |  -   |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 팀 목록 조회 <a id="team-list"></a>

### `GET /api/team/list`

### permission

- `permission.do_global_setting`

### request

| param               | type |  data   | required | desc                                  |
| ------------------- | :--: | :-----: | :------: | ------------------------------------- |
| include_me          | path | integer |    X     | 1 (본인이 포함된 팀 리스트만 뽑을 때) |
| not_me_in_user_list | path | integer |    X     | 1 (팀 리스트에 본인을 빼고 뽑을 때)   |
| is_on               | path | integer |    X     | 1 (액티브 상태의 팀 리스트만 뽑을 때) |

- 일반적인 사용 예: `/api/team/list`
- 본인이 포함된 팀 리스트 사용 예: `/api/team/list/include_me/1`
- 본인이 포함된 팀 중 액티브 상태의 팀 리스트 사용 예: `/api/team/list/include_me/1/active/1`

### response

- `is_on`: `1`은 활성화(active). `2`는 비활화(archived)

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"teams": [
			{
				"idx": "1",
				"name": "team1",
				"description": "설명1",
				"users": [
					{
						"idx": "1",
						"name": "c2monster"
					}
				],
				"is_on": "1"
			},
			{
				"idx": "2",
				"name": "team #2",
				"description": "설명2",
				"users": [
					{
						"idx": "2",
						"name": "Mio Ito"
					},
					{
						"idx": "1",
						"name": "c2monster"
					},
					{
						"idx": "5",
						"name": "\ubc15 252883559"
					}
				],
				"is_on": "1"
			},
			{
				"idx": "3",
				"name": "team 333",
				"description": "설명3",
				"users": [
					{
						"idx": "2",
						"name": "Mio Ito"
					},
					{
						"idx": "1",
						"name": "c2monster"
					}
				],
				"is_on": "1"
			},
			{
				"idx": "4",
				"name": "t^4",
				"description": "설명4",
				"users": [
					{
						"idx": "2",
						"name": "Mio Ito"
					}
				],
				"is_on": "1"
			}
		]
	}
}
```

---

## 2. 팀 등록 <a id="team-create"></a>

### `POST /api/team/create`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data  | required | desc |
| ----------- | :---: | :----: | :------: | ---- |
| team_name   | query | string |    O     |      |
| description | query | string |    X     |      |

### response

```json
{
    "error": {
        "code": 200,
        "message": "The Team is added."
    },
    "data": {
        "team": {
            "idx": "6",
            "name": "zxv",
            "pos": "5",
            "description": "zxcv"
        }
    }
}
```

---

## 3. 팀 정보 엑셀 내보내기 <a id="team-export-xls"></a>

### `POST /api/team/export`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
	"error": {
		"code": 200,
		"message": "팀 정보가 다운로드 되었습니다."
	}
}
```

---

## 4. 팀 참여가능한 이용자 목록조회 <a id="team-user-list"></a>

### `GET /api/team/{team_idx}/user/list`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc |
| -------- | :--: | :-----: | :------: | ---- |
| team_idx | path | integer |    O     |      |

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
				"name": "c2m"
			},
			{
				"idx": "2",
				"name": "c3m"
			},
			{
				"idx": "3",
				"name": "c4m"
			}
		],
		"user_idx_with_team": ["1", "2"],
		"user_idx_without_team": ["3"]
	}
}
```

---

## 5. 팀 활성화 <a id="team-activate"></a>

### `POST /api/team/{team_idx}/activate`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc |
| -------- | :--: | :-----: | :------: | ---- |
| team_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "팀이 활성화됐습니다."
	},
	"data": null
}
```

---

## 6. 팀 비활성화 <a id="team-deactivate"></a>

### `POST /api/team/{team_idx}/deactivate`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc |
| -------- | :--: | :-----: | :------: | ---- |
| team_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "팀이 비활성화됐습니다."
	},
	"data": null
}
```

---

## 7. 팀 삭제 <a id="team-delete"></a>

### `POST /api/team/{team_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc |
| -------- | :--: | :-----: | :------: | ---- |
| team_idx | path | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "팀이 삭제됐습니다."
	},
	"data": null
}
```

---

## 8. 팀 정보 수정 <a id="team-update"></a>

### `POST /api/team/{team_idx}/update`

### permission

- `permission.do_global_setting`

- 팀 하나의 1가지 정보만 선택해서 수정 \* column: name, description

### request

| param    | type  |  data   | required | desc             |
| -------- | :---: | :-----: | :------: | ---------------- |
| team_idx | path  | integer |    O     |                  |
| column   | query | string  |    O     |                  |
| old_val  | query | string  |    O     | 공백일 수는 있음 |
| new_val  | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "팀 정보가 수정됐습니다."
	},
	"data": null
}
```

---

## 9. 팀 구성원 변경하기 <a id="team-add-user"></a>

### `POST /api/team/{team_idx}/user/add`

### permission

- `permission.do_global_setting`

### request

| param                   | type  |       data       | required | desc |
| ----------------------- | :---: | :--------------: | :------: | ---- |
| team_idx                | path  |     integer      |    O     |      |
| user_idx_with_team[]    | query | array of integer |    O     |      |
| user_idx_without_team[] | query | array of integer |    O     |      |

- 파라미터를 `team_idx[]` 로 정하고, 이를 반복해서 설정함
- 아래는 `$.ajax`로 보내기 위한 파라미터를 생성하는 방법 예제

```javascript
var user_idxs = ["2", "3"];

var data_to_send = [];

for (i = 0; i < team_idxs.length; i++) {
	data_to_send.push({
		name: "user_idx[]",
		value: users_idxs[i],
	});
}
console.log(data_to_send);
```

### response

```json
{
	"error": {
		"code": 200,
		"message": "팀 구성원이 변경되었습니다."
	},
	"data": {
		"user_idx_with_team": [
			{
				"user_idx": 1,
				"name": "user1"
			},
			{
				"user_idx": 2,
				"name": "user2"
			}
		]
	}
}
```

---

## 끝

[팀 목록 조회]: #team-list
[팀 등록]: #team-create
[팀 정보 엑셀 내보내기]: #team-export-xls
[팀 참여 가능한 이용자 목록]: #team-user-list
[팀 활성화]: #team-activate
[팀 비활성화]: #team-deactivate
[팀 삭제]: #team-delete
[팀 정보 수정]: #team-update
[팀 구성원 변경하기]: #team-add-user
