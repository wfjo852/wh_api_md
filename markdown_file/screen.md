# WH2API::Screen

## 목차

| 내용                               | slug                                                     |    서버 구현     | 웹 적용 | 웹훅 | 로그 |
| :--------------------------------- | :------------------------------------------------------- | :--------------: | :-----: | :--: | :--: |
| 1. [타임라인 태스크타입 목록 조회] | -                                                        | 참조<sup>1</sup> |    O    |  -   |  -   |
| 2. [타임라인 버전 상태 목록 조회]  | -                                                        | 참조<sup>2</sup> |    O    |  -   |  -   |
| 3. [타임라인 샷 리스트 조회]       | /api/project/{project_idx}/shot/{shot_idx}/timeline/read |       POST       |    O    |  -   |  -   |
| 4. [리스트 조회]                   | -                                                        | 참조<sup>3</sup> |    O    |  -   |  -   |

- 참조<sup>1</sup> - [project-detail.md](./project-detail.md) "1. 태스크타입 할당 조회" api 이용
- 참조<sup>2</sup> - [project.md](./project.md) "9. 프로젝트에 할당된 상태 코드 목록 조회" api 이용
- 참조<sup>3</sup> - [version.md](./version.md) "13. 버전 목록 조회" api 이용

---

## 0. 참고

---

## 3. 타임라인 샷 리스트 조회 <a id="timeline-shot-read"></a>

### `POST /api/project/{proect_idx}/shot/{shot_idx}/timeline/read`

### permission

- `permission.read_shot_task_overview`

### request

| param       | type  |  data   |              required               | desc                                                                                    |
| ----------- | :---: | :-----: | :---------------------------------: | --------------------------------------------------------------------------------------- |
| project_idx | path  | integer |                  O                  |                                                                                         |
| shot_idx    | path  | integer |                  O                  |                                                                                         |
| direction   | query | string  |                  O                  | `shot_idx`를 기준으로 `init` - 최초 호출, `prev` - 이전, `next` - 다음 샷 리스트를 부름 |
| shot_num    | query | integer | `direction`이 `prev`, `next`일 때 O | `direction`이 `prev` or `next` 일 때 부를 샷의 갯수 (`init`이면 31개 고정)              |

### response

- `direction`
  - `init` 일 때는 파라미터 `shot_idx` 앞뒤로 15개(총 31개)를 리스트로 구성해서 내려줌
- `loop_play`
  - `direction`이 `init`이면 파라미터 `shot_idx`의 `loop_play` 값만 `1` (나머지 샷의 `loop_play`는 모두 `0`)
  - `direction`이 `prev`, `next`이면 모두 `0`
  - 현재 어노테이션 중이라면, 현재 선택 중인 샷의 `loop_play`를 자동으로 `1`로 켬 (프론트엔드에서 연두색 테두리)
- `current_play`는 현재 재생 중인 샷에 `1`, 나머지는 `0` (cf. 프론트엔드에서는 하늘색 테두리)
- 샷에 포함된 버전은 `version_idx` 내림차순으로 정렬

```json
{
	"error": {
		"code": 200,
		"message": "성공"
	},
	"data": {
		"shots": [
			{
				"shot_idx": "2",
				"shot_order": "2",
				"shot_name": "s0010_c0020",
				"shot_thumbnail": "http://localhost:81/2019/04/08/d45d311d6b86ae96.jpg",
				"shot_status_idx": "1",
				"shot_status_name": "wip",
				"current": 0,
				"loop_play": 0,
				"selected_version": 0,
				"selected_tasktype": 0,
				"tasktypes": [
					{
						"tasktype_idx": "1",
						"tasktype_name": "Animation"
					}
				],
				"versions": [
					{
						"version_idx": "2",
						"version_name": "big_s0010_c0020_anim_v001",
						"version_thumbnail": "http://localhost:81/2019/04/08/d45d311d6b86ae96.jpg",
						"version_url": "http://localhost:81/2019/04/08/c54e0282e55506af.mp4",
						"version_filename_original": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0020_anim_v001.mp4",
						"version_status_idx": "2",
						"version_status_name": "confirm",
						"task_idx": "3",
						"tasktype_idx": "1",
						"tasktype_name": "Animation",
						"task_status_idx": "2",
						"task_status_name": "confirm"
					}
				]
			},
			{
				"shot_idx": "3",
				"shot_order": "3",
				"shot_name": "s0010_c0030",
				"shot_thumbnail": "http://localhost:81/2019/04/08/fbb2b3da21623e7b.jpg",
				"shot_status_idx": "1",
				"shot_status_name": "wip",
				"current": 0,
				"loop_play": 0,
				"selected_version": 0,
				"selected_tasktype": 1,
				"tasktypes": [
					{
						"tasktype_idx": "1",
						"tasktype_name": "Animation"
					},
					{
						"tasktype_idx": "3",
						"tasktype_name": "Comp"
					}
				],
				"versions": [
					{
						"version_idx": "7",
						"version_name": "big_s0010_c0030_anim_v003",
						"version_thumbnail": "http://localhost:81/2019/04/08/fbb2b3da21623e7b.jpg",
						"version_url": "http://localhost:81/2019/04/08/073c439ed5951ae2.mp4",
						"version_filename_original": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0030_anim_v003.mp4",
						"version_status_idx": "5",
						"version_status_name": "final",
						"task_idx": "61",
						"tasktype_idx": "3",
						"tasktype_name": "Comp",
						"task_status_idx": "1",
						"task_status_name": "wip"
					},
					{
						"version_idx": "6",
						"version_name": "big_s0010_c0030_anim_v002",
						"version_thumbnail": "http://localhost:81/2019/04/08/fbb2b3da21623e7b.jpg",
						"version_url": "http://localhost:81/2019/04/08/7e595c4c194ed061.mp4",
						"version_filename_original": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0030_anim_v002.mp4",
						"version_status_idx": "3",
						"version_status_name": "retake",
						"task_idx": "9",
						"tasktype_idx": "1",
						"tasktype_name": "Animation",
						"task_status_idx": "5",
						"task_status_name": "final"
					}
				]
			}
		]
	}
}
```

---

## 끝

[타임라인 샷 리스트 조회]: #timeline-shot-read
