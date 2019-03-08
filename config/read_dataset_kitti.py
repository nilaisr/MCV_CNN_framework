from os import listdir

dataset_dir = '/home/mcv/datasets/M5/classification/KITTI/'

f = open(dataset_dir+'train_images.txt')

for img in listdir(dataset_dir + 'train/'):
    f.write(img+'\n')


f.close()


f = open(dataset_dir+'valid_images.txt')

for img in listdir(dataset_dir + 'valid/'):
    f.write(img+'\n')


f.close()


f = open(dataset_dir+'test_images.txt')

for img in listdir(dataset_dir + 'test/'):
    f.write(img+'\n')


f.close()