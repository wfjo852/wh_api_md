# WH2API::Stats

## 목차

| 내용                         | slug                                               | 서버 구현 | 웹 적용 |
| :--------------------------- | :------------------------------------------------- | :-------: | :-----: |
| 1. [데일리 태스크 통계 갱신] | /api/stats/daily_task/update                       |   POST    |    O    |
| 2. [데일리 태스크 통계 보기] | /api/stats/daily_task/{date}/read                  |    GET    |    O    |

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 데일리 태스크 통계 갱신 <a id="daily-task-update"></a>

### `POST /api/stats/daily_task/update`

### permission

- `permission.do_global_setting`

### request

| param       | type  |  data   | required | desc |
| ----------- | :---: | :-----: | :------: | ---- |
| project_idx | query | integer |    O     |      |

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

## 2. 데일리 태스크 통계 보기 <a id="daily-task-read"></a>

### `GET /api/stats/daily_task/{date}/read`

### permission

- `permission.do_global_setting`

### request

| param | type |  data  | required | desc       |
| ----- | :--: | :----: | :------: | ---------- |
| date  | path | string |    O     | YYYY-MM-DD |

### response

```json
{
	"error": {
		"code": 200,
		"message": "Success"
	},
	"data": {
		"stats_daily_task": [
			{
				"artist_user_idx": "1",
				"artist_user_name": "C2Monster",
				"artist_user_thumbnail": "http://localhost:81/2019/04/08/c1f855a779d0543e.png",
				"num_tasks": {
					"0000-00-00": "14",
					"2019-03-31": 0,
					"2019-04-01": 0,
					"2019-04-02": 0
				}
			},
			{
				"artist_user_idx": "2",
				"artist_user_name": "Artist",
				"artist_user_thumbnail": "http://localhost:81/2019/04/08/dc3295a0a38e89e9.png",
				"num_tasks": {
					"0000-00-00": "6",
					"2019-03-31": 0,
					"2019-04-01": 0,
					"2019-04-02": 0
				}
			}
		]
	}
}
```

---

## 끝

[데일리 태스크 통계 갱신]: #daily-task-update
[데일리 태스크 통계 보기]: #daily-task-read