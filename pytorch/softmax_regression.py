import torch
from torch.distributions.multivariate_normal import MultivariateNormal
import matplotlib.pyplot as plt

mean = torch.tensor([[2., 2.], [8., 3.], [3., 6.]])
cov = torch.eye(2)

distribute1 = MultivariateNormal(mean[0], torch.eye(2))

x1 = torch.empty(30, 2)
for i in range(30):
    x1[i] = distribute1.sample()

print(x1)
print(x1.shape)
print(x1[0])


def display_somethings(x):
    plt.scatter(x[:, 0], x[:, 1])
    plt.show()


display_somethings(x1)
