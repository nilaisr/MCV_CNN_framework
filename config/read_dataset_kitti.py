from os import listdir

dataset_dir = '/home/mcv/datasets/M5/classification/KITTI/'

save_dir = '/home/M5/MCV_CNN_framework/'

f = open(save_dir+'train_images.txt',"w+")

print('pas1')

for clas in listdir(dataset_dir + 'train/'):
    print('pas2')
    for img in listdir(dataset_dir + 'train/' + clas + '/'):
        f.write(img+'\n')
        print('pas3')

f.close()


f = open(save_dir+'valid_images.txt',"w+")

for img in listdir(dataset_dir + 'valid/'):
    for img in listdir(dataset_dir + 'valid/' + clas + '/'):
        f.write(img + '\n')

f.close()


f = open(save_dir+'test_images.txt',"w+")

for img in listdir(dataset_dir + 'test/'):
    for img in listdir(dataset_dir + 'test/' + clas + '/'):
        f.write(img + '\n')

f.close()
