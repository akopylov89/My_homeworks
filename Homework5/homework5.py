import os
import Image
import sys
input_file_directory = sys.argv[1]
for d, dirs,pictures in os.walk(input_file_directory):
    for picture in pictures:
        full_path = d + os.path.sep + picture
        im = Image.open(full_path)
        new_width  = im.size[0] / 2
        new_height = im.size[1] / 2
        im = im.resize(new_width, new_height)
        im = im.save(d + os.path.sep + 'resised_' + picture)


# python homework5.py d:/python/homework5/pictures
