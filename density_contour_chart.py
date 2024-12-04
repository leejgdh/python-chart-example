import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generate_density_contour_chart(filename):
    # 샘플 데이터 생성
    np.random.seed(42)
    x = np.random.normal(loc=0, scale=1, size=10000)  # x축 데이터: 정규 분포
    y = np.random.normal(loc=0, scale=1, size=10000)  # y축 데이터: 정규 분포

    # 플롯 설정
    plt.figure(figsize=(6, 6))
    sns.kdeplot(
        x=x, 
        y=y, 
        cmap='Reds', 
        fill=True, 
        thresh=0.05,  # 밀도가 낮은 부분의 임계값
        levels=100,   # 등고선 레벨
        alpha=0.9     # 투명도
    )
    sns.kdeplot(
        x=x, 
        y=y, 
        color="white",  # 등고선 외곽선 색상
        levels=10,      # 외곽선 개수
    )
    plt.gca().set_facecolor('#fdf5e6')  # 배경색 설정
    plt.axis('off')  # 축 숨김
    plt.title("Density Contour Plot")

    # 파일 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Density contour chart saved to {filepath}")
    return filepath

# 호출
generate_density_contour_chart('density_contour_chart')
