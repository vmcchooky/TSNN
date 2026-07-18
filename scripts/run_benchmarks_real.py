import asyncio
import aiohttp
import time
import numpy as np
import random
import json

URL = "http://127.0.0.1:8080/v1/analyze?domain="

async def fetch(session, domain):
    start = time.time()
    try:
        async with session.get(URL + domain, timeout=5) as response:
            await response.read()
            return time.time() - start
    except Exception:
        return time.time() - start

async def benchmark_concurrency(domains, concurrency, duration=5):
    async with aiohttp.ClientSession() as session:
        end_time = time.time() + duration
        reqs = 0
        
        async def worker():
            nonlocal reqs
            while time.time() < end_time:
                domain = random.choice(domains)
                await fetch(session, domain)
                reqs += 1
                
        tasks = [asyncio.create_task(worker()) for _ in range(concurrency)]
        await asyncio.gather(*tasks)
        return reqs / duration

async def measure_latency(domains, samples=20):
    async with aiohttp.ClientSession() as session:
        latencies = []
        for _ in range(samples):
            domain = random.choice(domains)
            lat = await fetch(session, domain)
            latencies.append(lat * 1000) # ms
        return np.mean(latencies), latencies

async def main():
    print("Gathering real benchmark data...")
    
    # 1. Measure Latency
    print("Measuring Latency...")
    # Cache (Redis/Bloom): known domain, hit repeatedly
    cache_avg, _ = await measure_latency(["google.com"], samples=50)
    
    # SQLite / Local (Miss cache, but lexical safe):
    sqlite_avg, _ = await measure_latency([f"local-safe-{random.randint(1,10000)}.com" for _ in range(50)], samples=50)
    
    # AI (Suspicious domain triggering AI):
    # Using 'verify-account-update' usually triggers high lexical score but maybe ambiguous
    ai_avg, ai_distribution = await measure_latency([f"verify-account-update-{random.randint(1,10000)}.com" for _ in range(20)], samples=20)
    
    print(f"Cache Latency: {cache_avg:.2f} ms")
    print(f"SQLite Latency: {sqlite_avg:.2f} ms")
    print(f"AI Latency: {ai_avg:.2f} ms")
    
    # 2. Measure Throughput
    print("Measuring Throughput...")
    concurrencies = [10, 50, 100, 200, 500, 1000]
    qps_cache = []
    qps_ai = []
    
    for c in concurrencies:
        print(f"  Testing concurrency {c} for Cache...")
        q_cache = await benchmark_concurrency(["google.com"], c, duration=3)
        qps_cache.append(int(q_cache))
        
        # Lower duration for AI to not abuse API limits excessively
        print(f"  Testing concurrency {c} for AI...")
        # Since it takes long, just 2 seconds
        q_ai = await benchmark_concurrency([f"ai-test-{random.randint(1,10000)}.com" for _ in range(100)], c, duration=2)
        qps_ai.append(int(q_ai))
        
    print("QPS Cache:", qps_cache)
    print("QPS AI:", qps_ai)
    
    # 3. Output a new plotting script
    with open("plot_real.py", "w", encoding="utf-8") as f:
        f.write(f'''
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.style.use('bmh')

def plot_latency():
    plt.figure(figsize=(8, 5))
    scenarios = ['Redis Cache Hit', 'SQLite Local Hit', 'AI Inference (Miss)']
    latency = [{cache_avg:.1f}, {sqlite_avg:.1f}, {ai_avg:.1f}]
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    bars = plt.bar(scenarios, latency, color=colors, width=0.6)
    plt.title('So sánh độ trễ phân giải tên miền (Thực tế)', fontsize=14, pad=15)
    plt.ylabel('Độ trễ trung bình (ms)', fontsize=12)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + (max(latency)*0.02), f'{{yval}} ms', ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig('../img/benchmark_latency.png', dpi=300)
    plt.close()

def plot_throughput():
    plt.figure(figsize=(8, 5))
    concurrency = {concurrencies}
    qps_cache = {qps_cache}
    qps_ai = {qps_ai}
    plt.plot(concurrency, qps_cache, marker='o', linewidth=2.5, color='#2ecc71', label='Cache Hit (Redis)')
    plt.plot(concurrency, qps_ai, marker='s', linewidth=2.5, color='#e74c3c', label='AI Inference (Miss)')
    plt.title('Khả năng chịu tải thực tế (Throughput)', fontsize=14, pad=15)
    plt.xlabel('Số lượng kết nối đồng thời (Concurrency)', fontsize=12)
    plt.ylabel('Truy vấn mỗi giây (QPS)', fontsize=12)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig('../img/benchmark_throughput.png', dpi=300)
    plt.close()

def plot_inference():
    plt.figure(figsize=(8, 5))
    data = {ai_distribution}
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='#9b59b6', color='#8e44ad'),
                medianprops=dict(color='white', linewidth=2), vert=False)
    plt.title('Phân phối thời gian suy luận AI (Thực tế)', fontsize=14, pad=15)
    plt.xlabel('Thời gian phản hồi (ms)', fontsize=12)
    plt.yticks([1], ['Mô hình AI'])
    plt.tight_layout()
    plt.savefig('../img/benchmark_inference.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    plot_latency()
    plot_throughput()
    plot_inference()
    print("New real charts generated!")
''')

if __name__ == "__main__":
    asyncio.run(main())
