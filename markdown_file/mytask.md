# WH2API::MyTask

## 목차

| 내용                           | slug                                        | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
|:-------------------------------|:--------------------------------------------|:---------:|:-------:|:----:|:----:|
| 1. [To-Do 조회]                | /api/mytask/todo/read[/progress/{progress}] |    GET    |    O    |  -   |  -   |
| 2. [In-Progress 조회]          | /api/mytask/inprogress/read[/{last}]        |    GET    |    O    |  -   |  -   |
| 3. [Done 조회]                 | /api/mytask/done/read                       |    GET    |    O    |  -   |  -   |
| 4. [CC 목록 조회]              | /api/mytask/cc/read[/{last}]                |    GET    |    O    |  -   |  -   |
| 5. [마이태스크 설정 목록 조회] | /api/mytask/setting/list                    |    GET    |    O    |  -   |  -   |
| 6. [마이태스크 설정 정보 저장] | /api/mytask/setting/update                  |   POST    |    O    |  -   |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. To-Do 조회 조회 <a id="mytask-todo-read"></a>

### `GET /api/mytask/todo/read[/progress/{progress}]`

### permission

- `permission.read_mytask`

### request

| param    | type |  data  | required | desc            |
|----------|:----:|:------:|:--------:|-----------------|
| progress | path | string |    X     | progress의 값 1 |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "version_overview": [
            {
                "receiver_idx": "23",
                "idx": "4",
                "kind": "shot",
                "thumbnail": "http://localhost:81/2019/04/08/44e0a6ec7ea7bbbb.jpg",
                "shot_asset_name": "s0020_c0030",
                "task": {
                    "name": "Animation",
                    "idx": "24",
                    "status": {
                        "idx": "4",
                        "name": "pub"
                    },
                    "is_on": "1"
                },
                "name": "big_s0020_c0030_anim_v001",
                "status": {
                    "idx": "2",
                    "name": "confirm"
                },
                "comment": "Detail_animation_Check",
                "artist": {
                    "user": {
                        "name": "C2Monster",
                        "idx": "1"
                    }
                },
                "reviewer": {
                    "user": {
                        "name": "C2Monster",
                        "idx": "1"
                    }
                },
                "last_comment": null,
                "last_comment_time": null,
                "request_time": "2019-04-08 17:34:45",
                "project": {
                    "idx": "1"
                }
            },
            {
                "receiver_idx": "25",
                "idx": "16",
                "kind": "shot",
                "thumbnail": "http://localhost:81/2021/03/09/ac3c4b57e3ed6ed5.jpg",
                "shot_asset_name": "s0020_c0010",
                "task": {
                    "name": "Animation",
                    "idx": "21",
                    "status": {
                        "idx": "2",
                        "name": "confirm"
                    },
                    "is_on": "1"
                },
                "name": "big_s0010_c0030_anim_v001",
                "status": {
                    "idx": "2",
                    "name": "confirm"
                },
                "comment": "",
                "artist": {
                    "user": {
                        "name": "C2Monster",
                        "idx": "1"
                    }
                },
                "reviewer": {
                    "user": {
                        "name": "C2Monster",
                        "idx": "1"
                    }
                },
                "last_comment": "xxx",
                "last_comment_time": "2021-03-09 15:16:04",
                "request_time": "2021-03-09 15:13:03",
                "project": {
                    "idx": "1"
                }
            }
        ],
        "task_shots": [
            {
                "idx": "8",
                "kind": "shot",
                "shot": {
                    "name": "s0010_c0050",
                    "thumbnail": "http://localhost:81/2019/04/08/13f8004c570ac3c3.jpg"
                },
                "project": {
                    "idx": "1",
                    "name": "Demo_Bigbuck_Bunny"
                },
                "episode": {
                    "name": "Ep01"
                },
                "sequence": {
                    "name": "s0010"
                },
                "task": {
                    "name": "Comp"
                },
                "start_date": null,
                "end_date": null,
                "description": "",
                "status": {
                    "idx": "1",
                    "name": "wip"
                },
                "task_is_on": "1",
                "prev_tasks": "Animation - wip",
                "prev_tasks_progress_average": 5
            }
        ],
        "task_assets": [
            {
                "idx": "8",
                "kind": "asset",
                "asset": {
                    "idx": "4",
                    "name": "en_tree",
                    "thumbnail": "http://localhost:81/2019/04/08/a912022aa81e647d.png",
                    "used": null
                },
                "project": {
                    "idx": "1",
                    "name": "Demo_Bigbuck_Bunny"
                },
                "asset_category": {
                    "name": "env"
                },
                "task": {
                    "name": "Concept"
                },
                "start_date": "2021-03-07",
                "end_date": "2021-03-19",
                "description": "",
                "status": {
                    "idx": "2",
                    "name": "confirm"
                },
                "task_is_on": "1",
                "prev_tasks": "Modeling - wip\nTexture - wip",
                "prev_tasks_progress_average": 5
            }
        ],
        "mytasktype_setting": {
            "task_statuses": [
                {
                    "idx": "1",
                    "name": "wip",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "2",
                    "name": "confirm",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "3",
                    "name": "retake",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "4",
                    "name": "pub",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "5",
                    "name": "final",
                    "include": [
                        "Done"
                    ]
                }
            ],
            "version_statuses": [
                {
                    "idx": "1",
                    "name": "wip",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "2",
                    "name": "confirm",
                    "include": [
                        "To-Do",
                        "In-Progress"
                    ]
                },
                {
                    "idx": "3",
                    "name": "retake",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "4",
                    "name": "pub",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "5",
                    "name": "final",
                    "include": [
                        "In-Progress"
                    ]
                }
            ]
        },
        "filters": {
            "shot_tasks_filters": [
                {
                    "column": "7",
                    "operation": "conjunction",
                    "conditions": [
                        {
                            "name": "by_value",
                            "args": [
                                [
                                    "PE_06_01",
                                    "s0010_c0020",
                                    "s0010_c0050",
                                    "s0010_c0060",
                                    "s0010_c0070",
                                    "s0010_c0080",
                                    "s0010_c0090",
                                    "s0010_c0100",
                                    "s0020_c0010",
                                    "s0020_c0020",
                                    "s0020_c0030",
                                    "s0020_c0040",
                                    "s0020_c0050",
                                    "s0020_c0060",
                                    "s0020_c0070",
                                    "s0020_c0080"
                                ]
                            ]
                        }
                    ]
                }
            ],
            "asset_tasks_filters": [
                {
                    "column": "6",
                    "operation": "conjunction",
                    "conditions": [
                        {
                            "name": "by_value",
                            "args": [
                                [
                                    "ch_bunny",
                                    "en_tree"
                                ]
                            ]
                        }
                    ]
                }
            ],
            "confirm_filters": []
        }
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
|-------|:----:|:------:|:--------:|----------|
| last  | path | string |    X     | 값: last |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "myversion_overview": {
            "versions": [
                {
                    "idx": "64",
                    "name": "ep296_sc121_kimchi",
                    "kind": "asset",
                    "thumbnail": "http://localhost:81/2021/02/01/2e08a9aecfbe920c.jpg",
                    "shot_asset_name": "ch_bunny",
                    "task": {
                        "idx": "6",
                        "name": "Concept",
                        "status": {
                            "idx": "2",
                            "name": "confirm"
                        }
                    },
                    "status": {
                        "idx": "2",
                        "name": "confirm"
                    },
                    "comment": "test",
                    "artist": {
                        "user": {
                            "idx": "1",
                            "name": "C2Monster"
                        }
                    },
                    "reviewer": {
                        "user": {
                            "idx": "1",
                            "name": "C2Monster"
                        }
                    },
                    "last_comment": null,
                    "last_comment_time": null,
                    "request_time": "2021-02-01 18:23:54",
                    "project": {
                        "idx": "1"
                    }
                }
            ]
        },
        "mytasktype_setting": {
            "task_statuses": [
                {
                    "idx": "1",
                    "name": "wip",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "2",
                    "name": "confirm",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "3",
                    "name": "retake",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "4",
                    "name": "pub",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "5",
                    "name": "final",
                    "include": [
                        "Done"
                    ]
                },
                {
                    "idx": "14",
                    "name": "A_tests",
                    "include": null
                },
                {
                    "idx": "15",
                    "name": "test1111333",
                    "include": [
                        "To-Do"
                    ]
                }
            ],
            "version_statuses": [
                {
                    "idx": "1",
                    "name": "wip",
                    "include": null
                },
                {
                    "idx": "2",
                    "name": "confirm",
                    "include": [
                        "To-Do",
                        "In-Progress"
                    ]
                },
                {
                    "idx": "3",
                    "name": "retake",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "4",
                    "name": "pub",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "5",
                    "name": "final",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "14",
                    "name": "A_tests",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "15",
                    "name": "test1111333",
                    "include": null
                }
            ]
        },
        "filters": {
            "my_version_filters": [
                {
                    "column": "4",
                    "operation": "conjunction",
                    "conditions": [
                        {
                            "name": "by_value",
                            "args": [
                                [
                                    "Concept",
                                    "Modeling"
                                ]
                            ]
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
                                    "confirm",
                                    "wip"
                                ]
                            ]
                        }
                    ]
                }
            ],
            "confirm_filters": [
                {
                    "column": "4",
                    "operation": "conjunction",
                    "conditions": [
                        {
                            "name": "by_value",
                            "args": [
                                [
                                    "Concept",
                                    "animation"
                                ]
                            ]
                        }
                    ]
                }
            ]
        }
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
|-------|:-----:|:-------:|:--------:|------|
| page  | query | integer |    X     | X    |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
        "task_shot_overview": {
            "tasks": [
                {
                    "idx": "8",
                    "kind": "shot",
                    "shot": {
                        "thumbnail": "http://localhost:81/2019/04/08/13f8004c570ac3c3.jpg",
                        "name": "s0010_c0050"
                    },
                    "project": {
                        "idx": "1",
                        "name": "Demo_Bigbuck_Bunny"
                    },
                    "episode": {
                        "name": "Ep01"
                    },
                    "sequence": {
                        "name": "s0010"
                    },
                    "name": "comp",
                    "start_date": "2020-10-15",
                    "end_date": null,
                    "description": "",
                    "status": {
                        "idx": "5",
                        "name": "final",
                        "list": [
                            "wip",
                            "confirm",
                            "retake",
                            "pub",
                            "final",
                            "A_tests"
                        ]
                    }
                }
            ]
        },
        "task_asset_overview": {
            "tasks": [
                {
                    "idx": "2",
                    "kind": "asset",
                    "asset": {
                        "idx": "1",
                        "name": "ch_bunny",
                        "used": "1111",
                        "thumbnail": "http://localhost:81/2021/02/01/2e08a9aecfbe920c.jpg"
                    },
                    "project": {
                        "name": "Demo_Bigbuck_Bunny",
                        "idx": "1"
                    },
                    "asset_category": {
                        "name": "char"
                    },
                    "name": "Modeling",
                    "start_date": "2021-01-05",
                    "end_date": null,
                    "description": "qqq",
                    "status": {
                        "idx": "5",
                        "name": "final"
                    }
                }
            ]
        },
        "mytasktype_setting": {
            "task_statuses": [
                {
                    "idx": "1",
                    "name": "wip",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "2",
                    "name": "confirm",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "3",
                    "name": "retake",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "4",
                    "name": "pub",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "5",
                    "name": "final",
                    "include": [
                        "Done"
                    ]
                },
                {
                    "idx": "14",
                    "name": "A_tests",
                    "include": null
                },
                {
                    "idx": "15",
                    "name": "test1111333",
                    "include": [
                        "To-Do"
                    ]
                }
            ],
            "version_statuses": [
                {
                    "idx": "1",
                    "name": "wip",
                    "include": null
                },
                {
                    "idx": "2",
                    "name": "confirm",
                    "include": [
                        "To-Do",
                        "In-Progress"
                    ]
                },
                {
                    "idx": "3",
                    "name": "retake",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "4",
                    "name": "pub",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "5",
                    "name": "final",
                    "include": [
                        "In-Progress"
                    ]
                },
                {
                    "idx": "14",
                    "name": "A_tests",
                    "include": [
                        "To-Do"
                    ]
                },
                {
                    "idx": "15",
                    "name": "test1111333",
                    "include": null
                }
            ]
        },
        "filters": {
            "shot_tasks_filters": null,
            "asset_tasks_filters": [
                {
                    "column": "5",
                    "operation": "conjunction",
                    "conditions": [
                        {
                            "name": "by_value",
                            "args": [
                                [
                                    "ch_bunny"
                                ]
                            ]
                        }
                    ]
                }
            ]
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
|-------|:----:|:------:|:--------:|----------|
| last  | path | string |    X     | 값: last |

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
                "idx": "2",
                "name": "big_s0010_c0020_anim_v001",
                "kind": "shot",
                "thumbnail": "http://localhost:81/2019/04/08/d45d311d6b86ae96.jpg",
                "shot_asset_name": "s0010_c0020",
                "task": {
                    "idx": "3",
                    "name": "animation",
                    "status": {
                        "idx": "14",
                        "name": "A_tests"
                    }
                },
                "status": {
                    "idx": "2",
                    "name": "confirm"
                },
                "comment": "Confirm",
                "artist": {
                    "user": {
                        "idx": "2",
                        "name": "Artist"
                    }
                },
                "reviewer": {
                    "user": {
                        "idx": "1",
                        "name": "C2Monster"
                    }
                },
                "last_comment": null,
                "last_comment_time": null,
                "request_time": "2019-04-08 17:32:03",
                "project": {
                    "idx": "1"
                }
            }
        ],
        "filters": {
            "version_filters": [
                {
                    "column": "7",
                    "operation": "conjunction",
                    "conditions": [
                        {
                            "name": "by_value",
                            "args": [
                                [
                                    "confirm"
                                ]
                            ]
                        }
                    ]
                }
            ]
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
|-------|:----:|:----:|:--------:|------|
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
|----------------|:-----:|:----------------:|:--------:|-------------------------------------|
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
