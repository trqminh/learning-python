import numpy as np
import json

def cost(x, y, theta):
    # TODO Calculate cost for current model
    m = len(x[:,0])
    return np.sum(np.square(x.dot(theta) - y)) / (2*m)

def gradient(x, y, theta):
    # TODO Calculate gradient vector of cost function at current position of theta
    m = len(x[:,0])
    
    E = x.dot(theta) - y
    grad = ((x.transpose()).dot(E)) / m

    return grad
    

def gradient_descent(x, y, alpha, init_theta, n_iter):
    # TODO Implement gradient descent algorithm
    
    result_theta = init_theta
    while n_iter:
        grad = gradient(x,y,result_theta)
        result_theta = result_theta - grad*alpha

        print('Theta:\n ',result_theta)
        print('Cost: ', cost(x,y,result_theta))
        n_iter-=1

    return result_theta


def load_data(file_path):
    # TODO Load data from file
    
    x = []
    y = []
    
    with open(file_path,'r') as f:
        for line in f:
            xi, yi = list(map(float, line.split(' ')))
            x.append(xi)
            y.append(yi)

    x = np.asfarray(x, dtype = np.float).reshape(-1,1)
    x = np.hstack([np.ones(shape = (5,1)), x])
    y = np.asfarray(y, dtype = np.float).reshape(-1,1)

    return (x,y)
    

def load_config():
    # TODO Load configurations from file config.json
    
    with open('config.json') as f:
        config = json.load(f)


    return config



def predict(X, theta):
    # TODO Predict output for new input
    
    return X.dot(theta)

def main():
    # TODO Wrap up every thing

    config = load_config()

    data_file_path = config['Dataset']
    init_theta = np.asfarray(config['Theta']).reshape(-1,1)
    alpha = config['Alpha']
    n_iter = config['NumIter']

    
    data = load_data(data_file_path)
    x = data[0]
    y = data[1]
    
    
    result_theta = gradient_descent(x,y,alpha,init_theta,n_iter)
    

    

if __name__ == "__main__":
    # TODO Call main function
    main()
