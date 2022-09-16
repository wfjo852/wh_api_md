# WH2API::Draft

## 목차

| 내용                                       | slug                                                                               | 서버 구현 | 웹/앱 적용 |
| :----------------------------------------- | :--------------------------------------------------------------------------------- | :-------: | :--------: |
| 1. [드래프트 버전 코멘트 그룹 목록 조회]   | /api/project/{project_idx}/draft/version/comment/group/list                        |    GET    |     O      |
| 2. [드래프트 버전 코멘트 그룹 생성]        | /api/project/{project_idx}/draft/version/comment/group/create                      |   POST    |     O      |
| 3. [드래프트 버전 코멘트 그룹 업데이트]    | /api/project/{project_idx}/draft/version/comment/group/update                      |   POST    |     O      |
| 4. [드래프트 버전 코멘트 그룹 삭제]        | /api/project/{project_idx}/draft/version/comment/group/delete                      |   POST    |     O      |
| 5. [드래프트 버전 코멘트 아이템 목록 조회] | /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/list       |    GET    |     O      |
| 6. [드래프트 버전 코멘트 아이템 생성]      | /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/create     |   POST    |     O      |
| 7. [드래프트 버전 코멘트 아이템 업데이트]  | /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/update     |   POST    |     O      |
| 8. [드래프트 버전 코멘트 아이템 삭제]      | /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/delete     |   POST    |     O      |
| 9. [드래프트 버전 코멘트 아이템 레지스터]  | /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/register   |   POST    |     O      |
| 10. [드래프트 버전 코멘트 아이템 초기화]   | /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/initialize |   POST    |     O      |
| 11. [드래프트 파일 업로드]                 | /api/draft/attachment/create                                                       |   POST    |     X      |
| 12. [드래프트 파일 목록 조회]              | /api/draft/attachment/list                                                         |    GET    |     O      |
| 13. [드래프트 파일 조회]                   | /api/draft/attachment/{attachment_idx}/read                                        |    GET    |     O      |
| 14. [드래프트 파일 업데이트]               | /api/draft/attachment/{attachment_idx}/update                                      |   POST    |     O      |
| 15. [드래프트 파일 삭제]                   | /api/draft/attachment/{attachment_idx}/delete                                      |   POST    |     O      |
| 16. [드래프트 파일 벌크 삭제]              | /api/draft/attachment/bulk/delete                                                  |   POST    |     O      |
| 17. [드래프트 파일 링크]                   | /api/draft/attachment/attach                                                       |   POST    |     O      |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 드래프트 버전 코멘트 그룹 목록 조회 <a id="draft-version-comment-group-list"></a>

### `GET /api/project/{project_idx}/draft/version/comment/group/list`

### permission

- `permission.read_draft`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "draft": {
      "groups": [
        {
          "idx": "2",
          "project": {
            "idx": "3",
            "name": "Carbot",
            "description": "TV_Animation",
            "is_on": "1",
            "start_date": "2020-12-01",
            "end_date": "2030-12-31"
          },
          "user": {
            "idx": "175",
            "name": "c6m",
            "is_on": "1",
            "id": "c6m",
            "email": "",
            "thumbnail": "/assets/images/thumbnail/user/small/default.png"
          },
          "which": "asset",
          "description": "test",
          "is_on": "1"
        },
        {
          "idx": "3",
          "project": {
            "idx": "3",
            "name": "Carbot",
            "description": "TV_Animation",
            "is_on": "1",
            "start_date": "2020-12-01",
            "end_date": "2030-12-31"
          },
          "user": {
            "idx": "175",
            "name": "c6m",
            "is_on": "1",
            "id": "c6m",
            "email": "",
            "thumbnail": "/assets/images/thumbnail/user/small/default.png"
          },
          "which": "asset",
          "description": "test",
          "is_on": "1"
        }
      ]
    }
  }
}
```

---

## 2. 드래프트 버전 코멘트 목록 생성 <a id="draft-version-comment-group-create"></a>

### `POST /api/project/{project_idx}/draft/version/comment/group/create`

### permission

- `permission.update_draft`

### request

| param       | type  |  data   | required | desc                 |
| ----------- | :---: | :-----: | :------: | -------------------- |
| project_idx | path  | integer |    O     |                      |
| kind        | query | integer |    O     | 1 - asset / 2 - shot |
| description | query | string  |    O     | YYYY-MM-DD           |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "draft": {
      "group": {
        "idx": 4
      }
    }
  }
}
```

---

## 3. 드래프트 버전 코멘트 그룹 업데이트 <a id="draft-version-comment-group-update"></a>

### `POST /api/project/{project_idx}/draft/version/comment/group/update`

### permission

- `permission.update_draft`

### request

| param       | type  |  data   | required | desc                 |
| ----------- | :---: | :-----: | :------: | -------------------- |
| project_idx | path  | integer |    O     |                      |
| group_idx   | query | integer |    O     |                      |
| kind        | query | integer |    O     | 1 - asset / 2 - shot |
| description | query | string  |    O     |                      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": null
}
```

---

## 4. 드래프트 버전 코멘트 그룹 삭제 <a id="draft-version-comment-group-delete"></a>

### `POST /api/project/{project_idx}/draft/version/comment/group/delete`

### permission

- `permission.update_draft`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| group_idx   | query | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": null
}
```

---

## 5. 드래프트 버전 코멘트 아이템 목록 조회 <a id="draft-version-comment-item-list"></a>

### `GET /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/list`

### permission

- `permission.read_draft`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| group_idx   | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "draft": {
      "items": [
        {
          "idx": "5",
          "memo": null,
          "comment": null,
          "attachment": {
            "idxes": ["1", "2"],
            "count": 2
          },
          "episode": {
            "idx": "3",
            "name": "Ep02"
          },
          "sequence": {
            "idx": null,
            "name": null
          },
          "shot": {
            "idx": null,
            "name": null
          },
          "task": {
            "idx": null,
            "name": null,
            "status": {
              "idx": null,
              "name": null
            }
          },
          "version": {
            "idx": null,
            "name": null,
            "status": {
              "idx": null,
              "name": null
            }
          },
          "pass_to_user": {
            "idx": null,
            "name": null
          },
          "sequences": [],
          "sequence_names": [],
          "tasks": [],
          "task_names": [],
          "task_statuses": [],
          "task_status_names": [],
          "versions": [],
          "version_names": [],
          "version_statuses": [],
          "version_status_names": [],
          "pass_to_users": [],
          "pass_to_user_names": []
        },
        {
          "idx": "6",
          "memo": null,
          "comment": null,
          "attachment": {
            "idxes": null
          },
          "episode": {
            "idx": null,
            "name": null
          },
          "sequence": {
            "idx": null,
            "name": null
          },
          "shot": {
            "idx": null,
            "name": null
          },
          "task": {
            "idx": null,
            "name": null,
            "status": {
              "idx": null,
              "name": null
            }
          },
          "version": {
            "idx": null,
            "name": null,
            "status": {
              "idx": null,
              "name": null
            }
          },
          "pass_to_user": {
            "idx": null,
            "name": null
          },
          "sequences": [],
          "sequence_names": [],
          "tasks": [],
          "task_names": [],
          "task_statuses": [],
          "task_status_names": [],
          "versions": [],
          "version_names": [],
          "version_statuses": [],
          "version_status_names": [],
          "pass_to_users": [],
          "pass_to_user_names": []
        },
        {
          "idx": "7",
          "memo": null,
          "comment": null,
          "attachment": {
            "idxes": null
          },
          "episode": {
            "idx": null,
            "name": null
          },
          "sequence": {
            "idx": null,
            "name": null
          },
          "shot": {
            "idx": null,
            "name": null
          },
          "task": {
            "idx": null,
            "name": null,
            "status": {
              "idx": null,
              "name": null
            }
          },
          "version": {
            "idx": null,
            "name": null,
            "status": {
              "idx": null,
              "name": null
            }
          },
          "pass_to_user": {
            "idx": null,
            "name": null
          },
          "sequences": [],
          "sequence_names": [],
          "tasks": [],
          "task_names": [],
          "task_statuses": [],
          "task_status_names": [],
          "versions": [],
          "version_names": [],
          "version_statuses": [],
          "version_status_names": [],
          "pass_to_users": [],
          "pass_to_user_names": []
        }
      ],
      "episodes": [
        {
          "idx": "3",
          "name": "Ep02"
        },
        {
          "idx": "1",
          "name": "Ep01"
        }
      ],
      "statuses": {
        "task": [
          {
            "idx": "1",
            "name": "wip",
            "color": "#dbd8db"
          },
          {
            "idx": "2",
            "name": "confirm",
            "color": "#03a9f4"
          },
          {
            "idx": "3",
            "name": "retake",
            "color": "#f44336"
          },
          {
            "idx": "4",
            "name": "pub",
            "color": "#ff9800"
          },
          {
            "idx": "5",
            "name": "final",
            "color": "#607d8b"
          }
        ],
        "version": [
          {
            "idx": "1",
            "name": "wip",
            "color": "#dbd8db"
          },
          {
            "idx": "2",
            "name": "confirm",
            "color": "#03a9f4"
          },
          {
            "idx": "3",
            "name": "retake",
            "color": "#f44336"
          },
          {
            "idx": "4",
            "name": "pub",
            "color": "#ff9800"
          },
          {
            "idx": "5",
            "name": "final",
            "color": "#607d8b"
          }
        ]
      },
      "pass_to_users": [
        {
          "idx": "1",
          "name": "C2Monster"
        },
        {
          "idx": "4",
          "name": "Supervisor"
        }
      ]
    }
  }
}
```

---

## 6. 드래프트 버전 코멘트 아이템 생성 <a id="draft-version-comment-item-create"></a>

### `post /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/create`

### permission

- `permission.update_draft`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| group_idx   | path | integer |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "draft": {
      "item": {
        "idx": 3
      }
    }
  }
}
```

---

## 7. 드래프트 버전 코멘트 아이템 업데이트 <a id="draft-version-comment-item-update"></a>

### `post /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/update`

### permission

- `permission.update_draft`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| group_idx   | path  | integer |    O     |      |
| item_idx    | query | integer |    O     |      |
| column      | query | string  |    O     |      |
| new_val     | query | string  |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "draft": {
      "item": {
        "idx": 8,
        "episode": {
          "idx": "1",
          "name": "Ep01"
        },
        "sequence": {
          "idx": "1",
          "name": "s0010"
        },
        "shot": {
          "idx": "3",
          "name": "s0010_c0030"
        },
        "task": {
          "idx": "9",
          "name": "Animation",
          "status": {
            "idx": "5",
            "name": "Done"
          }
        },
        "version": {
          "idx": "5",
          "name": "big_s0010_c0030_anim_v001",
          "status": {
            "idx": "4",
            "name": "pub"
          }
        },
        "pass_to_user": {
          "idx": "1",
          "name": "C2Monster"
        }
      }
    }
  }
}
```

## 8. 드래프트 버전 코멘트 아이템 삭제 <a id="draft-version-comment-item-delete"></a>

### `post /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/delete`

### permission

- `permission.update_draft`

### request

| param       | type  |       data       | required | desc |
| ----------- | :---: | :--------------: | :------: | ---- |
| project_idx | path  |     integer      |    O     |      |
| group_idx   | path  |     integer      |    O     |      |
| item_idx[]  | query | array of integer |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": null
}
```

## 9. 드래프트 버전 코멘트 아이템 레지스터 <a id="draft-version-comment-item-register"></a>

### `post /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/register`

### permission

- `permission.update_draft`

### request

| param                | type  |      data      | required | desc                |
| -------------------- | :---: | :------------: | :------: | ------------------- |
| project_idx          | path  |    integer     |    O     |                     |
| group_idx            | path  |    integer     |    O     |                     |
| item_idx[]           | query |     array      |    O     |                     |
| version_idx[]        | query |     array      |    O     |                     |
| task_idx[]           | query |     array      |    O     |                     |
| task_status_idx[]    | query |     array      |    O     |                     |
| version_status_idx[] | query |     array      |    O     |                     |
| comment[]            | query |     array      |    O     |                     |
| pass_to_user[]       | query |     array      |    O     |                     |
| attachment_idx[]     | query | array of array |    O     | 2차원 배열          |
| is_attachment_delete | query |    integer     |    O     | 0 - 유지 / 1 - 삭제 |

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "registered_item_idxes": [1, 2, 3],
    "registered_group_idx": 1
  }
}
```

## 10. 드래프트 버전 코멘트 아이템 초기화 <a id="draft-version-comment-item-initialize"></a>

### `post /api/project/{project_idx}/draft/version/comment/group/{group_idx}/item/initialize`

### permission

- `permission.update_draft`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| group_idx   | path  | integer |    O     |      |
| item_idx    | query | integer |    O     |      |
| column      | query | string  |    O     |      |
| new_val     | query | string  |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "draft": {
      "item": {
        "idx": 8,
        "episode": {
          "idx": "1",
          "name": "Ep01"
        },
        "sequence": {
          "idx": "1",
          "name": "s0010"
        },
        "shot": {
          "idx": "3",
          "name": "s0010_c0030"
        },
        "task": {
          "idx": "9",
          "name": "Animation",
          "status": {
            "idx": "5",
            "name": "Done"
          }
        },
        "version": {
          "idx": "5",
          "name": "big_s0010_c0030_anim_v001",
          "status": {
            "idx": "4",
            "name": "pub"
          }
        },
        "pass_to_user": {
          "idx": "1",
          "name": "C2Monster"
        }
      }
    }
  }
}
```

## 11. 드래프트 파일 업로드 <a id="draft-attachment-create"></a>

### `post /api/draft/attachment/create`

### permission

- `permission.update_draft`

### request

| param           | type  |      data       | required | desc                          |
| --------------- | :---: | :-------------: | :------: | ----------------------------- |
| project_idx     | query |     integer     |    X     |                               |
| attached[]      | query | array of files  |    O     |                               |
| thumbnail[]     | query | array of files  |    X     |                               |
| attached_path[] | query | array of string |    X     | 첨부 파일의 오리지널 풀패스   |
| metadata[]      | query | array of string |    X     | 첨부 파일의 메타데이터 (json) |

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "draft": {
      "attachments": [
        [
          {
            "idx": "13",
            "name": "/2021/07/19/f6ee93ab1ca0e3be.png",
            "name_original": "ss.png",
            "url_thumbnail": "/2021/07/19/f6ee93ab1ca0e3be_t.png"
          },
          {
            "idx": "14",
            "name": "/2021/07/19/c25afab1edb984d5.png",
            "name_original": "스크린샷 2021-07-19 오후 5.37.27.png",
            "url_thumbnail": "/2021/07/19/c25afab1edb984d5_t.png"
          }
        ]
      ]
    }
  }
}
```

## 12. 드래프트 파일 목록조회 <a id="draft-attachment-list"></a>

### `get /api/draft/attachment/list`

### permission

- `permission.update_draft`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | query | integer |    X     |      |
| item_idx    | query | integer |    X     |      |

- `item_idx`가 있는 경우에만 `is_selected`가 0,1,2로 표시되며 `item_idx`가 없는 경우엔 모두 0으로 출력.
- 0: 링크된 아이템 없음 / 1: `해당 item`에 링크 됨 / 2: `다른 item`에 링크 됨

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "draft": {
      "attachments": [
        {
          "idx": "32",
          "user": {
            "idx": "1",
            "name": "C2Monster"
          },
          "url_thumbnail": "http://localhost:81/2021/07/20/a076d84c9bc40521.png",
          "name": "ss.png",
          "description": null,
          "is_selected": 0,
          "created_time": "2021-07-20 13:52:13"
        },
        {
          "idx": "33",
          "user": {
            "idx": "1",
            "name": "C2Monster"
          },
          "url_thumbnail": "http://localhost:81/2021/07/20/e168dc2410322625.png",
          "name": "스크린샷 2021-07-19 오후 5.37.27.png",
          "description": null,
          "is_selected": 1,
          "created_time": "2021-07-20 13:52:13"
        }
      ]
    }
  }
}
```

## 13. 드래프트 파일 조회 <a id="draft-attachment-read"></a>

### `get /api/draft/attachment/{attachment_idx}/read`

### permission

- `permission.update_draft`

### request

| param          | type |  data   | required | desc |
| -------------- | :--: | :-----: | :------: | ---- |
| attachment_idx | path | integer |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "draft": {
      "attachment": [
        {
          "idx": "26",
          "user": {
            "idx": "1",
            "name": "C2Monster"
          },
          "file_path": "http://localhost:81/2021/07/20/475f330f3fa1db64.png",
          "name": "ss.png",
          "description": null,
          "created_time": "2021-07-20 13:49:51"
        }
      ]
    }
  }
}
```

## 14. 드래프트 파일 업데이트 <a id="draft-attachment-update"></a>

### `get /api/draft/attachment/{attachment_idx}/update`

### permission

- `permission.update_draft`

### request

| param          | type  |  data   | required | desc |
| -------------- | :---: | :-----: | :------: | ---- |
| attachment_idx | path  | integer |    O     |      |
| name           | query | string  |    O     |      |
| description    | query | string  |    X     |      |

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

## 15. 드래프트 파일 삭제 <a id="draft-attachment-delete"></a>

### `POST /api/draft/attachment/{attachment_idx}/delete`

### permission

- `permission.update_draft`

### request

| param          | type |  data   | required | desc |
| -------------- | :--: | :-----: | :------: | ---- |
| attachment_idx | path | integer |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

## 16. 드래프트 파일 벌크 삭제 <a id="draft-attachment-bulk-delete"></a>

### `POST /api/draft/attachment/bulk/delete`

### permission

- `permission.update_draft`

### request

| param            | type  |       data       | required | desc |
| ---------------- | :---: | :--------------: | :------: | ---- |
| attachment_idx[] | query | integer of array |    O     |      |

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

## 17. 드래프트 파일 링크 <a id="draft-attachment-attach"></a>

### `POST /api/draft/attachment/attach`

### permission

- `permission.update_draft`

### request

| param            | type  |       data       | required | desc                    |
| ---------------- | :---: | :--------------: | :------: | ----------------------- |
| item_idx         | query |     integer      |    O     |                         |
| which            | query |      string      |    O     | 'draft_version_comment' |
| attachment_idx[] | query | integer of array |    X     | 모두 해체 시 필수 X     |

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

## 끝

[드래프트 버전 코멘트 그룹 목록 조회]: #draft-version-comment-group-list
[드래프트 버전 코멘트 그룹 생성]: #draft-version-comment-group-create
[드래프트 버전 코멘트 그룹 업데이트]: #draft-version-comment-group-update
[드래프트 버전 코멘트 그룹 삭제]: #draft-version-comment-group-delete
[드래프트 버전 코멘트 아이템 목록 조회]: #draft-version-comment-item-list
[드래프트 버전 코멘트 아이템 생성]: #draft-version-comment-item-create
[드래프트 버전 코멘트 아이템 업데이트]: #draft-version-comment-item-update
[드래프트 버전 코멘트 아이템 삭제]: #draft-version-comment-item-delete
[드래프트 버전 코멘트 아이템 레지스터]: #draft-version-comment-item-register
[드래프트 버전 코멘트 아이템 초기화]: #draft-version-comment-item-initialize
[드래프트 파일 업로드]: #draft-attachment-create
[드래프트 파일 목록조회]: #draft-attachment-list
[드래프트 파일 조회]: #draft-attachment-read
[드래프트 파일 업데이트]: #draft-attachment-update
[드래프트 파일 삭제]: #draft-attachment-delete
[드래프트 파일 벌크 삭제]: #draft-attachment-bulk-delete
[드래프트 파일 링크]: #draft-attachment-attach
