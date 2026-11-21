
import matplotlib.pyplot as plt

from huffman import build_huffman_tree


def visualize_huffman_tree(root):

    if root is None:
        print("No data available!")
        return

    positions = {}
    edges = []

    counter = [0]

    def calculate_positions(node, depth=0):

        if node is None:
            return

        if node.left is None and node.right is None:
            x = counter[0]
            counter[0] += 1
        else:
            calculate_positions(node.left, depth + 1)
            calculate_positions(node.right, depth + 1)

            left_x = positions[id(node.left)][0] if node.left else 0
            right_x = positions[id(node.right)][0] if node.right else left_x

            x = (left_x + right_x) / 2

        positions[id(node)] = (x, -depth)

        if node.left:
            edges.append((node, node.left, "0"))

        if node.right:
            edges.append((node, node.right, "1"))

    calculate_positions(root)

    fig, ax = plt.subplots(figsize=(12, 7))

    # Draw branches
    for parent, child, label in edges:

        x1, y1 = positions[id(parent)]
        x2, y2 = positions[id(child)]

        ax.plot([x1, x2], [y1, y2], linewidth=2)

        ax.text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            label,
            fontsize=12
        )

    # Draw nodes
    def draw_nodes(node):

        if node is None:
            return

        x, y = positions[id(node)]

        if node.char is not None:
            character = repr(node.char)
            label = f"{character}\nFreq: {node.freq}"
        else:
            label = f"Freq: {node.freq}"

        ax.scatter(x, y, s=1400, zorder=3)

        ax.text(
            x, y,
            label,
            ha="center",
            va="center",
            fontsize=9,
            color="white"
        )

        draw_nodes(node.left)
        draw_nodes(node.right)

    draw_nodes(root)

    ax.set_title("Huffman Coding - Binary Tree Visualization")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig("huffman_tree.png")
    plt.show()

    print("Huffman Tree generated successfully!")


# Read input file
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Build tree and visualize
root = build_huffman_tree(text)

visualize_huffman_tree(root)
