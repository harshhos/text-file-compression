from huffman import HuffmanCoding
from time import sleep
import os
from tkinter import filedialog
from tkinter import Tk



def open_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.update()
    original_size = os.path.getsize(file_path)
    print(f'Original size:{original_size}')
    return file_path


path = open_file()

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)