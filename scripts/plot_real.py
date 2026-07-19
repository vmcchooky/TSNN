
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.style.use('bmh')

def plot_latency():
    plt.figure(figsize=(8, 5))
    scenarios = ['Redis Cache Hit', 'SQLite Local Hit', 'Phân tích ngữ vựng (Miss)']
    latency = [2.6, 3.4, 2.1]
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    bars = plt.bar(scenarios, latency, color=colors, width=0.6)
    plt.title('So sánh độ trễ phân giải tên miền (Thực tế)', fontsize=14, pad=15)
    plt.ylabel('Độ trễ trung bình (ms)', fontsize=12)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + (max(latency)*0.02), f'{yval} ms', ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig('../img/benchmark_latency.png', dpi=300)
    plt.close()

def plot_throughput():
    plt.figure(figsize=(8, 5))
    concurrency = [10, 50, 100, 200, 500, 1000]
    qps_cache = [1680, 1470, 1368, 1515, 1562, 1687]
    qps_ai = [1319, 1411, 1568, 1580, 1604, 1702]
    plt.plot(concurrency, qps_cache, marker='o', linewidth=2.5, color='#2ecc71', label='Cache Hit (Redis)')
    plt.plot(concurrency, qps_ai, marker='s', linewidth=2.5, color='#e74c3c', label='Phân tích ngữ vựng (Miss)')
    plt.title('Khả năng chịu tải thực tế (Throughput)', fontsize=14, pad=15)
    plt.xlabel('Số lượng kết nối đồng thời (Concurrency)', fontsize=12)
    plt.ylabel('Truy vấn mỗi giây (QPS)', fontsize=12)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig('../img/benchmark_throughput.png', dpi=300)
    plt.close()

def plot_inference():
    plt.figure(figsize=(8, 5))
    data = [3.5643577575683594, 1.7809867858886719, 1.880645751953125, 1.8422603607177734, 1.538991928100586, 1.5521049499511719, 1.6012191772460938, 1.8436908721923828, 2.608060836791992, 2.179861068725586, 2.3088455200195312, 2.106189727783203, 1.8885135650634766, 1.8310546875, 1.5759468078613281, 2.045869827270508, 2.579927444458008, 2.2983551025390625, 2.039194107055664, 1.9748210906982422]
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='#9b59b6', color='#8e44ad'),
                medianprops=dict(color='white', linewidth=2), vert=False)
    plt.title('Phân phối thời gian phân tích ngữ vựng (Thực tế)', fontsize=14, pad=15)
    plt.xlabel('Thời gian phản hồi (ms)', fontsize=12)
    plt.yticks([1], ['Lexical Analyzer'])
    plt.tight_layout()
    plt.savefig('../img/benchmark_inference.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    plot_latency()
    plot_throughput()
    plot_inference()
    print("New real charts generated!")
