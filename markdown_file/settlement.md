# WH2API::Settlement

## 목차

| 내용                               | slug                                                    |    서버 구현     | 웹 적용 |
| :--------------------------------- | :------------------------------------------------------ | :--------------: | :-----: |
| 1. [프로젝트별 결산 프로젝트 리셋] | /api/settlement/per_project/project/{project_idx}/reset |       POST       |    O    |
| 2. [프로젝트별 결산 보기]          | /api/settlement/per_project/{yyyy}/{mm}/read            |       GET        |    X    |
| 3. [이용자 급여 수정]              | -                                                       | 참조<sup>1</sup> |    X    |
| 4. [이용자 업무일 수정]            | -                                                       | 참조<sup>2</sup> |    X    |
| 5. [하루 근무 시간 수정]           | -                                                       | 참조<sup>3</sup> |    X    |
| 5. [초과 근무 배수 수정]           | -                                                       | 참조<sup>4</sup> |    X    |

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
		"message": "Success"
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
}
```

---

## 끝

[프로젝트별 결산 프로젝트 리셋]: #settlement-per-project-reset
[프로젝트별 결산 보기]: #settlement-per-project-read
