import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import os

def generate_voronoi_density_chart(filename):
    # 샘플 데이터 생성
    np.random.seed(42)
    points = np.random.rand(1000, 2)  # 0~1 사이의 랜덤 좌표

    # Voronoi 다이어그램 생성
    vor = Voronoi(points)

    # 플롯 생성
    plt.figure(figsize=(8, 8))
    voronoi_plot_2d(vor, show_points=False, show_vertices=False, s=1, line_colors='orange')
    plt.scatter(points[:, 0], points[:, 1], color='black', s=5)  # 데이터 점 표시
    plt.title('Voronoi Density Plot Example')

    # 파일 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')  # DPI와 여백 설정
    plt.close()
    print(f"Voronoi density chart saved to {filepath}")
    return filepath

# 호출
generate_voronoi_density_chart('voronoi_density_chart')
