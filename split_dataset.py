import os 
from glob import glob
from natsort import natsorted
import random
import shutil

PATH = './datasets'

VAL_RATIO = 0.2
SEED = 110511233

random.seed(SEED)

if not os.path.exists(os.path.join(PATH, 'images/val')):
    os.mkdir(os.path.join(PATH, 'images/val'))

if not os.path.exists(os.path.join(PATH, 'labels/val')):
    os.mkdir(os.path.join(PATH, 'labels/val'))

image_names = natsorted(glob(os.path.join(PATH, 'images/train', '*.jpg')))

assert len(image_names) == 4715

image_names = list(map(lambda x: os.path.basename(x), image_names))
random.shuffle(image_names)

train_set, val_set = image_names[:int(len(image_names)*(1-VAL_RATIO))], \
    image_names[int(len(image_names)*(1-VAL_RATIO)):]

for x in val_set:
    shutil.move(os.path.join(PATH, 'images/train', x), os.path.join(PATH, 'images/val', x))
    x = x.replace('.jpg', '.txt')
    shutil.move(os.path.join(PATH, 'labels/train', x), os.path.join(PATH, 'labels/val', x))

train_set = natsorted(train_set)
train_set = list(map(lambda x: os.path.join('datasets/images/train', x).replace("\\","/"), train_set))

with open(os.path.join(PATH, 'train_list.txt'), 'w') as f:
    f.write('\n'.join(train_set))

val_set = natsorted(val_set)
val_set = list(map(lambda x: os.path.join('datasets/images/val', x).replace("\\","/"), val_set))

with open(os.path.join(PATH, 'val_list.txt'), 'w') as f:
    f.write('\n'.join(val_set))

