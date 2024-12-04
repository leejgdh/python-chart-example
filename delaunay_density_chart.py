import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import matplotlib.cm as cm
import os

def generate_delaunay_density_chart(filename):
    # 샘플 데이터 생성
    np.random.seed(42)
    points = np.random.rand(1000, 2)  # 0~1 사이의 랜덤 좌표

    # Delaunay Triangulation 생성
    tri = Delaunay(points)

    # 삼각형 면적 계산 (밀도 기반 색상 설정)
    triangles = points[tri.simplices]
    areas = np.abs(
        0.5 * (
            (triangles[:, 0, 0] * (triangles[:, 1, 1] - triangles[:, 2, 1])) +
            (triangles[:, 1, 0] * (triangles[:, 2, 1] - triangles[:, 0, 1])) +
            (triangles[:, 2, 0] * (triangles[:, 0, 1] - triangles[:, 1, 1]))
        )
    )

    # 플롯 생성
    plt.figure(figsize=(8, 8))
    plt.tripcolor(
        points[:, 0], points[:, 1], tri.simplices, facecolors=areas,
        cmap='Oranges', edgecolors='white', linewidth=0.5
    )
    plt.scatter(points[:, 0], points[:, 1], color='black', s=5, alpha=0.7)  # 데이터 점 표시
    plt.title('Delaunay Density Plot')
    plt.axis('off')

    # 파일 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Delaunay density chart saved to {filepath}")
    return filepath

# 호출
generate_delaunay_density_chart('delaunay_density_chart')
