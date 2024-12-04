import networkx as nx
import matplotlib.pyplot as plt
import os

def generate_network_chart(filename):
    # 그래프 생성
    G = nx.random_geometric_graph(500, 0.125)  # 노드 500개, 연결 거리 0.125

    # 노드 위치 가져오기
    pos = nx.get_node_attributes(G, 'pos')

    # 그래프 플롯
    plt.figure(figsize=(8, 8))
    nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='gray')
    nx.draw_networkx_nodes(G, pos, node_size=10, node_color='black')
    plt.title('Network Graph Example')
    plt.axis('off')

    # 파일 저장
    filepath = f"charts/{filename}.png"
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig(filepath, dpi=300)  # DPI를 설정해 고해상도로 저장
    plt.close()
    print(f"Chart saved to {filepath}")
    return filepath

# 호출
generate_network_chart('network_graph')
