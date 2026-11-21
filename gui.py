
import tkinter as tk
from tkinter import filedialog, messagebox
import os

from huffman import compress_file, decompress_file


# Main Window
root = tk.Tk()
root.title("Huffman File Compression System")
root.geometry("850x600")
root.resizable(False, False)
root.configure(bg="#101827")


# Colors
BG = "#101827"
CARD = "#1E293B"
ACCENT = "#38BDF8"
GREEN = "#22C55E"
WHITE = "#F8FAFC"
MUTED = "#94A3B8"


# Header
header = tk.Frame(root, bg=BG)
header.pack(pady=30)

tk.Label(
    header,
    text="HUFFMAN CODING",
    font=("Arial", 27, "bold"),
    fg=ACCENT,
    bg=BG
).pack()

tk.Label(
    header,
    text="Smart File Compression & Decompression System",
    font=("Arial", 11),
    fg=MUTED,
    bg=BG
).pack(pady=8)


# Main Card
card = tk.Frame(root, bg=CARD, padx=35, pady=25)
card.pack(padx=40, fill="both", expand=True)


tk.Label(
    card,
    text="Welcome!",
    font=("Arial", 22, "bold"),
    fg=WHITE,
    bg=CARD
).pack(pady=8)

tk.Label(
    card,
    text="Select an operation to get started",
    font=("Arial", 11),
    fg=MUTED,
    bg=CARD
).pack(pady=5)


# Result area
result_label = tk.Label(
    card,
    text="Your results will appear here.",
    font=("Arial", 11),
    fg=WHITE,
    bg="#334155",
    justify="left",
    wraplength=650,
    padx=20,
    pady=18
)
result_label.pack(fill="x", pady=20)


def compress_action():
    input_file = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save compressed file",
        defaultextension=".huf",
        filetypes=[("Huffman Files", "*.huf")]
    )

    if not output_file:
        return

    try:
        original_size, encoded_bits, codes = compress_file(
            input_file, output_file
        )

        compressed_size = os.path.getsize(output_file)

        if original_size > 0:
            saving = (1 - compressed_size / original_size) * 100
        else:
            saving = 0

        result = (
            "COMPRESSION SUCCESSFUL!\n\n"
            f"Original Size: {original_size} bytes\n"
            f"Compressed Size: {compressed_size} bytes\n"
            f"Encoded Bits: {encoded_bits}\n"
            f"Storage Saving: {saving:.2f}%\n\n"
            f"Saved File: {os.path.basename(output_file)}"
        )

        result_label.config(text=result, fg=GREEN)

        messagebox.showinfo(
            "Success",
            "Your file has been compressed successfully!"
        )

    except Exception as error:
        messagebox.showerror("Error", str(error))


def decompress_action():
    input_file = filedialog.askopenfilename(
        title="Select compressed file",
        filetypes=[("Huffman Files", "*.huf"), ("All Files", "*.*")]
    )

    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save decompressed file",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if not output_file:
        return

    try:
        decoded_text = decompress_file(input_file, output_file)

        result = (
            "DECOMPRESSION SUCCESSFUL!\n\n"
            f"Recovered Characters: {len(decoded_text)}\n"
            f"Output File: {os.path.basename(output_file)}\n\n"
            "Original text has been recovered."
        )

        result_label.config(text=result, fg=GREEN)

        messagebox.showinfo(
            "Success",
            "Your file has been decompressed successfully!"
        )

    except Exception as error:
        messagebox.showerror("Error", str(error))


# Buttons
button_frame = tk.Frame(card, bg=CARD)
button_frame.pack(pady=15)

compress_button = tk.Button(
    button_frame,
    text="COMPRESS FILE",
    command=compress_action,
    font=("Arial", 12, "bold"),
    bg=ACCENT,
    fg="#101827",
    activebackground="#0EA5E9",
    width=20,
    height=2,
    relief="flat",
    cursor="hand2"
)
compress_button.grid(row=0, column=0, padx=12, pady=10)


decompress_button = tk.Button(
    button_frame,
    text="DECOMPRESS FILE",
    command=decompress_action,
    font=("Arial", 12, "bold"),
    bg=GREEN,
    fg="#101827",
    activebackground="#16A34A",
    width=20,
    height=2,
    relief="flat",
    cursor="hand2"
)
decompress_button.grid(row=0, column=1, padx=12, pady=10)


# Footer
tk.Label(
    root,
    text="Developed using Python | Greedy Algorithm | Huffman Coding",
    font=("Arial", 9),
    fg=MUTED,
    bg=BG
).pack(pady=15)


root.mainloop()
