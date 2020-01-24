import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC


def main():
    means = [[2, 2], [4, 1]]
    cov = [[.3, .2], [.2, .3]]
    n = 10
    x0 = np.random.multivariate_normal(means[0], cov, n)
    x1 = np.random.multivariate_normal(means[1], cov, n)
    x1[-1, :] = [2.7, 2]  # noise
    x = np.concatenate((x0.T, x1.T), axis=1).transpose()
    y = np.concatenate((np.ones((1, n)), -1*np.ones((1, n))), axis=1).transpose()

    # hinge
    lam = 0.1
    w = svm_hinge_loss(x, y, lam)
    w1 = w[0][0]
    w2 = w[1][0]
    bias = w[2][0]
    x_w = np.linspace(0, 5, 1000)
    y_w = (w1 * x_w + bias) / -w2

    # skl svm
    w, b = svm_skl(x, y)
    w1_sk = w[0]
    w2_sk = w[1]
    x_sk = np.linspace(0, 5, 1000)
    y_sk = (w1_sk * x_sk + b) / -w2_sk

    plt.scatter(x0[:, 0], x0[:, 1])
    plt.scatter(x1[:, 0], x1[:, 1])
    plt.plot(x_w, y_w)
    plt.plot(x_sk, y_sk)
    plt.show()


def svm_skl(x, y):
    c = 100
    clf = SVC(kernel='linear', C=c)
    clf.fit(x, y)

    w = clf.coef_.reshape(-1, 1)
    b = clf.intercept_[0]
    return w, b


def bias_trick(x):
    return np.hstack((x, np.ones([x.shape[0], 1], dtype=float)))


def compute_hinge_loss(x, y, w, lam):
    # hinge_loss
    u = 1 - y*(x.dot(w))
    u = np.maximum(u, 0)
    hinge = np.sum(u, axis=0)
    # regularization
    reg = 0.5 * lam * w.transpose().dot(w) - 0.5 * lam * w[-1]*w[-1]
    return hinge + reg


def compute_grad(x, y, w, lam):
    u = 1 - y*(x.dot(w))
    index = np.where(u > 0)[0]
    w_tmp = w.copy()
    w_tmp[-1] = 0  # no regularization for bias
    grad = -np.sum(y[index, :]*x[index, :], axis=0).reshape(w_tmp.shape) + lam*w_tmp

    return grad


def numerical_grad(x, y, w, lam):
    eps = 1e-6
    g = np.zeros_like(w)
    for i in range(len(w)):
        wp = w.copy()
        wm = w.copy()
        wp[i] += eps
        wm[i] -= eps
        g[i] = compute_hinge_loss(x, y, wp, lam) - compute_hinge_loss(x, y, wm, lam)
        g[i] /= 2*eps

    return g


def svm_hinge_loss(x, y, lam):
    # bias trick
    x = bias_trick(x)
    # init weight with standard normal distribution
    w = np.random.randn(x.shape[1], 1)  # that w has b as the last column
    # hinge loss
    hinge_loss = compute_hinge_loss(x, y, w, lam)
    # gradient
    grad = compute_grad(x, y, w, lam)
    check_grad = numerical_grad(x, y, w, lam)

    print('diff', np.linalg.norm(grad - check_grad))

    # batch gradient descent
    it = 1000000
    while it:
        w -= 0.05 * grad
        grad = compute_grad(x, y, w, lam)
        it -= 1

    print(compute_hinge_loss(x, y, w, lam))
    return w


if __name__ == '__main__':
    main()
