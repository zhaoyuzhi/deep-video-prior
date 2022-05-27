import os
import cv2
import numpy as np
import argparse

def text_readlines(filename):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename, 'r')
    except IOError:
        error = []
        return error
    content = file.readlines()
    # This for loop deletes the EOF (like \n)
    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]
    file.close()
    return content

def savetxt(name, loss_log):
    np_loss_log = np.array(loss_log)
    np.savetxt(name, np_loss_log)

def get_files(path):
    # read a folder, return the complete path
    ret = []
    for root, dirs, files in os.walk(path):
        for filespath in files:
            ret.append(os.path.join(root, filespath))
    return ret

def get_jpgs(path):
    # read a folder, return the image name
    ret = []
    for root, dirs, files in os.walk(path):
        for filespath in files:
            ret.append(filespath)
    return ret

def text_save(content, filename, mode = 'a'):
    # save a list to a txt
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]) + '\n')
    file.close()

def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


parser = argparse.ArgumentParser()
parser.add_argument("--dvp_result_path", type=str, default='./result/colorization', help="")
parser.add_argument("--save_path", type=str, \
    default='/home/zyz/Documents/SVCNet/DVP_results', help="")
ARGS = parser.parse_args()

ret = get_files(ARGS.dvp_result_path)
# print(ret)
# [..., './result/colorization/CIC+DVP/DAVIS/car-roundabout/0025/predictions_00070.png', 
# './result/colorization/CIC+DVP/DAVIS/car-roundabout/0025/out_main_00006.png', 
# './result/colorization/CIC+DVP/DAVIS/car-roundabout/0025/out_main_00021.png', 
# './result/colorization/CIC+DVP/DAVIS/car-roundabout/0025/predictions_00054.png', ...]

for i in range(len(ret)):
    # only save the result images
    if 'out_main_' in ret[i] and '.png' in ret[i]:
        img = cv2.imread(ret[i])
        method_name = ret[i].split('/')[-5]
        dataset_name = ret[i].split('/')[-4]
        subfolder_name = ret[i].split('/')[-3]
        img_name = ret[i].split('/')[-1].split('out_main_')[-1]

        save_folder = os.path.join(ARGS.save_path, method_name, dataset_name, subfolder_name)
        check_path(save_folder)
        save_img_path = os.path.join(ARGS.save_path, method_name, dataset_name, subfolder_name, img_name)
        cv2.imwrite(save_img_path, img)
        print(i, len(ret), save_img_path)
