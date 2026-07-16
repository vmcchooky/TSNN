import matplotlib.pyplot as plt
import os

# Data from loadtest
concurrencies = [10, 50, 100, 200, 500, 1000]
rps = [] # We will fill this in based on the Go output

def plot(rps_data):
    plt.figure(figsize=(8, 5))
    
    # Plotting line chart with markers
    plt.plot(concurrencies, rps_data, marker='o', linestyle='-', color='#03A9F4', linewidth=2, markersize=8)
    
    plt.xlabel('Số luồng xử lý đồng thời (Concurrent Workers)', fontsize=12)
    plt.ylabel('Thông lượng - RPS (Requests Per Second)', fontsize=12)
    plt.title('Mối tương quan giữa Mức độ đồng thời và Thông lượng (Backend)', fontsize=14, pad=15)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Add values on points
    for i, txt in enumerate(rps_data):
        plt.annotate(f'{int(txt)}', (concurrencies[i], rps_data[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
    
    plt.tight_layout()
    
    os.makedirs('img', exist_ok=True)
    plt.savefig('img/benchmark_throughput.png', dpi=300)
    print("Saved img/benchmark_throughput.png")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        data = [float(x) for x in sys.argv[1].split(',')]
        plot(data)
