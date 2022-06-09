import os
import shutil
from PIL import Image


path = "./"
resized_folder = path + 'resized/'
if not os.path.isdir(resized_folder):
    os.makedirs(resized_folder)
original_folder = path + 'original/'
if not os.path.isdir(original_folder):
    os.makedirs(original_folder)
dirs = os.listdir(path)
final_size = 128


def resize_aspect_fit():
    for item in dirs:
        not_allowed = ['.DS_Store', '.py', 'resized', '.db']
        skip = False
        for na in not_allowed:
            if na in item:
                skip = True
        if skip:
            continue

        if os.path.isfile(path + item):
            print(item)
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            size = im.size
            if size[0] > size[1]:
                ratio = float(final_size) / size[0]
                new_image_size = tuple([int(x * ratio) for x in size])
            else:
                ratio = float(final_size) / size[1]
                new_image_size = tuple([int(x * ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            im.save('./resized/' + f + '.png', 'PNG', quality=90)
            shutil.move(path + item, original_folder + item)


if __name__ == '__main__':
    resize_aspect_fit()
