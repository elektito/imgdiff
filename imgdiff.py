#!/usr/bin/env python3

import argparse
from PIL import Image


class Region:
    def __init__(self, value):
        x1, y1, x2, y2 = value.split(',')
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)


    def __contains__(self, point):
        x, y = point
        return x >= self.x1 and y >= self.y1 and \
            x <= self.x2 and y <= self.y2


def main():
    parser = argparse.ArgumentParser(description='Image diff tool.')

    parser.add_argument(
        'base_image',
        help='Base image.')
    parser.add_argument(
        'derived_image', nargs='+',
        help='Image to diff against base image.')
    parser.add_argument(
        '--region', '-r', type=Region,
        help='The region of the image to diff. A comma separated of '
        'four integers, the first two being the coordinates of '
        'top-left of the region, and the second two the coordinates '
        'of bottom-left.')

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
        diff = get_image_diff(base_image, base_pixels, derived_pixels,
                              region=args.region)
        diff.save(f'diff{i}.png')


def get_image_diff(base_image, base_pixels, derived_pixels, region):
    diff = Image.new(base_image.mode, base_image.size, color='white')
    diff.putpalette(base_image.palette)

    diffpixels = diff.load()

    for x in range(base_image.size[0]):
        for y in range(base_image.size[1]):
            if (x, y) not in region:
                continue
            pixel1 = base_pixels[x, y]
            pixel2 = derived_pixels[x, y]
            if pixel1 != pixel2:
                diffpixels[x, y] = pixel2

    return diff


if __name__ == '__main__':
    main()
