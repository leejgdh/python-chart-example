import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generate_density_chart(filename):
    # 샘플 데이터 생성
    np.random.seed(42)
    x = np.random.normal(loc=0, scale=1, size=10000)  # x 좌표: 정규 분포
    y = np.random.normal(loc=0, scale=1, size=10000)  # y 좌표: 정규 분포

    # 밀도 차트 생성
    plt.figure(figsize=(8, 8))
    sns.kdeplot(x=x, y=y, cmap='Oranges', fill=True, thresh=0, levels=100)
    plt.title('Density Plot Example')

    # 파일 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')  # DPI와 여백 설정
    plt.close()
    print(f"Density chart saved to {filepath}")
    return filepath

# 호출
generate_density_chart('density_chart')
