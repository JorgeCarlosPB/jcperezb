# used for manipulating directory paths
import os

# Scientific and vector computation for python
import numpy as np

# Plotting library
from matplotlib import pyplot

# Optimization module in scipy
from scipy import optimize

# will be used to load MATLAB mat datafile format
# from scipy.io import loadmat

# library written for this exercise providing additional functions for assignment submission, and others
# import utils


# tells matplotlib to embed plots within the notebook
%matplotlib inline

from google.colab import drive
drive.mount('/content/gdrive')

#  datos de entrenamiento almacenados en los arreglos X, y
data = np.loadtxt("/content/gdrive/MyDrive/Inteligencia Artificial/Machine learning/Datasets/new-thyroid.csv", delimiter=',')
# print(data)
X, y = data[:, :-1], data[:,5]

y = np.array([int(e) for e in y])
print(y.shape)
y = np.squeeze(y)

y[y == 1] = 0
y[y == 2] = 1
y[y == 3] = 2

Xp= X[150:,:]
X = X[:150,:]

yp = y[150:]
y = y[:150]


# print(npy)
# print(npy.shape)
# y = Y
# establecer el dígito cero en 0, en lugar del 10 asignado a este conjunto de datos
# Esto se hace debido a que el conjunto de datos se utilizó en MATLAB donde no hay índice 0
# m = y.size
print(X.shape)
print(y.shape)
print(Xp.shape)
print(yp.shape)

# print(X)
print(y)

# Configurando parametros necesario
input_layer_size  = 5  # Entrada de 5 caracteristicas
hidden_layer_size = 4   # 4 unidades ocultas
num_labels = 3          # 3 etiquetas, de 0 a 2

# carga los pesos en las variables Theta1 y Theta2
# weights = loadmat(os.path.join('/content/gdrive/MyDrive/Colab Notebooks/machine learning/data', 'ex4weights.mat'))
# weights = np.array()
pesos = {}
pesos['Theta1'] = np.random.rand(4, 6)
pesos['Theta2'] = np.random.rand(3, 5)
# print(pesos['Theta1'][:].shape)
# print(pesos['Theta2'][:].shape)

# print(weights['Theta1'][:].shape)
# print(weights['Theta2'][:].shape)

# print(weights['Theta1'][0])
# print(np.roll(weights['Theta1'][0], 1, axis=0))
# Theta1 tiene un tamaño de 25x401
# Theta2 tiene un tamañó de 10x26
# Theta1, Theta2 = weights['Theta1'], weights['Theta2']
Theta1, Theta2 = pesos['Theta1'], pesos['Theta2']
# se intercambia la ultima columa con la primera de Theta2, por cuestiones de indices que utiliza MATLAB
# print(Theta2)
# print(np.roll(Theta2, 1, axis=0))

# Theta2 = np.roll(Theta2, 1, axis=0)

# Desenrollar parámetros
print(Theta1.ravel().shape)
print(Theta2.ravel().shape)

nn_params = np.concatenate([Theta1.ravel(), Theta2.ravel()])
print(nn_params.shape)


def sigmoid(z):
    """
    Computes the sigmoid of z.
    """
    return 1.0 / (1.0 + np.exp(-z))


def sigmoidGradient(z):
    g = np.zeros(z.shape)

    g = sigmoid(z) * (1 - sigmoid(z))

    return g


def nnCostFunction(nn_params,
                   input_layer_size,
                   hidden_layer_size,
                   num_labels,
                   X, y, lambda_=0.001):
    # Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
    # for our 2 layer neural network
    Theta1 = np.reshape(nn_params[:hidden_layer_size * (input_layer_size + 1)],
                        (hidden_layer_size, (input_layer_size + 1)))

    Theta2 = np.reshape(nn_params[(hidden_layer_size * (input_layer_size + 1)):],
                        (num_labels, (hidden_layer_size + 1)))

    m = y.size

    J = 0
    Theta1_grad = np.zeros(Theta1.shape)
    Theta2_grad = np.zeros(Theta2.shape)

    a1 = np.concatenate([np.ones((m, 1)), X], axis=1)

    a2 = sigmoid(a1.dot(Theta1.T))
    a2 = np.concatenate([np.ones((a2.shape[0], 1)), a2], axis=1)

    a3 = sigmoid(a2.dot(Theta2.T))

    # print("-"*20)
    # print(y.shape)
    # print(y.reshape(-1))
    # print("-"*20)
    y_matrix = y.reshape(-1)
    # print(y.shape)
    y_matrix = np.eye(num_labels)[y_matrix]
    # print(y_matrix)

    temp1 = Theta1
    temp2 = Theta2

    # Agregar el termino de regularización

    reg_term = (lambda_ / (2 * m)) * (np.sum(np.square(temp1[:, 1:])) + np.sum(np.square(temp2[:, 1:])))

    J = (-1 / m) * np.sum((np.log(a3) * y_matrix) + np.log(1 - a3) * (1 - y_matrix)) + reg_term

    # Backpropogation

    delta_3 = a3 - y_matrix
    delta_2 = delta_3.dot(Theta2)[:, 1:] * sigmoidGradient(a1.dot(Theta1.T))

    Delta1 = delta_2.T.dot(a1)
    Delta2 = delta_3.T.dot(a2)

    # Agregar regularización al gradiente

    Theta1_grad = (1 / m) * Delta1
    Theta1_grad[:, 1:] = Theta1_grad[:, 1:] + (lambda_ / m) * Theta1[:, 1:]

    Theta2_grad = (1 / m) * Delta2
    Theta2_grad[:, 1:] = Theta2_grad[:, 1:] + (lambda_ / m) * Theta2[:, 1:]

    # ===================== Alterntate solutions =====================
    # my_final_matrix = np.zeros(a3.shape)
    # for c in np.arange(num_labels):
    #    my_final_matrix[:, c] = (np.log(a3[:, c]) * (y == c)) + (np.log(1 - a3[:, c]) * (1 - (y == c)))
    # J = (-1 / m) * np.sum(my_final_matrix)
    # ================================================================

    # ================================================================
    # Unroll gradients
    # grad = np.concatenate([Theta1_grad.ravel(order=order), Theta2_grad.ravel(order=order)])

    grad = np.concatenate([Theta1_grad.ravel(), Theta2_grad.ravel()])

    return J, grad

lambda_ = 0.001
J, _ = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambda_)
print('Costo en parametros (cargado de ex4weights): %.6f ' % J)
print('El costo debe esta cercano a               : 0.287629')

z = np.array([-1, -0.5, 0, 0.5, 1])
g = sigmoidGradient(z)
print('Gradiente sigmoide evaluada con [-1 -0.5 0 0.5 1]:\n  ')
print(g)


def randInitializeWeights(L_in, L_out, epsilon_init=0.12):
    """
    Randomly initialize the weights of a layer in a neural network.

    Parameters
    ----------
    L_in : int
        Number of incomming connections.

    L_out : int
        Number of outgoing connections.

    epsilon_init : float, optional
        Range of values which the weight can take from a uniform
        distribution.

    Returns
    -------
    W : array_like
        The weight initialiatized to random values.  Note that W should
        be set to a matrix of size(L_out, 1 + L_in) as
        the first column of W handles the "bias" terms."""

    W = np.zeros((L_out, 1 + L_in))
    W = np.random.rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init

    return W

print('Inicialización de parámetros de redes neuronales...')

initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size)
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels)

# Desenrrollr parametros
initial_nn_params = np.concatenate([initial_Theta1.ravel(), initial_Theta2.ravel()], axis=0)
#  After you have completed the assignment, change the maxiter to a larger
#  value to see how more training helps.
options = {'maxiter': 1000}

#  You should also try different values of lambda
lambda_ = 0.5

# Create "short hand" for the cost function to be minimized
costFunction = lambda p: nnCostFunction(p, input_layer_size,
                                        hidden_layer_size,
                                        num_labels, X, y, lambda_)

# Now, costFunction is a function that takes in only one argument
# (the neural network parameters)
res = optimize.minimize(costFunction,
                        initial_nn_params,
                        jac=True,
                        method='TNC',
                        options=options)

# get the solution of the optimization
nn_params = res.x

# Obtain Theta1 and Theta2 back from nn_params
Theta1 = np.reshape(nn_params[:hidden_layer_size * (input_layer_size + 1)],
                    (hidden_layer_size, (input_layer_size + 1)))

Theta2 = np.reshape(nn_params[(hidden_layer_size * (input_layer_size + 1)):],
                    (num_labels, (hidden_layer_size + 1)))

def predict(Theta1, Theta2, X):
    """
    Predict the label of an input given a trained neural network
    Outputs the predicted label of X given the trained weights of a neural
    network(Theta1, Theta2)
    """
    # Useful values
    m = X.shape[0]
    num_labels = Theta2.shape[0]

    # You need to return the following variables correctly
    p = np.zeros(m)
    h1 = sigmoid(np.dot(np.concatenate([np.ones((m, 1)), X], axis=1), Theta1.T))
    h2 = sigmoid(np.dot(np.concatenate([np.ones((m, 1)), h1], axis=1), Theta2.T))
    p = np.argmax(h2, axis=1)
    return p

pred = predict(Theta1, Theta2, X[:,:])
print(pred)
print('Training Set Accuracy: %f' % (np.mean(pred == y[:]) * 100))

pred = predict(Theta1, Theta2, Xp[:,:])
print(pred)
print('Training Set Accuracy: %f' % (np.mean(pred == yp[:]) * 100))


