import matplotlib.pyplot as plt
import os
import numpy as np

def generate_scatter_chart(filename):
    # 샘플 데이터 생성 (x와 y는 랜덤 데이터)
    np.random.seed(42)  # 재현 가능한 랜덤 데이터
    x = np.random.uniform(0, 10, 1000)  # 0~10 사이의 값 1000개
    y = np.random.exponential(0.5, 1000)  # 지수 분포로 랜덤 y 값 생성

    # 산포도 생성
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, color='orange', alpha=0.5, s=5)  # 점 크기와 투명도 조정
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Scatter Plot')

    # 이미지 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath)
    plt.close()
    print(f"Chart saved to {filepath}")
    return filepath

# 차트 생성 호출
generate_scatter_chart('scatter_plot')
