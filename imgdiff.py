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
    base_image = Image.open(args.base_image)
    derived_images = [Image.open(i) for i in args.derived_image]

    for img in derived_images:
        if base_image.size != img.size:
            print('Images dot not have the same size.')
            exit(1)

        if base_image.mode != img.mode:
            print('Images do not have the same mode.')
            exit(1)

    base_pixels = base_image.load()
    for i, img in enumerate(derived_images):
        derived_pixels = img.load()
        diff = get_image_diff(base_image, base_pixels, derived_pixels)
        diff.save(f'diff{i}.png')


def get_image_diff(base_image, base_pixels, derived_pixels):
    diff = Image.new(base_image.mode, base_image.size, color='white')
    diff.putpalette(base_image.palette)

    diffpixels = diff.load()

    for x in range(base_image.size[0]):
        for y in range(base_image.size[1]):
            pixel1 = base_pixels[x, y]
            pixel2 = derived_pixels[x, y]
            if pixel1 != pixel2:
                diffpixels[x, y] = pixel2

    return diff


if __name__ == '__main__':
    main()
