# utilizado para la manipulación de directorios y rutas
import os

# Cálculo científico y vectorial para python
import numpy as np

# Libreria para graficos
from matplotlib import pyplot

# Modulo de optimizacion en scipy
from scipy import optimize

# le dice a matplotlib que incruste gráficos en el cuaderno
%matplotlib inline

from google.colab import drive
drive.mount('/content/gdrive')
data = np.loadtxt("/content/gdrive/MyDrive/Inteligencia Artificial/Machine learning/Datasets/new-thyroid.csv", delimiter=',')
#print(data)
X, y = data[:, :-1], data[:, 5]
print(X)
print(y)
# print(X.shape)
# print(y.shape)

XPrueba = X[-3:, :].copy()
yPrueba = y[-3:].copy()
print(XPrueba)
print(yPrueba)

input_layer_size  = 5
num_labels = 3
m = y.size

def sigmoid(z):
    # Calcula la sigmoide de z.

    return 1.0 / (1.0 + np.exp(-z))


def lrCostFunction(theta, X, y, lambda_):
    # Inicializa algunos valores utiles
    m = y.size

    # convierte las etiquetas a valores enteros si son boleanos
    if y.dtype == bool:
        y = y.astype(int)

    J = 0
    grad = np.zeros(theta.shape)

    h = sigmoid(X.dot(theta.T))

    temp = theta
    temp[0] = 0

    J = (1 / m) * np.sum(-y.dot(np.log(h)) - (1 - y).dot(np.log(1 - h))) + (lambda_ / (2 * m)) * np.sum(np.square(temp))

    grad = (1 / m) * (h - y).dot(X)
    grad = grad + (lambda_ / m) * temp

    return J, grad
# valores de prueba para los parámetros theta
theta_t = np.array([-2, -1, 1, 2], dtype=float)

# valores de prueba para las entradas
X_t = np.concatenate((np.ones((5, 1)), np.arange(1, 16).reshape(5, 3, order='F')/10.0), axis=1)
print(X_t)
# valores de testeo para las etiquetas
y_t = np.array([1, 0, 1, 0, 1])

# valores de testeo para el parametro de regularizacion
lambda_t = 3

J, grad = lrCostFunction(theta_t, X_t, y_t, lambda_t)

print('Costo         : {:.6f}'.format(J))
print('Costo esperadot: 2.534819')
print('-----------------------')
print('Gradientes:')
print(' [{:.6f},{:.6f}, {:.6f}, {:.6f}]'.format(*grad))
print('Gradientes esperados:')
print(' [0.146561, -0.548558, 0.724722, 1.398003]');


def oneVsAll(X, y, num_labels, lambda_):
    m, n = X.shape

    all_theta = np.zeros((num_labels, n + 1))

    # Agrega unos a la matriz X
    X = np.concatenate([np.ones((m, 1)), X], axis=1)

    for c in np.arange(num_labels):
        initial_theta = np.zeros(n + 1)
        options = {'maxiter': 150}
        res = optimize.minimize(lrCostFunction,
                                initial_theta,
                                (X, (y == (c + 1)), lambda_),
                                jac=True,
                                method='BFGS',
                                options=options)

        all_theta[c] = res.x

    return all_theta

lambda_ = 0.5
all_theta = oneVsAll(X, y, num_labels, lambda_)

print(all_theta)
print(all_theta.shape)

def predictOneVsAll(all_theta, X):
    m = X.shape[0];
    num_labels = all_theta.shape[0]
    p = np.zeros(m)

    # Add ones to the X data matrix
    X = np.concatenate([np.ones((m, 1)), X], axis=1)
    p = np.argmax(sigmoid(X.dot(all_theta.T)), axis = 1)

    return p + 1
print(X.shape)
pred = predictOneVsAll(all_theta, X)
print('Precision del conjuto de entrenamiento: {:.2f}%'.format(np.mean(pred == y) * 100))
XPrueba = X[145:155, :].copy()
#yPrueba = y[-8:].copy()
yPrueba=[0]
# XPrueba = [[112,10.6,1.6,0.9,-0.1]]
# yPrueba = [3]
# print(XPrueba.shape)
# print(len(XPrueba))
print(XPrueba)
# print(yPrueba.shape)
print(yPrueba)

#print(np.ones((1)))
#p = np.zeros(1)
XPrueba = np.concatenate((np.ones((10, 1)), XPrueba), axis=1)
# print(XPrueba.shape)
# print(XPrueba)
p = np.argmax(sigmoid(XPrueba.dot(all_theta.T)), axis = 1)
#print(p)
print(p + 1)