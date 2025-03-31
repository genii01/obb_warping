# Image Warping Project

이 프로젝트는 이미지의 OBB(Oriented Bounding Box) 좌표를 기반으로 이미지를 warping하는 Python 기반 도구입니다.

## OBB YOLO 모델

이 프로젝트는 YOLO-OBB(Oriented Bounding Box) 모델을 사용하여 이미지에서 카드의 방향성을 감지합니다. YOLO-OBB는 기존 YOLO 모델을 확장하여 회전된 객체를 감지할 수 있도록 한 버전입니다.

![OBB YOLO Detection Example](obb_image.png)

### OBB 좌표 형식

YOLO-OBB 모델은 다음과 같은 형식으로 좌표를 출력합니다:
- `[x1, y1, x2, y2, x3, y3, x4, y4]`
- 각 좌표는 이미지의 픽셀 좌표를 나타냅니다
- 좌표는 시계방향으로 정렬됩니다

### 현재 설정된 OBB 좌표
```python
obb_res = [120, 307, 371, 538, 909, 237, 634, 47]
```

## 기능

- 이미지의 OBB 좌표를 기반으로 이미지 warping
- 원본 이미지에 OBB 좌표 시각화
- Warping된 결과 이미지 생성
- 결과 이미지 시각화 및 저장

## 요구사항

- Python 3.x
- OpenCV (cv2)
- NumPy
- Matplotlib

## 설치 방법

1. 저장소 클론:
```bash
git clone [repository-url]
cd obb_warping
```

2. 의존성 설치:
```bash
make install
```

## 사용 방법

1. 입력 이미지 준비:
   - `card1.png` 파일을 프로젝트 루트 디렉토리에 위치시킵니다.

2. OBB 좌표 설정:
   - `image_warping.py` 파일의 `main()` 함수에서 OBB 좌표를 설정합니다.
   - 현재 설정된 좌표: `[120, 307, 371, 538, 909, 237, 634, 47]`

3. 실행:
```bash
make run
```

4. 결과 확인:
   - `original_with_points.jpg`: OBB 좌표가 표시된 원본 이미지
   - `warped_result.jpg`: Warping된 결과 이미지

## Makefile 명령어

- `make run`: 이미지 warping 스크립트 실행
- `make clean`: 생성된 파일 삭제
- `make install`: 필요한 의존성 설치
- `make help`: 사용 가능한 명령어 목록 표시

## 프로젝트 구조

```
obb_warping/
├── README.md
├── Makefile
├── image_warping.py
├── card1.png
└── obb_image.png
```

## 주요 함수

### warp_image()
- 입력 이미지를 주어진 OBB 좌표를 기반으로 warping
- 파라미터:
  - `image_path`: 입력 이미지 경로
  - `corners`: warping할 4개의 모서리 좌표
  - `warp_size`: 출력 이미지 크기

### visualize_results()
- 원본 이미지와 warping된 이미지를 시각화
- 파라미터:
  - `original_img`: 원본 이미지
  - `warped_img`: warping된 이미지

## 주의사항

- 입력 이미지 파일이 존재하지 않을 경우 에러가 발생합니다.
- OBB 좌표는 이미지 크기를 벗어나지 않도록 설정해야 합니다.
- Warping 크기(warp_size)는 카드의 일반적인 비율에 맞게 조정되어 있습니다.

## 라이선스

[라이선스 정보 추가]

## 기여 방법

[기여 방법 설명 추가]
