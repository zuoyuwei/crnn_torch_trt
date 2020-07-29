import glob
import os

imgs_path = ''
label_txt = ''
imgs_name = os.listdir(imgs_path)
for img_name in imgs_name:
    img = img_name.split()
    label = img_name.split()
    with open(label_txt, 'w') as f:
        f.write(img_name + ' ' + label)
        f.write('\n')
