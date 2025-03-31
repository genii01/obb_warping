import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 로드
image_path = "./card1.png"
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit(1)

# 원본 이미지 복사본 생성 (시각화용)
output_image = image.copy()

# OBB 좌표 (x1, y1, x2, y2, x3, y3, x4, y4)
obb_res = [120, 307, 371, 538, 909, 237, 634, 47]

# 좌표를 4개의 점으로 변환
points = np.array(obb_res).reshape(-1, 2).astype(np.int32)

# 꼭지점 그리기
for i, point in enumerate(points):
    x, y = point
    # 꼭지점 위치에 원 그리기
    cv2.circle(output_image, (x, y), 5, (0, 0, 255), -1)
    # 꼭지점 번호 표시
    cv2.putText(
        output_image,
        str(i + 1),
        (x - 10, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        2,
    )

    # 좌표 출력
    print(f"Point {i+1}: ({x}, {y})")

# 꼭지점을 선으로 연결
cv2.polylines(output_image, [points], True, (0, 255, 0), 2)

# 결과 이미지 표시
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title("OBB Points Visualization")
plt.axis("off")
plt.show()

# 결과 이미지 저장
cv2.imwrite("obb_points_result.jpg", output_image)
print("\nResult image saved as 'obb_points_result.jpg'")
