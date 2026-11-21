
import matplotlib.pyplot as plt

# Performance data from your benchmark
sizes = [851, 4144, 8251, 41144]

times = [0.866, 2.142, 2.334, 7.770]

savings = [24.44, 43.77, 46.52, 48.72]

# Graph 1: Execution Time
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', linewidth=2)

plt.title("Huffman Coding - Execution Time Analysis")
plt.xlabel("Input File Size (Bytes)")
plt.ylabel("Execution Time (Milliseconds)")
plt.grid(True)

plt.savefig("execution_time.png")
plt.show()

# Graph 2: Storage Saving
plt.figure(figsize=(8, 5))
plt.plot(sizes, savings, marker='o', linewidth=2)

plt.title("Huffman Coding - Storage Saving Analysis")
plt.xlabel("Input File Size (Bytes)")
plt.ylabel("Storage Saving (%)")
plt.grid(True)

plt.savefig("storage_saving.png")
plt.show()

print("Both performance graphs generated successfully!")
