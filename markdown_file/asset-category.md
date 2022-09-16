# WH2API:: AssetCategory

- `project.md` 와 일부 합칠 예정

## 목차

| 내용                         | slug                                                                      | 서버 구현 | 웹 적용 |  웹훅  | 로그 |
| :--------------------------- | :------------------------------------------------------------------------ | :-------: | :-----: | :----: | :--: |
| 1. [에셋 카테고리 목록 조회] | /api/project/{project_idx}/asset/asset_category/list[/{detail}]           |    GET    |    O    |   -    |  -   |
| 2. [에셋 카테고리 생성]      | /api/project/{project_idx}/asset/asset_category/create                    |   POST    |    O    | hooked |  O   |
| 3. [에셋 카테고리 수정]      | /api/project/{project_idx}/asset/category/{category_idx}/update           |   POST    |    O    |   -    |  O   |
| 4. [에셋 카테고리 삭제]      | /api/project/{project_idx}/asset/asset_category/{category_idx}/delete     |   POST    |    O    |   -    |  O   |
| 5. [에셋 카테고리 활성화]    | /api/project/{project_idx}/asset/asset_category/{category_idx}/activate   |   POST    |    O    |   -    |  -   |
| 6. [에셋 카테고리 비활성화]  | /api/project/{project_idx}/asset/asset_category/{category_idx}/deactivate |   POST    |    O    |   -    |  -   |

---

## 0. 참고

- 기본적으로 필요한 `user_idx`(를 비롯한 이용자 정보)는 `jwt`의 것을 가져다 쓰거나
- 아예 `api`의 `pathname` 에 포함시킨다. (즉, 본인인 경우 파라미터로는 보내지 않음)

---

## 1. 에셋 카테고리 목록 조회 <a id="project-asset-category-list"></a>

### `GET /api/project/{project_idx}/asset/asset_category/list[/{detail}]`

### permission

- `permission.read_project`

### request

| param       | type |  data   | required | desc          |
| ----------- | :--: | :-----: | :------: | ------------- |
| project_idx | path | integer |    O     |               |
| detail      | path | string  |    O     | 값은 'detail' |

- api 간단 버전 호출 예: `/api/project/1/asset/category/list`
- api 상세 버전 호출 예: `/api/project/1/asset/category/list/detail`

### response (간단)

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "asset_categories": [
      {
        "idx": "1",
        "name": "animalsm",
        "description": "desc"
      },
      {
        "idx": "2",
        "name": "building",
        "description": "desc"
      }
    ]
  }
}
```

### response (상세)

```json
{
  "error": {
    "code": 200,
    "message": "성공"
  },
  "data": {
    "asset_categories": [
      {
        "idx": "1",
        "name": "animal",
        "description": "this is animal.",
        "is_on": "1",
        "asset_count": "1",
        "duration_count": "0 Days",
        "progress": "100.00%",
        "task": {
          "total": "1",
          "assigned_users": "1"
        }
      },
      {
        "idx": "2",
        "name": "building",
        "description": "building is tall.",
        "is_on": "1",
        "asset_count": "0",
        "duration_count": "0 Days",
        "progress": "0%",
        "task": {
          "total": "0",
          "assigned_users": "0"
        }
      }
    ]
  }
}
```

---

## 2. 에셋 카테고리 생성 <a id="project-asset-category-create"></a>

### `POST /api/project/{project_idx}/asset/asset_category/create`

### Webhook

- event: asset category
- action: create

### permission

- `permission.update_project`

### request

| param               | type  |  data   | required | desc |
| ------------------- | :---: | :-----: | :------: | ---- |
| project_idx         | path  | integer |    O     |      |
| asset_category_name | query | string  |    O     |      |
| description         | query | string  |    X     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 카테고리가 등록됐습니다."
  },
  "data": {
    "asset_category": {
      "idx": 1
    }
  }
}
```

---

## 3. 에셋 카테고리 수정 <a id="project-asset-category-update"></a>

### `POST /api/project/{project_idx}/asset/category/{category_idx}/update`

### permission

- `permission.update_project`

### request

| param        | type  |  data   | required | desc             |
| ------------ | :---: | :-----: | :------: | ---------------- |
| project_idx  | path  | integer |    O     |                  |
| category_idx | path  | integer |    O     |                  |
| column       | query | string  |    O     |                  |
| old_val      | query | string  |    O     | 공백일 수는 있음 |
| new_val      | query | string  |    O     | 공백일 수는 있음 |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 카테고리 정보가 수정됐습니다."
  },
  "data": {
    "category": {
      "idx": "4",
      "column": "description",
      "value": "until 4"
    }
  }
}
```

---

## 4. 에셋 카테고리 삭제 <a id="project-asset-category-delete"></a>

### `POST /api/project/asset/category/{category_idx}/delete`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| category_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "카테고리가 삭제됐습니다."
  },
  "data": null
}
```

---

## 5. 에셋 카테고리 활성화 <a id="project-asset-category-activate"></a>

### `POST /api/project/{project_idx}/asset/category/{category_idx}/activate`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| category_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 카테고리가 활성화 되었습니다."
  },
  "data": null
}
```

---

## 6. 에셋 카테고리 비활성화 <a id="project-asset-category-deactivate"></a>

### `POST /api/project/{project_idx}/asset/category/{category_idx}/deactivate`

### permission

- `permission.update_project`

### request

| param        | type |  data   | required | desc |
| ------------ | :--: | :-----: | :------: | ---- |
| project_idx  | path | integer |    O     |      |
| category_idx | path | integer |    O     |      |

### response

```json
{
  "error": {
    "code": 200,
    "message": "에셋 카테고리가 비활성화 되었습니다."
  },
  "data": null
}
```

---

## 끝

[에셋 카테고리 목록 조회]: #project-asset-category-list
[에셋 카테고리 생성]: #project-asset-category-create
[에셋 카테고리 수정]: #project-asset-category-update
[에셋 카테고리 삭제]: #project-asset-category-delete
[에셋 카테고리 활성화]: #project-asset-category-activate
[에셋 카테고리 비활성화]: #project-asset-category-activate
