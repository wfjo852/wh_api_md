# WH2API::MyTask

## 목차

| 내용                           | slug                                 | 서버 구현 | 웹 적용 |
| :----------------------------- | :----------------------------------- | :-------: | :-----: |
| 1. [To-Do 조회]                | /api/mytask/todo/read                |    GET    |    O    |
| 2. [In-Progress 조회]          | /api/mytask/inprogress/read[/{last}] |    GET    |    O    |
| 3. [Done 조회]                 | /api/mytask/done/read                |    GET    |    O    |
| 4. [CC 목록 조회]              | /api/mytask/cc/read[/{last}]         |    GET    |    O    |
| 5. [마이태스크 설정 목록 조회] | /api/mytask/setting/list             |    GET    |    O    |
| 6. [마이태스크 설정 정보 저장] | /api/mytask/setting/update           |   POST    |    O    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. To-Do 조회 조회 <a id="mytask-todo-read"></a>

### `GET /api/mytask/todo/read`

### permission

- `permission.read_mytask`

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
    "version_overview": null,
    "task_shot_overview": [
      {
        "task_idx": "2",
        "kind": "shot",
        "shot_thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/d45d311d6b86ae96.jpg",
        "project_name": "Demo_Bigbuck_Bunny",
        "episode_name": "Ep01",
        "sequence_name": "s0010",
        "shot_name": "s0010_c0020",
        "task_name": "Comp",
        "start_date": null,
        "end_date": null,
        "description": "",
        "status_name": "wip",
        "project_idx": "1",
        "task_is_on": "1"
      }
    ],
    "task_asset_overview": [
      {
        "task_idx": "4",
        "kind": "asset",
        "asset_thumbnail": "http://localhost:81/2019/04/08/e1ec4ac7862fc307.jpg",
        "project_name": "Demo_Bigbuck_Bunny",
        "asset_category_name": "char",
        "asset_name": "ch_squirrel",
        "task_name": "Texture",
        "start_date": null,
        "end_date": null,
        "description": "",
        "status_name": "confirm",
        "project_idx": "1",
        "task_is_on": "1"
      }
    ]
  }
}
```

---

## 2. In-Progress 목록 조회 <a id="mytask-inprogress-read"></a>

### `GET /api/mytask/inprogress/read[/{last}]`

### permission

- `permission.read_mytask`

### request

| param | type |  data  | required | desc     |
| ----- | :--: | :----: | :------: | -------- |
| last  | path | string |    X     | 값: last |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "to_do": [
      {
        "task_idx": 1,
        "thumbnail": "/assets/images/common/shot_img07.jpg",
        "shot_asset_name": "s0010_c0010",
        "task_name": "com",
        "task_status": "Waiting",
        "version_name": "s0010_c0010_comp_v002.mp4",
        "version_status": "retake",
        "comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
        "artist": "박종호",
        "reviewer": "김상인",
        "pass_to": "이진영",
        "review_comment": "",
        "request_time": "2018-12-19 17:39:20",
        "answer_time": "",
        "project_idx": "1"
      },
      {
        "task_idx": 2,
        "thumbnail": "/assets/images/common/shot_img07.jpg",
        "shot_asset_name": "s0010_c0010",
        "task_name": "com",
        "task_status": "Waiting",
        "version_name": "s0010_c0010_comp_v002.mp4",
        "version_status": "retake",
        "comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
        "artist": "박종호",
        "reviewer": "김상인",
        "pass_to": "이진영",
        "review_comment": "",
        "request_time": "2018-12-19 17:39:20",
        "answer_time": "",
        "project_idx": "1"
      }
    ]
  }
}
```

---

## 3. Done 목록 조회 <a id="mytask-done-read"></a>

### `GET /api/mytask/done/read`

### permission

- `permission.read_mytask`

### request

| param | type  |  data   | required | desc |
| ----- | :---: | :-----: | :------: | ---- |
| page  | query | integer |    X     | X    |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "done": [
      {
        "task_idx": 1,
        "thumbnail": "/assets/images/common/shot_img04.jpg",
        "shot_asset_name": "s0010_c0010",
        "task_name": "comp",
        "task_status": "Waiting",
        "version_name": "s0010_c0010_comp_v002.mp4",
        "version_status": "retake",
        "comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
        "artist": "박종호",
        "reviewer": "김상인",
        "pass_to": "이진영",
        "review_comment": "",
        "request_time": "2018-12-19 17:39:20",
        "answer_time": "",
        "task_idx": 1,
        "thumbnail": "/assets/images/common/shot_img01.jpg",
        "project": "Project Name 001",
        "category": "Category01",
        "asset_name": "Asset Name01",
        "task_name": "Task Name 001",
        "used": "",
        "start_date": "2018-01-15",
        "end_date": "2018-08-11",
        "description": "Lorem Ipsum is simply",
        "status": "Waiting",
        "change_status": "Apply",
        "project_idx": 1
      },
      {
        "task_idx": 2,
        "thumbnail": "/assets/images/common/shot_img04.jpg",
        "shot_asset_name": "s0010_c0010",
        "task_name": "comp",
        "task_status": "Waiting",
        "version_name": "s0010_c0010_comp_v002.mp4",
        "version_status": "retake",
        "comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
        "artist": "박종호",
        "reviewer": "김상인",
        "pass_to": "이진영",
        "review_comment": "",
        "request_time": "2018-12-19 17:39:20",
        "answer_time": "",
        "task_idx": 1,
        "thumbnail": "/assets/images/common/shot_img01.jpg",
        "project": "Project Name 001",
        "category": "Category01",
        "asset_name": "Asset Name01",
        "task_name": "Task Name 001",
        "used": "",
        "start_date": "2018-01-15",
        "end_date": "2018-08-11",
        "description": "Lorem Ipsum is simply",
        "status": "Waiting",
        "change_status": "Apply",
        "project_idx": 1
      }
    ],
    "paging": {
      "cur_page": 1,
      "start_page": 1,
      "last_page": 1,
      "total_page": 1
    }
  }
}
```

---

## 4. CC 목록 조회 <a id="mytask-cc-read"></a>

### `GET /api/mytask/cc/read[/{last}]`

### permission

- `permission.read_mytask`

### request

| param | type |  data  | required | desc     |
| ----- | :--: | :----: | :------: | -------- |
| last  | path | string |    X     | 값: last |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "done": [
      {
        "task_idx": 1,
        "thumbnail": "/assets/images/common/shot_img07.jp",
        "shot_asset_name": "s0010_c0010",
        "task_name": "comp",
        "task_status": "Waiting",
        "version_name": "s0010_c0010_comp_v002.mp",
        "version_status": "retake",
        "comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
        "artist": "박종호",
        "reviewer": "김상인",
        "pass_to": "이진영",
        "review_comment": "",
        "request_time": "2018-12-19 17:39:20",
        "answer_time": "",
        "project_idx": 1
      },
      {
        "task_idx": 1,
        "thumbnail": "/assets/images/common/shot_img07.jp",
        "shot_asset_name": "s0010_c0010",
        "task_name": "comp",
        "task_status": "Waiting",
        "version_name": "s0010_c0010_comp_v002.mp",
        "version_status": "retake",
        "comment": "컨펌 부탁드리겠습니다. 중간에 저 부분이 좀 이상한 거 같습니다.",
        "artist": "박종호",
        "reviewer": "김상인",
        "pass_to": "이진영",
        "review_comment": "",
        "request_time": "2018-12-19 17:39:20",
        "answer_time": "",
        "project_idx": 1
      }
    ],
    "paging": {
      "cur_page": 1,
      "start_page": 1,
      "last_page": 1,
      "total_page": 1
    }
  }
}
```

---

## 5. 마이태스크 설정 목록 조회 <a id="mytask-setting-list"></a>

### `GET /api/mytask/setting/list`

### permission

- `permission.do_mytask_setting`

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
    "mytask_setting": {
      "idx_1": {
        "col1": {
          "mytasktype_idx": "1",
          "enabled": "0",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": null
        },
        "col2": {
          "mytasktype_idx": "1",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["1", "4"]
        },
        "col3": {
          "mytasktype_idx": "1",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["2", "4", "5"]
        },
        "col4": {
          "mytasktype_idx": "1",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["2", "3"]
        }
      },
      "idx_2": {
        "col1": {
          "mytasktype_idx": "2",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["1", "3"]
        },
        "col2": {
          "mytasktype_idx": "2",
          "enabled": "0",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": null
        },
        "col3": {
          "mytasktype_idx": "2",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["2", "4"]
        },
        "col4": {
          "mytasktype_idx": "2",
          "enabled": "0",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": null
        }
      },
      "idx_3": {
        "col1": {
          "mytasktype_idx": "3",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["4", "5"]
        },
        "col2": {
          "mytasktype_idx": "3",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["2"]
        },
        "col3": {
          "mytasktype_idx": "3",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["1", "3"]
        },
        "col4": {
          "mytasktype_idx": "3",
          "enabled": "1",
          "statuses": [
            {
              "status_idx": "1",
              "name": "wip"
            },
            {
              "status_idx": "2",
              "name": "confirm"
            },
            {
              "status_idx": "3",
              "name": "retake"
            },
            {
              "status_idx": "4",
              "name": "pub"
            },
            {
              "status_idx": "5",
              "name": "final"
            }
          ],
          "checked_status": ["1"]
        }
      }
    }
  }
}
```

---

## 6. 마이태스크 설정 정보 저장 <a id="#mytask-setting-update"></a>

### `POST /api/mytask/setting/update`

### permission

- `permission.do_mytask_setting`

### request

| param          | type  |       data       | required | desc                                |
| -------------- | :---: | :--------------: | :------: | ----------------------------------- |
| mytasktype_idx | query |     integer      |    O     | 서버가 내려주는 정보를 그대로 이용  |
| col1[]         | query | array of integer |    X     | 1번째 컬럼에서 선택된 status 인덱스 |
| col2[]         | query | array of integer |    X     | 2번째 컬럼에서 선택된 status 인덱스 |
| col3[]         | query | array of integer |    X     | 3번째 컬럼에서 선택된 status 인덱스 |
| col4[]         | query | array of integer |    X     | 4번째 컬럼에서 선택된 status 인덱스 |

- col1[] ~ col4[] 는 그 안에 값을 1개만 전달해도 배열 형태로 전송해야 함

### response

```json
{
  "error": {
    "code": 200,
    "message": "마이태스크 설정을 저장했습니다."
  },
  "data": null
}
```

---

## 끝

[to-do 조회]: #mytask-todo-read
[in-progress 조회]: #mytask-inprogress-read
[done 조회]: #mytask-done-read
[cc 목록 조회]: #mytask-cc-read
[마이태스크 설정 목록 조회]: #mytask-setting-list
[마이태스크 설정 정보 저장]: #mytask-setting-update
