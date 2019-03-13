# ref: https://github.com/vanhuyz/udacity-dl/blob/master/1_notmnist.ipynb

import numpy as np
import os
import matplotlib.pyplot as plt

data_root = '.'


def load_and_show(bin_filename):
    a = np.load(bin_filename)
    plt.imshow(a[0], cmap='Greys_r')  # cmap for geting grayscale color
    plt.show()


def main():
    image_dataset = 'image_folder_B'
    bin_filename = os.path.join(data_root, image_dataset) + '.pickle'
    load_and_show(bin_filename)


if __name__ == '__main__':
    main()
