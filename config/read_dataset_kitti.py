from os import listdir

dataset_dir = '/home/mcv/datasets/M5/classification/KITTI/'

f = open(dataset_dir+'train_images.txt',"w+")

for clas in listdir(dataset_dir + 'train/'):
    for img in listdir(dataset_dir + 'train/' + clas):
        f.write(img+'\n')

f.close()


f = open(dataset_dir+'valid_images.txt',"w+")

for img in listdir(dataset_dir + 'valid/'):
    for img in listdir(dataset_dir + 'valid/' + clas):
        f.write(img + '\n')

f.close()


f = open(dataset_dir+'test_images.txt',"w+")

for img in listdir(dataset_dir + 'test/'):
    for img in listdir(dataset_dir + 'test/' + clas):
        f.write(img + '\n')

f.close()
