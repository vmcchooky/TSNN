import matplotlib.pyplot as plt
import os

times = list(range(16))
# Extracted from Go runtime.ReadMemStats().Alloc
mem = [0.79, 2.68, 2.35, 2.25, 1.41, 2.31, 1.22, 2.62, 1.32, 2.87, 1.21, 1.19, 1.46, 2.20, 1.44, 2.39]

plt.figure(figsize=(8, 5))
plt.plot(times, mem, marker='o', linestyle='-', color='#03A9F4', linewidth=2, markersize=6)
plt.fill_between(times, mem, color='#03A9F4', alpha=0.1)

plt.xlabel('Thời gian (Giây)', fontsize=12)
plt.ylabel('Bộ nhớ tiêu thụ (MB)', fontsize=12)
plt.title('Memory Profiling: Bài kiểm tra Tải nặng & Memory Leak', fontsize=14, pad=15)
plt.grid(True, linestyle='--', alpha=0.6)

plt.ylim(0, max(mem) * 1.5)

plt.tight_layout()
os.makedirs('img', exist_ok=True)
plt.savefig('img/benchmark_memory.png', dpi=300)
print("Saved img/benchmark_memory.png")
