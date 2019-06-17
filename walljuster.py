#!/usr/bin/env python3

from typing import List, Tuple
from PIL import Image
import argparse
import sys
from pathlib import Path
import re

def main():
	args = parse_args()

	img_path = Path(args.image)
	img_ext = img_path.suffix

	img: Image.Image = Image.open(img_path)
	
	sizes: List[Size] = [Size.from_str(s) for s in args.sizes]

	w = 0
	h = 0
	x = args.x_offset or 0
	y = args.y_offset or 0

	out_path = img_path.stem + "-{}" + img_path.suffix

	for i, size in enumerate(sizes):
		crop = img.crop((
			w + x + size.x,
			h + y + size.y,
			w + size.w + x + size.x,
			h + size.h + y + size.y
		))
		w += crop.width
		crop.save(out_path.format(i), format=img.format)

class Size:
	def __init__(self, w, h, x, y):
		self.w = w
		self.h = h
		self.x = x
		self.y = y
	
	RE_FORMAT = re.compile(r"^(\d+)[xX](\d+)([-+]\d+){0,1}([-+]\d+){0,1}$")
	
	def from_str(s):
		m = re.match(Size.RE_FORMAT, s)

		if m is None:
			raise ValueError("Invalid size format: \"" + s + "\"")
		
		(w, h, x, y) = m.groups()
		return Size(int(w), int(h), int(x or 0), int(y or 0))

def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Split an image for use as a single wallpaper spread across multiple monitors."
	)
	parser.add_argument("image", help="Image to be processed.")
	parser.add_argument("sizes", nargs='+', help="Display sizes to split the image for, in `<width>x<height><x offset><y offset>` notation, such as \"1920x1080+3-4\". The \"x\" case-insensitive.")
	parser.add_argument("-x", "--x_offset", type=int, help="Offset all splits horizontally by the specified number of pixels.")
	parser.add_argument("-y", "--y_offset", type=int, help="Offset all splits vertically by the specified number of pixels.")
	return parser.parse_args();
	return parser.parse_args();

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)	

if __name__ == "__main__":
	sys.exit(main() or 0)