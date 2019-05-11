import numpy as np
import matplotlib.pyplot as plt
import scipy.special


def compute_logits(X, W, biases):
  # sofmax function
  hX = X.dot(W) + biases
  hX = np.exp(hX - np.max(hX, axis=1, keepdims=True))
  return hX / ((np.sum(hX, axis=1)).reshape(-1, 1))


def softmax_regression(X, y, learning_rate):
  #init weight
  W = np.random.randn(X.shape[1], y.shape[1])
  biases = np.ones(shape=[X.shape[0], y.shape[1]], dtype=np.float32)

  # batch gradient descent
  it = 10000
  while it:
    it -= 1
    logits = compute_logits(X, W, biases)
    W -= learning_rate*X.transpose().dot(logits - y)
    biases -= learning_rate*(logits - y)

  return W, biases


def main():
  means = [[2, 2], [8, 3], [3, 6]]
  cov = [[1, 0], [0, 1]]
  N = 500
  num_labels = 3

  X0 = np.random.multivariate_normal(means[0], cov, N)
  X1 = np.random.multivariate_normal(means[1], cov, N)
  X2 = np.random.multivariate_normal(means[2], cov, N)

  X = np.concatenate((X0, X1, X2), axis=0)

  y = np.ndarray(shape=[X.shape[0], num_labels], dtype=np.int32)

  # assign label
  for i in range(X.shape[0]):
    if i < N:
      y[i] = np.array([1, 0, 0], dtype=np.int32)
    elif i >= N and i < 2*N:
      y[i] = np.array([0, 1, 0], dtype=np.int32)
    else:
      y[i] = np.array([0, 0, 1], dtype=np.int32)


  learning_rate = 0.1
  W, biases = softmax_regression(X, y, learning_rate)

  x_w = np.linspace(0, 10, 5000)
  y_w = ((W[0][1] - W[0][0])*x_w + (biases[0][1] - biases[0][0])) / (W[1][0] - W[1][1])

  x_w1 = np.linspace(0, 10, 5000)
  y_w1 = ((W[0][0] - W[0][2])*x_w + (biases[0][0] - biases[0][2])) / (W[1][2] - W[1][0])

  x_w2 = np.linspace(0, 10, 5000)
  y_w2 = ((W[0][2] - W[0][1])*x_w + (biases[0][2] - biases[0][1])) / (W[1][1] - W[1][2])

  print(W)



  # plot data and result

  plt.scatter(X[:,0], X[:,1])
  # plt.plot(x_w, y_w)
  # plt.plot(x_w1,y_w1)
  plt.plot(x_w2,y_w2)


  plt.show()


if __name__ == '__main__':
    main()