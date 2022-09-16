# WH2API::Attachment

## 목차

| 내용                           | slug                                                                    | 서버 구현 | 웹 적용 | 웹훅 | 로그 |
| :----------------------------- | :---------------------------------------------------------------------- | :-------: | :-----: | :--: | :--: |
| 1. [객체의 첨부 파일 삭제]     | /api/project/{project_idx}/{which}/attachment/{attachment_idx}/delete   |   POST    |    X    |  -   |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 프로젝트 내 첨부 파일 삭제 <a id="project-attachment-delete"></a>

### `POST /api/project/{project_idx}/{which}/attachment/{attachment_idx}/delete`

### permission

- `permission.read_shot_task_overview`

### request

| param          | type |  data   | required | desc                 |
| -------------- | :--: | :-----: | :------: | -------------------- |
| project_idx    | path | integer |    O     |                      |
| which          | path | integer |    O     | issue, issue_comment |
| attachment_idx | path | integer |    O     |                      |

### response

```json
{
	"error": {
		"code": 200,
		"message": "첨부파일이 삭제됐습니다."
	},
	"data": null
}
```

---

## 끝

[프로젝트 내 첨부 파일 삭제]: #project-attachment-delete
