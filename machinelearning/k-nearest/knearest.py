import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def myweights(distance):
    sigma_square = .5
    return np.exp(-distance**2/sigma_square)


def main():
    iris = datasets.load_iris()

    iris_X = iris.data
    iris_y = iris.target

    num_labels = len(np.unique(iris_y))
    data_size = len(iris_y)

    print('Number of class %d ' %num_labels)
    print('Number of data point %d' %data_size)

    # display some data

    for i in range(num_labels):
        print('label ', i, ':', iris_X[iris_y == i, :][0,:])

    
    X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size = 50)

    training_size = len(y_train)
    test_size = len(y_test)

    print(training_size, test_size)

    # do the things with 1 nearest neighbor
    clf = neighbors.KNeighborsClassifier(n_neighbors = 1,p=2) # p = 2 mean norm 2
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print('Accuracy of 1NN: %.2f %%' %(100*accuracy_score(y_test, y_pred)))


    #do the things with 10 nearest neighbor, decide by what class appear most in 10 NN
    clf = neighbors.KNeighborsClassifier(n_neighbors = 10,p=2) # p = 2 mean norm 2
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print('Accuracy of 10 NN with major voting: %.2f %%' %(100*accuracy_score(y_test, y_pred)))


    # do the thing with 10 nearest neigbor
    # nearer point has bigger weight

    #default weights is uniform, 10 point is treated the same
    clf = neighbors.KNeighborsClassifier(n_neighbors = 10,p=2, weights = 'distance') # p = 2 mean norm 2
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print('Accuracy of 1NN, weights = distance : %.2f %%' %(100*accuracy_score(y_test, y_pred)))

    # do the thing with 10 nearest neigbor
    # nearer point has bigger weight
    # custom weights

    #default weights is uniform, 10 point is treated the same
    clf = neighbors.KNeighborsClassifier(n_neighbors = 10,p=2, weights = myweights) # p = 2 mean norm 2
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print('Accuracy of 1NN, weights = custom weights : %.2f %%' %(100*accuracy_score(y_test, y_pred)))



if __name__ == '__main__':
    main()
