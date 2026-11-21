
from huffman import compress_file, decompress_file
import os

print("\n====================================")
print("     HUFFMAN FILE COMPRESSION")
print("====================================")

while True:
    print("\n1. Compress a text file")
    print("2. Decompress a compressed file")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        input_file = input("Enter text file name: ")
        output_file = input("Enter output file name (default: compressed.huf): ")

        if not output_file:
            output_file = "compressed.huf"

        try:
            original_size, encoded_bits, codes = compress_file(
                input_file, output_file
            )

            compressed_size = os.path.getsize(output_file)

            print("\nCharacter Codes:")
            for char, code in codes.items():
                print(repr(char), ":", code)

            print("\n========== COMPRESSION RESULT ==========")
            print("Original Size:", original_size, "bytes")
            print("Encoded Bits:", encoded_bits)
            print("Actual Compressed File Size:", compressed_size, "bytes")

            if original_size > 0:
                saving = (1 - compressed_size / original_size) * 100
                print("Storage Saving:", round(saving, 2), "%")

                if compressed_size < original_size:
                    print("Result: File compressed successfully!")
                else:
                    print("Result: File is small; metadata overhead increased its size.")

            print("Compressed File:", output_file)

        except FileNotFoundError:
            print("Error: Input file not found!")

        except Exception as error:
            print("Compression Error:", error)

    elif choice == "2":
        input_file = input("Enter compressed file name: ")
        output_file = input("Enter output text file name (default: decompressed.txt): ")

        if not output_file:
            output_file = "decompressed.txt"

        try:
            decoded_text = decompress_file(input_file, output_file)

            print("\n========== DECOMPRESSION RESULT ==========")
            print("Decompression successful!")
            print("Recovered Text:", decoded_text)
            print("Output File:", output_file)

        except FileNotFoundError:
            print("Error: Compressed file not found!")

        except Exception as error:
            print("Decompression Error:", error)

    elif choice == "3":
        print("Thank you for using Huffman Compression!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
