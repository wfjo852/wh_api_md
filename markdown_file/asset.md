# WH2API::Asset

## 목차

| 내용                                     | slug                                                                            | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :--------------------------------------- | :------------------------------------------------------------------------------ | :-------: | :-----: | :----: | :--: |
| 1. [에셋 등록]                           | /api/project/{project_idx}/asset_category/{asset_category_idx}/asset/create     |   POST    |    O    | hooked |  O   |
| 2. [에셋 정보 수정]                      | /api/project/{project_idx}/asset/{asset_idx}/update                             |   POST    |    O    | hooked |  O   |
| 3. [에셋 벌크 삭제]                      | /api/project/{project_idx}/asset/bulk/delete                                    |   POST    |    O    |   -    |  O   |
| 4. [에셋 썸네일 업데이트]                | /api/project/{project_idx}/asset/{asset_idx}/thumbnail/update                   |   POST    |    O    |   -    |  O   |
| 5. [에셋 벌크 등록]                      | /api/project/{project_idx}/asset/bulk/create                                    |   POST    |    O    | hooked |  O   |
| 6. [에셋 벌크 목록 조회]                 | /api/project/{project_idx}/asset/bulk/list                                      |    GET    |    O    |   -    |  -   |
| 7. [에셋에 관련된 샷과 태스크 목록 조회] | /api/project/{project_idx}/asset/task/{task_idx}/relation/read[/with/{setting}] |    GET    |    X    |   -    |  -   |
| 8. [에셋 목록 조회]                      | /api/project/{project_idx}/asset_category/{asset_category_idx}/asset/list       |    GET    |    X    |   -    |  -   |
| 9. [프로젝트내 에셋 목록 조회]           | /api/project/{project_idx}/asset/list                                           |    GET    |    X    |   -    |  -   |

## 목차 V2

| 내용                      | slug                           | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :------------------------ | :----------------------------- | :-------: | :-----: | :----: | :--: |
| A1. [에셋 계열 벌크 검증] | /api/assets/bulk/validate      |   POST    |    O    |   -    |  -   |
| A2. [에셋 정보 수정]      | /api/assets/{asset_idx}/update |   POST    |    O    | hooked |  O   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에셋 등록 <a id="project-asset-create"></a>

### `POST /api/project/{project_idx}/asset_category/{asset_category_idx}/asset/create`

### Webhook

- event: asset
- action: create

### permission

- `permission.update_project`

### request

| param              | type  |  data   | required | desc |
| ------------------ | :---: | :-----: | :------: | ---- |
| project_idx        | path  | integer |    O     |      |
| asset_category_idx | path  | integer |    O     |      |
| asset_order        | query |  float  |    X     |      |
| asset_name         | query | string  |    O     |      |
| asset_thumbnail    | query |  file   |    X     |      |
| description        | query | string  |    X     |      |
| status_idx         | query | integer |    O     |      |

### response

```json
{
    "error": {
        "code": 200,
        "message": "An asset has been registered."
    },
    "data": {
        "asset": {
			"project":[
                "idx": 1
            ],
            "asset_category": {
                "idx": "2",
                "name": "env"
            },
            "idx": "31",
            "name": "Asset name",
            "thumbnail": null,
            "order": "29",
            "description": "Asset Description",
            "status": {
                "idx": "1",
                "name": "wip"
            },
            "used": null,
            "reference path": null,
            "hdri path": null,
            "source path": null
        }
    }
}
```

---

## 2. 에셋 정보 수정 <a id="project-asset-update"></a>

### `POST /api/project/asset/{asset_idx}/update`

### Webhook

- event: asset
- action: update

### permission

- `permission.update_asset_and_task`

### request

| param     | type  |  data   | required | desc             |
| --------- | :---: | :-----: | :------: | ---------------- |
| asset_idx | path  | integer |    O     |                  |
| column    | query | string  |    O     |                  |
| old_val   | query | string  |    O     | 공백일 수는 있음 |
| new_val   | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷 정보가 수정됐습니다."
  },
  "data": {
    "asset": {
      "idx": 2,
      "column": "asset_name",
      "value": "godzilla"
    }
  }
}
```

---

## 3. 에셋 벌크 삭제 <a id="project-asset-delete"></a>

### `POST /api/project/asset/bulk/delete`

### permission

- `permission.update_project`

### request

| param       | type |       data       | required | desc |
| ----------- | :--: | :--------------: | :------: | ---- |
| asset_idx[] | path | array of integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 정보가 삭제됐습니다."
  },
  "data": null
}
```

---

## 4. 에셋 썸네일 업데이트 <a id="project-asset-thumbnail"></a>

### `POST /api/project/{project_idx}/asset/{asset_idx}/thumbnail/update`

### permission

- `permission.update_asset_and_task`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| asset_idx   | path  | integer |    O     |      |
| attached    | query |  file   |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 썸네일이 등록됐습니다."
  },
  "data": {
    "asset": {
      "idx": 4,
      "thumbnail": "http://localhost:81/2019/02/21/05ed16a5d80f3f4b.png"
    }
  }
}
```

---

## 5. 에셋 벌크 등록 <a id="project-asset-bulk-create"></a>

### `POST /api/project/{project_idx}/asset/bulk/create`

### Webhook

- event: asset
- action: bulk create

### permission

- `permission.update_project`

### request

- handsontable의 데이터를 보냅니다.

| param                 | type  |      data       | required | desc                                              |
| --------------------- | :---: | :-------------: | :------: | ------------------------------------------------- |
| project_idx           | path  |     integer     |    O     |                                                   |
| asset_category_name[] | query | array of string |    O     | 신규인지 기존에 존재하는 시퀀스인지는 서버가 판단 |
| asset_name[]          | query | array of string |    O     |                                                   |
| description[]         | query | array of string |    O     |                                                   |
| attached[]            | query |  array of file  |    X     |                                                   |
| reference_path[]      | query | array of string |    X     |                                                   |
| hdri_path[]           | query | array of string |    X     |                                                   |
| source_path[]         | query | array of string |    X     |                                                   |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋이 등록됐습니다."
  },
  "data": {
    "assets": [
      {
        "idx": "45",
        "name": "s0020_c0110",
        "order": 10,
        "description": "the squirrelis looking at bunny",
        "asset_category": {
          "idx": "22",
          "name": "s0020",
          "description": null
        }
      },
      {
        "idx": "46",
        "name": "s0020_c0120",
        "order": 11,
        "description": "while bunny is smelling the flower, he moves",
        "asset_category": {
          "idx": "22",
          "name": "s0020",
          "description": null
        }
      }
    ],
    "duplicated": ["s0020_c0080", "s0020_c0090"]
  }
}
```

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋이 등록됐습니다."
  },
  "data": {
    "assets": [
      {
        "idx": "7",
        "name": "big ant"
      },
      {
        "idx": "8",
        "name": "small ant"
      }
    ],
    "duplicated": ["old ant", "young ant"]
  }
}
```

---

## 6. 에셋 벌크 목록 조회 <a id="project-asset-bulk-list"></a>

- 사용 예: http://localhost/project/1/asset/task/add

### `GET /api/project/{project_idx}/asset/bulk/list`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "assets": [
      {
        "idx": "1",
        "name": "ch_bunny",
        "thumbnail": "http://localhost:81/2019/04/08/78b9d804eb4a7f53.jpg",
        "asset_category": {
          "name": "char"
        },
        "description": "Hero character",
        "tasks": {
          "Modeling": {
            "idx": "2",
            "duration_init": "10",
            "user": {
              "idx": "2",
              "name": "Artist"
            }
          },
          "Texture": {
            "idx": "1",
            "duration_init": "5",
            "user": {
              "idx": "2",
              "name": "Artist"
            }
          },
          "Concept": {
            "idx": "6",
            "duration_init": "15",
            "user": {
              "idx": "1",
              "name": "C2Monster"
            }
          }
        }
      },
      {
        "idx": "2",
        "name": "ch_bird",
        "thumbnail": "http://localhost:81/2019/04/08/f56811cc547e2caf.jpg",
        "asset_category": {
          "name": "char"
        },
        "description": "A bird in the middle",
        "tasks": {
          "Modeling": {
            "idx": "7",
            "duration_init": "3",
            "user": {
              "idx": "2",
              "name": "Artist"
            }
          },
          "Texture": {
            "idx": null,
            "duration_init": null,
            "user": {
              "idx": null,
              "name": null
            }
          },
          "Concept": {
            "idx": null,
            "duration_init": null,
            "user": {
              "idx": null,
              "name": null
            }
          }
        }
      },
      {
        "idx": "3",
        "name": "ch_squirrel",
        "thumbnail": "http://localhost:81/2019/04/08/e1ec4ac7862fc307.jpg",
        "asset_category": {
          "name": "char"
        },
        "description": "Character to fight Bunny",
        "tasks": {
          "Modeling": {
            "idx": "3",
            "duration_init": "5",
            "user": {
              "idx": "2",
              "name": "Artist"
            }
          },
          "Texture": {
            "idx": "4",
            "duration_init": "3",
            "user": {
              "idx": "1",
              "name": "C2Monster"
            }
          },
          "Concept": {
            "idx": "5",
            "duration_init": "15",
            "user": {
              "idx": "1",
              "name": "C2Monster"
            }
          }
        }
      }
    ]
  }
}
```

---

## 7. 에셋에 관련된 샷과 태스크 목록 조회 <a id="asset-shot-list"></a>

### `GET /api/project/{project_idx}/asset/task/{task_idx}/relation/read[/with/{setting}]`

### permission

- `permission.update_project`

### request

| param       | type  |  data   | required | desc           |
| ----------- | :---: | :-----: | :------: | -------------- |
| project_idx | path  | integer |    O     |                |
| asset_idx   | path  | integer |    O     |                |
| setting     | query | string  |    X     | 값은 'setting' |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "assets": [
      {
        "shot_idx": "1",
        "name": "s0010_c0010",
        "episode_name": "e01",
        "sequence_name": "s0010",
        "start_date": "2019-09-11",
        "end_date": "2019-09-15",
        "tasks": {
          "Modeling": {
            "task_idx": "7",
            "status_name": "wip",
            "status_color": "#dbd8db",
            "status_idx": "1"
          },
          "Texture": {
            "task_idx": null,
            "status_name": null,
            "status_color": null,
            "status_idx": null
          },
          "Concept": {
            "task_idx": null,
            "status_name": null,
            "status_color": null,
            "status_idx": null
          }
        }
      },
      {
        "shot_idx": "2",
        "name": "s0010_c0020",
        "episode_name": "e01",
        "sequence_name": "s0010",
        "start_date": "2019-09-12",
        "end_date": "2019-09-17",
        "tasks": {
          "Modeling": {
            "task_idx": "2",
            "status_name": "wip",
            "status_color": "#dbd8db",
            "status_idx": "1"
          },
          "Texture": {
            "task_idx": "1",
            "status_name": "wip",
            "status_color": "#dbd8db",
            "status_idx": "1"
          },
          "Concept": {
            "task_idx": "6",
            "status_name": "confirm",
            "status_color": "#03a9f4",
            "status_idx": "2"
          }
        }
      }
    ],
    "setting_column": [
      {
        "data": "episode_name",
        "type": "text",
        "width": 100,
        "editor": false
      },
      {
        "data": "sequence_name",
        "type": "text",
        "width": 100,
        "editor": false
      },
      {
        "data": "name",
        "type": "text",
        "width": 100,
        "editor": false
      },
      {
        "data": "start_date",
        "type": "date",
        "width": 100,
        "editor": false
      },
      {
        "data": "end_date",
        "type": "date",
        "width": 100,
        "editor": false
      },
      {
        "data": "tasks.Modeling.status_name",
        "type": "text",
        "width": 80,
        "editor": false
      },
      {
        "data": "tasks.Texture.status_name",
        "type": "text",
        "width": 80,
        "editor": false
      },
      {
        "data": "tasks.Concept.status_name",
        "type": "text",
        "width": 80,
        "editor": false
      }
    ],
    "headers": [
      "Episode Name",
      "Sequence Name",
      "Shot Name",
      "Modeling",
      "Texture",
      "Concept"
    ]
  }
}
```

- `setting_column`과 `header`는 `/with/setting`으로 접근할 때만 표시됨

---

## 8. 에셋 목록 조회 <a id="asset-list"></a>

### `GET /api/project/{project_idx}/asset_category/{asset_category_idx}/asset/list`

### permission

- `permission.read_project`

### request

| param              | type |  data   | required | desc |
| ------------------ | :--: | :-----: | :------: | ---- |
| project_idx        | path | integer |    O     |      |
| asset_category_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "assets": [
      {
        "idx": "2",
        "name": "ch_bird",
        "order": "2"
      },
      {
        "idx": "1",
        "name": "ch_bunny",
        "order": "1"
      },
      {
        "idx": "3",
        "name": "ch_squirrel",
        "order": "3"
      }
    ]
  }
}
```

- `setting_column`과 `header`는 `/with/setting`으로 접근할 때만 표시됨

---

## 9.프로젝트내 내 에셋 목록 조회 <a id="category-asset-list"></a>

### `GET /api/project/{project_idx}/asset/list`

### permission

- `permission.read_project`

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
    "asset": [
      {
        "idx": "1",
        "name": "s0010_c0010",
        "description": "Opening_sequence",
        "category": {
          "idx": "1",
          "name": "s0010",
          "description": "Opening Sequence"
        },
        "status": {
          "idx": "1",
          "name": "wip"
        }
      },
      {
        "idx": "1",
        "name": "s0010_c0010",
        "description": "Opening_sequence",
        "category": {
          "idx": "1",
          "name": "s0010",
          "description": "Opening Sequence"
        },
        "status": {
          "idx": "1",
          "name": "wip"
        }
      }
    ],
    "project": {
      "idx": "1",
      "name": "Demo_Bigbuck_Bunny",
      "description": "Demo_Bigbuck_Bunny",
      "start_date": "2018-12-11",
      "end_date": "2019-04-12"
    }
  }
}
```

---

## A1. 에셋 계열 벌크 검증 <a id="assets-bulk-validate"></a>

### `GET /api/assets/bulk/validate`

### permission

- `permission.read_project`

### request

| param                 | type  |      data       | required | desc |
| --------------------- | :---: | :-------------: | :------: | ---- |
| project_name[]        | query | array of string |    O     |      |
| asset_category_name[] | query | array of string |    O     |      |
| asset_name[]          | query | array of string |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "validations": [
      {
        "project": {
          "idx": "1",
          "name": "Big Bunny"
        },
        "episode": {
          "idx": "3",
          "name": "Ep03"
        },
        "asset_category": {
          "idx": "1",
          "name": "cars"
        },
        "asset": {
          "idx": "1",
          "name": "blue_car"
        }
      },
      {
        "project": {
          "idx": "2",
          "name": "Turbo"
        },
        "asset_category": {
          "idx": "2",
          "name": "trees"
        },
        "asset": {
          "idx": "11",
          "name": "small_beech"
        }
      }
    ]
  }
}
```

---

## A2. 에셋 정보 수정 <a id="assets-update"></a>

### `POST /api/assets/{asset_idx}/update`

### Webhook

- event: asset
- action: update

### permission

- `permission.update_asset_and_task`

### request

| param                | type  |  data   | required | desc   |
| -------------------- | :---: | :-----: | :------: | ------ |
| asset_idx            | path  | integer |    O     |        |
| {property_name}[new] | query |   any   |    O     | 컬럼명 |
| {property_name}[old] | query |   any   |    X     | 컬럼명 |

- {property_name}을 칼럼별로 이용하여 여러 컬럼을 동시에 수정할 수 있음
- 예) `POST /api/assets/1/update?name[new]=red_car&name[old]=red_ca&description[new]=red&description[old]=car`

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 정보가 수정됐습니다."
  },
  "data": {
    "shot": {
      "idx": 14,
      "columns": [
        {
          "name": "description",
          "value": "wow"
        },
        {
          "name": "source_path",
          "value": "abc/def/ggg"
        }
      ]
    }
  }
}
```

---

## 끝

[에셋 등록]: #project-asset-create
[에셋 정보 수정]: #project-asset-update
[에셋 삭제]: #project-asset-delete
[에셋 썸네일 업데이트]: #project-asset-thumbnail
[에셋 벌크 등록]: #project-asset-bulk-create
[에셋 벌크 목록 조회]: #project-asset-bulk-list
[에셋에 관련된 샷과 태스크 목록 조회]: #asset-shot-list
[에셋 목록 조회]: #asset-list
[프로젝트내 내 에셋 목록 조회]: #category-asset-list
[에셋 계열 벌크 검증]: #assets-bulk-validate
[에셋 정보 수정]: #assets-update
