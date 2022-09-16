# WH2API::User

## 목차

| 내용                            | slug                                     | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :------------------------------ | :--------------------------------------- | :-------: | :-----: | :----: | :--: |
| 1. [이용자 목록 조회]           | /api/user/list                           |    GET    |    O    |   -    |  -   |
| 2. [이용자 정보 수정]           | /api/user/{user_idx}/update              |   POST    |    O    |   -    |  -   |
| 3. [이용자 계정 등록]           | /api/user/create                         |   POST    |    O    |   -    |  -   |
| 4. [이용자 정보 엑셀 내보내기]  | /api/user/export-xls                     |     X     |    X    |   -    |  -   |
| 5. [이용자 계정 삭제]           | /api/user/{user_idx}/delete              |   POST    |    O    |   -    |  -   |
| 6. [이용자 계정 활성화]         | /api/user/{user_idx}/activate            |   POST    |    O    |   -    |  -   |
| 7. [이용자 계정 비활성화]       | /api/user/{user_idx}/deactivate          |   POST    |    O    |   -    |  -   |
| 8. [이용자 비밀번호 초기화]     | /api/user/{user_idx}/password/initialize |   POST    |    O    |   -    |  -   |
| 9. [참여 팀 목록]               | /api/user/{user_idx}/team/list           |    GET    |    O    |   -    |  -   |
| 10. [참여 프로젝트 목록 조회]   | /api/user/{user_idx}/project/list        |    GET    |    O    |   -    |  -   |
| 11. [이용자 팀 참여하기]        | /api/user/{user_idx}/team/add            |   POST    |    O    |   -    |  -   |
| 12. [이용자 프로젝트 참여하기]  | /api/user/{user_idx}/project/add         |   POST    |    O    |   -    |  -   |
| 13. [이용자 역할 목록 조회]     | /api/user/role/list                      |    GET    |    O    |   -    |  -   |
| 14. [이용자 썸네일 업데이트]    | /api/user/{user_idx}/thumbnail/update    |   POST    |    O    |   -    |  -   |
| 15. [본인 프로필 조회]          | /api/user/profile/read                   |    GET    |    O    |   -    |  -   |
| 16. [본인 프로필 내용 수정]     | /api/user/profile/update                 |   POST    |    O    |   -    |  -   |
| 17. [퍼미션 목록 조회]          | /api/user/permission/list                |    O\*    |    O    |   -    |  -   |
| 18. [퍼미션 설정 저장]          | /api/user/permission/update              |   POST    |    O    |   -    |  -   |
| 19. [퍼미션 초기화]             | /api/user/permission/reset               |  X POST   |    X    |   -    |  -   |
| 20. [이용자 로그인]             | /api/user/auth                           |   POST    |    O    | hooked |  -   |
| 21. [이용자 급여 수정]          | /api/user/{user_idx}/salary/update       |   POST    |    O    |   -    |  -   |
| 22. [이용자 업무일 수정]        | /api/user/{user_idx}/working_day/update  |   POST    |    O    |   -    |  -   |
| 23. [비이용자 역할 목록 조회]   | /api/guest/role/list                     |    GET    |    O    |   -    |  -   |
| 24. [이용자 가입]               | /api/user/join                           |   POST    |    O    | hooked |  -   |
| 25. [마이태스크타입 수정]       | /api/user/mytasktype/update              |   POST    |    X    |   -    |  -   |
| 26. [이용자 정보 조회]          | /api/user/{user_idx}/read                |    GET    |    X    |   -    |  -   |
| 27. [이용자 부가정보 업데이트]  | /api/user/meta/update                    |   POST    |    O    |   -    |  -   |
| 28. [이용자 급여 벌크 업데이트] | /api/user/salary/bulk/update             |   POST    |    O    |   -    |  -   |

- O\* - api 없이 콘트롤러에 직접 구현

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 이용자 목록 조회 <a id="user-list"></a>

- TODO: payload 에서 컬럼을 지정하면 지정한 컬럼이 내려오게 하는 식으로 구현하는 것은 그 다음 작업에.
- 태스크 디테일에서 Pass To 목록 조회는 supervisor, artist+supervisor 조회

### `GET /api/user/list`

### permission

- `permission.do_global_setting`

### request

| param      | type |  data   | required | desc                                                        |
| ---------- | :--: | :-----: | :------: | ----------------------------------------------------------- |
| search     | path | string  |    X     | 검색 필드 (user_name, email, phone, mobile)                 |
| keyword    | path | string  |    X     | 검색어                                                      |
| exclude_me | path | integer |    X     | 1 (리스트에서 본인을 제외하고 싶을 때)                      |
| project    | path | integer |    X     | 프로젝트 인덱스                                             |
| mytasktype | path | integer |    X     | 1: artist / 2: supervisor / 3: artist+supervisor / 4: 1과 3 |

- `keyword`(검색어)는 반드시 `search`(검색 필드)가 존재해야 제대로 작동함.
  - 검색 예: `/api/user/list/search/user_name/hong`
- 본인 제외는 값을 1만 허용함.
  - 본인 제외 예: `/api/user/list/exclude_me/1`
- 프로젝트 내에 존재하는 이용자만 검색하려면 `project`를 이용함.
  - 프로젝트 내 검색 예: `/api/user/list/project/1`
- 마이태스크타입으로 검색할 때는 `mytasktype`을 이용함.
  - 프로젝트 내 검색 예: `/api/user/list/mytasktype/2`
- 위의 검색어들은 복합 이용이 가능함. (단, `search`와 `keyword`는 함께 사용해야 함)
  - 복합 사용 예) `/api/user/list/search/user_name/keyword/hong/exclude_me/1`
  - 복합 사용 예) `/api/user/list/search/exclude_me/1/project/1`
  - 복합 사용 예) `/api/user/list/search/exclude_me/1/project/1/mytasktype/4`

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  {
  "data": {
    "users": [
      {
        "idx": "1",
        "id": "c2m",
        "name": "c2monster",
        "thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png",
        "user_role": "artist",
        "email": "c2m@c2m.com",
        "phone": "82 2-561-5335",
        "mobile": "010-1234-5678",
        "is_on": "1",
        "teams": [
          {"idx": 1, "name": "team #2"},
          {"idx": 2, "name": "team #2"},
        ],
        "projects": [
          {"idx": 1, "name": "Popo Cuca"},
          {"idx": 2, "name": "Popo Cuca3"},
        ]
      },
      {
        "idx": "2",
        "id": "c3m",
        "name": "Mio Ito",
        "thumbnail": "http://127.0.0.1:81/2019/04/08/dc3295a0a38e89e9.png",
        "user_role": "artist",
        "email": "c3m@c2.com",
        "phone": "+82 2-561-5335",
        "mobile": "111-222-3333",
        "is_on": "1",
        "teams": [
          {"idx": 1, "name": "team #2"},
          {"idx": 2, "name": "team #2"},
        ],
        "projects": [
          {"idx": 1, "name": "Popo Cuca"},
          {"idx": 2, "name": "Popo Cuca3"},
        ]
      }
    ]
  }
}
```

---

## 2. 이용자 정보 수정 <a id="user-update"></a>

- 이용자 1명의 1가지 정보만 선택해서 수정

### `POST /api/user/{user_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param    | type  |  data   | required | desc                                       |
| -------- | :---: | :-----: | :------: | ------------------------------------------ |
| user_idx | path  | integer |    O     | **본인 아님**                              |
| column   | query | string  |    O     | user_name, user_role, email, phone, mobile |
| old_val  | query | string  |    O     | 공백일 수는 있음                           |
| new_val  | query | string  |    O     | 공백일 수는 있음                           |

### response

```json
{
  "error": {
    "code": 200,
    "message": "User account information is edited."
  },
  "data": null
}
```

---

## 3. 이용자 계정 등록 <a id="user-create"></a>

### `POST /api/user/create`

### permission

- `permission.do_global_setting`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| user_id       | query | string  |    O     |      |
| user_name     | query | string  |    O     |      |
| user_password | query | string  |    O     |      |
| user_role_idx | query | integer |    O     |      |
| email         | query | string  |    X     |      |
| attached      | query |  file   |    X     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "User account is added."
  },
  "data": {
    "user": {
      "idx": "10",
      "name": "Director",
      "id": "c5m",
      "email": "director@c2monster.com",
      "thumbnail": "http://localhost:81/2020/08/12/6271d217cdbbc2da.png",
      "user_role_name": "Director"
    }
  }
}
```

---

## 4. 이용자 정보 엑셀 내보내기 <a id="user-export-xls"></a>

### `POST /api/user/export-xls`

### permission

- `permission.do_global_setting`

### request

```json
{
  "columns": [
    "thumbnail",
    "user_id",
    "user_name",
    "team",
    "type",
    "email",
    "office_tel",
    "mobile",
    "password",
    "skills"
  ],
  "users": [
    {
      "idx": "23",
      "thumbnail": "sample.jpg",
      "user_id": "id0001",
      "user_name": "UserName 001",
      "team": "Team001",
      "type": "Coordinator",
      "email": "id001@gmail.com",
      "office_tel": "000-0000-0000",
      "mobile": "010-1111-1111",
      "skills": ["Production", "Art", "Layout", "Manage"]
    },
    {
      "idx": "23",
      "thumbnail": "sample.jpg",
      "user_id": "id0001",
      "user_name": "UserName 001",
      "team": "Team001",
      "type": "Coordinator",
      "email": "id001@gmail.com",
      "office_tel": "000-0000-0000",
      "mobile": "010-1111-1111",
      "skills": ["Production", "Art", "Layout", "Manage"]
    },
    {
      "idx": "23",
      "thumbnail": "sample.jpg",
      "user_id": "id0001",
      "user_name": "UserName 001",
      "team": "Team001",
      "type": "Coordinator",
      "email": "id001@gmail.com",
      "office_tel": "000-0000-0000",
      "mobile": "010-1111-1111",
      "skills": ["Production", "Art", "Layout", "Manage"]
    }
  ]
}
```

### response

```json
{
  "error": {
    "code": 200,
    "message": "엑셀 다운로드가 되었습니다."
  }
}
```

---

## 5. 이용자 계정 삭제 <a id="user-delete"></a>

### `POST /api/user/{user_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc          |
| -------- | :--: | :-----: | :------: | ------------- |
| user_idx | path | integer |    O     | **본인 아님** |

### response

```json
{
  "error": {
    "code": 200,
    "message": "User account is removed."
  },
  "data": {
    "user": {
      "idx": "21",
      "name": "c6m",
      "id": "c6m",
      "email": "c6m@c2monster.com",
      "thumbnail": "/assets/images/thumbnail/user/small/default.png"
    }
  }
}
```

---

## 6. 이용자 계정 활성화 <a id="user-activate"></a>

### `POST /api/user/{user_idx}/activate`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc          |
| -------- | :--: | :-----: | :------: | ------------- |
| user_idx | path | integer |    O     | **본인 아님** |

### response

```json
{
  "error": {
    "code": 200,
    "message": "User account has been activated."
  },
  "data": {
    "user": {
      "idx": "20",
      "name": "c6m",
      "id": "c6m",
      "email": "c6m@c2monster.com",
      "thumbnail": "/assets/images/thumbnail/user/small/default.png"
    }
  }
}
```

---

## 7. 이용자 계정 비활성화 <a id="user-deactivate"></a>

### `POST /api/user/{user_idx}/deactivate`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc          |
| -------- | :--: | :-----: | :------: | ------------- |
| user_idx | path | integer |    O     | **본인 아님** |

### response

```json
{
  "error": {
    "code": 200,
    "message": "User account is being deactivated."
  },
  "data": null
}
```

---

## 8. 이용자 비밀번호 초기화 <a id="user-pwd-init"></a>

### `POST /api/user/{user_idx}/password/initialize`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc          |
| -------- | :--: | :-----: | :------: | ------------- |
| user_idx | path | integer |    O     | **본인 아님** |

- 본인 아님. `user_idx`가 `url`에 포함되어 있음.

### response

```json
{
  "error": {
    "code": 200,
    "message": "User's account password is initialized."
  },
  "data": {
    "user": {
      "idx": "20",
      "name": "c6m",
      "id": "c6m",
      "email": "c6m@c2monster.com",
      "thumbnail": "/assets/images/thumbnail/user/small/default.png"
    }
  }
}
```

---

## 9. 참여 팀 목록 <a id="user-team-list"></a>

- 시스템에 존재하는 모든 팀이 리스팅되며, `user_idx`가 포함된/포함 안 된 팀 인덱스가 주어진다.

### `GET /api/user/{user_idx}/team/list`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc          |
| -------- | :--: | :-----: | :------: | ------------- |
| user_idx | path | integer |    O     | **본인 아님** |

### response

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
        "name": "team #1"
      },
      {
        "idx": "2",
        "name": "team #2"
      },
      {
        "idx": "3",
        "name": "team #3"
      }
    ],
    "team_idx_with_user": ["1", "2"],
    "team_idx_without_user": ["3"]
  }
}
```

---

## 10. 참여 프로젝트 목록 <a id="user-project-list"></a>

- 시스템에 존재하는 모든 프로젝트가 리스팅되며, `user_idx`가 포함된/포함 안 된 프로젝트 인덱스가 주어진다.

### `GET /api/user/{user_idx}/project/list`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc          |
| -------- | :--: | :-----: | :------: | ------------- |
| user_idx | path | integer |    O     | **본인 아님** |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "projects": [
      {
        "idx": "1",
        "name": "project #1"
      },
      {
        "idx": "2",
        "name": "project #2"
      },
      {
        "idx": "3",
        "name": "project #3"
      }
    ],
    "project_idx_with_user": ["1", "2"],
    "project_idx_without_user": ["3"]
  }
}
```

---

## 11. 이용자 팀 참여하기 <a id="user-add-team"></a>

TODO: 순서가 지정되어야해서 순서대로 보내는데 아직 서버에서 미구현
TODO: 제외된 이용자 삭제 서버에서 미구현

### `POST /api/user/{user_idx}/team/add`

### permission

- `permission.do_global_setting`

### request

| param                   | type  |  data   | required | desc          |
| ----------------------- | :---: | :-----: | :------: | ------------- |
| user_idx                | path  | integer |    O     | **본인 아님** |
| team_idx_with_user[]    | query | integer |    X     |               |
| team_idx_without_user[] | query | integer |    X     |               |
| add_team_name[]         | query | string  |    X     |               |

- 파라미터를 `team_idx[]` 로 정하고, 이를 반복해서 설정함
- 아래는 `$.ajax`로 보내기 위한 파라미터를 생성하는 방법 예제

```javascript
var team_idxs = ["2", "3"];

var data_to_send = [];

for (i = 0; i < team_idxs.length; i++) {
  data_to_send.push({
    name: "team_idx[]",
    value: team_idxs[i],
  });
}
console.log(data_to_send);
// data_to_send 값을 $.ajax()의 data에 넣어서 보내면 됨.
```

### response

```json
{
  "error": {
    "code": 200,
    "message": "이용자가 팀에 추가됐습니다."
  },
  "data": {
    "team_idx_with_user": [
      {
        "idx": 1,
        "name": "team1"
      },
      {
        "idx": 2,
        "name": "team2"
      }
    ]
  }
}
```

---

## 12. 이용자 프로젝트 참여하기 <a id="user-add-project"></a>

TODO: 순서가 지정되어야해서 순서대로 보내는데 아직 서버에서 미구현
TODO: 제외된 프로젝트 삭제 서버에서 미구현

### `POST /api/user/{user_idx}/project/add`

### permission

- `permission.do_global_setting`

### request

| param                   | type  |  data   | required | desc          |
| ----------------------- | :---: | :-----: | :------: | ------------- |
| user_idx                | path  | integer |    O     | **본인 아님** |
| project_idx_with_user[] | query | integer |    O     |               |
| add_project_name[]      | query | string  |    X     |               |

- 파라미터를 `team_idx[]` 로 정하고, 이를 반복해서 설정함
- 아래는 `$.ajax`로 보내기 위한 파라미터를 생성하는 방법 예제

```javascript
var team_idxs = ["2", "3"];

var data_to_send = [];

for (i = 0; i < team_idxs.length; i++) {
  data_to_send.push({
    name: "team_idx[]",
    value: team_idxs[i],
  });
}
console.log(data_to_send);
// data_to_send 값을 $.ajax()의 data에 넣어서 보내면 됨.
```

### response

```json
{
  "error": {
    "code": 200,
    "message": "이용자가 프로젝트에 참여하게 되었습니다."
  },
  "data": {
    "project_idx_with_user": [
      {
        "idx": 1,
        "name": "project01"
      },
      {
        "idx": 2,
        "name": "project02"
      }
    ]
  }
}
```

---

## 13. 이용자 역할 목록 조회 <a id="user-role-list"></a>

### `GET /api/user/role/list`

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
    "message": "Success"
  },
  "data": {
    "user_roles": [
      {
        "idx": "1",
        "name": "Administrator",
        "mytasktype": {
          "idx": "3"
        },
        "description": "\uad00\ub9ac\uc790"
      },
      {
        "idx": "2",
        "name": "Artist",
        "mytasktype": {
          "idx": "1"
        },
        "description": "\uc791\uc5c5\uc790"
      },
      {
        "idx": "3",
        "name": "Producer",
        "mytasktype": {
          "idx": "0"
        },
        "description": "\uc81c\uc791 PD"
      },
      {
        "idx": "4",
        "name": "Coordinator",
        "mytasktype": {
          "idx": "0"
        },
        "description": "\uc2a4\ucf00\uc904 \uad00\ub9ac"
      },
      {
        "idx": "5",
        "name": "Main Supervisor",
        "mytasktype": {
          "idx": "2"
        },
        "description": "\ucd5c\uc885 \uacb0\uc815\uad8c\uc790"
      },
      {
        "idx": "6",
        "name": "Sub Supervisor",
        "mytasktype": {
          "idx": "3"
        },
        "description": "\uc911\uac04 \uacb0\uc815\uad8c\uc790"
      },
      {
        "idx": "7",
        "name": "Leader",
        "mytasktype": {
          "idx": "3"
        },
        "description": "\ud300\uc7a5"
      },
      {
        "idx": "8",
        "name": "Director",
        "mytasktype": {
          "idx": "2"
        },
        "description": "\ud504\ub85c\uc81d\ud2b8 \ub2f4\ub2f9 \uac10\ub3c5"
      },
      {
        "idx": "9",
        "name": "outsourcing",
        "mytasktype": {
          "idx": "1"
        },
        "description": "\uc678\uc8fc \uc5c5\uccb4"
      }
    ],
    "mytasktypes": [
      {
        "idx": "1",
        "name": "artist"
      },
      {
        "idx": "2",
        "name": "supervisor"
      },
      {
        "idx": "3",
        "name": "artist + supervisor"
      }
    ]
  }
}
```

---

## 14. 이용자 썸네일 업데이트 <a id="user-thumbnail"></a>

### `POST /api/user/{user_idx}/thumbnail/update`

### permission

- `permission.do_global_setting`

### request

| param    | type  |  data   | required | desc          |
| -------- | :---: | :-----: | :------: | ------------- |
| user_idx | path  | integer |    O     | **본인 아님** |
| attached | query |  file   |    O     |               |

### response

```json
{
  "error": {
    "code": 200,
    "message": "User's thumbnail is being uploaded."
  },
  "data": {
    "idx": "4",
    "name": "Supervisor",
    "id": "c4m",
    "email": "",
    "thumbnail": "http://localhost:81/2020/08/13/ab4b6b30937a805a.png"
  }
}
```

---

## 15. 본인 프로필 조회 <a id="#myprofile-read"></a>

- 본인 기준에서의 메시지 채널 목록을 조회하는 것임.

### `GET /api/user/profile/read`

### permission

- every user can do it.

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "user": {
      "id": "c2m",
      "name": "C2Monster",
      "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png",
      "email": "contact@c2monster.com",
      "phone": "+82 2-561-5335",
      "mobile": "010-1234-5678",
      "lang": "EN"
    }
  }
}
```

---

## 16. 본인 프로필 내용 수정 <a id="#myprofile-update"></a>

### `POST /api/user/profile/update`

### permission

- every user can do it.

### request

| param        | type  |  data  | required | desc                 |
| ------------ | :---: | :----: | :------: | -------------------- |
| user_name    | query | string |    O     |                      |
| lang         | query | string |    O     | 'KO' or 'EN' or 'CN' |
| attached     | query |  file  |    X     |                      |
| email        | query | string |    X     |                      |
| phone        | query | string |    X     |                      |
| mobile       | query | string |    X     |                      |
| old_password | query | string |    O     |                      |
| new_password | query | string |    O     |                      |

- 이용자 아이디 user_id 는 수정하지 못하기 때문에 보낼 필요가 없음
- 서버에 전송하기 전 패스워드 체크 필요.
  _ `old_password`를 입력하지 않으면 클라이언트에서 에러 처리
  _ `new_password` 와 `old_password`를 비교해서 다르면 클라이언트에서 에러 처리

### response

```json
{
  "error": {
    "code": 200,
    "message": "Profile information is benig edited."
  },
  "data": {
    "user": {
      "idx": "1",
      "name": "C2Monster",
      "id": "c2m",
      "email": "contact@c2monster.com",
      "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
    }
  }
}
```

- 이용자 썸네일을 업데이트하면 data.user.thumbnail 에 바뀐 이용자 썸네일의 주소가 표시된다.

---

## 17. 퍼미션 목록 조회 <a id="user-permission-list"></a>

### `GET /api/user/permission/list`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| X     |  X   |  X   |    X     | X    |

### response

- 콘트롤러에서 직접 내려줌.

---

## 18. 퍼미션 설정 저장 <a id="user-permission-update"></a>

### `POST /api/user/permission/update`

### permission

- `permission.do_global_setting`

### request

| param                                           | type  |  data   | required | desc |
| ----------------------------------------------- | :---: | :-----: | :------: | ---- |
| user_role_idx[]                                 | query | integer |    O     |      |
| mytasktype_idx[]                                | query | integer |    O     |      |
| menu_global_setting[]                           | query | integer |    O     |      |
| menu_forum[]                                    | query | integer |    O     |      |
| menu_mytask[]                                   | query | integer |    O     |      |
| menu_shot[]                                     | query | integer |    O     |      |
| menu_asset[]                                    | query | integer |    O     |      |
| menu_track[]                                    | query | integer |    O     |      |
| menu_message[]                                  | query | integer |    O     |      |
| menu_profile_edit[]                             | query | integer |    O     |      |
| project_setting_project_read[]                  | query | integer |    O     |      |
| project_setting_project_add_del_edit[]          | query | integer |    O     |      |
| project_setting_episode_sequence_read[]         | query | integer |    O     |      |
| project_setting_episode_sequence_add_del_edit[] | query | integer |    O     |      |
| project_setting_shot_asset_read[]               | query | integer |    O     |      |
| project_setting_shot_asset_add_del_edit[]       | query | integer |    O     |      |
| project_setting_track_read[]                    | query | integer |    O     |      |
| project_setting_track_add_del_edit[]            | query | integer |    O     |      |
| project_setting_track_allocation[]              | query | integer |    O     |      |
| project_setting_track_deallocation[]            | query | integer |    O     |      |
| schedule_artist_allocation[]                    | query | integer |    O     |      |
| schedule_artist_deallocation[]                  | query | integer |    O     |      |
| schedule_schedule_edit[]                        | query | integer |    O     |      |
| version_version_add[]                           | query | integer |    O     |      |
| version_version_del[]                           | query | integer |    O     |      |
| version_version_edit[]                          | query | integer |    O     |      |
| version_version_read[]                          | query | integer |    O     |      |
| version_comment_add[]                           | query | integer |    O     |      |
| version_comment_delete[]                        | query | integer |    O     |      |
| version_comment_edit[]                          | query | integer |    O     |      |
| version_comment_read[]                          | query | integer |    O     |      |
| publish_add[]                                   | query | integer |    O     |      |
| publish_edit[]                                  | query | integer |    O     |      |
| publish_read[]                                  | query | integer |    O     |      |
| status_project_status_change[]                  | query | integer |    O     |      |
| status_episode_status_change[]                  | query | integer |    O     |      |
| status_sequence_status_change[]                 | query | integer |    O     |      |
| status_shot_status_change[]                     | query | integer |    O     |      |
| status_asset_category_status_change[]           | query | integer |    O     |      |
| status_asset_status_change[]                    | query | integer |    O     |      |
| status_task_status_change[]                     | query | integer |    O     |      |
| status_version_status_change[]                  | query | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "이용자 퍼미션 설정이 수정됐습니다."
  },
  "data": null
}
```

---

## 19. 퍼미션 초기화 <a id="user-permission-reset"></a>

### `POST /api/user/permission/reset`

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
    "message": "이용자 퍼미션 설정이 초기화 되었습니다."
  },
  "data": null
}
```

---

## 20. 이용자 로그인 <a id="user-auth"></a>

### `POST /api/user/auth`

### Webhook

- event: user
- action: auth

### permission

- all

### request

| param         | type  |  data   | required | desc                                                                          |
| ------------- | :---: | :-----: | :------: | ----------------------------------------------------------------------------- |
| userid        | query | string  |    O     |                                                                               |
| userpw        | query | string  |    O     | SHA256 해시 후 base64 인코딩                                                  |
| origin_server | query | string  |    O     | 접속하려는 웜홀 서버 도메인 (예: http://127.1.2.3 / https://wh.c2monster.com) |
| outside       | query | integer |    X     | 외부 접속이면 1, 일반 내부 접속이면 0. 기본값은 0                             |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "token": "nwefisdjijqwdf.ewijidsijf.sdijiij",
    "expires": 81283182312
  }
}
```

---

## 21. 이용자 급여 수정 <a id="user-salary-update"></a>

### `POST /api/user/{user_idx}/salary/update`

### permission

- `permission.do_global_setting`

### request

| param    | type  |  data   | required | desc          |
| -------- | :---: | :-----: | :------: | ------------- |
| user_idx | path  | integer |    O     | **본인 아님** |
| yyyy     | query | string  |    O     | year (YYYY)   |
| mm       | query | string  |    O     | month (MM)    |
| salary   | query | integer |    X     | 안보내면 삭제 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "이용자 급여 정보가 수정됐습니다."
  },
  "data": null
}
```

---

## 22. 이용자 업무일 수정 <a id="user-working-day-update"></a>

### `POST /api/user/{user_idx}/working_day/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc          |
| ----------- | :---: | :-----: | :------: | ------------- |
| user_idx    | path  | integer |    O     | **본인 아님** |
| yyyy        | query | string  |    O     | year (YYYY)   |
| mm          | query | string  |    O     | month (MM)    |
| working_day | query | integer |    X     | 안보내면 삭제 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "이용자 업무일 정보가 수정됐습니다."
  },
  "data": null
}
```

---

## 23. 비이용자 역할 목록 조회 <a id="guest-role-list"></a>

### `GET /api/guest/role/list`

### permission

- all

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
    "user_roles": [
      {
        "idx": "2",
        "name": "Artist"
      },
      {
        "idx": "5",
        "name": "Main Supervisor"
      },
      {
        "idx": "6",
        "name": "Sub Supervisor"
      },
      {
        "idx": "7",
        "name": "Leader"
      },
      {
        "idx": "8",
        "name": "Director"
      },
      {
        "idx": "9",
        "name": "outsourcing"
      },
      {
        "idx": "999",
        "name": "set for later"
      }
    ]
  }
}
```

---

## 24. 이용자 가입 <a id="user-join"></a>

### `POST /api/user/join`

### Webhook

- event: user
- action: join

### permission

- all

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| user_id       | query | string  |    O     |      |
| user_name     | query | string  |    O     |      |
| user_password | query | string  |    O     |      |
| user_role_idx | query | integer |    O     |      |
| email         | query | string  |    X     |      |
| attached      | query |  file   |    X     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "가입이 완료됐습니다. 관리자 승인 후 이용할 수 있습니다."
  },
  "data": {
    "user": {
      "idx": "8",
      "id": "tomb",
      "name": "Thomas Doe",
      "user_role": {
        "idx": "1",
        "name": "Artist"
      }
    }
  }
}
```

---

## 25. 마이태스크타입 수정 <a id="mytasktype-update"></a>

### `POST /api/user/mytasktype/update`

### request

| param          | type  |  data   | required | desc |
| -------------- | :---: | :-----: | :------: | ---- |
| user_role_idx  | query | integer |    O     |      |
| mytasktype_idx | query | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "마이태스크 세팅이 변경되었습니다."
  },
  "data": null
}
```

---

## 26. 이용자 정보 조회 <a id ="user-read"></a>

### `GET /api/user/{user_idx}/read`

### permission

- `permission.do_global_setting`

### request

| param    | type |  data   | required | desc |
| -------- | :--: | :-----: | :------: | ---- |
| user_idx | path | integer |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "user": {
      "idx": "1",
      "id": "c2m",
      "name": "C2Monster",
      "email": "contact@c2monster.com",
      "role": "Administrator",
      "phone": "+82 2-561-5335",
      "mobile": "010-1234-5678",
      "thumbnail": "http://127.0.0.1:81/2019/04/08/c1f855a779d0543e.png",
      "is_on": "1",
      "teams": [
        {
          "idx": "2",
          "name": "team1",
          "description": "1 team"
        },
        {
          "idx": "3",
          "name": "team2",
          "description": "2 team"
        }
      ],
      "projects": [
        {
          "idx": "1",
          "name": "Demo_Bigbuck_Bunny",
          "description": "Demo_Bigbuck_Bunny",
          "start_date": "2018-12-11",
          "end_date": "2019-04-12"
        }
      ]
    }
  }
}
```

---

## 27. 이용자 부가정보 업데이트 <a id ="user-meata-update"></a>

### `POST /api/user/meta/update`

### permission

- `permission.do_global_setting`

### request

| param         | type  |  data   | required | desc |
| ------------- | :---: | :-----: | :------: | ---- |
| project_idx   | query | integer |    X     |      |
| setting_name  | query | string  |    O     |      |
| setting_value | query |  array  |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "성공."
  },
  "data": null
}
```

---

## 28. 이용자 급여 벌크 업데이트 <a id ="user-salary-bulk-update"></a>

### `POST /api/user/salary/bulk/update`

### permission

- `permission.do_global_setting`

### request

| param  | type  |  data   | required | desc                          |
| ------ | :---: | :-----: | :------: | ----------------------------- |
| action | query | integer |    O     | init - 초기화 / remain - 유지 |
| yyyy   | query | string  |    O     | year (YYYY)                   |
| mm     | query | string  |    O     | month (MM)                    |
| salary | query | integer |    X     | init일 때 초기 세팅 금액      |

```json
{
  "error": {
    "code": 200,
    "message": "성공."
  },
  "data": null
}
```

---

## 끝

[이용자 목록 조회]: #user-list
[이용자 정보 수정]: #user-update
[이용자 계정 등록]: #user-create
[이용자 정보 엑셀 내보내기]: #user-export-xls
[이용자 계정 삭제]: #user-delete
[이용자 계정 활성화]: #user-activate
[이용자 계정 비활성화]: #user-deactivate
[이용자 비밀번호 초기화]: #user-pwd-init
[참여 팀 목록]: #user-team-list
[참여 프로젝트 목록 조회]: #user-project-list
[이용자 팀 참여하기]: #user-add-team
[이용자 프로젝트 참여하기]: #user-add-project
[이용자 역할 목록 조회]: #user-role-list
[이용자 썸네일 업데이트]: #user-thumbnail
[본인 프로필 조회]: #myprofile-read
[본인 프로필 내용 수정]: #myprofile-update
[퍼미션 목록 조회]: #user-permission-list
[퍼미션 설정 저장]: #user-permission-update
[퍼미션 초기화]: #user-permission-reset
[이용자 로그인]: #user-auth
[이용자 급여 수정]: #user-salary-update
[이용자 업무일 수정]: #user-working-day-update
[비이용자 역할 목록 조회]: #guest-role-list
[이용자 가입]: #user-join
[마이태스크타입 수정]: #mytasktype-update
[이용자 정보 조회]: #user-read
[이용자 부가정보 업데이트]: #user-meta-update
[이용자 급여 벌크 업데이트]: #user-salary-bulk-update
