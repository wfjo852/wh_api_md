# WH2API::Settlement

## 목차

| 내용                                  | slug                                                                               |    서버 구현     | 웹 적용 | 웹훅 | 로그 | 크론탭 |
| :------------------------------------ | :--------------------------------------------------------------------------------- | :--------------: | :-----: | :--: | :--: | ------ |
| 1. [프로젝트별 결산 프로젝트 리셋]    | /api/settlement/per_project/project/{project_idx}/reset                            |       POST       |    O    |  -   |  -   | -      |
| 2. [프로젝트별 결산 보기]             | /api/settlement/per_project/{yyyy}/{mm}/read                                       |       GET        |    X    |  -   |  -   | -      |
| 3. [이용자 급여 수정]                 | -                                                                                  | 참조<sup>1</sup> |    X    |  -   |  -   | -      |
| 4. [이용자 업무일 수정]               | -                                                                                  | 참조<sup>2</sup> |    X    |  -   |  -   | -      |
| 5. [하루 근무 시간 수정]              | -                                                                                  | 참조<sup>3</sup> |    X    |  -   |  -   | -      |
| 5. [초과 근무 배수 수정]              | -                                                                                  | 참조<sup>4</sup> |    X    |  -   |  -   | -      |
| 6. [정산 개요 목록 조회]              | /api/settlement/summary/read                                                       |       GET        |    O    |  -   |  -   | -      |
| 7. [프로젝트 정산 개요 조회]          | /api/settlement/project/{project_idx}/summary/read                                 |       GET        |    O    |  -   |  -   | -      |
| 8. [프로젝트 마일스톤 목록 조회]      | /api/settlement/project/{project_idx}/milestone/list                               |       GET        |    O    |  -   |  -   | -      |
| 9. [프로젝트 마일스톤 등록]           | /api/settlement/project/{project_idx}/milestone/create                             |       POST       |    O    |  -   |  -   | -      |
| 10. [프로젝트 마일스톤 수정]          | /api/settlement/project/{project_idx}/milestone/{milestone_idx}/update             |       POST       |    O    |  -   |  -   | -      |
| 11. [프로젝트 마일스톤 삭제]          | /api/settlement/project/{project_idx}/milestone/{milestone_idx}/delete             |       POST       |    O    |  -   |  -   | -      |
| 12. [프로젝트 예상 인원 목록 조회]    | /api/settlement/project/{project_idx}/estimated/user/list                          |       GET        |    O    |  -   |  -   | -      |
| 13. [프로젝트 예상 팀 목록 조회]      | /api/settlement/project/{project_idx}/estimated/team/list                          |       GET        |    O    |  -   |  -   | -      |
| 14. [프로젝트 예상 인원 등록]         | /api/settlement/project/{project_idx}/estimated/user/create                        |       POST       |    O    |  -   |  -   | -      |
| 15. [프로젝트 예상 인원 수정]         | /api/settlement/project/{project_idx}/estimated/user/{user_idx}/update             |       POST       |    O    |  -   |  -   | -      |
| 16. [프로젝트 예상 인원 삭제]         | /api/settlement/project/{project_idx}/estimated/user/{estimated_user_idx}/delete   |       POST       |    O    |  -   |  -   | -      |
| 17. [프로젝트 예상 금액 목록 조회]    | /api/settlement/project/{project_idx}/estimated/money/list                         |       GET        |    O    |  -   |  -   | -      |
| 18. [프로젝트 예상 금액 등록]         | /api/settlement/project/{project_idx}/estimated/money/create                       |       POST       |    O    |  -   |  -   | -      |
| 19. [프로젝트 예상 금액 수정]         | /api/settlement/project/{project_idx}/estimated/money/{money_idx}/update           |       POST       |    O    |  -   |  -   | -      |
| 20. [프로젝트 예상 금액 삭제]         | /api/settlement/project/{project_idx}/estimated/money/{estimated_money_idx}/delete |       POST       |    O    |  -   |  -   | -      |
| 21. [프로젝트 실제 인원 목록 조회]    | /api/settlement/project/{project_idx}/current/user/{yyyy}/{mm}/list                |       GET        |    O    |  -   |  -   | -      |
| 22. [프로젝트 실제 팀별 인건비 조회]  | /api/settlement/project/{project_idx}/current/team/costs/list                      |       GET        |    O    |  -   |  -   | -      |
| 23. [프로젝트 실제 금액 목록 조회]    | /api/settlement/project/{project_idx}/current/money/list                           |       GET        |    O    |  -   |  -   | -      |
| 24. [프로젝트 실제 금액 등록]         | /api/settlement/project/{project_idx}/current/money/create                         |       POST       |    O    |  -   |  -   | -      |
| 25. [프로젝트 실제 금액 수정]         | /api/settlement/project/{project_idx}/current/money/{money_idx}/update             |       POST       |    O    |  -   |  -   | -      |
| 26. [프로젝트 실제 금액 삭제]         | /api/settlement/project/{project_idx}/current/money/{current_money_idx}/delete     |       POST       |    O    |  -   |  -   | -      |
| 27. [프로젝트 워크로그 조회]          | /api/settlement/project/{project_idx}/log/{yyyy}/{mm}/list                         |       GET        |    O    |  -   |  -   | -      |
| 28. [프로젝트 워크로그 이용자별 보기] | /api/settlement/project/{project_idx}/log/user/{user_idx}/{yyyy}/{mm}/{dd}/read    |       GET        |    O    |  -   |  -   | -      |
| 32. [프로젝트 로그 오프셋 업데이트]   | /api/settlement/project/{project_idx}/log/offset/update                            |       POST       |    O    |  -   |  -   | -      |
| 33. [프로젝트별 유저 리스트]          | /api/settlement/summary/user/{yyyy}/{mm}/list                                      |       GET        |    O    |  -   |  -   | -      |
| 34. [일별 스냅샷 생성 (cron)]         | /api/settlement/cron/snapshot/daily/create                                         |       GET        |    X    |  -   |  -   | O      |

## 목차 V2

| 내용                          | slug                                             | 서버 구현 | 웹 적용 | 웹훅 | 로그 | 크론탭 |
| :---------------------------- | :----------------------------------------------- | :-------: | :-----: | :--: | :--: | ------ |
| A1. [워크로그 조회]           | /api/worklogs/read                               |    GET    |    O    |  -   |  -   | -      |
| A2. [워크로그 기타 업무 등록] | /api/worklogs/other_task/create                  |   POST    |    O    |  -   |  -   | -      |
| A3. [워크로그 기타 업무 수정] | /api/worklogs/other_task/{other_task_idx}/update |   POST    |    O    |  -   |  -   | -      |
| A4. [워크로그 기타 업무 삭제] | /api/worklogs/other_task/{other_task_idx}/delete |   POST    |    O    |  -   |  -   | -      |
| A5. [워크로그 목록 조회]      | /api/worklogs/list                               |    GET    |    X    |  -   |  -   | -      |

- 참조<sup>1</sup> - /api/user/{user_idx}/salary/update 이용 (user.md 21번 참조)
- 참조<sup>2</sup> - /api/user/{user_idx}/working_day/update 이용 (user.md 22번 참조)
- 참조<sup>3</sup> - /api/org/{org_id}/working_hours_per_day/update 이용 (org.md 6번 참조)
- 참조<sup>4</sup> - /api/org/{org_id}/overtime_multiple/update 이용 (org.md 7번 참조)

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 프로젝트별 결산 프로젝트 리셋 <a id="settlement-per-project-reset"></a>

### `POST /api/stats/settlement_per_project/project/{project_idx}/reset`

### permission

- `permission.do_global_setting`

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
  "data": null
}
```

---

## 2. 프로젝트별 결산 보기 <a id="settlement-per-project-read"></a>

### `GET /api/stats/settlement_per_project/{yyyy}/{mm}/read`

### permission

- `permission.do_global_setting`

### request

| param | type |  data  | required | desc        |
| ----- | :--: | :----: | :------: | ----------- |
| yyyy  | path | string |    O     | year (YYYY) |
| mm    | path | string |    O     | month (MM)  |

### response

```json
{
    "error": {
        "code": 200,
        "message": "성공"
    },
    "data": {
    "nested_headers" : [
        "User Idx",
        "User Name",
        "Salary",
        "시간 외 수당",
        "오늘까지 지급액",
        "실업무 비용",
        "월급 대비 작업량",
        "업무일",
        "project name 01",
        "project name 02",
        "project name 03",
        "project name 04",
        "project name 05",
        "project name 06",
        "누적 시간",
        "미확인 시간",
        "시간외 근무"
    ],
    "setting_column" : [
        {"data":"user_idx", "type":"numeric", "width":"50", "readOnly": true},
        {"data":"user_name", "type":"text", "width":"50", "editor": false, "readOnly": true, "renderer": "renderUserPhoto"},
        {"data":"salary", "type":"numeric", "width":"40", "readOnly": false, "renderer": "renderSalary"}},
        {"data":"overtime_allowance", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderOvertimeAllowance"},
        {"data":"monthly_pay_until_today", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderMonthlyPayUntilToday"},
        {"data":"monthly_pay_by_working", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderMonthlyPayByWorking"},
        {"data":"workload_by_salary", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderWorkloadBySalary"},
        {"data":"custom_working_days", "type":"numeric", "width":"40", "readOnly": false, "renderer": "renderCustomWorkingDays"},
        {"data":"project_name_01", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderFormat"},
        {"data":"project_name_02", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderFormat"},
        {"data":"project_name_03", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderFormat"},
        {"data":"project_name_04", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderFormat"},
        {"data":"project_name_05", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderFormat"},
        {"data":"project_name_06", "type":"numeric", "width":"40", "readOnly": true,"renderer": "renderFormat"},
        {"data":"working", "type":"numeric", "width":"40",  "readOnly": true,"renderer": "renderWorking"}, // 누적
        {"data":"unconfirmed", "type":"numeric", "width":"40", "readOnly": true, "renderer": "renderUnconfirmed"}, // 미확인
        {"data":"overtime", "type":"numeric", "width":"40", "readOnly": true, "renderer": "renderOvertime"}, // 시간외
    ],
    "settlements" : [
        {"user_idx":1, "user_thumbnail":"", "user_name":"User 01", "salary": 2600000, "overtime_allowance": 1, "monthly_pay_until_today":null, "monthly_pay_by_working":1, "workload_by_salary":1, "custom_working_days": null, "project_name_01": 0, "project_name_02": 20, "project_name_03": 20, "project_name_04": 15, "project_name_05": 15, "project_name_06": 14, "working": 0, "unconfirmed":0, "overtime":0},
        {"user_idx":2, "user_thumbnail":"", "user_name":"User 02", "salary": 2600000, "overtime_allowance": 1, "monthly_pay_until_today":null, "monthly_pay_by_working":1, "workload_by_salary":1,  "custom_working_days": null, "project_name_01": 0, "project_name_02": 20, "project_name_03": 40, "project_name_04": 10, "project_name_05": 10, "project_name_06": 0, "working": 0, "unconfirmed":0, "overtime":0}
    ],
    "base" : {
      "workdays": 22, // 현재 달의 총 업무일
      "settlement_start_date": "2019-10-01", // 정산 시작일
      "settlement_end_date": "2010-10-10", // 정산 종료일
      "working_hours_per_day": 8, // 하루 작업 시간
      "overtime_multiple": 0, // 오버 타임 배수
      "current_workdays": 10 // 현재 달의 총 업무일중(work_days) 몇번째 일 인지
    }
}
```

---

## 6. 정산 개요 목록 조회 <a id="settlement-summary-read"></a>

### `GET /api/settlement/summary/read`

### permission

- `permission.do_global_setting`

### request

| param | type | data | required | desc |
| ----- | :--: | :--: | :------: | ---- |
| x     |  x   |  x   |    x     | x    |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "project_costs_graph": {
      "dates": [
        "2020-02",
        "2020-03",
        "2020-04",
        "2020-05",
        "2020-06",
        "2020-07",
        "2020-08",
        "2020-09",
        "2020-10",
        "2020-11",
        "2020-12",
        "2021-01"
      ],
      "projects": [
        {
          "name": "test111",
          "costs": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        },
        {
          "name": "Demo_Bigbuck_Bunny",
          "costs": [0, 0, 0, 0, 0, 0, 0, 0, 0, -5000, 1231, -23444]
        }
      ]
    },
    "project_hours_graph": {
      "dates": [
        "2020-02",
        "2020-03",
        "2020-04",
        "2020-05",
        "2020-06",
        "2020-07",
        "2020-08",
        "2020-09",
        "2020-10",
        "2020-11",
        "2020-12",
        "2021-01"
      ],
      "projects": [
        {
          "name": "test111",
          "hours": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        },
        {
          "name": "Demo_Bigbuck_Bunny",
          "hours": [0, 0, 0, 0, 0, 0, 0, 0, 0, 88, 144, 0]
        }
      ]
    },
    "projects": [
      {
        "idx": "9",
        "name": "test111",
        "start_date": "2020-12-08",
        "end_date": "2020-12-31",
        "progresses": {
          "shot_progress": 0,
          "asset_progress": 0
        },
        "total_cost": 0,
        "hour_spent": 0,
        "work_days": 29
      },
      {
        "idx": "1",
        "name": "Demo_Bigbuck_Bunny",
        "start_date": "2018-12-11",
        "end_date": "2019-04-12",
        "progresses": {
          "shot_progress": 24.97,
          "asset_progress": 24.92
        },
        "total_cost": -27213,
        "hour_spent": "273",
        "work_days": 757
      }
    ]
  }
}
```

---

## 7. 프로젝트 정산 개요 조회 <a id="settlement-project-summary"></a>

### `GET /api/settlement/project/{project_idx}/summary`

### permission

- `permission.do_global_setting`

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
    "summary": {
      "shot": {
        "episode": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        },
        "sequence": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        },
        "shot": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        },
        "frame": {
          "total": 2843,
          "waiting": 285,
          "done": 2558
        },
        "task": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        }
      },
      "asset": {
        "asset_category": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        },
        "asset": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        },
        "task": {
          "count": 6,
          "waiting": 3,
          "in_progress": 1,
          "done": 5
        }
      }
    }
  }
}
```

---

## 8. 프로젝트 마일스톤 목록 조회 <a id="settlement-project-milestone-list"></a>

### `GET /api/settlement/project/{project_idx}/milestone/list`

### permission

- `permission.do_global_setting`

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
    "milestones": [
      {
        "idx": "0",
        "date": "2021-02-01",
        "description": "프로젝트 시작",
        "progress": "0"
      },
      {
        "idx": "7",
        "date": "2021-02-17",
        "description": "10%",
        "progress": "10"
      },
      {
        "idx": "0",
        "date": "2022-07-30",
        "description": "프로젝트 종료",
        "progress": "100"
      }
    ],
    "milestones_graph": {
      "dates": [
        "2021-02-01",
        "2021-02-17",
        "2021-02-22",
        "2021-03-05",
        "2021-03-15",
        "2021-03-25",
        "2021-04-06",
        "2021-04-18",
        "2021-04-28",
        "2021-05-09",
        "2021-05-19",
        "2021-05-30",
        "2021-06-10",
        "2021-06-20",
        "2021-07-03",
        "2021-07-13",
        "2021-07-23",
        "2021-08-04",
        "2021-08-14",
        "2021-08-25",
        "2021-09-05",
        "2021-09-15",
        "2021-09-27",
        "2021-10-08",
        "2021-10-19",
        "2021-10-30",
        "2021-11-09",
        "2021-11-19",
        "2021-12-01",
        "2021-12-12",
        "2021-12-22",
        "2022-01-03",
        "2022-01-14",
        "2022-01-24",
        "2022-02-07",
        "2022-02-17",
        "2022-02-27",
        "2022-03-10",
        "2022-03-21",
        "2022-04-03",
        "2022-04-13",
        "2022-04-25",
        "2022-05-06",
        "2022-05-16",
        "2022-05-26",
        "2022-06-06",
        "2022-06-16",
        "2022-06-28",
        "2022-07-09",
        "2022-07-19",
        "2022-07-30"
      ],
      "progresses": {
        "estimated_progresses": [
          0, 10, 10.85, 12.73, 14.43, 16.14, 18.18, 20.23, 21.93, 23.81, 25.51,
          27.39, 29.26, 30.97, 33.18, 34.89, 36.59, 38.64, 40.34, 42.22, 44.09,
          45.8, 47.84, 49.72, 51.59, 53.47, 55.17, 56.88, 58.92, 60.8, 62.5,
          64.55, 66.42, 68.13, 70.51, 72.22, 73.92, 75.8, 77.67, 79.89, 81.59,
          83.64, 85.51, 87.22, 88.92, 90.8, 92.5, 94.55, 96.42, 98.13, 100
        ],
        "current_progresses": {
          "project_progresses": [
            2.41, 2.41, 5.24, 6.72, 9.22, 10.91, 12.41, 14.1, 15.59, 17.25,
            18.94, 21.1, 22.79, 24.13, 26.15, 27.42, 28.83, 30.14, 30.87, 32.93,
            34.63, 36.76, 39.03, 41.13, 42.76, 45.11, 46.67, 47.79, 48.91,
            50.24, 52.01, 53.77, 55.35, 57.21, 61.27, 64.05, 65.64, 66.97,
            68.91, 71.35, 73.43, 74.16, 75.61, 76.13, 77.7, 79.54, 81.35, 82.69,
            84.31, 86.31, 87.37
          ],
          "project_workload_progresses": [
            3.35, 3.35, 7.09, 8.38, 9.2, 10.94, 12.62, 14.1, 15.48, 16.67,
            17.75, 18.8, 20.19, 21.71, 24.03, 25.9, 28.14, 30.6, 32.06, 33.37,
            34.64, 36.55, 38.5, 40.8, 42.42, 43.57, 45.22, 45.96, 48.62, 49.63,
            51.24, 52.88, 54.61, 56.4, 59.18, 60.99, 62.35, 65.43, 67.39, 68.72,
            70.74, 73.46, 75.49, 76.79, 79.05, 80.15, 81.01, 82.12, 83.59,
            84.69, 85.63
          ]
        }
      }
    }
  }
}
```

---

## 9. 프로젝트 마일스톤 등록 <a id="settlement-project-milestone-create"></a>

### `POST /api/settlement/project/{project_idx}/milestone/create`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc       |
| ----------- | :---: | :-----: | :------: | ---------- |
| project_idx | path  | integer |    O     |            |
| date        | query |  date   |    O     | YYYY-MM-DD |
| description | query | string  |    O     |            |
| progress    | query | integer |    O     | 0 ~ 100    |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "milestone": {
      "idx": 7
    }
  }
}
```

---

## 10. 프로젝트 마일스톤 수정 <a id="settlement-project-milestone-update"></a>

### `POST /api/settlement/project/{project_idx}/milestone/{milestone_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param         | type  |  data   | required | desc       |
| ------------- | :---: | :-----: | :------: | ---------- |
| project_idx   | path  | integer |    O     |            |
| milestone_idx | path  | integer |    O     |            |
| date          | query |  date   |    O     | YYYY-MM-DD |
| description   | query | string  |    O     |            |
| progress      | query | integer |    O     | 0 ~ 100    |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "milestone": {
      "idx": 1
    }
  }
}
```

---

## 11. 프로젝트 마일스톤 삭제 <a id="settlement-project-milestone-delete"></a>

### `POST /api/settlement/project/{project_idx}/milestone/{milestone_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param         | type |  data   | required | desc |
| ------------- | :--: | :-----: | :------: | ---- |
| project_idx   | path | integer |    O     |      |
| milestone_idx | path | integer |    O     |      |

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

## 12. 프로젝트 예상 인원 목록 조회 <a id="settlement-project-estimated-user-list"></a>

### `GET /api/settlement/project/{project_idx}/estimated/user/list`

### permission

- `permission.do_global_setting`

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
    "estimated_users": [
      {
        "idx": "9",
        "team": "디자인팀",
        "role": "팀장",
        "count": "2",
        "average_salary": "400",
        "participation_rate": "100",
        "start_date": "2020-12-16",
        "end_date": "2021-01-14"
      }
    ],
    "estimated_salary_graph": {
      "dates": ["2020-12", "2021-01"],
      "teams": [
        {
          "name": "디자인팀",
          "salary": [413, 362]
        }
      ]
    }
  }
}
```

---

## 13. 프로젝트 예상 팀 목록 조회 <a id="settlement-project-estimated-team-list"></a>

### `GET /api/settlement/project/{project_idx}/estimated/team/list`

### permission

- `permission.do_global_setting`

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
    "teams": ["개발팀", "디자인팀"]
  }
}
```

---

## 14. 프로젝트 예상 인원 등록 <a id="settlement-project-estimated-user-create"></a>

### `POST /api/settlement/project/{project_idx}/estimated/user/create`

### permission

- `permission.do_global_setting`

### request

| param              | type  |  data   | required | desc             |
| ------------------ | :---: | :-----: | :------: | ---------------- |
| project_idx        | path  | integer |    O     |                  |
| team               | query | string  |    O     | 팀명             |
| name               | query | string  |    O     | 이름 (혹은 역할) |
| count              | query | integer |    O     | 인원 수          |
| average_salary     | query | integer |    O     |                  |
| participation_rate | query | integer |    O     | 0 ~ 100          |
| start_date         | query |  date   |    O     | YYYY-MM-DD       |
| end_date           | query |  date   |    O     | YYYY-MM-DD       |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "estimated_user": {
      "idx": 7
    }
  }
}
```

---

## 15. 프로젝트 예상 인원 수정 <a id="settlement-project-estimated-user-update"></a>

### `POST /api/settlement/project/{project_idx}/estimated/user/{user_idx}/update`

### permission

- `permission.do_global_setting`

### request

| param              | type  |  data   | required | desc             |
| ------------------ | :---: | :-----: | :------: | ---------------- |
| project_idx        | path  | integer |    O     |                  |
| user_idx           | path  | integer |    O     |                  |
| team               | query | string  |    O     | 팀명             |
| name               | query | string  |    O     | 이름 (혹은 역할) |
| count              | query | integer |    O     | 인원 수          |
| average_salary     | query | integer |    O     |                  |
| participation_rate | query | integer |    O     | 0 ~ 100          |
| start_date         | query |  date   |    O     | YYYY-MM-DD       |
| end_date           | query |  date   |    O     | YYYY-MM-DD       |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "estimated_user": {
      "idx": 1
    }
  }
}
```

---

## 16. 프로젝트 예상 인원 삭제 <a id="settlement-project-estimated-user-delete"></a>

### `POST /api/settlement/project/{project_idx}/estimated/user/{estimated_user_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param              | type |  data   | required | desc |
| ------------------ | :--: | :-----: | :------: | ---- |
| project_idx        | path | integer |    O     |      |
| estimated_user_idx | path | integer |    O     |      |

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

## 17. 프로젝트 예상 금액 목록 조회 <a id="settlement-project-estimated-money-list"></a>

### `GET /api/settlement/project/{project_idx}/estimated/money/list`

### permission

- `permission.do_global_setting`

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
    "estimated_money": [
      {
        "idx": "1",
        "which": "D",
        "date": "2020-10-10",
        "amount": "1,100,000",
        "description": "OOOO 입금"
      },
      {
        "idx": "1",
        "which": "W",
        "date": "2020-10-15",
        "amount": "300,000",
        "description": "XXX 출금"
      }
    ]
  }
}
```

---

## 18. 프로젝트 예상 금액 등록 <a id="settlement-project-estimated-money-create"></a>

### `POST /api/settlement/project/{project_idx}/estimated/money/create`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc                |
| ----------- | :---: | :-----: | :------: | ------------------- |
| project_idx | path  | integer |    O     |                     |
| which       | query | string  |    O     | D (입금) / W (출금) |
| date        | query |  date   |    O     | YYYY-MM-DD          |
| amount      | query | integer |    O     |                     |
| description | query | string  |    O     |                     |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "estimated_money": {
      "idx": 7
    }
  }
}
```

---

## 19. 프로젝트 예상 금액 수정 <a id="settlement-project-estimated-money-update"></a>

### `POST /api/settlement/project/{project_idx}/estimated/money/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc                |
| ----------- | :---: | :-----: | :------: | ------------------- |
| project_idx | path  | integer |    O     |                     |
| money_idx   | path  | integer |    O     |                     |
| which       | query | string  |    O     | D (입금) / W (출금) |
| date        | query |  date   |    O     | YYYY-MM-DD          |
| amount      | query | integer |    O     |                     |
| description | query | string  |    O     |                     |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "estimated_money": {
      "idx": 1
    }
  }
}
```

## 20. 프로젝트 예상 금액 등록 삭제 <a id="settlement-project-estimated-money-delete"></a>

### `POST /api/settlement/project/{project_idx}/estimated/money/{estimated_money_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param               | type |  data   | required | desc |
| ------------------- | :--: | :-----: | :------: | ---- |
| project_idx         | path | integer |    O     |      |
| estimated_money_idx | path | integer |    O     |      |

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

## 21. 프로젝트 실제 인원 목록 조회 <a id="settlement-project-current-user-list"></a>

### `GET /api/settlement/project/{project_idx}/current/user/{yyyy}/{mm}/list`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| yyyy        | path | integer |    O     | YYYY |
| nn          | path | integer |    O     | MM   |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "current_users": [
      {
        "idx": "1",
        "name": "C2Monster",
        "user_role": "Administrator",
        "amount": null,
        "teams": [
          {
            "idx": "2",
            "name": "test_team"
          }
        ],
        "participation_rate": 0,
        "hour_spent": {
          "project": 0,
          "all": 0
        },
        "current_amount": 0
      },
      {
        "idx": "2",
        "name": "Artist",
        "user_role": "Artist",
        "amount": null,
        "teams": null,
        "participation_rate": 0,
        "hour_spent": {
          "project": 0,
          "all": 0
        },
        "current_amount": 0
      },
      {
        "idx": "4",
        "name": "Supervisor",
        "user_role": "Main Supervisor",
        "amount": null,
        "teams": null,
        "participation_rate": 0,
        "hour_spent": {
          "project": 0,
          "all": 0
        },
        "current_amount": 0
      }
    ],
    "current_amount_graph": {
      "dates": ["2019-04", "2020-12"],
      "users": [
        {
          "name": "C2Monster",
          "amounts": [3000000, 924732]
        },
        {
          "name": "Artist",
          "amounts": [2000000, 0]
        },
        {
          "name": "Supervisor",
          "amounts": [0, 0]
        }
      ]
    }
  }
}
```

---

## 22. 프로젝트 실제 팀별 인건비 조회 <a id="settlement-project-current-team-costs-list"></a>

### `GET /api/settlement/project/{project_idx}/current/team/costs/list`

### permission

- `permission.do_global_setting`

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
    "current_amount_graph": {
      "dates": [
        "2020-12",
        "2021-01",
        "2021-02",
        "2021-03",
        "2021-04",
        "2021-05"
      ],
      "teams": [
        {
          "name": "W_Concept Art",
          "amounts": [0, 0, 0, 0, 0, 0]
        },
        {
          "name": "W_Planning",
          "amounts": [0, 0, 0, 0, 0, 0]
        },
        {
          "name": "무소속",
          "amounts": [0, 0, 0, 0, 0, 0]
        }
      ]
    }
  }
}
```

---

## 23. 프로젝트 실제 금액 목록 조회 <a id="settlement-project-current-money-list"></a>

### `GET /api/settlement/project/{project_idx}/current/money/list`

### permission

- `permission.do_global_setting`

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
    "current_monies": [
      {
        "idx": 0,
        "date": "2019-04-30",
        "amount": 5000000,
        "memo": "2019년 04월 인건비",
        "which": "W"
      },
      {
        "idx": 0,
        "date": "2020-12-31",
        "amount": 924732,
        "memo": "2020년 12월 인건비",
        "which": "W"
      }
    ]
  }
}
```

---

## 24. 프로젝트 실제 금액 등록 <a id="settlement-project-current-money-create"></a>

### `POST /api/settlement/project/{project_idx}/current/money/create`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc                |
| ----------- | :---: | :-----: | :------: | ------------------- |
| project_idx | path  | integer |    O     |                     |
| which       | query | string  |    O     | D (입금) / W (출금) |
| date        | query |  date   |    O     | YYYY-MM-DD          |
| amount      | query | integer |    O     |                     |
| description | query | string  |    O     |                     |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "current_money": {
      "idx": 7
    }
  }
}
```

---

## 25. 프로젝트 실제 금액 수정 <a id="settlement-project-current-money-update"></a>

### `POST /api/settlement/project/{project_idx}/current/money/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc                |
| ----------- | :---: | :-----: | :------: | ------------------- |
| project_idx | path  | integer |    O     |                     |
| money_idx   | path  | integer |    O     |                     |
| which       | query | string  |    O     | D (입금) / W (출금) |
| date        | query |  date   |    O     | YYYY-MM-DD          |
| amount      | query | integer |    O     |                     |
| description | query | string  |    O     |                     |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "current_money": {
      "idx": 1
    }
  }
}
```

## 26. 프로젝트 실제 금액 등록 삭제 <a id="settlement-project-current-money-delete"></a>

### `POST /api/settlement/project/{project_idx}/current/money/{current_money_idx}/delete`

### permission

- `permission.do_global_setting`

### request

| param             | type |  data   | required | desc |
| ----------------- | :--: | :-----: | :------: | ---- |
| project_idx       | path | integer |    O     |      |
| current_money_idx | path | integer |    O     |      |

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

## 27. 프로젝트 워크로그 조회 <a id="settlement-project-log-list"></a>

### `GET /api/settlement/project/{project_idx}/log/{yyyy}/{mm}/list`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| yyyy        | path | integer |    O     |      |
| mm          | path | string  |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "logs": {
      "YYYY": 2019,
      "mm": "04",
      "logs": [
        {
          "user": {
            "idx": "1",
            "name": "C2Monster",
            "role": "Administrator"
          },
          "teams": [
            {
              "idx": "2",
              "name": "test_team"
            }
          ],
          "total": 23,
          "offset": 0,
          "times": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 4.5,
            "9": 18.5,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
            "14": 0,
            "15": 0,
            "16": 0,
            "17": 0,
            "18": 0,
            "19": 0,
            "20": 0,
            "21": 0,
            "22": 0,
            "23": 0,
            "24": 0,
            "25": 0,
            "26": 0,
            "27": 0,
            "28": 0,
            "29": 0,
            "30": 0
          }
        },
        {
          "user": {
            "idx": "2",
            "name": "Artist",
            "role": "Artist"
          },
          "teams": [
            {
              "idx": "2",
              "name": "test_team"
            }
          ],
          "total": 18,
          "offset": 0,
          "times": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 18,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
            "14": 0,
            "15": 0,
            "16": 0,
            "17": 0,
            "18": 0,
            "19": 0,
            "20": 0,
            "21": 0,
            "22": 0,
            "23": 0,
            "24": 0,
            "25": 0,
            "26": 0,
            "27": 0,
            "28": 0,
            "29": 0,
            "30": 0
          }
        }
      ]
    }
  }
}
```

---

## 28. 프로젝트 워크로그 이용자별 보기 <a id="settlement-project-log-read"></a>

### `GET /api/settlement/project/{project_idx}/log/user/{user_idx}/{yyyy}/{mm}/{dd}/read`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc |
| ----------- | :--: | :-----: | :------: | ---- |
| project_idx | path | integer |    O     |      |
| user_idx    | path | integer |    O     |      |
| yyyy        | path | integer |    O     |      |
| mm          | path | string  |    O     |      |
| dd          | path | string  |    O     |      |

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
        "idx": "66",
        "name": "s0010-s0010_c0010-comp",
        "hour_spent": "9",
        "project": {
          "name": "Demo_Bigbuck_Bunny"
        },
        "shot_asset": {
          "name": "s0010_c0010"
        },
        "task": {
          "name": "comp"
        }
      },
      {
        "idx": "67",
        "name": "s0010-s0010_c0010-comp",
        "hour_spent": "9",
        "project": {
          "name": "Demo_Bigbuck_Bunny"
        },
        "shot_asset": {
          "name": "s0010_c0010"
        },
        "task": {
          "name": "Animation"
        }
      }
    ],
    "other_tasks": [
      {
        "idx": "135",
        "name": "test",
        "hour_spent": "3"
      }
    ]
  }
}
```

---

## 32. 프로젝트 로그 오프셋 업데이트 <a id="settlement-project-offset-update"></a>

### `POST /api/settlement/project/{project_idx}/log/offset/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | path  | integer |    O     |      |
| user_idx    | query | integer |    O     |      |
| yyyy        | query | integer |    O     |      |
| mm          | query | string  |    O     |      |
| hour_spent  | query |  float  |    O     |      |

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

## 33. 프로젝트별 유저 리스트 <a id="settlement-summary-user-list"></a>

### `GET /api/settlement/summary/user/{yyyy}/{mm}/list`

### permission

- `permission.do_global_setting`

### request

| param | type |  data   | required | desc |
| ----- | :--: | :-----: | :------: | ---- |
| yyyy  | path | integer |    O     |      |
| mm    | path | string  |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "users": [
      {
        "idx": "1",
        "name": "C2Monster",
        "user_role": "Administrator",
        "teams": [
          {
            "idx": "2",
            "name": "c2monster"
          }
        ],
        "salary": 300000,
        "working_hours": 23,
        "unconfirmed_hours": 145,
        "overtime_hours": 0
      },
      {
        "idx": "2",
        "name": "Artist",
        "user_role": "Artist",
        "teams": [
          {
            "idx": "3",
            "name": "vasline"
          }
        ],
        "salary": 150000,
        "working_hours": 18,
        "unconfirmed_hours": 150,
        "overtime_hours": 0
      },
      {
        "idx": "4",
        "name": "Supervisor",
        "user_role": "Main Supervisor",
        "teams": null,
        "salary": 0,
        "working_hours": 0,
        "unconfirmed_hours": 168,
        "overtime_hours": 0
      }
    ]
  }
}
```

---

## 34. 일별 스냅샷 생성 (cron) <a id="settlement-cron-snapshot-daily-create"></a>

### `GET /api/settlement/cron/snapshot/daily/create`

### permission

- `permission.do_global_setting`

### request

| param | type  |  data  | required | desc                                        |
| ----- | :---: | :----: | :------: | ------------------------------------------- |
| date  | query | string |    X     | 특정 날짜의 스냅샷을 다시 찍고 싶을 때 입력 |

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

## A1. 워크로그 조회 <a id="worklog-read"></a>

### `GET /api/worklogs/read`

### permission

- all

### request

| param    | type  |  data   | required | desc            |
| -------- | :---: | :-----: | :------: | --------------- |
| date     | query | string  |    O     | YYYY-MM-DD      |
| user_idx | query | integer |    X     | 안 보내면 자신Ï |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "report": {
      "total_hour_spent": 4.5,
      "versions": [
        {
          "idx": "3",
          "name": "big_s0020_c0010_anim_v001",
          "description": "Confirm Detail_animation Check",
          "hour_spent": "1.5",
          "is_on": "1",
          "thumbnail": "/assets/images/thumbnail/task/default.light.svg",
          "kind": "shot",
          "project": {
            "idx": "1",
            "name": "Demo_Bigbuck_Bunny",
            "description": "Demo_Bigbuck_Bunny",
            "is_on": "1",
            "start_date": "2018-12-11",
            "end_date": "2019-04-12"
          },
          "episode": {
            "idx": "1",
            "name": "Ep01",
            "description": "Demo_Bigbuck_Bunny_First",
            "is_on": "1",
            "order": "1"
          },
          "sequence": {
            "idx": "2",
            "name": "s0020",
            "description": "Fighting in the Jungle",
            "is_on": "1",
            "sequence_order": "2",
            "order": "2"
          },
          "shot": {
            "idx": "11",
            "name": "s0020_c0010",
            "is_on": "1",
            "thumbnail": "http://localhost:81/2019/04/08/47d3b3bab83a31d9.jpg",
            "order": "11"
          },
          "task": {
            "idx": "21",
            "is_on": "1",
            "description": "Detail Animation",
            "duration": "3",
            "start_date": "2019-04-08",
            "end_date": "2019-04-11"
          },
          "tasktype": {
            "idx": "21",
            "name": "Ani",
            "description": "for Animation",
            "is_on": "1",
            "pos": "1",
            "color": "#ff0033",
            "kind": "shot"
          },
          "status": {
            "idx": "4",
            "name": "pub",
            "description": "다음 담당으로 이관",
            "is_on": "1",
            "pos": "7",
            "color": "#00bcd4",
            "progress": "90"
          },
          "user": {
            "idx": "1",
            "name": "C2Monster",
            "is_on": "1",
            "id": "c2m",
            "email": "contact@c2monster.com",
            "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
          },
          "main_reviewer": null,
          "cc_reviewers": [
            {
              "idx": "2",
              "name": "Artist_test",
              "id": "c3m",
              "email": "artist@c2monster.com",
              "thumbnail": "http://localhost:81/2019/04/08/dc3295a0a38e89e9.png"
            }
          ]
        }
      ],
      "other_tasks": [
        {
          "idx": "4",
          "user": {
            "idx": "1",
            "name": "C2Monster",
            "is_on": "1",
            "id": "c2m",
            "email": "contact@c2monster.com",
            "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png"
          },
          "project": {
            "idx": "1",
            "name": "Demo_Bigbuck_Bunny",
            "description": "Demo_Bigbuck_Bunny",
            "is_on": "1",
            "start_date": "2018-12-11",
            "end_date": "2019-04-12"
          },
          "name": "K-D 외근",
          "hour_spent": "3",
          "created_time": "2022-02-18"
        }
      ]
    }
  }
}
```

---

## A2. 워크로그 기타 업무 등록 <a id="worklog-other-task-create"></a>

### `POST /api/worklogs/other_task/create`

### permission

- all

### request

| param           | type  |  data   | required | desc                                                  |
| --------------- | :---: | :-----: | :------: | ----------------------------------------------------- |
| project_idx     | query | integer |    O     |                                                       |
| user_idx        | query | integer |    X     | 본인이 아닌 경우 (관리자가 다른 이용자를 입력할 경우) |
| other_task_name | query | string  |    O     |                                                       |
| hour_spent      | query |  float  |    O     |                                                       |
| date            | query | string  |    O     | YYYY-MM-DD                                            |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "idx": 1
  }
}
```

---

## A3. 워크로그 기타 업무 수정 <a id="worklog-other-task-update"></a>

### `POST /api/worklogs/other_task/{other_task_idx}/update`

### permission

- all

### request

| param          | type  |       data        | required | desc                              |
| -------------- | :---: | :---------------: | :------: | --------------------------------- |
| other_task_idx | path  |      integer      |    O     |                                   |
| column         | query |      string       |    O     | name OR hour_spent OR project_idx |
| old_val        | query | string OR integer |    O     |                                   |
| new_val        | query | string OR integer |    O     |                                   |

### response

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "idx": 1
  }
}
```

---

## A4. 워크로그 기타 업무 삭제 <a id="worklog-other-task-delete"></a>

### `POST /api/worklogs/other_task/{other_task_idx}/delete`

### permission

- all

### request

| param          | type |  data   | required | desc |
| -------------- | :--: | :-----: | :------: | ---- |
| other_task_idx | path | integer |    O     |      |

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

## A5. 워크로그 목록 조회 <a id="worklog-list"></a>

### `GET /api/worklogs/list`

### permission

- `permission.do_global_setting`

### request

| param       | type |  data   | required | desc     |
| ----------- | :--: | :-----: | :------: | -------- |
| yyyy        | path | integer |    O     | 연도     |
| mm          | path | integer |    O     | 월Ï      |
| project_idx | path | integer |    X     | 프로젝트 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "Success"
  },
  "data": {
    "users": [
      {
        "idx": "1",
        "name": "C2Monster",
        "is_on": "1",
        "id": "c2m",
        "email": "contact@c2monster.com",
        "thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png",
        "worklogs": {
          "2022-04-01": 0,
          "2022-04-02": 3,
          "2022-04-03": 42,
          "2022-04-04": 0,
          "2022-04-05": 0,
          "2022-04-06": 0,
          "2022-04-07": 0,
          "2022-04-08": 0,
          "2022-04-09": 0,
          "2022-04-10": 0,
          "2022-04-11": 3,
          "2022-04-12": 3,
          "2022-04-13": 3,
          "2022-04-14": 3,
          "2022-04-15": 0,
          "2022-04-16": 0,
          "2022-04-17": 0,
          "2022-04-18": 0,
          "2022-04-19": 0,
          "2022-04-20": 0,
          "2022-04-21": 0,
          "2022-04-22": 0,
          "2022-04-23": 0,
          "2022-04-24": 0,
          "2022-04-25": 0,
          "2022-04-26": 0,
          "2022-04-27": 0,
          "2022-04-28": 0,
          "2022-04-29": 0,
          "2022-04-30": 0
        }
      },
      {
        "idx": "2",
        "name": "Artist",
        "is_on": "1",
        "id": "c3m",
        "email": "artist@c2monster.com",
        "thumbnail": "http://localhost:81/2019/04/08/dc3295a0a38e89e9.png",
        "worklogs": {
          "2022-04-01": 0,
          "2022-04-02": 0,
          "2022-04-03": 0,
          "2022-04-04": 3,
          "2022-04-05": 3,
          "2022-04-06": 0,
          "2022-04-07": 0,
          "2022-04-08": 3,
          "2022-04-09": 0,
          "2022-04-10": 0,
          "2022-04-11": 0,
          "2022-04-12": 0,
          "2022-04-13": 0,
          "2022-04-14": 0,
          "2022-04-15": 0,
          "2022-04-16": 0,
          "2022-04-17": 0,
          "2022-04-18": 0,
          "2022-04-19": 0,
          "2022-04-20": 0,
          "2022-04-21": 0,
          "2022-04-22": 0,
          "2022-04-23": 0,
          "2022-04-24": 0,
          "2022-04-25": 0,
          "2022-04-26": 0,
          "2022-04-27": 0,
          "2022-04-28": 0,
          "2022-04-29": 0,
          "2022-04-30": 0
        }
      },
      {
        "idx": "3",
        "name": "Spito",
        "is_on": "1",
        "id": "spito",
        "email": "spito@example.com",
        "thumbnail": "/assets/images/thumbnail/user/small/default.png",
        "worklogs": {
          "2022-04-01": 0,
          "2022-04-02": 0,
          "2022-04-03": 3,
          "2022-04-04": 0,
          "2022-04-05": 0,
          "2022-04-06": 0,
          "2022-04-07": 0,
          "2022-04-08": 0,
          "2022-04-09": 0,
          "2022-04-10": 0,
          "2022-04-11": 0,
          "2022-04-12": 0,
          "2022-04-13": 0,
          "2022-04-14": 0,
          "2022-04-15": 0,
          "2022-04-16": 0,
          "2022-04-17": 0,
          "2022-04-18": 0,
          "2022-04-19": 0,
          "2022-04-20": 0,
          "2022-04-21": 0,
          "2022-04-22": 0,
          "2022-04-23": 0,
          "2022-04-24": 0,
          "2022-04-25": 0,
          "2022-04-26": 0,
          "2022-04-27": 0,
          "2022-04-28": 0,
          "2022-04-29": 0,
          "2022-04-30": 0
        }
      },
      {
        "idx": "4",
        "name": "Supervisor",
        "is_on": "1",
        "id": "c4m",
        "email": "",
        "thumbnail": "http://localhost:81/2019/04/08/d63b00a6934f6b55.png",
        "worklogs": {
          "2022-04-01": 0,
          "2022-04-02": 0,
          "2022-04-03": 3,
          "2022-04-04": 0,
          "2022-04-05": 0,
          "2022-04-06": 0,
          "2022-04-07": 0,
          "2022-04-08": 0,
          "2022-04-09": 0,
          "2022-04-10": 0,
          "2022-04-11": 0,
          "2022-04-12": 0,
          "2022-04-13": 0,
          "2022-04-14": 0,
          "2022-04-15": 0,
          "2022-04-16": 0,
          "2022-04-17": 0,
          "2022-04-18": 0,
          "2022-04-19": 0,
          "2022-04-20": 0,
          "2022-04-21": 0,
          "2022-04-22": 0,
          "2022-04-23": 0,
          "2022-04-24": 0,
          "2022-04-25": 0,
          "2022-04-26": 0,
          "2022-04-27": 0,
          "2022-04-28": 0,
          "2022-04-29": 0,
          "2022-04-30": 0
        }
      }
    ]
  }
}
```

---

## 끝

[프로젝트별 결산 프로젝트 리셋]: #settlement-per-project-reset
[프로젝트별 결산 보기]: #settlement-per-project-read
[정산 개요 목록 조회]: #settlement-summary
[프로젝트 정산 개요 조회]: #settlement-project-summary
[프로젝트 마일스톤 목록 조회]: #settlement-project-milestone-list
[프로젝트 마일스톤 등록]: #settlement-project-milestone-create
[프로젝트 마일스톤 수정]: #settlement-project-milestone-update
[프로젝트 마일스톤 삭제]: #settlement-project-milestone-delete
[프로젝트 예상 인원 목록 조회]: #settlement-project-estimated-user-list
[프로젝트 예상 인원 등록]: #settlement-project-estimated-user-create
[프로젝트 예상 인원 수정]: #settlement-project-estimated-user-update
[프로젝트 예상 인원 삭제]: #settlement-project-estimated-user-delete
[프로젝트 예상 금액 목록 조회]: #settlement-project-estimated-money-list
[프로젝트 예상 금액 등록]: #settlement-project-estimated-money-create
[프로젝트 예상 금액 수정]: #settlement-project-estimated-money-update
[프로젝트 예상 금액 삭제]: #settlement-project-estimated-money-delete
[프로젝트 실제 인원 목록 조회]: #settlement-project-current-user-list
[프로젝트 실제 팀별 인건비 조회]: #settlement-project-current-team-costs-list
[프로젝트 실제 금액 목록 조회]: #settlement-project-current-money-list
[프로젝트 실제 금액 등록]: #settlement-project-current-money-create
[프로젝트 실제 금액 수정]: #settlement-project-current-money-update
[프로젝트 실제 금액 삭제]: #settlement-project-current-money-delete
[프로젝트 워크로그 조회]: #settlement-project-log-list
[프로젝트 워크로그 이용자별 보기]: #settlement-project-log-read
[프로젝트 로그 일괄 추가]: #settlement-project-work-time-create
[프로젝트 로그 일괄 삭제]: #settlement-project-work-time-delete
[워크로그 조회]: #worklog-read
[워크로그 기타 업무 등록]: #worklog-other-task-create
[워크로그 기타 업무 수정]: #worklog-other-task-update
[워크로그 기타 업무 삭제]: #worklog-other-task-delete
[워크로그 목록 조회]: #worklog-list
