#!/usr/bin/env python3

import argparse
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description='Image diff tool.')

    parser.add_argument(
        'base_image',
        help='Base image.')
    parser.add_argument(
        'derived_image', nargs='+',
        help='Image to diff against base image.')

    args = parser.parse_args()
    img1 = Image.open(args.base_image)
    img2 = Image.open(args.derived_image)
    pixels1 = img1.load()
    pixels2 = img2.load()

    if img1.size != img2.size:
        print('Images dot not have the same size.')
        exit(1)

    if img1.mode != img2.mode:
        print('Images do not have the same mode.')
        exit(1)

    diff = Image.new(img1.mode, img1.size, color='white')
    diff.putpalette(img1.palette)

    diffpixels = diff.load()

    for x in range(img1.size[0]):
        for y in range(img1.size[1]):
            pixel1 = pixels1[x, y]
            pixel2 = pixels2[x, y]
            if pixel1 != pixel2:
                diffpixels[x, y] = pixel2
    diff.save('diff.png')


if __name__ == '__main__':
    main()
