"""One-day world news image for 25 November 2026.

Copies the editorial infographic entry.png (a navy header naming the day,
then five numbered stories from 25 November 2026, each with a one-line
factual summary) to /output/entry.png, unchanged.
"""
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")
MAX_BYTES = 1048576
MAX_DIM = 1024

with open(SRC, "rb") as f:
    header = f.read(33)
if header[:8] != b"\x89PNG\r\n\x1a\n":
    raise ValueError("entry.png is not a PNG file")
if os.path.getsize(SRC) > MAX_BYTES:
    raise ValueError("entry.png is over 1 MiB")
width, height = struct.unpack(">II", header[16:24])
if width > MAX_DIM or height > MAX_DIM:
    raise ValueError("entry.png is larger than 1024 by 1024 pixels")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, OUT)
size = os.path.getsize(OUT)
print("Wrote", OUT, "(", size, "bytes )")
