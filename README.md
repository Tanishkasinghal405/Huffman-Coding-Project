# Huffman Coding File Compression System

## Project Overview
This project implements a file compression and decompression system using the **Huffman Coding Algorithm**, a lossless data compression technique based on variable-length prefix codes.

The system assigns shorter binary codes to frequently occurring characters and longer codes to less frequent characters, helping reduce file size without losing information.

## Features
- Lossless file compression
- File decompression
- Huffman Tree construction using a Priority Queue
- Binary file storage
- Graphical User Interface (GUI) using Tkinter
- Benchmark testing for different input sizes
- Graphical performance visualization

## Technologies Used
- Python
- Heapq
- Tkinter
- Matplotlib
- JSON

## Project Structure
```text
Huffman-Coding-Project/
│
├── main.py
├── huffman.py
├── gui.py
├── benchmark.py
├── graph.py
├── tree_visualization.py
├── sample.txt
├── execution_time.png
├── storage_saving.png
└── huffman_tree.png
```

## Algorithm
1. Calculate the frequency of each character.
2. Create leaf nodes for each character.
3. Insert nodes into a Min Heap.
4. Build the Huffman Tree by repeatedly combining the two nodes with the lowest frequencies.
5. Generate binary codes from the tree.
6. Encode the input file and save the compressed output.
7. Decode the compressed file to recover the original content.

## How to Run

### 1. Run the command-line application
```bash
py main.py
```

### 2. Run the GUI application
```bash
py gui.py
```

### 3. Run Benchmark
```bash
py benchmark.py
```

### 4. Generate Graphs
```bash
py graph.py
```

### 5. Generate Huffman Tree Visualization
```bash
py tree_visualization.py
```

## Performance Analysis
The project evaluates:
- Compression ratio
- Storage savings
- Execution time
- Performance across different input sizes

## Applications
- Data compression
- File storage optimization
- Data transmission
- Lossless encoding systems

## Conclusion
The project demonstrates the practical implementation of Huffman Coding using Data Structures and Algorithms. It shows how Greedy Algorithms and Priority Queues can be used to achieve efficient lossless data compression.

---
**Developed as a Data Structures and Algorithms (DAA) Project.**
