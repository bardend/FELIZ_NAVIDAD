import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

class K_Means :
    def __init__(self, k, tol = 0.0001, maxn = 2) :
        self.k = k
        self.tol = tol
        self.maxn = maxn
        self.list_centroid = None 

    def fit(self, data) :
        self.list_centroid = data[np.random.choice(data.shape[0], size = self.k, replace = False)]

        for _ in range(self.maxn) :

            self.cluster = [[] for _ in range(self.k)]
            self.represent = [None] * data.shape[0] 

            for ind,features in enumerate(data) : 
                distance = [np.linalg.norm(features - center) for center in self.list_centroid]
                label = distance.index(min(distance))
                self.cluster[label].append(features)
                self.represent[ind] = label
                
            pre_list = self.list_centroid

            for label in range(self.k) :
                self.list_centroid[label] = np.average(self.cluster[label], axis = 0)

            stop = 0


    def get_centroids(self) :
        return self.list_centroid

    def get_labels(self) :
        return self.represent


"""

kmean = K_Means(4)
dt = np.random.rand(50, 2) * 10
kmean.fit(dt)
list_centroid = kmean.get_centroids()
lst = kmean.get_labels()


x1, y1 = dt[:, 0], dt[:, 1]
x2, y2 = list_centroid[:, 0], list_centroid[:, 1]

# Crear un gráfico de dispersión 2D para cada conjunto de datos
plt.scatter(x1, y1,  s=50, c='blue')  # s es el tamaño, c es el color
plt.scatter(x2, y2,  s=100, c='red')

# Etiquetas y título del gráfico
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de dispersión 2D con dos conjuntos de datos')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
"""
