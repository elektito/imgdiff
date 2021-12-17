# imgdiff

This is a tool to compare one image file against one or more others,
and create images containing the differences. Sample usage:

    ./imgdiff.py img1.png img{2..10}.png

This will create nine diff images named diff0.png to diff8.png. You
can specify only a region of the image to be compared using the
--region/-r argument:

    ./imgdiff.py img1.png img{2..10}.png -r 100,100,199,199

This compare the region with the top-left at (100, 100) and the
bottom-left at (199, 199). Both are inclusive.

## Note

If you're looking for a way to remove duplicate files in the output,
you can use the `fdupes` utility:

    fdupes -d .

