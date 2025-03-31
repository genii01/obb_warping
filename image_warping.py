import cv2
import numpy as np
import matplotlib.pyplot as plt


def warp_image(image_path: str, corners: np.ndarray, warp_size: tuple = (800, 500)):
    """
    이미지를 주어진 좌표를 기반으로 warping 수행

    Parameters:
        image_path (str): 입력 이미지 경로
        corners (np.ndarray): warping할 4개의 모서리 좌표
        warp_size (tuple): 출력 이미지 크기

    Returns:
        tuple: (원본 이미지, warping된 이미지)
    """
    # 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image from {image_path}")

    # Warping 후의 좌표 설정 (좌상, 우상, 우하, 좌하 순서)
    warp_corners = np.float32(
        [
            [0, 0],  # 좌상 (1번)
            [warp_size[0] - 1, 0],  # 우상 (2번)
            [warp_size[0] - 1, warp_size[1] - 1],  # 우하 (3번)
            [0, warp_size[1] - 1],  # 좌하 (4번)
        ]
    )

    # 변환 행렬 계산
    transform_matrix = cv2.getPerspectiveTransform(corners, warp_corners)

    # Warping 수행
    warped_img = cv2.warpPerspective(img, transform_matrix, warp_size)

    # 원본 이미지에 좌표 표시
    img_with_points = img.copy()

    # 점 그리기
    for i, point in enumerate(corners):
        x, y = map(int, point)
        cv2.circle(img_with_points, (x, y), 5, (0, 0, 255), -1)
        # 점 번호 표시
        cv2.putText(
            img_with_points,
            str(i + 1),
            (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2,
        )

    # 선 그리기
    for i in range(4):
        pt1 = tuple(map(int, corners[i]))
        pt2 = tuple(map(int, corners[(i + 1) % 4]))
        cv2.line(img_with_points, pt1, pt2, (0, 255, 0), 2)

    return img_with_points, warped_img


def visualize_results(original_img: np.ndarray, warped_img: np.ndarray):
    """
    원본 이미지와 warping된 이미지를 시각화

    Parameters:
        original_img (np.ndarray): 원본 이미지
        warped_img (np.ndarray): warping된 이미지
    """
    plt.figure(figsize=(15, 5))

    # 원본 이미지 표시
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image with OBB Points")
    plt.axis("off")

    # Warping된 이미지 표시
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB))
    plt.title("Warped Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


def main():
    # 입력 이미지 경로
    image_path = "./card1.png"

    # OBB 좌표
    obb_res = [120, 307, 371, 538, 909, 237, 634, 47]

    # 이미지의 점 번호 순서대로 좌표 재배열 (1->2->3->4)
    corners = np.float32(
        # [
        #     [obb_res[0], obb_res[1]],  # 1번 점 (좌상)
        #     [obb_res[2], obb_res[3]],  # 2번 점 (우상)
        #     [obb_res[4], obb_res[5]],  # 3번 점 (우하)
        #     [obb_res[6], obb_res[7]],  # 4번 점 (좌하)
        # ]
        [
            [obb_res[0], obb_res[1]],  # 1번 점 (좌상)
            [obb_res[6], obb_res[7]],  # 2번 점 (우상)
            [obb_res[4], obb_res[5]],  # 3번 점 (우하)
            [obb_res[2], obb_res[3]],  # 4번 점 (좌하)
        ]
    )

    # Warping 크기 설정 (카드 비율에 맞게 조정)
    warp_size = (800, 500)  # 카드의 일반적인 비율로 조정

    try:
        # 이미지 warping 수행
        original_img, warped_img = warp_image(image_path, corners, warp_size)

        # 결과 시각화
        visualize_results(original_img, warped_img)

        # 결과 저장
        cv2.imwrite("original_with_points.jpg", original_img)
        cv2.imwrite("warped_result.jpg", warped_img)
        print("\nResults saved as 'original_with_points.jpg' and 'warped_result.jpg'")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
