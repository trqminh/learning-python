# this code for store a dataset of image to a binary file
# which is a 3D array (image index, x, y) of floating point values,
# normalized to have approximately zero mean and standard deviation ~0.5
# purpose: more manageable and easy to train

# ref: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb

import os
import imageio
import numpy as np
import pickle


image_size = 28
pixel_depth = 255.0
data_root = '.'


def store_set_of_image_to_3d_array(image_dataset):
    image_files = os.listdir(os.path.join(data_root, image_dataset))  # list of img file name in dataset

    # an 3d array to store all images data in the dataset with (image index, x, y)
    result_dataset = np.ndarray(shape=(len(image_files), image_size, image_size), dtype=np.float32)

    num_of_image = 0  # number of image in dataset

    for image_file in image_files:
        image_file_dir = os.path.join(data_root, os.path.join(image_dataset, image_file))
        # print(image_file_dir)
        data_in_image_file = (imageio.imread(image_file_dir).astype(float) - pixel_depth / 2) / pixel_depth
        result_dataset[num_of_image, :, :] = data_in_image_file
        num_of_image += 1

    # print(result_dataset[0].shape) #verify the dimension

    return result_dataset


def dump_set_of_image_to_binary_file(image_dataset, force=False):
    _3d_array_dataset = store_set_of_image_to_3d_array(image_dataset)
    binary_file_name = os.path.join(data_root, image_dataset) + '.pickle'

    if os.path.exists(binary_file_name) and not force:
        print('Already exist')
    else:
        print('Dumping...')
        try:
            with open(binary_file_name, 'wb') as f:
                pickle.dump(_3d_array_dataset, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print('Unable to save data to', binary_file_name, ':', e)

    return binary_file_name


def main():
    image_dataset_A = 'image_folder_A'
    image_dataset_B = 'image_folder_B'
    image_dataset_C = 'image_folder_C'
    dump_set_of_image_to_binary_file(image_dataset_A)
    dump_set_of_image_to_binary_file(image_dataset_B)
    dump_set_of_image_to_binary_file(image_dataset_C)



if __name__ == '__main__':
    main()
