#merge datasets which each datasets illustrate one class
#the final dataset consists training, validation set

# ref: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb

import os
import numpy as np
import sys
import pickle
import matplotlib.pyplot as plt


image_sz = 28

def merge_data(list_of_datasets, train_size, valid_size=0):
    num_classes = len(list_of_datasets) 

    #init validation dataset
    valid_dataset = np.ndarray(shape = (valid_size, image_sz, image_sz), dtype= np.float32)
    valid_labels = np.ndarray(valid_size, dtype = np.int32)
    vsize_per_class = valid_size // num_classes
    start_v = 0
    end_v = vsize_per_class

    #init training dataset
    train_dataset = np.ndarray(shape = (train_size, image_sz, image_sz), dtype= np.float32)
    train_labels = np.ndarray(train_size, dtype = np.int32)
    tsize_per_class = train_size // num_classes
    start_t = 0
    end_t = tsize_per_class



    for label, pickle_file in enumerate(list_of_datasets):
        try:
            with open(pickle_file, 'rb') as f:
                letter_set = pickle.load(f)   #for example: set of letter A
                np.random.shuffle(letter_set)

                valid_letter = letter_set[:vsize_per_class, :,:]
                valid_dataset[start_v:end_v, :, :] = valid_letter
                valid_labels[start_v: end_v] = label
                
                start_v += vsize_per_class
                end_v += vsize_per_class
                
                ###########################################
                train_letter = letter_set[vsize_per_class:(vsize_per_class+tsize_per_class), :,:]
                train_dataset[start_t:end_t, :,:] = train_letter
                train_labels[start_t: end_t] = label

                start_t += tsize_per_class
                end_t += tsize_per_class

        except Exception as e:
            print('Fail')
            raise


    return valid_dataset, valid_labels, train_dataset, train_labels


def randomize_shuffle(dataset, labels):
    permut = np.random.permutation(labels.shape[0])
    shuffled_dataset = dataset[permut, :, :]
    shuffle_labels = labels[permut]
    return shuffled_dataset, shuffle_labels



def main():
    train_size = 12
    valid_size = 6

    list_of_datasets = ['./image_folder_A.pickle', './image_folder_B.pickle', './image_folder_C.pickle']
    v_data, v_labels, t_data, t_labels = merge_data(list_of_datasets,train_size, valid_size)
    print(v_data.shape, t_data.shape)

    v_data, v_labels = randomize_shuffle(v_data, v_labels)
    t_data, t_labels = randomize_shuffle(t_data, t_labels)

    #show validation dataset
    for i in range(len(v_data)):
        plt.imshow(v_data[i],cmap = 'Greys_r')
        plt.title('Letter: ' + chr(65+ v_labels[i]))
        plt.show()
    
    
    #show training dataset
    for i in range(len(t_data)):
        plt.imshow(t_data[i],cmap = 'Greys_r')
        plt.title('Letter: ' + chr(65+ t_labels[i]))
        plt.show()
  


if __name__ == '__main__':
    main()
