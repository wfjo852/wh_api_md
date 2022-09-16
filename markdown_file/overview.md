# WH2API::ShotTaskOverview

## 목차

| 내용                                | slug                                                                                                   | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :---------------------------------- | :----------------------------------------------------------------------------------------------------- | :-------: | :-----: | :--: | :--: |
| 1. [샷 오버뷰 조회]                 | /api/project/{project_idx}/episode/{episode_idx}/shot/task/overview/read                               |    GET    |    O    |  -   |  -   |
| 2. [샷 오버뷰 컬럼 너비 수정]       | /api/project/{project_idx}/shot/task/overview/column/width/update                                      |  X POST   |    X    |  -   |  -   |
| 3. [에셋 오버뷰 조회]               | /api/project/{project_idx}/asset/task/overview/read                                                    |    GET    |    O    |  -   |  -   |
|                                     | /api/project/{project_idx}/asset_category/{asset_category_idx}/asset/task/overview/read                |    GET    |    O    |  -   |  -   |
| 4. [릴레이션 에피소드 리스트 조회]  | /api/project/{project_idx}/relation/episode/list                                                       |    GET    |    O    |  -   |  -   |
|                                     | /api/project/{project_idx}/relation/episode/{episode_idx}/list                                         |    GET    |    O    |  -   |  -   |
| 5. [릴레이션 시퀀스 리스트 조회]    | /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/list                                |    GET    |    O    |  -   |  -   |
|                                     | /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/{sequence_idx}/list                 |    GET    |    O    |  -   |  -   |
| 6. [릴레이션 샷 리스트 조회]        | /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/{sequence_idx}/shot/list            |    GET    |    O    |  -   |  -   |
|                                     | /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/{sequence_idx}/shot/{shot_idx}/list |    GET    |    O    |  -   |  -   |
| 7. [릴레이션 카테고리 별 에셋 조회] | /api/project/{project_idx}/{which}/{which_idx}/relation/asset/list                                     |    GET    |    O    |  -   |  -   |
| 8. [릴레이션 카테고리 별 에셋 할당] | /api/project/{project_idx}/which/{which_idx}/asset/relation/bulk/add                                   |   POST    |    O    |  -   |  -   |
| 9. [에셋 오버뷰 컬럼 너비 수정]     | /api/project/{project_idx}/asset/task/overview/column/width/update                                     |   POST    |    X    |  -   |  -   |

- O\* - 3, 4, 5번 동시 적용

## 목차 V2

| 내용                                       | slug                                                      | 서버 구현 | 웹 적용 | 웹훅 | 로그 | 크론탭 |
| :----------------------------------------- | :-------------------------------------------------------- | :-------: | :-----: | :--: | :--: | ------ |
| A1. [오버뷰 템플릿 목록 조회]              | /api/overview_templates/list                              |    GET    |    O    |  -   |  -   | -      |
| A2. [오버뷰 템플릿 조회]                   | /api/overview_templates/{overview_template_idx}/read      |    GET    |    X    |  -   |  -   | -      |
| A3. [오버뷰 템플릿 수정]                   | /api/overview_templates/{overview_template_idx}/update    |   POST    |    O    |  -   |  -   | -      |
| A4. [오버뷰 템플릿 복사]                   | /api/overview_templates/{overview_template_idx}/duplicate |   POST    |    O    |  -   |  -   | -      |
| A5. [오버뷰 템플릿 삭제]                   | /api/overview_templates/{overview_template_idx}/delete    |   POST    |    O    |  -   |  -   | -      |
| A6. [오버뷰 템플릿 초기화]                 | /api/overview_templates/{overview_template_idx}/reset     |   POST    |    O    |  -   |  -   | -      |
| A7. [오버뷰 기본 템플릿 조회]              | /api/overview_templates/default/read                      |    GET    |    O    |  -   |  -   | -      |
| A8. [오버뷰 기본 템플릿 수정]              | /api/overview_templates/default/update                    |   POST    |    O    |  -   |  -   | -      |
| A9. [오버뷰 컬럼 너비 수정]                | /api/tables/width/update                                  |  X POST   |    X    |  -   |  -   | -      |
| A10. [오버뷰 기본 템플릿 필터 초기화]      | /api/overview_templates/default/filter/reset              |   POST    |    X    |  -   |  -   | -      |
| A11. [오버뷰 기본 템플릿 접힘 컬럼 초기화] | /api/overview_templates/default/collapsed_column/reset    |   POST    |    X    |  -   |  -   | -      |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 샷 오버뷰 조회 <a id="read"></a>

### `GET /api/project/{project_idx}/episode/{episode_idx}/shot/task/overview/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc      |
| ----------- | :---: | :-----: | :------: | --------- |
| project_idx | path  | integer |    O     |           |
| episode_idx | path  | integer |    O     |           |
| page        | query | integer |    X     | 생략 시 1 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "project": {
      "name": "Demo_Bigbuck_Bunny"
    },
    "episode": {
      "name": null
    },
    "shots": [
      {
        "idx": "365",
        "name": "1111",
        "order": "1",
        "thumbnail": "",
        "episode": {
          "idx": "6",
          "name": "EP02"
        },
        "sequence": {
          "idx": "30",
          "name": "123"
        },
        "status": {
          "name": "wip"
        },
        "description": "",
        "last_version_thumbnail": null,
        "location": null,
        "note": null,
        "length": null,
        "handle_in": null,
        "handle_out": null,
        "importance": "0",
        "difficulty": null,
        "c1": null,
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
        "stereo_dof": null,
        "camera_note": null,
        "tasks": {
          "comp": {
            "artist": null,
            "pub": null,
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "description": "",
            "is_on": "1",
            "idx": "236",
            "tasktype": {
              "idx": "3",
              "name": "comp",
              "color": "#FFD906"
            },
            "user": {
              "id": null
            },
            "status": {
              "name": "wip"
            }
          },
          "Task03": {
            "idx": "",
            "tasktype": {
              "idx": "",
              "name": "",
              "color": ""
            },
            "user": {
              "idx": ""
            },
            "artist": "",
            "pub": "",
            "start_date": "",
            "end_date": "",
            "duration": "",
            "status": {
              "name": ""
            },
            "description": ""
          },
          "task02": {
            "idx": "",
            "tasktype": {
              "idx": "",
              "name": "",
              "color": ""
            },
            "user": {
              "idx": ""
            },
            "artist": "",
            "pub": "",
            "start_date": "",
            "end_date": "",
            "duration": "",
            "status": {
              "name": ""
            },
            "description": ""
          },
          "Task01": {
            "idx": "",
            "tasktype": {
              "idx": "",
              "name": "",
              "color": ""
            },
            "user": {
              "idx": ""
            },
            "artist": "",
            "pub": "",
            "start_date": "",
            "end_date": "",
            "duration": "",
            "status": {
              "name": ""
            },
            "description": ""
          }
        }
      }
    ],
    "setting_column": [
      {
        "data": "idx",
        "type": "numeric",
        "width": 50,
        "editor": false
      },
      {
        "data": "order",
        "type": "text",
        "width": 50
      },
      {
        "data": "episode.name",
        "type": "text",
        "readOnly": true,
        "width": 120,
        "editor": false
      },
      {
        "data": "sequence.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["s0010", "123", "s0020", "s0030", "s", "111", "1", "a"],
        "width": 120
      },
      {
        "data": "name",
        "type": "text",
        "width": 180
      },
      {
        "data": "thumbnail",
        "renderer": "renderShotThumbnail",
        "width": 84,
        "editor": false
      },
      {
        "data": "description",
        "type": "text",
        "width": 190
      },
      {
        "data": "status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["wip", "A_tests", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "location",
        "type": "text",
        "width": 120
      },
      {
        "data": "note",
        "type": "text",
        "width": 160
      },
      {
        "data": "length",
        "renderer": "renderLength",
        "type": "text",
        "width": 85
      },
      {
        "data": "handle_in",
        "type": "text",
        "width": 95
      },
      {
        "data": "handle_out",
        "type": "text",
        "width": 95
      },
      {
        "data": "importance",
        "type": "text",
        "width": 110
      },
      {
        "data": "difficulty",
        "type": "text",
        "width": 80
      },
      {
        "data": "c1",
        "type": "text",
        "width": 120
      },
      {
        "data": "camera_clip",
        "type": "text",
        "width": 150
      },
      {
        "data": "camera_name",
        "type": "text",
        "width": 125
      },
      {
        "data": "lens_type",
        "type": "text",
        "width": 125
      },
      {
        "data": "focal_length",
        "type": "text",
        "width": 130
      },
      {
        "data": "grip",
        "type": "text"
      },
      {
        "data": "camera_filter",
        "type": "text"
      },
      {
        "data": "iso",
        "type": "text"
      },
      {
        "data": "shutter_speed",
        "type": "text",
        "width": 150
      },
      {
        "data": "f_stop",
        "type": "text",
        "width": 150
      },
      {
        "data": "stereo_type",
        "type": "text",
        "width": 120
      },
      {
        "data": "stereo_iod",
        "type": "text",
        "width": 100
      },
      {
        "data": "stereo_converged_point",
        "type": "text",
        "width": 180
      },
      {
        "data": "stereo_rig",
        "type": "text",
        "width": 100
      },
      {
        "data": "stereo_dof",
        "type": "text",
        "width": 100
      },
      {
        "data": "camera_note",
        "type": "text",
        "width": 100
      },
      {
        "data": "tasks.comp.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.comp.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["wip", "A_tests", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.comp.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.comp.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.comp.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.comp.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.comp.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.comp.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      },
      {
        "data": "tasks.Task03.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.Task03.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["wip", "A_tests", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.Task03.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.Task03.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.Task03.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.Task03.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Task03.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Task03.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      },
      {
        "data": "tasks.task02.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.task02.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["wip", "A_tests", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.task02.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.task02.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.task02.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.task02.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.task02.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.task02.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      },
      {
        "data": "tasks.Task01.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.Task01.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["wip", "A_tests", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.Task01.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.Task01.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.Task01.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.Task01.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Task01.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Task01.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      },
      {
        "type": "numeric",
        "width": 10,
        "editor": false
      }
    ],
    "collapsible_columns": [
      {
        "row": -2,
        "col": 4,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 15,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 16,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 31,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 39,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 47,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 55,
        "collapsible": true
      }
    ],
    "nested_headers": [
      [
        "idx",
        "Order",
        "Episode",
        "Sequence",
        {
          "label": "Shots",
          "colspan": 11
        },
        {
          "label": "Customs",
          "colspan": 1
        },
        {
          "label": "Camera",
          "colspan": 15
        },
        {
          "label": "comp",
          "colspan": 8
        },
        {
          "label": "Task03",
          "colspan": 8
        },
        {
          "label": "task02",
          "colspan": 8
        },
        {
          "label": "Task01",
          "colspan": 8
        },
        "end"
      ],
      [
        "-",
        "-",
        "Name",
        "Name",
        "Shot Name",
        "Thumbnail",
        "Description",
        "Status",
        "Location",
        "Direction Note",
        "Length",
        "Handle In",
        "Handle Out",
        "Importance",
        "Level",
        "test",
        "Camera Clip",
        "Camera Name",
        "Lens Type",
        "Focal Length",
        "Grip",
        "Filter",
        "ISO",
        "Shutter Speed",
        "F-Stop",
        "Stereo Type",
        "Stereo IOD",
        "Stereo Converged Point",
        "Stereo Rig",
        "Stereo DOF",
        "Note",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "-"
      ]
    ],
    "statuses": [
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
      },
      {
        "idx": "14",
        "name": "A_tests",
        "color": "#4caf50"
      }
    ],
    "filters": [
      {
        "column": "3",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [["s0010"]]
          }
        ],
        "prop": "sequence.name"
      }
    ]
  }
}
```

- 모든 태스크들에 있는 duration 값은 샷의 '태스크 할당'에서 입력하는 값(실수)을 가져옴
  - http://localhost/project/abc/shot/task/add (샷의 태스크 할당)
  - 태스크 할당에서 입력한 값에 소수점이 있을 경우 올림해서 정수로 표기함
- 태스크 헤더에는 태스크의 color가 표기되어야 함

---

## 2. 샷 오버뷰 컬럼 너비 수정 <a id="column-width-update"></a>

### `POST /api/project/{project_idx}/shot/task/overview/column/width/update`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| column      | query | string  |    O     |      |
| width       | query | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## 3. 에셋 오버뷰 조회 <a id="project-asset-task-overview-read"></a>

### `GET /api/project/{project_idx}/asset/task/overview/read`

### `GET /api/project/{project_idx}/asset_category/{asset_category_idx}/asset/task/overview/read`

### permission

- `permission.read_asset_task_overview`

### request

| param              | type  |  data   | required | desc      |
| ------------------ | :---: | :-----: | :------: | --------- |
| project_idx        | path  | integer |    O     |           |
| asset_category_idx | path  | integer |    X     |           |
| page               | query | integer |    X     | 생략 시 1 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "project": {
      "name": "Demo_Bigbuck_Bunny"
    },
    "asset_category": {
      "name": null
    },
    "assets": [
      {
        "idx": "14",
        "name": "123",
        "order": "0.1",
        "thumbnail": "http://localhost:81/2020/11/13/51e1124b5e8f2f3d.png",
        "asset_category": {
          "idx": "2",
          "name": "env"
        },
        "status": {
          "name": "wip"
        },
        "description": "",
        "last_version_thumbnail": "/2020/11/13/51e1124b5e8f2f3d.png",
        "tasks": {
          "Concept": {
            "artist": null,
            "pub": null,
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "description": "",
            "is_on": "1",
            "idx": "42",
            "tasktype": {
              "idx": "16",
              "name": "Concept",
              "color": "#4caf50"
            },
            "user": {
              "id": null
            },
            "status": {
              "name": "wip"
            }
          },
          "Modeling": {
            "artist": "C2Monster",
            "pub": "big_s0010_c0010_animation_v001",
            "start_date": "2021-01-22",
            "end_date": "2021-01-30",
            "duration": "0",
            "description": "qqq",
            "is_on": "1",
            "idx": "20",
            "tasktype": {
              "idx": "14",
              "name": "Modeling",
              "color": "#f44336"
            },
            "user": {
              "id": "c2m"
            },
            "status": {
              "name": "retake"
            }
          },
          "Texture": {
            "artist": "C2Monster",
            "pub": null,
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "description": "qqq",
            "is_on": "1",
            "idx": "21",
            "tasktype": {
              "idx": "15",
              "name": "Texture",
              "color": "#3f51b5"
            },
            "user": {
              "id": "c2m"
            },
            "status": {
              "name": "wip"
            }
          }
        }
      }
    ],
    "setting_column": [
      {
        "data": "idx",
        "type": "numeric",
        "width": 50,
        "editor": false
      },
      {
        "data": "order",
        "type": "text",
        "width": 50
      },
      {
        "data": "asset_category.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": [
          "ㅅㄷㄴㅅ",
          "env",
          "char",
          "7",
          "6",
          "5",
          "4",
          "3",
          "222",
          "2",
          "111",
          "1"
        ],
        "width": 120
      },
      {
        "data": "name",
        "type": "text",
        "width": 180
      },
      {
        "data": "thumbnail",
        "renderer": "renderAssetThumbnail",
        "width": 84,
        "editor": false
      },
      {
        "data": "description",
        "type": "text",
        "width": 190
      },
      {
        "data": "status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["A_tests", "wip", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.Concept.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.Concept.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["A_tests", "wip", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.Concept.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.Concept.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.Concept.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.Concept.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Concept.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Concept.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      },
      {
        "data": "tasks.Modeling.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.Modeling.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["A_tests", "wip", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.Modeling.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.Modeling.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.Modeling.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.Modeling.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Modeling.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Modeling.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      },
      {
        "data": "tasks.Texture.idx",
        "renderer": "renderSummary",
        "readOnly": true,
        "width": 120
      },
      {
        "data": "tasks.Texture.status.name",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["A_tests", "wip", "confirm", "retake", "pub", "final"],
        "renderer": "renderStatus",
        "width": 120
      },
      {
        "data": "tasks.Texture.description",
        "renderer": "renderTaskDescription",
        "type": "text",
        "width": 120
      },
      {
        "data": "tasks.Texture.pub",
        "type": "text",
        "editor": false,
        "width": 120
      },
      {
        "data": "tasks.Texture.artist",
        "renderer": "renderArtist",
        "type": "dropdown",
        "allowInvalid": false,
        "source": ["C2Monster", "Artist", "12322233", "test0"],
        "width": 120
      },
      {
        "data": "tasks.Texture.start_date",
        "renderer": "renderStartDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Texture.end_date",
        "renderer": "renderEndDate",
        "type": "date",
        "dateFormat": "YYYY-MM-DD",
        "width": 120
      },
      {
        "data": "tasks.Texture.duration",
        "renderer": "renderDuration",
        "type": "text",
        "width": 100
      }
    ],
    "collapsible_columns": [
      {
        "row": -2,
        "col": 3,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 7,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 15,
        "collapsible": true
      },
      {
        "row": -2,
        "col": 23,
        "collapsible": true
      }
    ],
    "nested_headers": [
      [
        "idx",
        "Order",
        "Category",
        {
          "label": "Asset Info",
          "colspan": 4
        },
        {
          "label": "Concept",
          "colspan": 8
        },
        {
          "label": "Modeling",
          "colspan": 8
        },
        {
          "label": "Texture",
          "colspan": 8
        },
        "end"
      ],
      [
        "-",
        "-",
        "Name",
        "Asset Name",
        "Thumbnail",
        "Description",
        "Status",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "Summary",
        "Status",
        "Description",
        "Pub",
        "Artist",
        "Start Date",
        "End Date",
        "Duration",
        "-"
      ]
    ],
    "statuses": [
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
      },
      {
        "idx": "14",
        "name": "A_tests",
        "color": "#4caf50"
      }
    ],
    "filters": [
      {
        "column": "2",
        "operation": "conjunction",
        "conditions": [
          {
            "name": "by_value",
            "args": [["char"]]
          }
        ],
        "prop": "asset_category.name"
      }
    ]
  }
}
```

---

## 4. 릴레이션 에피소드 리스트 조회 <a id="releation-episode-list"></a>

### `GET /api/project/{project_idx}/relation/episode/list`

### `GET /api/project/{project_idx}/relation/episode/{episode_idx}/list`

### permission

- `permission.read_asset_task_overview`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| episode_idx | path | integer |    X     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "episodes": [
      {
        "idx": "20",
        "name": "ep309",
        "progress": 100,
        "count": 10,
        "shot_count": 230
      },
      {
        "idx": "19",
        "name": "ep308",
        "progress": 100,
        "count": 1,
        "shot_count": 230
      },
      {
        "idx": "18",
        "name": "ep307",
        "progress": 74.31,
        "count": 413,
        "shot_count": 230
      }
    ]
  }
}
```

---

## 5. 릴레이션 시퀀스 리스트 조회 <a id="releation-ext-episode-sequence-list"></a>

### `GET /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/list`

### `GET /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/{sequence_idx}/list`

### permission

- `permission.read_asset_task_overview`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    X     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "sequences": [
      {
        "idx": "65",
        "name": "111",
        "progress": 0,
        "count": 0
      },
      {
        "idx": "63",
        "name": "14",
        "progress": 0,
        "count": 0
      },
      {
        "idx": "62",
        "name": "13",
        "progress": 0,
        "count": 0
      }
    ]
  }
}
```

---

## 6. 릴레이션 샷 리스트 조회 <a id="releation-ext-episode-sequence-shot-list"></a>

### `GET /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/{sequence_idx}/shot/list`

### `GET /api/project/{project_idx}/relation/episode/{episode_idx}/sequence/{sequence_idx}/shot/{shot_idx}/list`

### permission

- `permission.read_asset_task_overview`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| episode_idx  | path | integer |    O     |      |
| sequence_idx | path | integer |    X     |      |

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
        "idx": "5403",
        "name": "Artist2",
        "thumbnail": "/assets/images/thumbnail/shot/default.light.svg",
        "progress": 0,
        "count": 0
      },
      {
        "idx": "5387",
        "name": "sc216d",
        "thumbnail": "/assets/images/thumbnail/shot/default.light.svg",
        "progress": 0,
        "count": 0
      },
      {
        "idx": "5386",
        "name": "sc216c",
        "thumbnail": "/assets/images/thumbnail/shot/default.light.svg",
        "progress": 0,
        "count": 0
      }
    ]
  }
}
```

---

## 7. 릴레이션 카테고리 별 에셋 조회 <a id="releation-ext-asset-list"></a>

### `GET /api/project/{project_idx}/{which}/{which_idx}/relation/asset/list`

### permission

- `permission.read_asset_task_overview`

### request

| param       | type |  data   | required | desc                    |
| ----------- | :--: | :-----: | :------: | ----------------------- |
| project_idx | path | integer |    O     |                         |
| which       | path | string  |    O     | episode, sequence, shot |
| which_idx   | path | integer |    O     |                         |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "asset_idxes": ["1", "2", "3", "4"]
  }
}
```

---

## 8. 릴레이션 카테고리 별 에셋 할당 <a id="releation-bulk-add"></a>

### `POST /api/project/{project_idx}/which/{which_idx}/asset/relation/bulk/add`

### permission

- `permission.read_asset_task_overview`

### request

| param       | type  |  data   | required | desc                    |
| ----------- | :---: | :-----: | :------: | ----------------------- |
| project_idx | path  | integer |    O     |                         |
| which       | path  | string  |    O     | episode, sequence, shot |
| which_idx   | path  | integer |    O     |                         |
| asset_idx[] | query |  array  |    O     |                         |
| checked[]   | query |  array  |    O     |                         |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## 9. 에셋 오버뷰 컬럼 너비 수정 <a id="project-asset-task-overview-column-width-update"></a>

### `POST /api/project/{project_idx}/asset/task/overview/column/width/update`

### permission

- `permission.read_asset_task_overview`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| column      | query | string  |    O     |      |
| width       | query | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A1. 오버뷰 템플릿 목록 조회 <a id="template-list"></a>

### `GET /api/overview_templates/list`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc            |
| ----------- | :---: | :-----: | :------: | --------------- |
| project_idx | query | integer |    O     |                 |
| which       | query | string  |    O     | 'shot', 'asset' |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "templates": [
      {
        "idx": "11",
        "type": "personal",
        "user": {
          "idx": "1",
          "name": "C2Monster",
          "is_on": "1",
          "id": "c2m",
          "email": "contact@c2monster.com",
          "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
        },
        "name": "my first personal template",
        "description": "you can edit/duplicate/delete it.",
        "created_time": "2022-07-20 14:38:44",
        "updated_time": "2022-07-20 14:38:44",
        "in_use": 1
      }
    ]
  }
}
```

---

## A2. 오버뷰 템플릿 조회 <a id="template-read"></a>

### `GET /api/overview_templates/{overview_template_idx}/read`

### permission

- `permission.read_shot_task_overview`

### request

| param                 | type |  data   | required | desc |
| --------------------- | :--: | :-----: | :------: | ---- |
| overview_template_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A3. 오버뷰 템플릿 수정 <a id="template-update"></a>

### `POST /api/overview_templates/{overview_template_idx}/update`

### permission

- `permission.read_shot_task_overview`

### request

| param                 | type  |  data   | required | desc             |
| --------------------- | :---: | :-----: | :------: | ---------------- |
| overview_template_idx | path  | integer |    O     |                  |
| name                  | query | string  |    O     |                  |
| description           | query | string  |    X     |                  |
| shot_columns          | query | string  |    O     | stringified json |
| camera_columns        | query | string  |    O     | stringified json |
| custom_columns        | query | string  |    O     | stringified json |
| tasktype_columns      | query | string  |    O     | stringified json |
| settings              | query | string  |    O     | stringified json |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A4. 오버뷰 템플릿 복사 <a id="template-duplicate"></a>

### `POST /api/overview_templates/{overview_template_idx}/duplicate`

### permission

- `permission.read_shot_task_overview`

### request

| param                 | type  |  data   | required | desc                    |
| --------------------- | :---: | :-----: | :------: | ----------------------- |
| overview_template_idx | path  | integer |    O     |                         |
| name                  | query | string  |    O     |                         |
| description           | query | string  |    X     |                         |
| type                  | query | string  |    O     | 'personal' or 'project' |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "template": {
      "idx": 5
    }
  }
}
```

---

## A5. 오버뷰 템플릿 삭제 <a id="template-delete"></a>

### `POST /api/overview_templates/{overview_template_idx}/delete`

### permission

- `permission.read_shot_task_overview`

### request

| param                 | type |  data   | required | desc |
| --------------------- | :--: | :-----: | :------: | ---- |
| overview_template_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A6. 오버뷰 템플릿 초기화 <a id="template-reset"></a>

### `POST /api/overview_templates/{overview_template_idx}/reset`

### permission

- `permission.read_shot_task_overview`

### request

| param                 | type |  data   | required | desc |
| --------------------- | :--: | :-----: | :------: | ---- |
| overview_template_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A7. 오버뷰 기본 템플릿 조회 <a id="template-default-read"></a>

### `GET /api/overview_templates/default/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc            |
| ----------- | :---: | :-----: | :------: | --------------- |
| project_idx | query | integer |    O     |                 |
| which       | query | string  |    O     | 'asset', 'shot' |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "shot_columns": [
      {
        "column": "order",
        "name": "Order",
        "visible": true
      },
      {
        "column": "episode.name",
        "name": "Episode Name",
        "visible": false
      },
      {
        "column": "sequence.name",
        "name": "Sequence Name",
        "visible": false
      },
      {
        "column": "name",
        "name": "Shot Name",
        "visible": true
      },
      {
        "column": "thumbnail",
        "name": "Thumbnail",
        "visible": false
      },
      {
        "column": "description",
        "name": "Description",
        "visible": true
      },
      {
        "column": "status.name",
        "name": "Status",
        "visible": true
      },
      {
        "column": "location",
        "name": "Location",
        "visible": false
      },
      {
        "column": "note",
        "name": "Direction Note",
        "visible": false
      },
      {
        "column": "length",
        "name": "Length",
        "visible": false
      },
      {
        "column": "handle_in",
        "name": "Handle In",
        "visible": false
      },
      {
        "column": "handle_out",
        "name": "Handle Out",
        "visible": false
      },
      {
        "column": "frame_in",
        "name": "Frame In",
        "visible": false
      },
      {
        "column": "frame_out",
        "name": "Frame Out",
        "visible": false
      },
      {
        "column": "timecode_in",
        "name": "Timecode In",
        "visible": false
      },
      {
        "column": "timecode_out",
        "name": "Timecode Out",
        "visible": false
      },
      {
        "column": "importance",
        "name": "Importance",
        "visible": false
      },
      {
        "column": "difficulty",
        "name": "Level",
        "visible": false
      },
      {
        "column": "original_path",
        "name": "Original Edit Path",
        "visible": false
      }
    ],
    "camera_columns": [
      {
        "column": "camera_clip",
        "name": "Camera Clip",
        "visible": false
      },
      {
        "column": "camera_name",
        "name": "Camera Name",
        "visible": false
      },
      {
        "column": "lens_type",
        "name": "Lens Type",
        "visible": false
      },
      {
        "column": "focal_length",
        "name": "Focal Length",
        "visible": false
      },
      {
        "column": "grip",
        "name": "Grip",
        "visible": false
      },
      {
        "column": "camera_filter",
        "name": "Filter",
        "visible": false
      },
      {
        "column": "iso",
        "name": "ISO",
        "visible": false
      },
      {
        "column": "shutter_speed",
        "name": "Shutter Speed",
        "visible": false
      },
      {
        "column": "f_stop",
        "name": "F-Stop",
        "visible": false
      },
      {
        "column": "stereo_type",
        "name": "Stereo Type",
        "visible": false
      },
      {
        "column": "stereo_iod",
        "name": "Stereo IOD",
        "visible": false
      },
      {
        "column": "stereo_converged_point",
        "name": "Stereo Converged Point",
        "visible": false
      },
      {
        "column": "stereo_rig",
        "name": "Stereo Rig",
        "visible": false
      },
      {
        "column": "stereo_dof",
        "name": "Stereo DOF",
        "visible": false
      },
      {
        "column": "camera_note",
        "name": "Note",
        "visible": false
      }
    ],
    "custom_columns": [
      {
        "column": "c1",
        "name": "first",
        "visible": false
      },
      {
        "column": "c2",
        "name": "second",
        "visible": false
      },
      {
        "column": "c3",
        "name": "third",
        "visible": false
      }
    ],
    "tasktypes": [
      {
        "column": "Animation",
        "name": "Animation",
        "visible": false
      },
      {
        "column": "Comp",
        "name": "Comp",
        "visible": false
      }
    ],
    "settings": [
      {
        "type": "group",
        "name": "shot info",
        "children": [
          {
            "type": "shot",
            "name": "Order",
            "column": "order"
          },
          {
            "type": "shot",
            "name": "Shot Name",
            "column": "name"
          },
          {
            "type": "shot",
            "name": "Status",
            "column": "status.name"
          },
          {
            "type": "shot",
            "name": "Description",
            "column": "description"
          }
        ]
      }
    ]
  }
}
```

---

## A8. 오버뷰 기본 템플릿 수정 <a id="template-default-update"></a>

### `POST /api/overview_templates/default/update`

### permission

- `permission.read_shot_task_overview`

### request

| param                 | type  |  data   | required | desc            |
| --------------------- | :---: | :-----: | :------: | --------------- |
| project_idx           | query | integer |    O     |                 |
| which                 | query | string  |    O     | 'shot', 'asset' |
| overview_template_idx | query | integer |    O     |                 |

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

## A9. 오버뷰 컬럼 너비 수정 <a id="user-table-width-update"></a>

### `POST /api/tables/width/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | query | integer |    X     |      |
| table_name  | query | string  |    O     |      |
| column_name | query | string  |    O     |      |
| width       | query | integer |    O     |      |

### list table_name

- shot_overview
- asset_overview

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A10. 오버뷰 기본 템플릿 필터 초기화 <a id="template-default-filter-reset"></a>

### `POST /api/overview_templates/default/filter/reset`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc            |
| ----------- | :---: | :-----: | :------: | --------------- |
| project_idx | query | integer |    O     |                 |
| which       | query | string  |    O     | 'shot', 'asset' |

### list table_name

- shot_overview
- asset_overview

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## A11. 오버뷰 기본 템플릿 접힘 컬럼 초기화 <a id="template-default-collapsed-column-reset"></a>

### `POST /api/overview_templates/default/collapsed_column/reset`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc            |
| ----------- | :---: | :-----: | :------: | --------------- |
| project_idx | query | integer |    O     |                 |
| which       | query | string  |    O     | 'shot', 'asset' |

### list table_name

- shot_overview
- asset_overview

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": null
}
```

---

## 끝

[샷 오버뷰 조회]: #read
[샷 오버뷰 컬럼 너비 수정]: #column-width-update
[에셋 오버뷰 조회]: #project-asset-task-overview-read
[릴레이션 에피소드 리스트 조회]: #releation-episode-list
[릴레이션 시퀀스 조회]: #releation-episode-sequence-list
[릴레이션 샷 조회]: #releation-episode-sequence-shot-list
[릴레이션 카테고리 별 에셋 조회]: #releation-asset-list
[릴레이션 카테고리 별 에셋 할당]: #releation-bulk-add
[에셋 오버뷰 컬럼 너비 수정]: #project-asset-task-overview-column-width-update
[오버뷰 템플릿 목록 조회]: #template-list
[오버뷰 템플릿 조회]: #template-read
[오버뷰 템플릿 수정]: #template-update
[오버뷰 템플릿 복사]: #template-duplicate
[오버뷰 템플릿 삭제]: #template-delete
[오버뷰 템플릿 초기화]: #template-reset
[오버뷰 기본 템플릿 조회]: #template-default-read
[오버뷰 기본 템플릿 수정]: #template-default-update
[오버뷰 컬럼 너비 수정]: #column-width-update
[오버뷰 기본 템플릿 필터 초기화]: #template-default-filter-reset
[오버뷰 기본 템플릿 접힘 컬럼 초기화]: #template-default-collapsed-column-reset
