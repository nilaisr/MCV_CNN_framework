import os
import argparse
parser   = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, default='',help='')

if __name__ == "__main__":
    FLAGS, unparsed = parser.parse_known_args()
    dataset = FLAGS.dataset_name
    path = "/home/grupo07/mcv/datasets/M5/segmentation/"+dataset
    path_to_save = "/home/grupo07/M5/MCV_CNN_framework/datasets_txt"
    arr = os.listdir(path)

    if "test" in arr:
        for folder in arr:
            if os.path.isdir(os.path.join(path, folder)):
                for subfolder in os.listdir(os.path.join(path, folder)):
                    if subfolder == "colors":
                        dir_images = []
                        for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                            dir_images.append(image)
                        dir_images.sort()
                        with open(path_to_save+"/"+dataset+"_"+folder+"_labels_"+subfolder+".txt", 'w') as f:
                            for item in dir_images:
                                f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                    if subfolder == "masks":
                        dir_images = []
                        for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                            dir_images.append(image)
                        dir_images.sort()
                        with open(path_to_save+"/"+dataset+"_"+folder+"_labels.txt", 'w') as f:
                            for item in dir_images:
                                f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                    if subfolder == "images":
                        dir_images = []
                        for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                            dir_images.append(image)
                        dir_images.sort()
                        with open(path_to_save+"/"+dataset+"_"+folder+"_images.txt", 'w') as f:
                            for item in dir_images:
                                f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))

    else:
        for folder in arr:
            if os.path.isdir(os.path.join(path, folder)):
                if folder == "train":
                    for subfolder in os.listdir(os.path.join(path, folder)):
                        if subfolder == "colors":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            with open(path_to_save+"/"+dataset+"_"+folder+"_labels_"+subfolder+".txt", 'w') as f:
                                for item in dir_images:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                        if subfolder == "masks":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            with open(path_to_save+"/"+dataset+"_"+folder+"_labels.txt", 'w') as f:
                                for item in dir_images:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                        if subfolder == "images":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            with open(path_to_save+"/"+dataset+"_"+folder+"_images.txt", 'w') as f:
                                for item in dir_images:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                if folder == "valid":
                    for subfolder in os.listdir(os.path.join(path, folder)):
                        if subfolder == "colors":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            dir_images_val = dir_images[:len(dir_images)//2]
                            dir_images_test = dir_images[len(dir_images)//2:]

                            with open(path_to_save+"/"+dataset+"_"+folder+"_labels_"+subfolder+".txt", 'w') as f:
                                for item in dir_images_val:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))

                            with open(path_to_save+"/"+dataset+"_"+"test_labels_"+subfolder+".txt", 'w') as f:
                                for item in dir_images_test:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))

                        if subfolder == "masks":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            dir_images_val = dir_images[:len(dir_images)//2]
                            dir_images_test = dir_images[len(dir_images)//2:]

                            with open(path_to_save+"/"+dataset+"_"+folder+"_labels.txt", 'w') as f:
                                for item in dir_images_val:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))

                            with open(path_to_save+"/"+dataset+"_"+"test_labels.txt", 'w') as f:
                                for item in dir_images_test:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))

                        if subfolder == "images":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            dir_images_val = dir_images[:len(dir_images)//2]
                            dir_images_test = dir_images[len(dir_images)//2:]

                            with open(path_to_save+"/"+dataset+"_"+folder+"_images.txt", 'w') as f:
                                for item in dir_images_val:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))

                            with open(path_to_save+"/"+dataset+"_"+"test_images.txt", 'w') as f:
                                for item in dir_images_test:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))


