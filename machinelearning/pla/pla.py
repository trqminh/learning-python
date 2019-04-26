#ref: https://machinelearningcoban.com/2017/01/21/perceptron/
# I will add bias term someday

import numpy as np
import matplotlib.pyplot as plt


def plot_data(X):
  #plot data
  plt.scatter(X[:,0], X[:,1])



def plot_boundary(W, X, it):
  w1 = W[0,0]
  w2 = W[1,0]

  x_w = np.linspace(0,5,1000)
  y_w = (w1*x_w) / -w2  # w1*x1 + w2*x2 = 0

  pause_time = 2

  plot_data(X)
  if it == 1000:
    plt.title('Last result')
    pause_time = 100
  else:
    plt.title('it: ' + str(it))

  plt.plot(x_w, y_w)
  plt.show(block = False)
  plt.pause(pause_time)
  plt.close()


def count_misclassified(X, y, W):
  cnt = 0
  for i in range(X.shape[0]):
    tmp = np.sign(X[i].dot(W))
    if tmp == 0:
      tmp = 1

    X_tmp = X[i].reshape(-1, 1)
    if tmp != y[i]:
      cnt += 1

  return cnt


def pla(X, y):

  # init weight
  W = np.random.randn(X.shape[1], 1)
  it = 0

  while True:
    # sgd
    it += 1
    for i in range(X.shape[0]):
      tmp = np.sign(X[i].dot(W))
      if tmp == 0:
        tmp = 1

      X_tmp = X[i].reshape(-1, 1)
      if tmp != y[i]:
        W += X_tmp*y[i]

    # check converge
    mis_num = count_misclassified(X, y, W)
    if mis_num < 1:
      break

    plot_boundary(W, X, it)


  return W



def main():

  means = [[2, 2], [4, 2]]
  cov = [[.3, .2], [.2, .3]]

  N = 10

  X0 = np.random.multivariate_normal(means[0], cov, N)
  X1 = np.random.multivariate_normal(means[1], cov, N)

  X = np.concatenate((X0, X1), axis=0)

  # assign label
  y = []
  for i in range(2*N):
    if (i < 10):
      y.append(-1)
    else:
      y.append(1)


  #plot data
  plot_data(X)
  plt.title('Init Data')
  plt.show(block=False)
  plt.pause(3)
  plt.close()


  W = pla(X, y)


  #plot boundary
  plot_boundary(W,X, 1000)




if __name__ == '__main__':
    main()
