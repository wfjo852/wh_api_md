# WH2API::Log

## 목차 V2

| 내용                       | slug               | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :------------------------- | :----------------- | :-------: | :-----: | :--: | :--: |
| 1. [이용자 로그 목록 조회] | /api/userlogs/list |    GET    |    X    |  -   |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 이용자 로그 목록 조회 <a id="userlog-list"></a>

### `GET /api/userlogs/list`

### permission

- `permission.do_global_setting`
- `permission.read_project`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | query | integer |    X     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  {
    "data": {
      "user_activity_logs": [
        {
          "idx": "410624",
          "action": "update",
          "which": "task_shot",
          "target_idx": "1",
          "project": {
            "idx": "1",
            "name": "Demo_Bigbuck_Bunny",
            "description": "Demo_Bigbuck_Bunny",
            "is_on": "1",
            "start_date": "2018-12-11",
            "end_date": "2019-04-12"
          },
          "user": {
            "idx": "1",
            "name": "C2Monster",
            "is_on": "1",
            "id": "c2m",
            "email": "contact@c2monster.com",
            "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
          },
          "detail": {
            "idx": "1",
            "column": "status",
            "new_val": "final",
            "old_val": "wip"
          },
          "created_time": "2022-03-18 16:20:11"
        }
      ]
    }
  }
}
```

## 끝

[이용자 로그 목록 조회]: #user-activity-log-list
