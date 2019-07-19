import torch
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.dataset import Dataset

from datapoint_generator import DataPoint2DGenerator
from softmax_regression import SoftmaxRegression
from my_data import MyDataset
import matplotlib.pyplot as plt
import numpy as np

def draw(w, b):
    x = np.linspace(0, 10, 100)
    y = (w[0] * x + b) / -w[1]

    plt.plot(x, y)


mean = [[2., 2.], [8., 3.], [3., 6.]]
cov = [[1., 0.], [0., 1.]]

data_generator = DataPoint2DGenerator(mean, cov, [10, 10, 10])
data = data_generator.generate()
data_generator.display()

dataset = MyDataset(data[0], data[1])

soft_reg = SoftmaxRegression(dataset, data_generator.num_class)
soft_reg.train()


# accuracy on train set
print('accuracy on train set: ', soft_reg.accuracy_on_train_set())

params = list(soft_reg.weights.parameters())

weight = params[0]
bias = params[1]


# print((weight[0] - weight[1]).numpy())
# print((bias[0] - bias[1]).numpy())

with torch.no_grad():
    for i in range(0, weight.shape[0] - 1, 1):
        for j in range(i+1, weight.shape[0], 1):
            w = weight[i] - weight[j]
            b = bias[i] - bias[j]
            w = w.numpy()
            b = b.numpy()
            draw(w, b)


plt.show()



#draw([1, 1], 0)
#plt.show()