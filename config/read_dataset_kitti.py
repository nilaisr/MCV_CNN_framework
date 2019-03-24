from os import listdir

dataset_dir = '/home/grupo07/mcv/datasets/M5/classification/KITTI/'

save_dir = '/home/grupo07/M5/MCV_CNN_framework/kitti_txt/'

f = open(save_dir+'train_images.txt',"w+")

for clas in listdir(dataset_dir + 'train/'):
    for img in listdir(dataset_dir + 'train/' + clas + '/'):
        f.write(dataset_dir + 'train/' + clas + '/' + img+'\n')

f.close()


f = open(save_dir+'valid_images.txt',"w+")

for img in listdir(dataset_dir + 'valid/'):
    for img in listdir(dataset_dir + 'valid/' + clas + '/'):
        f.write(dataset_dir + 'train/' + clas + '/' + img + '\n')

f.close()


f = open(save_dir+'test_images.txt',"w+")

for img in listdir(dataset_dir + 'test/'):
    for img in listdir(dataset_dir + 'test/' + clas + '/'):
        f.write(dataset_dir + 'train/' + clas + '/' + img + '\n')

f.close()




f = open(save_dir+'train_gt.txt',"w+")

for clas in listdir(dataset_dir + 'train/'):
    for img in listdir(dataset_dir + 'train/' + clas + '/'):
        f.write(clas +'\n')

f.close()


f = open(save_dir+'valid_gt.txt',"w+")

for img in listdir(dataset_dir + 'valid/'):
    for img in listdir(dataset_dir + 'valid/' + clas + '/'):
        f.write(clas +'\n')

f.close()


f = open(save_dir+'test_gt.txt',"w+")

for img in listdir(dataset_dir + 'test/'):
    for img in listdir(dataset_dir + 'test/' + clas + '/'):
        f.write(clas +'\n')

f.close()