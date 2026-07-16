import matplotlib.pyplot as plt
import numpy as np
import os

# Data
labels = ['Trung bình (Avg)', 'p50', 'p90', 'p95', 'p99']
latencies = [28.01, 28.01, 46.69, 53.59, 93.58]
colors = ['#4CAF50', '#8BC34A', '#FFC107', '#FF9800', '#F44336']

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, latencies, color=colors, width=0.6)

plt.ylabel('Độ trễ (ms)', fontsize=12)
plt.title('Biểu đồ phân phối độ trễ Backend (35,000+ Requests, RPS ~3,500)', fontsize=14, pad=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 110)

# Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}ms', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()

# Ensure Images directory exists
os.makedirs('Images', exist_ok=True)
plt.savefig('Images/benchmark_latency.png', dpi=300)
print("Saved benchmark_latency.png")
