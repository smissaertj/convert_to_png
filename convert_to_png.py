#!/usr/bin/env python3
#
# python3 convert_to_png.py /path/to/src_path/ /path/to/dst_path/
#

import sys
import os
from PIL import Image


try:
    # Check if the user provided the src_path and dst_path arguments
    if len(sys.argv) < 3:
        raise IndexError
    else:
        src_path = sys.argv[1]
        dst_path = sys.argv[2]

        # Ensure the dst_path exists or is created
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)

        # Check if the src_path has files
        if len(os.listdir(src_path)) == 0:
            raise IOError

        # Loop through the files in the src_path, convert and save to dst_path as PNG
        for index, file_name in enumerate(os.listdir(src_path)):
            img = Image.open(os.path.join(src_path, file_name))
            img.save(os.path.join(dst_path, file_name[:-4]+'.png'), 'png')

except IndexError:
    print('Please provide a source and destination path!')

except IOError:
    print('Make sure the source path exists and has files!')

else:
    print('Image conversion completed!')