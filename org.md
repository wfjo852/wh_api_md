# WH2API::Org

## 목차

| 내용                     | slug                                           | 서버 구현 | 웹 적용 |
| :----------------------- | :--------------------------------------------- | :-------: | :-----: |
| 1. [회사/조직 정보 조회] | /api/org/{org_id}/read                         |    GET    |    O    |
| 2. [회사/조직 정보 수정] | /api/org/{org_id}/info/update                  |   POST    |    O    |
| 3. [경로 정보 수정]      | /api/org/{org_id}/path/update                  |   POST    |    O    |
| 4. [워크데이 조회]       | /api/org/{org_id}/workday/read                 |    GET    |    O    |
| 5. [워크데이 수정]       | /api/org/{org_id}/workday/update               |   POST    |    O    |
| 6. [하루 근무 시간 수정] | /api/org/{org_id}/working_hours_per_day/update |   POST    |    X    |
| 7. [초과 수당 배수 수정] | /api/org/{org_id}/overtime_multiple/update     |   POST    |    X    |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 회사/조직 정보 조회 <a id="org-read"></a>

### `GET /api/org/{org_id}/read`

### permission

- everyone can do it.

### request

| param  | type |  data  | required | desc  |
| ------ | :--: | :----: | :------: | ----- |
| org_id | path | string |    O     | 'std' |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"org_info": {
			"org_name": "def",
			"logo_thumbnail": "",
			"fileserver_windows": "x:/",
			"fileserver_osx": "/Users/std/Documents/",
			"fileserver_linux": "/home/std/",
			"artist_windows": "d:/art/",
			"artist_osx": "/Users/art/Documents/",
			"artist_linux": "/home/art/",
			"lang": "en",
			"port_attached": "81",
			"working_hours_per_day": "8",
			"overtime_multiple": "1.5"
		}
	}
}
```

---

## 2. 회사/조직 정보 수정 <a id="org-info-update"></a>

### `POST /api/org/{org_id}/info/update`

### permission

- `permission.do_global_setting`

### request

| param                 | type  |  data   | required | desc                 |
| --------------------- | :---: | :-----: | :------: | -------------------- |
| org_id                | path  | string  |    O     | 'std'                |
| org_name              | query | string  |    O     |                      |
| logo                  | query | string  |    X     |                      |
| lang                  | query | string  |    O     | 'ko' or 'en' or 'cn' |
| port_attached         | query | integer |    O     | 첨부파일 포트        |
| working_hours_per_day | query |  float  |    O     | 하루 근무 시간       |
| overtime_multiple     | query |  float  |    O     | 오버타임 배수        |

### response

```json
{
	"error": {
		"code": 200,
		"message": "회사/조직 정보를 업데이트했습니다."
	},
	"data": null
}
```

---

## 3. 경로 정보 수정 <a id="org-path-update"></a>

### `POST /api/org/{org_id}/path/update`

### permission

- `permission.do_global_setting`

### request

| param              | type  |  data  | required | desc  |
| ------------------ | :---: | :----: | :------: | ----- |
| org_id             | query | string |    O     | 'std' |
| fileserver_windows | query | string |    X     |       |
| fileserver_osx     | query | string |    X     |       |
| fileserver_linux   | query | string |    X     |       |
| artist_windows     | query | string |    X     |       |
| artist_osx         | query | string |    X     |       |
| artist_linux       | query | string |    X     |       |

### response

```json
{
	"error": {
		"code": 200,
		"message": "경로 정보가 수정됐습니다."
	},
	"data": null
}
```

---

## 4. 워크데이 조회 <a id="org-workday-read"></a>

### `GET /api/org/{org_id}/workday/read`

### permission

- `permission.do_global_setting`

### request

| param  | type  |  data  | required | desc  |
| ------ | :---: | :----: | :------: | ----- |
| org_id | query | string |    O     | 'std' |

### response

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"workdays": {
			"workday_1": 1,
			"workday_2": 1,
			"workday_3": 1,
			"workday_4": 1,
			"workday_5": 1,
			"workday_6": 0,
			"workday_7": 0
		},
		"holidays": [
			{
				"holiday_date": "2013-11-12",
				"holiday_desc": "fr"
			},
			{
				"holiday_date": "2019-12-24",
				"holiday_desc": "ch"
			},
			{
				"holiday_date": "2019-12-25",
				"holiday_desc": "ch"
			}
		]
	}
}
```

---

## 5. 워크데이 수정 <a id="org-workday-update"></a>

### `POST /api/org/{org_id}/workday/update`

### permission

- `permission.do_global_setting`

### request

| param          | type  |     data      | required | desc           |
| -------------- | :---: | :-----------: | :------: | -------------- |
| org_id         | query |    string     |    O     | 'std'          |
| workday_1      | query |    integer    |    O     | 월요일. 1 or 0 |
| workday_2      | query |    integer    |    O     | 화요일. 1 or 0 |
| workday_3      | query |    integer    |    O     | 수요일. 1 or 0 |
| workday_4      | query |    integer    |    O     | 목요일. 1 or 0 |
| workday_5      | query |    integer    |    O     | 금요일. 1 or 0 |
| workday_6      | query |    integer    |    O     | 토요일. 1 or 0 |
| workday_7      | query |    integer    |    O     | 일요일. 1 or 0 |
| holiday_date[] | query | array of date |    X     | YYYY-MM-DD     |
| holiday_desc[] | query | array of date |    X     |                |

### response

```json
{
	"error": {
		"code": 200,
		"message": "워크데이 정보가 수정됐습니다."
	},
	"data": null
}
```

---

## 6. 하루 근무 시간 수정 <a id="org-working-hours-update"></a>

### `POST /api/org/{org_id}/working_hours_per_day/update`

### permission

- `permission.do_global_setting`

### request

| param  | type  |  data  | required | desc           |
| ------ | :---: | :----: | :------: | -------------- |
| org_id | query | string |    O     | 'std'          |
| value  | query | float  |    O     | 하루 근무 시간 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "하루 근무 시간이 수정됐습니다."
	},
	"data": null
}
```

---

## 7. 초과 수당 배수 수정 <a id="org-overtime-multiple-update"></a>

### `POST /api/org/{org_id}/overtime_multiple/update`

### permission

- `permission.do_global_setting`

### request

| param  | type  |  data  | required | desc           |
| ------ | :---: | :----: | :------: | -------------- |
| org_id | query | string |    O     | 'std'          |
| value  | query | float  |    O     | 초과 수당 배수 |

### response

```json
{
	"error": {
		"code": 200,
		"message": "초과 수당 배수가 수정됐습니다."
	},
	"data": null
}
```

---

## 끝

[회사/조직 정보 조회]: #org-read
[회사/조직 정보 수정]: #org-info-update
[경로 정보 수정]: org-path-update
[워크데이 조회]: #org-workday-read
[워크데이 수정]: #org-workday-update
[하루 근무 시간 수정]: #org-working-hours-update
[초과 수당 배수 수정]: #org-overtime-multiple-update
