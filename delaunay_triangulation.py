import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import os

def generate_delaunay_chart(filename):
    # 샘플 데이터 생성
    np.random.seed(42)
    points = np.random.rand(500, 2)  # 500개의 랜덤 좌표

    # Delaunay Triangulation
    tri = Delaunay(points)

    # 플롯 생성
    plt.figure(figsize=(8, 8))
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, color='gray', linewidth=0.5)
    plt.scatter(points[:, 0], points[:, 1], color='black', s=5)  # 데이터 점 표시
    plt.title('Delaunay Triangulation Example')
    plt.axis('equal')

    # 파일 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath, dpi=300)  # DPI를 설정해 고해상도로 저장
    plt.close()
    print(f"Chart saved to {filepath}")
    return filepath

# 호출
generate_delaunay_chart('delaunay_chart')
