import os


if __name__ == "__main__":
    dataset = "kitti"
    path = "home/grupo07/mcv/datasets/M5/segmentation/"+dataset
    path_to_save = "home/grupo07/M5/MCV_CNN_framework/datasets_txt"
    arr = os.listdir(path)

    image_format = None

    if "test" in arr:
        for folder in arr:
            if os.path.isdir(os.path.join(path, folder)):
                for subfolder in os.listdir(os.path.join(path, folder)):
                    if subfolder == "colors":
                        dir_images = []
                        for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                            dir_images.append(image)
                        dir_images.sort()
                        with open(path_to_save+"/"+folder+"_labels_"+subfolder+".txt", 'w') as f:
                            for item in dir_images:
                                f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                    if subfolder == "masks":
                        dir_images = []
                        for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                            dir_images.append(image)
                        dir_images.sort()
                        with open(path+"/"+folder+"_labels.txt", 'w') as f:
                            for item in dir_images:
                                f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                    if subfolder == "images":
                        dir_images = []
                        for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                            dir_images.append(image)
                        dir_images.sort()
                        with open(path+"/"+folder+"_images.txt", 'w') as f:
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
                            with open(path+"/"+folder+"_labels_"+subfolder+".txt", 'w') as f:
                                for item in dir_images:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                        if subfolder == "masks":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            with open(path+"/"+folder+"_labels.txt", 'w') as f:
                                for item in dir_images:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                        if subfolder == "images":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            with open(path+"/"+folder+"_images.txt", 'w') as f:
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
                            with open(path+"/"+folder+"_labels_"+subfolder+".txt", 'w') as f:
                                for item in dir_images_val:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                            with open(path+"/"+"test_labels_"+subfolder+".txt", 'w') as f:
                                for item in dir_images_test:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                        if subfolder == "masks":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            dir_images_val = dir_images[:len(dir_images)//2]
                            dir_images_test = dir_images[len(dir_images)//2:]
                            with open(path+"/"+folder+"_labels.txt", 'w') as f:
                                for item in dir_images_val:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                            with open(path+"/"+"test_labels.txt", 'w') as f:
                                for item in dir_images_test:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                        if subfolder == "images":
                            dir_images = []
                            for image in os.listdir(os.path.join(path, folder+"/"+subfolder)):
                                dir_images.append(image)
                            dir_images.sort()
                            dir_images_val = dir_images[:len(dir_images)//2]
                            dir_images_test = dir_images[len(dir_images)//2:]
                            with open(path+"/"+folder+"_images.txt", 'w') as f:
                                for item in dir_images_val:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))
                            with open(path+"/"+"test_images.txt", 'w') as f:
                                for item in dir_images_test:
                                    f.write("%s\n" % (path+"/"+folder+"/"+subfolder+"/"+item))


