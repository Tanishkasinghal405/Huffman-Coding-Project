
import time
import os
import random
import string
import statistics

from huffman import compress_file

sizes = [1000, 5000, 10000, 50000]

random.seed(42)

print("\n==============================================")
print("       HUFFMAN PERFORMANCE ANALYSIS")
print("==============================================")

print(f"{'Input Size':<15}{'Compressed':<15}{'Time (ms)':<15}{'Saving %'}")
print("-" * 60)

for size in sizes:

    # Generate test data
    text = (
        "Huffman coding is a greedy algorithm "
        * (size // 45 + 1)
    )[:size]

    with open("benchmark_input.txt", "w", encoding="utf-8") as file:
        file.write(text)

    execution_times = []

    for _ in range(3):
        start = time.perf_counter()

        compress_file(
            "benchmark_input.txt",
            "benchmark_output.huf"
        )

        end = time.perf_counter()
        execution_times.append((end - start) * 1000)

    avg_time = statistics.median(execution_times)

    original_size = os.path.getsize("benchmark_input.txt")
    compressed_size = os.path.getsize("benchmark_output.huf")

    saving = (
        (1 - compressed_size / original_size) * 100
    )

    print(
        f"{original_size:<15}"
        f"{compressed_size:<15}"
        f"{avg_time:<15.3f}"
        f"{saving:.2f}%"
    )

print("\nPerformance testing completed!")
