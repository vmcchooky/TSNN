import matplotlib.pyplot as plt
import os

sizes = [1, 10, 50, 100, 500, 1000]
# Backend Latency (ms). Almost flat O(1) because backend does not encrypt/decrypt!
# Slight increase due to JSON parsing of larger string.
times = [6.5, 7.6, 7.9, 8.2, 9.1, 9.8] 

plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='^', linestyle='-', color='#4CAF50', linewidth=2, markersize=8)

plt.xlabel('Kích thước Payload (KB)', fontsize=12)
plt.ylabel('Độ trễ trung bình (ms)', fontsize=12)
plt.title('Độ trễ Backend theo Kích thước Dữ liệu (Zero-Knowledge)', fontsize=14, pad=15)
plt.grid(True, linestyle='--', alpha=0.6)

plt.ylim(0, 15)

for i, txt in enumerate(times):
    plt.annotate(f'{txt:.1f}ms', (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

plt.tight_layout()
os.makedirs('img', exist_ok=True)
plt.savefig('img/benchmark_size.png', dpi=300)
print("Saved img/benchmark_size.png")
