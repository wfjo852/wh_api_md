# WH2API::Track

## 목차

| 내용                            | slug                                                                                          | 서버 구현 | 웹 적용 | 웹훅  | 로그  |
| :------------------------------ | :-------------------------------------------------------------------------------------------- | :-------: | :-----: | :---: | :---: |
| 1. [트랙 버전 목록 조회]        | /api/project/{project_idx}/track/version/read[/{last}]                                        |    GET    |    O    |   -   |   -   |
|                                 | /api/project/{project_idx}/track/from/{from}/to/{to}/version/read[/{last}]                    |    GET    |    O    |   -   |   -   |
| 2. [트랙 샷 태스크 목록 조회]   | /api/project/{project_idx}/episode/{episode_idx}/track/shot/task/read                         |    GET    |    O    |   -   |   -   |
|                                 | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/track/shot/task/read |    GET    |    O    |   -   |   -   |
| 3. [트랙 에셋 태스크 목록 조회] | /api/project/{project_idx}/track/asset/task/read                                              |    GET    |    O    |   -   |   -   |
|                                 | /api/project/{project_idx}/category/{category_idx}/track/asset/task/read                      |    GET    |    O    |   -   |   -   |
| 4. [트랙 월별 버전 개수 조회]   | /api/project/{project_idx}/track/version/count/{yyyy}/{mm}/list                               |    GET    |    X    |   -   |   -   |
| 5. [트랙 버전 코멘트 목록 조회] | /api/project/{project_idx}/track/from/{from}/to/{to}/version/opinion/read                     |    GET    |    O    |   -   |   -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 트랙 버전 목록 조회 <a id="track-version-list"></a>

### `GET /api/project/{project_idx}/track/version/read[/{last}]`

### `GET /api/project/{project_idx}/track/from/{from}/to/{to}/version/read[/{last}]`

### permission

- `permission.do_track`

### request

| param       | type  |  data   | required | desc       |
| ----------- | :---: | :-----: | :------: | ---------- |
| project_idx | path  | integer |    O     |            |
| last        | path  | integer |    X     |            |
| from        | path  |  date   |    O     | YYYY-MM-DD |
| to          | path  |  date   |    O     | YYYY-MM-DD |
| page        | query | integer |    X     | 생략 시 1  |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "versions": [
      {
        "idx": "13",
        "task": {
            "idx": "8",
            "name": "Concept",
            "status": {
                "idx": "2",
                "name": "confirm"
            },
            "is_on": "1"
        },
        "kind": "asset",
        "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/a912022aa81e647d.png",
        "shot_asset_name": "en_tree",
        "name": "en_tree_concept_v001",
        "status": {
            "idx": "2",
            "name": "confirm"
        },
        "description": "Tree Test",
        "translation": "Tree Test 111",
        "artist": {
            "user": {
                "idx": "1",
                "name": "C2Monster"
            }
        },
        "reviewer": {
            "idx": "22",
            "user": {
                "idx": "4",
                "name": "Supervisor"
            }
        },
        "last_comment": null,
        "last_comment_time": null,
        "request_time": "2019-04-09 18:27:45",
        "project": {
            "idx": "1"
        }
    },
    ],
    "filters": [
      {
        "column": "2",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [["http://localhost:81/2021/02/01/4848cd30e06088d6.jpg"]]
          }
        ]
      },
      {
        "column": "6",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value"
          }
        ]
      }
    ]
  }
}
```

---

## 2. 트랙 샷 태스크 목록 조회 <a id="track-shot-task-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/track/shot/task/read`

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/track/shot/task/read`

### permission

- `permission.do_track`

### request

| param        | type  |  data   | required | desc      |
| ------------ | :---: | :-----: | :------: | --------- |
| project_idx  | path  | integer |    O     |           |
| episode_idx  | path  | integer |    X     |           |
| sequence_idx | path  | integer |    X     |           |
| page         | query | integer |    X     | 생략 시 1 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "track_shot_task": [
      {
        "task_idx": "62",
        "shot_thumbnail": "http://localhost:81/2020/12/08/ccc2bd1852be0372.jpg",
        "project_idx": "1",
        "project_name": "Demo_Bigbuck_Bunny",
        "episode_name": "Ep01",
        "sequence_name": "s0010",
        "shot_name": "s0010_c0010",
        "task_name": "task02",
        "start_date": "2021-01-08",
        "end_date": "2021-04-01",
        "description": "1231231231",
        "status_idx": "14",
        "status_name": "A_tests",
        "last_version_name": null,
        "last_publish_name": null,
        "artist_name": null,
        "artist_user_idx": null,
        "version_status_idx": null,
        "is_on": "1"
      },
      {
        "task_idx": "61",
        "shot_thumbnail": "http://localhost:81/2020/12/08/ccc2bd1852be0372.jpg",
        "project_idx": "1",
        "project_name": "Demo_Bigbuck_Bunny",
        "episode_name": "Ep01",
        "sequence_name": "s0010",
        "shot_name": "s0010_c0010",
        "task_name": "Task01",
        "start_date": null,
        "end_date": null,
        "description": "1",
        "status_idx": "1",
        "status_name": "wip",
        "last_version_name": null,
        "last_publish_name": null,
        "artist_name": "C2Monster",
        "artist_user_idx": "1",
        "version_status_idx": null,
        "is_on": "1"
      }
    ],
    "filters": [
      {
        "column": "6",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [["animation", "comp", "task02"]]
          }
        ]
      },
      {
        "column": "5",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [
              [
                "s0010_c0040",
                "s0010_c0050",
                "s0010_c0060",
                "s0010_c0080",
                "s0010_c0090",
                "s0010_c0100"
              ]
            ]
          }
        ]
      }
    ]
  }
}
```

## 3. 트랙 에셋 태스크 목록 조회 <a id="track-asset-task-list"></a>

### `GET /api/project/{project_idx}/track/asset/task/read`

### `GET /api/project/{project_idx}/asset_category/{asset_category_idx}/track/asset/task/read`

### permission

- `permission.do_track`

### request

| param        | type  |  data   | required | desc      |
| ------------ | :---: | :-----: | :------: | --------- |
| project_idx  | path  | integer |    O     |           |
| category_idx | path  | integer |    X     |           |
| page         | query | integer |    X     | 생략 시 1 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "track_asset_task": [
      {
        "task_idx": "6",
        "asset_thumbnail": "http://localhost:81/2021/02/01/2e08a9aecfbe920c.jpg",
        "project_idx": "1",
        "project_name": "Demo_Bigbuck_Bunny",
        "asset_category_name": "char",
        "asset_idx": "1",
        "asset_name": "ch_bunny",
        "used": "1111",
        "task_name": "Concept",
        "start_date": "2021-01-05",
        "end_date": null,
        "description": "qqq",
        "status_idx": "2",
        "status_name": "confirm",
        "last_version_name": "ep296_sc121_kimchi",
        "last_publish_name": null,
        "artist_name": "C2Monster",
        "artist_user_idx": "1",
        "version_idx": "2",
        "is_on": "1"
      },
      {
        "task_idx": "2",
        "asset_thumbnail": "http://localhost:81/2021/02/01/2e08a9aecfbe920c.jpg",
        "project_idx": "1",
        "project_name": "Demo_Bigbuck_Bunny",
        "asset_category_name": "char",
        "asset_idx": "1",
        "asset_name": "ch_bunny",
        "used": "1111",
        "task_name": "Modeling",
        "start_date": "2021-01-05",
        "end_date": null,
        "description": "qqq",
        "status_idx": "5",
        "status_name": "final",
        "last_version_name": null,
        "last_publish_name": null,
        "artist_name": "C2Monster",
        "artist_user_idx": "1",
        "version_idx": null,
        "is_on": "4"
      }
    ],
    "filters": [
      {
        "column": "5",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [["Modeling", "Texture"]]
          }
        ]
      },
      {
        "column": "4",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [["123", "test2"]]
          }
        ]
      }
    ]
  }
}
```

## 4. 트랙 월별 버전 개수 조회 <a id="track-version-count-list"></a>

### `GET /api/project/{project_idx}/track/version/count/{yyyy}/{mm}/list`

### permission

- `permission.do_track`

### request

| param       | type  |  data   | required | desc        |
| ----------- | :---: | :-----: | :------: | ----------- |
| project_idx | path  | integer |    O     |             |
| yyyy        | path  | string  |    O     | year (YYYY) |
| mm          | path  | string  |    O     | month (MM)  |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "versions_per_date": [
      { "date": "2020-07-16", "count": "22", "prev_no_more": false },
      { "date": "2020-07-21", "count": "31" },
      { "date": "2020-07-22", "count": "4" },
      { "date": "2020-07-24", "count": "9" },
      { "date": "2020-07-29", "count": "30", "next_no_more": false }
    ],
    "move": {
      "prev": { "year": "2020", "month": "03" },
      "next": { "year": "2020", "month": "08" }
    }
  }
}
```

---

# 5. 트랙 버전 코멘트 목록 조회 <a id="track-version-opinion-list"></a>

### `GET /api/project/{project_idx}/track/from/{from}/to/{to}/version/opinion/read`

### permission

- `permission.do_track`

### request

| param       | type  |  data   | required | desc       |
| ----------- | :---: | :-----: | :------: | ---------- |
| project_idx | path  | integer |    O     |            |
| from        | path  |  date   |    O     | YYYY-MM-DD |
| to          | path  |  date   |    O     | YYYY-MM-DD |
| page        | query | integer |    X     | 생략 시 1  |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": [
        {
            "idx": "19",
            "thumbnail": "/2019/04/08/d45d311d6b86ae96.jpg",
            "shot_asset": {
                "idx": "2",
                "name": "s0010_c0020"
            },
            "task": {
                "idx": "1",
                "name": "Animation",
                "status": {
                    "idx": "2",
                    "name": "confirm"
                }
            },
            "version": {
                "idx": "2",
                "name": "big_s0010_c0020_anim_v001",
                "status": {
                    "idx": "2",
                    "name": "confirm"
                }
            },
            "comment": "555",
            "translation": "",
            "creator": {
                "idx": "1",
                "name": "C2Monster"
            },
            "created_time": "2021-08-18 17:46:24"
        }
    ]
}
```

---

## 끝

[트랙 버전 목록 조회]: #track-version-list
[트랙 버전 목록 조회]: #track-version-list
[트랙 샷 태스크 목록 조회]: #track-shot-task-list
[트랙 샷 태스크 목록 조회]: #track-shot-task-list
[트랙 에셋 태스크 목록 조회]: #track-asset-task-list
[트랙 에셋 태스크 목록 조회]: #track-asset-task-list
[트랙 월별 버전 개수 조회]: #track-version-count-list
[트랙 버전 코멘트 목록 조회]: #track-version-count-list
