#ref: https://machinelearningcoban.com/2017/01/01/kmeans/

import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from scipy.spatial.distance import cdist
import matplotlib.animation as animation

def one_d_normal_distribution(mean, variance, N):
    #random initialize a dataset
    X = np.random.normal(mean, variance, N)

    #display X

    y = np.zeros(N)

    #plt.scatter(X, y)
    #plt.show()

    return X


def two_d_normal_distribtion(mean, cov, N):
    X = np.random.multivariate_normal(mean, cov, N)

    #plt.scatter(X[:,0], X[:,1])
    #plt.show()

    return X
    

def kmean_init_center(X, k):
    return np.array(X[np.random.choice(X.shape[0], k, replace = False)])

def kmean_assign_point_to_cluster(X, centers):
    #return a labels list 
    D = cdist(X, centers) # D shape (1500, 3)

    return np.argmin(D, axis = 1)

def kmean_update_center(X, labels, k):
    
    centers = np.array([])
    for label in range(k):
        centers = np.append(centers, np.average(X[labels == label], axis = 0))
    
    centers = np.reshape(centers, [3,2])
    return centers
 
def kmean_check_converge(centers, new_centers):
    return (set([tuple(a) for a in centers]) == set([tuple(a) for a in new_centers]))


def kmean(X, k):
    centers = kmean_init_center(X, k)
    step = 0

    while True:
        step = step + 1

        labels = kmean_assign_point_to_cluster(X,centers)
       
        # plot here
        for i in range(k):
            plt.scatter(X[labels == i, 0], X[labels == i, 1])
    
        plt.scatter(centers[:,0], centers[:,1])
        plt.title('Step ' + str(step))
        plt.show(block = False)
        plt.pause(3)
        plt.close()

        # end plot here

        new_centers = kmean_update_center(X,labels, k)

        if kmean_check_converge(centers, new_centers):
            break

        centers = new_centers
    
    return centers, labels


def main():
    N = 500
    k = 3
    X0 = two_d_normal_distribtion([0,0], [[1,0],[0,1]], N)
    X1 = two_d_normal_distribtion([2,5], [[1,0],[0,1]], N)
    X2 = two_d_normal_distribtion([7,3], [[1,0],[0,1]], N)

    X = np.concatenate((X1, X2, X0), axis = 0)
    
    #display data
    plt.scatter(X[:,0], X[:,1])
    plt.title('Init data')
    plt.plot(block=False)
    plt.pause(4)
    plt.close()

    
    #show the result
    centers, labels = kmean(X,k)

    print (centers)
    for i in range(k):
        plt.scatter(X[labels == i, 0], X[labels == i, 1])
    
    plt.scatter(centers[:,0], centers[:,1])
    plt.title('Final result')
    plt.show()
    


if __name__ == '__main__':
    main()


