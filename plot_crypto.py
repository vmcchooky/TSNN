import matplotlib.pyplot as plt
import os

sizes = [1, 10, 50, 100, 500, 1000]
times = [0.1856, 0.1184, 0.1587, 0.2126, 0.6075, 1.0846]

plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='s', linestyle='-', color='#E91E63', linewidth=2, markersize=8)

plt.xlabel('Kích thước Payload (KB)', fontsize=12)
plt.ylabel('Thời gian mã hóa (ms)', fontsize=12)
plt.title('Tốc độ Mã hóa AES-GCM 256-bit tại Trình duyệt (WebCrypto API)', fontsize=14, pad=15)
plt.grid(True, linestyle='--', alpha=0.6)

# Add values on points
for i, txt in enumerate(times):
    plt.annotate(f'{txt:.2f}ms', (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

plt.tight_layout()
os.makedirs('img', exist_ok=True)
plt.savefig('img/benchmark_crypto.png', dpi=300)
print("Saved img/benchmark_crypto.png")
