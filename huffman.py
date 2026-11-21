
import heapq
import json
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    return build_tree_from_frequency(frequency)


def build_tree_from_frequency(frequency):
    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    if not heap:
        return None

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root):
    codes = {}

    def traverse(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code or "0"
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return codes


def encode(text, codes):
    return ''.join(codes[char] for char in text)


def decode(encoded, root):
    if root is None:
        return ""

    if root.char is not None:
        return root.char * len(encoded)

    result = []
    current = root

    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            result.append(current.char)
            current = root

    return ''.join(result)


def compress_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    frequency = Counter(text)
    root = build_tree_from_frequency(frequency)
    codes = generate_codes(root)

    encoded = encode(text, codes)
    bit_length = len(encoded)

    # Convert bits into actual binary bytes
    payload = bytearray()

    for i in range(0, bit_length, 8):
        chunk = encoded[i:i + 8].ljust(8, "0")
        payload.append(int(chunk, 2))

    # Store frequency information and bit length
    metadata = {
        "frequency": dict(frequency),
        "bit_length": bit_length
    }

    header = json.dumps(
        metadata, ensure_ascii=False
    ).encode("utf-8")

    # Format: 4-byte header length + header + binary data
    with open(output_file, "wb") as file:
        file.write(len(header).to_bytes(4, "big"))
        file.write(header)
        file.write(payload)

    return len(text.encode("utf-8")), len(encoded), codes


def decompress_file(input_file, output_file):
    with open(input_file, "rb") as file:
        header_size = int.from_bytes(file.read(4), "big")
        header = json.loads(file.read(header_size).decode("utf-8"))
        payload = file.read()

    frequency = header["frequency"]
    bit_length = header["bit_length"]

    root = build_tree_from_frequency(frequency)

    # Convert binary bytes back into bits
    bits = ''.join(format(byte, "08b") for byte in payload)
    bits = bits[:bit_length]

    decoded_text = decode(bits, root)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(decoded_text)

    return decoded_text

