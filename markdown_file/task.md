# WH2API::task

## 목차

| 내용                                      | slug                                                                           | 서버 구현 | 웹 적용 |  웹훅  | 로그  |
| :---------------------------------------- | :----------------------------------------------------------------------------- | :-------: | :-----: | :----: | :---: |
| 1. [에셋 태스크 벌크 등록]                | /api/project/{project_idx}/asset/task/bulk/create                              |   POST    |    O    | hooked |   O   |
| 2. [에셋 태스크 삭제]                     | /api/project/{project_idx}/asset/task/bulk/delete                              |   POST    |    O    |   -    |   O   |
| 3. [에셋 태스크 정보 수정]                | /api/project/{project_idx}/asset/task/{task_idx}/update                        |   POST    |    O    | hooked |   O   |
| 4. [샷 태스크 벌크 등록]                  | /api/project/{project_idx}/shot/task/bulk/create                               |   POST    |    O    | hooked |   O   |
| 5. [샷 태스크 삭제]                       | /api/project/{project_idx}/shot/task/bulk/delete                               |   POST    |    O    |   -    |   O   |
| 6. [샷 태스크 정보 수정]                  | /api/project/{project_idx}/shot/task/{task_idx}/update                         |   POST    |    O    | hooked |   O   |
| 7. [샷/에셋 태스크 상태 코드 수정 수정]   | /api/project/{project_idx}/{which}/task/{task_idx}/status/update               |   POST    |    O    | hooked |   O   |
| 8. [샷/에셋 태스크 업무 시작]             | /api/project/{project_idx}/{which}/task/{task_idx}/start                       |   POST    |    O    | hooked |   -   |
| 9. [샷/에셋 태스크 업무 정지]             | /api/project/{project_idx}/{which}/task/{task_idx}/stop                        |   POST    |    O    | hooked |   -   |
| 10. [샷 태스크의 에셋 릴레이션 목록 조회] | /api/project/{project_idx}/shot/task/{task_idx}/relation/read[/with/{setting}] |    GET    |    O    |   -    |   -   |
| 11. [샷 태스크 목록 조회]                 | /api/project/{project_idx}/shot/{shot_idx}/task/list                           |   X GET   |    X    |   -    |   -   |
| 12. [에셋 태스크 목록 조회]               | /api/project/{project_idx}/asset/{asset_idx}/task/list                         |   X GET   |    X    |   -    |   -   |
| 13. [샷 태스크 조회]                      | /api/shot/task/{task_idx}/read                                                 |    GET    |    X    |   -    |   -   |
| 14. [에셋 태스크 조회]                    | /api/asset/task/{task_idx}/read                                                |    GET    |    X    |   -    |   -   |
| 15. [에셋 태스크 벌크 수정]               | /api/project/{project_idx}/asset/task/bulk/update                              |   POST    |    O    | hooked |   O   |
| 16. [샷 태스크 벌크 수정]                 | /api/project/{project_idx}/shot/task/bulk/update                               |   POST    |    O    | hooked |   O   |

- O\* - 3, 4번 동시 적용

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에셋 태스크 벌크 등록 <a id="project-asset-task-create"></a>

### `POST /api/project/{project_idx}/asset/task/bulk/create`

### Webhook

- event: task
- action: create

### permission

- `permission.update_asset_and_task`

### request

| param           | type  |     data      | required | desc       |
| --------------- | :---: | :-----------: | :------: | ---------- |
| project_idx     | path  |    integer    |    O     |            |
| asset_idx[]     | query |    integer    |    O     |            |
| tasktype_name[] | query |    string     |    O     |            |
| status_idx[]    | query |    integer    |    X     |            |
| description[]   | query |    string     |    X     |            |
| user_idx[]      | query |    integer    |    X     |            |
| start_date[]    | query | array of date |    X     | YYYY-MM-DD |
| end_date[]      | query | array of date |    X     | YYYY-MM-DD |
| duration[]      | query |    double     |    X     |            |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 등록됐습니다."
	},
	"data": {
		"tasks": [
			{
				"kind": "asset",
				"idx": 3,
				"asset": {
					"idx": 1
				},
				"duration": 1,
				"status": {
					"name": "wip"
				}
			},
			{
				"kind": "asset",
				"idx": 4,
				"asset": {
					"idx": 2
				},
				"duration": 2,
				"status": {
					"name": "wip"
				}
			}
		]
	}
}
```

---

## 2. 에셋 태스크 삭제 <a id="project-asset-task-delete"></a>

### `POST /api/project/{project_idx}/asset/task/bulk/delete`

### permission

- `permission.update_asset_and_task`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| task_idx[]  | path  | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 삭제됐습니다."
	},
	"data": null
}
```

---

## 3. 에셋 태스크 정보 수정 <a id="project-asset-task-update"></a>

- 에셋 태스크 1개의 1가지 정보만 선택해서 수정
- 사용 예)
  - http://localhost/project/1/category/1/asset/task/add
  - task의 duration_init 값을 수정합니다.

### `POST /api/project/{project_idx}/asset/task/{task_idx}/update`

### Webhook

- event: task
- action: update

### permission

- `permission.update_asset_and_task`

### request

| param    | type  |  data   | required | desc             |
| -------- | :---: | :-----: | :------: | ---------------- |
| task_idx | path  | integer |    O     |                  |
| column   | query | string  |    O     |                  |
| old_val  | query | string  |    O     | 공백일 수는 있음 |
| new_val  | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
    "error": {
        "code": 200,
        "message": "Asset Task information is edited."
    },
    "data": {
        "task": {
            "kind": "asset",
            "idx": "5",
            "name": "Concept",
            "column": "status_name",
            "value": "confirm",
            "status": {
                "idx": "2",
                "name": "confirm",
                "color": "#03a9f4"
            }
        },
        "version": {
            "idx": "12",
            "name": "ch_squirrel_concpet_v001",
            "status": {
                "idx": "2",
                "name": "confirm",
                "color": "#03a9f4"
            }
        }
    }
}
```

---

## 4. 샷 태스크 벌크 등록 <a id="project-shot-task-create"></a>

### `POST /api/project/{project_idx}/shot/task/bulk/create`

### Webhook

- event: task
- action: create

### permission

- `permission.update_shot_and_task`

### request

| param           | type  |       data       | required | desc |
| --------------- | :---: | :--------------: | :------: | ---- |
| project_idx     | path  |     integer      |    O     |      |
| shot_idx[]      | query | array of integer |    O     |      |
| tasktype_name[] | query | array of string  |    O     |      |
| status_idx[]    | query | array of integer |    X     |      |
| description[]   | query | array of string  |    X     |      |
| user_idx[]      | query | array of integer |    X     |      |
| start_date[]    | query |  array of date   |    X     |      |
| end_date[]      | query |  array of date   |    X     |      |
| duration[]      | query | array of double  |    X     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 등록됐습니다."
	},
	"data": {
		"tasks": [
			{
				"idx": 3,
				"kind": "shot",
				"duration": 1,
				"shot": {
					"idx": 1
				},
				"status": {
					"name": "wip"
				}
			},
			{
				"idx": 4,
				"kind": "shot",
				"duration": 3,
				"shot": {
					"idx": 2
				},
				"status": {
					"name": "wip"
				}
			},
			{
				"idx": 5,
				"kind": "shot",
				"duration": 4,
				"shot": {
					"idx": 3
				},
				"status": {
					"name": "wip"
				}
			},
			{
				"idx": 6,
				"kind": "shot",
				"duration": 4,
				"shot": {
					"idx": 4
				},
				"status": {
					"name": "wip"
				}
			}
		]
	}
}
```

---

## 5. 샷 태스크 벌크 삭제 <a id="project-shot-task-delete"></a>

### `POST /api/project/{project_idx}/shot/task/bulk/delete`

### permission

- `permission.update_shot_and_task`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| task_idx[]  | path  | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 삭제됐습니다."
	},
	"data": null
}
```

---

## 6. 샷 태스크 정보 수정 <a id="project-shot-task-update"></a>

### `POST /api/project/{project_idx}/shot/task/{task_idx}/update`

### Webhook

- event: task
- action: update

### permission

- `permission.update_shot_and_task`

### request

| param    | type  |  data   | required | desc             |
| -------- | :---: | :-----: | :------: | ---------------- |
| task_idx | path  | integer |    O     |                  |
| column   | query | string  |    O     |                  |
| old_val  | query | string  |    O     | 공백일 수는 있음 |
| new_val  | query | string  |    O     | 공백일 수는 있음 |

- 이용자 정보를 없애려면 ''(공백)을 보냄

### response

```json
{
    "error": {
        "code": 200,
        "message": "Task information is edited."
    },
    "data": {
        "task": {
            "kind": "shot",
            "idx": "1",
            "name": "Comp",
            "column": "status_name",
            "value": "wip",
            "status": {
                "idx": "1",
                "name": "wip",
                "color": "#dbd8db"
            }
        },
        "version": {
            "idx": "15",
            "name": "sampe",
            "status": {
                "idx": "1",
                "name": "wip",
                "color": "#dbd8db"
            }
        }
    }
}
```

---

## 7. 샷/에셋 태스크 상태 코드 수정 <a id="task-status-update"></a>

### `POST /api/project/{project_idx}/{which}/task/{task_idx}/status/update`

### Webhook

- event: task
- action: status update

### permission

- `permission.do_task_and_version_status`

### request

| param       | type  |  data   | required | desc          |
| ----------- | :---: | :-----: | :------: | ------------- |
| project_idx | path  | integer |    O     |               |
| task_idx    | path  | integer |    O     |               |
| which       | path  | string  |    O     | asset or shot |
| status_idx  | query | integer |    O     |               |

### response

```json
{
    "error": {
        "code": 200,
        "message": "Status Code is edited."
    },
    "data": {
        "task": {
            "kind": "shot",
            "idx": 1,
            "name": "Comp",
            "status": {
                "idx": "1",
                "name": "wip",
                "color": "#dbd8db"
            }
        },
        "version": {
            "idx": "1",
            "name": "wip",
            "color": "#dbd8db"
        }
    }
}
```

---

## 8. 샷/에셋 태스크 업무 시작 <a id="task-start"></a>

### `POST /api/project/{project_idx}/{which}/task/{task_idx}/start`

### Webhook

- event: task
- action: start

### permission

- `permission.do_task_and_version_status`

### request

| param       | type  |  data   | required | desc          |
| ----------- | :---: | :-----: | :------: | ------------- |
| project_idx | path  | integer |    O     |               |
| task_idx    | path  | integer |    O     |               |
| which       | path  | string  |    O     | asset or shot |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 시작됐습니다."
	},
	"data": {
		"task": {
			"kind": "shot",
			"idx": 1,
			"project": {
				"idx": 1
			}
		}
	}
}
```

---

## 9. 샷/에셋 태스크 업무 정지 <a id="task-stop"></a>

### `POST /api/project/{project_idx}/{which}/task/{task_idx}/stop`

### Webhook

- event: task
- action: stop

### permission

- `permission.do_task_and_version_status`

### request

| param       | type  |  data   | required | desc          |
| ----------- | :---: | :-----: | :------: | ------------- |
| project_idx | path  | integer |    O     |               |
| task_idx    | path  | integer |    O     |               |
| which       | path  | string  |    O     | asset or shot |

### response

```json
{
	"error": {
		"code": 200,
		"message": "태스크가 정지됐습니다."
	},
	"data": {
		"task": {
			"kind": "shot",
			"idx": 1,
			"project": {
				"idx": 1
			}
		}
	}
}
```

---

## 10. 샷 태스크의 에셋 릴레이션 목록 조회 <a id="shot-task-relation-read"></a>

### `GET /api/project/{project_idx}/shot/task/{task_idx}/relation/read[/with/{setting}]`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   | required | desc           |
| ----------- | :---: | :-----: | :------: | -------------- |
| project_idx | path  | integer |    O     |                |
| task_idx    | path  | integer |    O     |                |
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
				"asset_idx": "1",
				"name": "ch_bunny",
				"asset_category_name": "char",
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
				"asset_idx": "2",
				"name": "ch_bird",
				"asset_category_name": "char"
			},
			{
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
				"data": "asset_category_name",
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
			"Asset Category",
			"Asset Name",
			"Modeling",
			"Texture",
			"Concept"
		]
	}
}
```

- `setting_column`과 `header`는 `/with/setting`으로 접근할 때만 표시됨

---

## 11. 샷 태스크 목록 조회 <a id="shot-task-list"></a>

### `GET /api/project/{project_idx}/shot/{shot_idx}/task/list`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| shot_idx    | path  | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"tasks": [
			{
                "idx": "1",
                "tasktype": {
                    "idx": "3",
                    "name": "Comp"
                },
                "start_date": null,
                "end_date": null,
                "duration": "0",
                "description": "",
                "status": {
                    "idx": "1",
                    "name": "wip",
                    "color": "#dbd8db"
                }
            },
            {
                "idx": "4",
                "tasktype": {
                    "idx": "1",
                    "name": "Animation"
                },
                "start_date": "2019-04-05",
                "end_date": "2019-04-11",
                "duration": "4",
                "description": "Detail Animation",
                "status": {
                    "idx": "2",
                    "name": "confirm",
                    "color": "#03a9f4"
                }
            }
		]
}
```

---

## 12. 에셋 태스크 목록 조회 <a id="asset-task-list"></a>

### `GET /api/project/{project_idx}/asset/{asset_idx}/task/list`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| asset_idx   | path  | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"tasks": [
			{
                "idx": "1",
                "tasktype": {
                    "idx": "15",
                    "name": "Texture"
                },
                "start_date": null,
                "end_date": null,
                "duration": "0",
                "description": "",
                "status": {
                    "idx": "1",
                    "name": "wip",
                    "color": "#dbd8db"
                }
            },
            {
                "idx": "2",
                "tasktype": {
                    "idx": "14",
                    "name": "Modeling"
                },
                "start_date": null,
                "end_date": null,
                "duration": "0",
                "description": "",
                "status": {
                    "idx": "1",
                    "name": "wip",
                    "color": "#dbd8db"
                }
            },
            {
                "idx": "6",
                "tasktype": {
                    "idx": "16",
                    "name": "Concept"
                },
                "start_date": null,
                "end_date": null,
                "duration": "0",
                "description": "",
                "status": {
                    "idx": "2",
                    "name": "confirm",
                    "color": "#03a9f4"
                }
            }
		]
}
```

---

## 13. 샷 태스크 조회 <a id="shot-task-read"></a>

### `GET /api/shot/task/{task_idx}/read`

### permission

- `permission.do_global_setting`

### request

| param    | type  |  data   | required | desc |
| -------- | :---: | :-----: | :------: | ---- |
| task_idx | path  | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"task": {
			"kind": "shot",
			"idx": "5",
			"url": "http://localhost/project/1/shot/task/1/detail",
			"tasktype": {
				"idx": "3",
				"name": "Comp"
			},
			"description": "",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
			},
			"start_date": null,
			"end_date": null,
			"status": {
				"idx": "2",
				"name": "confirm"
			},
			"duration": "0",
			"project": {
				"idx": "1",
				"name": "Demo_Bigbuck_Bunny"
			},
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
				"name": "s0010_c0030",
				"thumbnail": "http://localhost:81/2019/04/08/fbb2b3da21623e7b.jpg",
				"order": "3",
				"location": "Jungle_A",
				"description": "the chattering bird hit by pine cone.",
				"direction_note": "",
				"length": "174",
				"handle_in": "0",
				"handle_out": "0",
				"frame_in": "0",
				"frame_out": "173",
				"timecode_in": "00:00:00:00",
				"timecode_out": "",
				"importance": "0",
				"difficulty": "",
				"original_path": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0030_anim_v001.mp4",
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
				"custom_columns": {
					"cus1": "1",
					"cus2": "22",
					"abc": "33",
					"def": "4",
					"qqq": "5",
					"zzz": "6"
				}
			},
			"pubs": [
				{
					"idx": "1",
					"name": "pub-test",
					"tasktype": {
						"idx": "3",
						"name": "Comp"
					},
					"tags": ["wow", "bob"],
					"description": "memo memo",
					"user": {
						"idx": "1",
						"id": "c2m",
						"name": "C2Monster"
					},
					"created_time": "2020-04-09 00:00:00",
					"attachments": []
				}
			]
		},
		"tasks_in_progress": [
			{
				"idx": "9",
				"tasktype": {
					"idx": "1",
					"name": "Animation"
				},
				"start_date": "2019-04-15",
				"end_date": "2019-04-18",
				"duration": "4",
				"user": {
					"idx": "2",
					"id": "c3m",
					"name": "Artist"
				},
				"status": {
					"idx": "5",
					"name": "final"
				},
				"description": "Detail Animation",
				"publish": {
					"last_name": null
				}
			},
			{
				"idx": "5",
				"tasktype": {
					"idx": "3",
					"name": "Comp"
				},
				"start_date": null,
				"end_date": null,
				"duration": "0",
				"user": {
					"idx": "1",
					"id": "c2m",
					"name": "C2Monster"
				},
				"status": {
					"idx": "2",
					"name": "confirm"
				},
				"description": "",
				"publish": {
					"last_name": "pub-test"
				}
			}
		]
	}
}
```

---

## 14. 에셋 태스크 조회 <a id="asset-task-read"></a>

### `GET /api/asset/task/{task_idx}/read`

### permission

- `permission.do_global_setting`

### request

| param    | type  |  data   | required | desc |
| -------- | :---: | :-----: | :------: | ---- |
| task_idx | path  | integer |    O     |      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"task": {
			"kind": "asset",
			"idx": "1",
			"url": "http://localhost/project/1/asset/task/1/detail",
			"tasktype": {
				"idx": "15",
				"name": "Texture"
			},
			"description": "",
			"user": {
				"idx": "1",
				"name": "C2Monster",
				"id": "c2m",
				"email": "contact@c2monster.com",
				"thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
			},
			"start_date": null,
			"end_date": null,
			"status": {
				"idx": "2",
				"name": "confirm"
			},
			"duration": "0",
			"project": {
				"idx": "1",
				"name": "Demo_Bigbuck_Bunny"
			},
			"asset_category": {
				"idx": "1",
				"name": "char"
			},
			"asset": {
				"idx": "1",
				"name": "ch_bunny",
				"thumbnail": "http://localhost:81/2019/04/08/78b9d804eb4a7f53.jpg",
				"asset_order": "1",
				"description": "Hero character",
				"used": null,
				"reference_path": null,
				"hdri_path": null,
				"source_path": null
			},
			"pubs": null
		},
		"tasks_in_progress": [
			{
				"idx": "2",
				"tasktype": {
					"idx": "14",
					"name": "Modeling"
				},
				"start_date": null,
				"end_date": null,
				"duration": "0",
				"user": {
					"idx": "2",
					"id": "c3m",
					"name": "Artist"
				},
				"status": {
					"idx": "1",
					"name": "wip"
				},
				"description": "",
				"publish": {
					"last_name": null
				}
			},
			{
				"idx": "1",
				"tasktype": {
					"idx": "15",
					"name": "Texture"
				},
				"start_date": null,
				"end_date": null,
				"duration": "0",
				"user": {
					"idx": "4",
					"id": "c4m",
					"name": "Supervisor"
				},
				"status": {
					"idx": "2",
					"name": "confirm"
				},
				"description": "",
				"publish": {
					"last_name": ""
				}
			},
			{
				"idx": "6",
				"tasktype": {
					"idx": "16",
					"name": "Concept"
				},
				"start_date": null,
				"end_date": null,
				"duration": "0",
				"user": {
					"idx": "1",
					"id": "c2m",
					"name": "C2Monster"
				},
				"status": {
					"idx": "2",
					"name": "confirm"
				},
				"description": "",
				"publish": {
					"last_name": null
				}
			}
		]
	}
}
```

---

## 15. 에셋 태스크 벌크 수정 <a id="project-asset-task-bulk-update"></a>

### `POST /api/project/{project_idx}/asset/task/bulk/update`

### Webhook

- event: task
- action: update

### permission

- `permission.update_asset_and_task`

### request

| param      | type  |       data       | required | desc                            |
| ---------- | :---: | :--------------: | :------: | ------------------------------- |
| task_idx[] | query | array of integer |    O     |                                 |
| column[]   | query | array of string  |    O     |                                 |
| old_val[]  | query | array of string  |    O     |                                 |
| new_val[]  | query | array of string  |    O     |                                 |
| force      | query |     integer      |    X     | 1 - 강제 업데이트 / 0 - 기본 값 |

### response

```json
{
    "error": {
        "code": 200,
        "message": "Asset Task information is edited."
    },
    "data": {
        "tasks": [
			{
				"kind": "asset",
				"idx": "5",
				"name": "Concept",
				"column": "status_name",
				"value": "confirm",
				"status": {
					"idx": "2",
					"name": "confirm",
					"color": "#03a9f4"
				},
				"version": {
					"idx": "11",
					"name": "ch_squirrel_concpet_v001",
					"status": {
						"idx": "2",
						"name": "confirm",
						"color": "#03a9f4"
					}
				},
			},
		],
		"failed": [
			{"idx": 1, "name": "Concept (ch_squirrel_concpet_v001)", "column": "status_name", "old_val": "confirm", "server_old_val": "wip", "new_val": "retake", "read_only": true, "description": "삭제된 태크입니다."},
			{"idx": 2, "name": "Concept (ch_squirrel_concpet_v001)", "column": "status_name", "old_val": "confirm", "server_old_val": "wip", "new_val": "retake", "read_only": false, "description": ""},
			{"idx": 3, "name": "Concept (ch_squirrel_concpet_v001)", "column": "status_name", "old_val": "confirm", "server_old_val": "wip", "new_val": "retake", "read_only": false, "description": ""},
		]
    }
}
```

---

## 16. 샷 태스크 벌크 수정 <a id="project-shot-task-bulk-update"></a>

### `POST /api/project/{project_idx}/shot/task/bulk/update`

### Webhook

- event: task
- action: update

### permission

- `permission.update_shot_and_task`

### request

| param      | type  |       data       | required | desc                            |
| ---------- | :---: | :--------------: | :------: | ------------------------------- |
| task_idx[] | query | array of integer |    O     |                                 |
| column[]   | query | array of string  |    O     |                                 |
| old_val[]  | query | array of string  |    O     |                                 |
| new_val[]  | query | array of string  |    O     |                                 |
| force      | query |     integer      |    X     | 1 - 강제 업데이트 / 0 - 기본 값 |

### response

```json
{
    "error": {
        "code": 200,
        "message": "Shot Task information is edited."
    },
    "data": {
        "tasks": [
			{
				"kind": "shot",
				"idx": "5",
				"name": "Animation",
				"column": "status_name",
				"value": "confirm",
				"status": {
					"idx": "2",
					"name": "confirm",
					"color": "#03a9f4"
				},
				"version": {
					"idx": "11",
					"name": "ch_squirrel_concpet_v001",
					"status": {
						"idx": "2",
						"name": "confirm",
						"color": "#03a9f4"
					}
				},
			},
		],
		"failed": [
			{"idx": 1, "name": "Animation (s0010_c0010)", "column": "status_name", "old_val": "confirm", "server_old_val": "wip", "new_val": "retake", "read_only": true, "description": "삭제된 테스크입니다."},
			{"idx": 2, "name": "Animation (s0010_c0010)", "column": "status_name", "old_val": "confirm", "server_old_val": "wip", "new_val": "retake", "read_only": false, "description": ""},
			{"idx": 3, "name": "Animation (s0010_c0010)", "column": "status_name", "old_val": "confirm", "server_old_val": "wip", "new_val": "retake", "read_only": false, "description": ""},
		]
    }
}
```

---

## 끝

[에셋 태스크 등록]: #project-asset-task-create
[에셋 태스크 삭제]: #project-asset-task-delete
[에셋 태스크 정보 수정]: #project-asset-task-update
[샷 태스크 등록]: #project-shot-task-create
[샷 태스크 삭제]: #project-shot-task-delete
[샷 태스크 정보 수정]: project-shot-task-update
[샷/에셋 태스크 상태 코드 수정]: #task-status-update
[샷/에셋 태스크 업무 시작]: #task-start
[샷/에셋 태스크 업무 정지]: #task-stop
[샷 태스크의 에셋 릴레이션 목록 조회]: #shot-task-relation-read
[샷 태스크 목록 조회]: #shot-task-list
[에셋 태스크 목록 조회]: #asset-task-list
[샷 태스크 조회]: #shot-task-read
[에셋 태스크 조회]: #asset-task-read
[에셋 태스크 벌크 업데이트]: #project-asset-task-bulk-update
[샷 태스크 벌크 업데이트]: #project-shot-task-bulk-update
