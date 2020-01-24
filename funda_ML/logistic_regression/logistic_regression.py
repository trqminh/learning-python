import numpy as np
import scipy.special
import matplotlib.pyplot as plt


def compute_Z(W, X, biases):
    return scipy.special.expit(X.dot(W) + biases)


def loss_function_at_point(Zi, yi):
    return -yi*np.log(Zi) - (1 - yi)*np.log(1 - Zi)


def logistic_regression(X, y):

    W = np.random.randn(X.shape[1], 1)
    biases = np.ones(shape=[X.shape[0], 1])


    loss = 1000

    it = 100

    while it:
        # sgd
        it -= 1
        for i in range(X.shape[0]):
            Z = compute_Z(W, X, biases)

            loss = loss_function_at_point(Z[i], y[i])

            X_tmp = X[i].reshape(-1,1)


            W -= X_tmp * (Z[i] - y[i])
            biases -= (Z[i] - y[i])



    print('loss ', loss)

    return W, biases


def main():
    means = [[2, 2], [4, 2]]
    cov = [[.3, .2], [.2, .3]]

    N = 10
    num_class = 2

    X0 = np.random.multivariate_normal(means[0], cov, N)
    X1 = np.random.multivariate_normal(means[1], cov, N)

    X = np.concatenate((X0, X1), axis=0)

    # assign label
    y = []
    for i in range(2 * N):
        if (i < 10):
            y.append(0)
        else:
            y.append(1)

    W, biases = logistic_regression(X, y)

    # plot data
    plt.scatter(X[:, 0], X[:, 1])
    # plt.show(block = False)
    # plt.pause(3)
    # plt.close()

    # plot result

    W1 = W[0][0]
    W2 = W[1][0]

    x_w = np.linspace(0,5,1000)
    y_w = (W1*x_w + biases[0]) / -W2

    plt.plot(x_w,y_w)
    plt.show()





if __name__ == '__main__':
    main()