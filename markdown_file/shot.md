# WH2API::Shot

## 목차

| 내용                          | slug                                                                                 | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :---------------------------- | :----------------------------------------------------------------------------------- | :-------: | :-----: | :----: | :--: |
| 1. [샷 등록]                  | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/create |   POST    |    O    | hooked |  O   |
| 2. [샷 정보 수정]             | /api/project/{project_idx}/shot/{shot_idx}/update                                    |   POST    |    O    | hooked |  O   |
| 3. [샷 벌크 삭제]             | /api/project/{project_idx}/shot/bulk/delete                                          |   POST    |    O    |   -    |  O   |
| 4. [샷 정보 조회]             | /api/project/{project_idx}/shot/{shot_idx}/read                                      |    GET    |    X    |   -    |  -   |
| 5. [샷 썸네일 업데이트]       | /api/project/{project_idx}/shot/{shot_idx}/thumbnail/update                          |   POST    |    O    |   -    |  O   |
| 6. [샷 목록 조회]             | /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/list   |    GET    |    O    |   -    |  -   |
| 7. [샷 벌크 등록]             | /api/project/{project_idx}/shot/bulk/create                                          |   POST    |    O    | hooked |  O   |
| 8. [샷 벌크 목록 조회]        | /api/project/{project_idx}/episode/{episode_idx}/shot/bulk/list                      |    GET    |    O    |   -    |  -   |
| 9. [에피소드 내 샷 목록 조회] | /api/project/{project_idx}/episode/{episode_idx}/shot/list                           |    GET    |    X    |   -    |  -   |

## 목차 V2

| 내용                    | slug                     | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :---------------------- | :----------------------- | :-------: | :-----: | :----: | :--: |
| A1. [샷 계열 벌크 검증] | /api/shots/bulk/validate |   POST    |    O    |   -    |  -   |
| A2. [샷 정보 수정]      | /api/shots/{shot_idx}/update        |   POST    |    O    | hooked |  O   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 샷 등록 <a id="project-shot-create"></a>

### `POST /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/create`

### Webhook

- event: shot
- action: create

### permission

- `permission.update_project`

### request

| param        | type  |  data   | required | desc |
| ------------ | :---: | :-----: | :------: | ---- |
| project_idx  | path  | integer |    O     |      |
| episode_idx  | path  | integer |    O     |      |
| sequence_idx | path  | integer |    O     |      |
| shot_order   | query |  float  |    X     |      |
| shot_name    | query | string  |    O     |      |
| attached     | query |  file   |    X     |      |
| description  | query | string  |    X     |      |
| status_idx   | query | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷이 등록됐습니다."
  },
  "data": {
    "shot": {
      "idx": "32",
      "name": "s0010_c0160",
      "order": "32",
      "thumbnail": null,
      "status": {
        "idx": "1",
        "name": "wip"
      },
      "project": {
        "idx": "1"
      },
      "episode": {
        "idx": "1",
        "name": "Ep01"
      },
      "sequence": {
        "idx": "1",
        "name": "s0010"
      },
      "description": null,
      "location": null,
      "note": null,
      "length": null,
      "handle_in": null,
      "handle_out": null,
      "frame_in": null,
      "frame_out": null,
      "timecode_in": null,
      "timecode_out": null,
      "importance": "0",
      "difficulty": null,
      "original_path": null,
      "camera_clip": null,
      "camera_name": null,
      "lens_type": null,
      "focal_length": null,
      "grip": null,
      "camera_filter": null,
      "iso": null,
      "shutter_speed": null,
      "f_stop": null,
      "stereo_type": null,
      "stereo_iod": null,
      "stereo_converged_point": null,
      "stereo_rig": null,
      "camera_note": null
    }
  }
}
```

---

## 2. 샷 정보 수정 <a id="project-shot-update"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/update`

### Webhook

- event: shot
- action: update

### permission

- `permission.update_shot_and_task`

### request

| param       | type  |  data   | required | desc             |
| ----------- | :---: | :-----: | :------: | ---------------- |
| project_idx | path  | integer |    O     |                  |
| shot_idx    | path  | integer |    O     |                  |
| column      | query | string  |    O     |                  |
| old_val     | query | string  |    O     | 공백일 수는 있음 |
| new_val     | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷 정보가 수정됐습니다."
  },
  "data": {
    "shot": {
      "idx": 14,
      "column": "camera_clip",
      "value": "1"
    }
  }
}
```

- episode name, sequence name, shot name, 모든 태스크들의 summary는 수정이 불가능하고 그외의 모든 컬럼은 수정이 가능합니다.
- 숫자만 들어갈 수 있는 컬럼은 Shots 헤더의 Length, Handle In, Handle Out, Frame In, Frame Out 컬럼입니다.

---

## 3. 샷 벌크 삭제 <a id="project-shot-delete"></a>

### `POST /api/project/{project_idx}/shot/bulk/delete`

### permission

- `permission.update_project`

### request

| param       | type |       data       | required | desc |
| ----------- | :--: | :--------------: | :------: | ---- |
| project_idx | path |     integer      |    O     |      |
| shot_idx[]  | path | array of integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷이 삭제됐습니다."
  },
  "data": null
}
```

---

## 4. 샷 정보 조회 <a id="project-shot"></a>

### `GET /api/project/{project_idx}/shot/{shot_idx}/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| shot_idx    | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "shot": {
      "idx": "1",
      "name": "s0010_c0010",
      "order": "1",
      "thumbnail": "http://localhost:81/2019/04/08/24591d492b5b4b16.jpg",
      "project": {
        "idx": "1"
      },
      "episode": {
        "idx": "1",
        "name": "Ep01"
      },
      "sequence": {
        "idx": "1",
        "name": "s0010"
      },
      "status": {
        "idx": "1",
        "name": "wip"
      },
      "description": "Opening_sequence",
      "location": "Jungle_A",
      "note": "",
      "length": "285",
      "handle_in": "0",
      "handle_out": "0",
      "frame_in": "0",
      "frame_out": "284",
      "timecode_in": "00:00:00:00",
      "timecode_out": "",
      "importance": "0",
      "difficulty": "",
      "original_path": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0010_anim_v001.mp4",
      "camera_clip": null,
      "camera_name": null,
      "lens_type": null,
      "focal_length": null,
      "grip": null,
      "camera_filter": null,
      "iso": null,
      "shutter_speed": null,
      "f_stop": null,
      "stereo_type": null,
      "stereo_iod": null,
      "stereo_converged_point": null,
      "stereo_rig": null,
      "camera_note": null
    }
  }
}
```

---

## 5. 샷 썸네일 업데이트 <a id="project-shot-thumbnail"></a>

### `POST /api/project/{project_idx}/shot/{shot_idx}/thumbnail/update`

### permission

- `permission.update_shot_and_task`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| shot_idx    | path  | integer |    O     |      |
| attached    | query |  file   |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷 썸네일이 등록됐습니다."
  },
  "data": {
    "shot": {
      "idx": 4,
      "thumbnail": "http://localhost:81/2019/02/21/05ed16a5d80f3f4b.png"
    }
  }
}
```

---

## 6. 샷 목록 조회 <a id="project-shot-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/sequence/{sequence_idx}/shot/list`

### permission

- `permission.read_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "shots": [
      {
        "idx": "1",
        "name": "s0010_c0010",
        "shot_order": "1"
      },
      {
        "idx": "2",
        "name": "s0010_c0020",
        "shot_order": "2"
      },
      {
        "idx": "3",
        "name": "s0010_c0030",
        "shot_order": "3"
      }
    ]
  }
}
```

---

## 7. 샷 벌크 등록 <a id="#pproject-shot-bulk-create"></a>

### `POST /api/project/{project_idx}/shot/bulk/create`

### Webhook

- event: shot
- action: bulk create

### permission

- `permission.update_project`

### request

| param                | type  |       data       | required | desc                                              |
| -------------------- | :---: | :--------------: | :------: | ------------------------------------------------- |
| project_idx          | path  |     integer      |    O     |                                                   |
| episode_idx          | query |     integer      |    O     |                                                   |
| sequence_name[]      | query | array of string  |    O     | 신규인지 기존에 존재하는 시퀀스인지는 서버가 판단 |
| shot_name[]          | query | array of string  |    O     |                                                   |
| description[]        | query | array of string  |    O     |                                                   |
| direction_note[]     | query | array of string  |    O     |                                                   |
| attached[]           | query |  array of file   |    X     |                                                   |
| length[]             | query | array of integer |    X     |                                                   |
| timecode_in[]        | query | array of string  |    X     |                                                   |
| timecode_out[]       | query | array of string  |    X     |                                                   |
| original_edit_path[] | query | array of string  |    X     |                                                   |
| frame_in[]           | query | array of integer |    X     |                                                   |
| frame_out[]          | query | array of integer |    X     |                                                   |

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷이 등록됐습니다."
  },
  "data": {
    "shots": [
      {
        "idx": "45",
        "name": "s0020_c0110",
        "description": "the squirrelis looking at bunny",
        "sequence": {
          "idx": "22",
          "name": "s0020",
          "description": null,
          "sequence_order": "7"
        }
      },
      {
        "idx": "46",
        "name": "s0020_c0120",
        "description": "while bunny is smelling the flower, he moves",
        "sequence": {
          "idx": "22",
          "name": "s0020",
          "description": null,
          "sequence_order": "8"
        }
      }
    ],
    "duplicated": ["s0020_c0080", "s0020_c0090"]
  }
}
```

---

## 8. 샷 벌크 목록 조회 <a id="#project-shot-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/shot/bulk/list`

### permission

- `permission.update_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "shots": [
      {
        "idx": "1",
        "name": "s0010_c0010",
        "thumbnail": "http://localhost:81/2019/04/08/24591d492b5b4b16.jpg",
        "description": "Opening_sequence",
        "sequence": {
          "name": "s0010"
        },
        "tasks": {
          "Animation": {
            "idx": "4",
            "duration_init": "3",
            "user": {
              "idx": "2",
              "name": "Artist"
            }
          },
          "Comp": {
            "idx": "1",
            "duration_init": "3",
            "user": {
              "idx": "1",
              "name": "C2Monster"
            }
          }
        }
      },
      {
        "idx": "2",
        "name": "s0010_c0020",
        "thumbnail": "http://localhost:81/2019/04/08/d45d311d6b86ae96.jpg",
        "description": "river flows",
        "sequence": {
          "name": "s0010"
        },
        "tasks": {
          "Animation": {
            "idx": "4",
            "duration_init": "3",
            "user": {
              "idx": "2",
              "name": "Artist"
            }
          },
          "Comp": {
            "idx": "1",
            "duration_init": "3",
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

## 9. 에피소드 내 샷 목록 조회 <a id="episode-shot-list"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/shot/list`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "shots": [
      {
        "idx": "1",
        "name": "s0010_c0010",
        "description": "Opening_sequence",
        "sequence": {
          "idx": "1",
          "name": "s0010",
          "description": "Opening Sequence",
          "sequence_order": "1"
        },
        "status": {
          "idx": "1",
          "name": "wip"
        }
      },
      {
        "idx": "2",
        "name": "s0010_c0020",
        "description": "river flows",
        "sequence": {
          "idx": "1",
          "name": "s0010",
          "description": "Opening Sequence",
          "sequence_order": "1"
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
    },
    "episode": {
      "idx": "1",
      "name": "Ep01",
      "description": "Demo_Bigbuck_Bunny_First"
    }
  }
}
```

---

## A1. 샷 계열 벌크 검증 <a id="shots-bulk-validate"></a>

### `GET /api/shots/bulk/validate`

### permission

- `permission.read_project`

### request

| param           | type  |      data       | required | desc |
| --------------- | :---: | :-------------: | :------: | ---- |
| project_name[]  | query | array of string |    O     |      |
| episode_name[]  | query | array of string |    O     |      |
| sequence_name[] | query | array of string |    O     |      |
| shot_name[]     | query | array of string |    O     |      |

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
        "sequence": {
          "idx": "1",
          "name": "s0010"
        },
        "shot": {
          "idx": "1",
          "name": "s0010_c0010"
        }
      },
      {
        "project": {
          "idx": "2",
          "name": "Turbo"
        },
        "episode": {
          "idx": "2",
          "name": "Ep02"
        },
        "sequence": {
          "idx": "3",
          "name": "s0030"
        },
        "shot": {
          "idx": "11",
          "name": "s0030_c0030"
        }
      }
    ]
  }
}
```

---

## A2. 샷 정보 수정 <a id="shots-update"></a>

### `POST /api/shots/{shot_idx}/update`

### Webhook

- event: shot
- action: update

### permission

- `permission.update_shot_and_task`

### request

| param                | type  |  data   | required | desc   |
| -------------------- | :---: | :-----: | :------: | ------ |
| shot_idx             | path  | integer |    O     |        |
| {property_name}[new] | query |   any   |    O     | 컬럼명 |
| {property_name}[old] | query |   any   |    X     | 컬럼명 |

- {property_name}을 칼럼별로 이용하여 여러 컬럼을 동시에 수정할 수 있음
- 예) `POST /api/shots/1/update?name[new]=s0010_c0010&name[old]=s0010_&description[new]=scene&description[old]=abc`

### response

```json
{
  "error": {
    "code": 200,
    "message": "샷 정보가 수정됐습니다."
  },
  "data": {
    "shot": {
      "idx": 14,
      "columns": [
        {
          "name": "camera_clip",
          "value": "1"
        },
        {
          "name": "frame_in",
          "value": "2"
        }
      ]
    }
  }
}
```

- 숫자만 들어갈 수 있는 컬럼은 Shots 헤더의 Length, Handle In, Handle Out, Frame In, Frame Out 컬럼입니다.

---

## 끝

[샷 등록]: #project-shot-create
[샷 정보 수정]: #project-shot-update
[샷 삭제]: #project-shot-delete
[샷 정보 조회]: #project-shot
[샷 썸네일 업데이트]: #project-shot-thumbnail
[샷 목록 조회]: #project-shot-list
[샷 벌크 등록]: #project-shot-bulk-create
[샷 벌크 목록 조회]: #project-shot-list
[에피소드 내 샷 목록 조회]: #episode-shot-list
[샷 계열 벌크 검증]: #shots-bulk-validate
[샷 정보 수정]: #shots-update
