from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, entradas=3, saida=1, bias=0.5):
        self.entradas = np.zeros(entradas)
        self.saida = np.zeros(saida)
        
        self.pesos = np.random.uniform(low = -1, high = +1, size = entradas)
        self.bias = np.random.uniform(low = -1, high = +1, size = 1)
        
        self.saida_registro = []  # Lista para armazenar os valores de saída
        self.bias_registro = []   # Lista para armazenar os valores de bias
        self.pesos_registro = []  # Lista para armazenar os valores de pesos
        self.entrada_registro = []# Lista para armazenar os valores de entradas

    def input(self, array_in):
        for i, x_i in enumerate(array_in):
            self.entradas[i] = x_i

    def ativa(self):
        self.saida = np.dot(self.entradas, self.pesos) + self.bias

        self.entrada_registro.append(self.entradas)
        self.saida_registro.append(self.saida)  # Registra o valor de saída
        self.bias_registro.append(self.bias)    # Registra o valor do bias
        self.pesos_registro.append(self.pesos.copy())  # Registra os valores de pesos (cópia)
        
        return self.saida, self.bias, self.pesos

    def __str__(self):
        return f'Entradas: {self.entradas}, Pesos: {self.pesos}, Saída: {self.saida}, Bias: {self.bias}'

def re_lu(valor):
    return valor > 0 or 0
# -

num_entradas = 2
num_saidas = 1
perceptron = Perceptron(num_entradas, num_saidas)

# Lista para armazenar os dados para o plot 3D
x_data = []
y_data = []
z_data = []

# Iterando sobre várias entradas
for i in range(200):
    entrada = np.random.uniform(low=-1, high=1, size=num_entradas)
    perceptron.input(entrada)               # Insere o vetor de entrada
    saida, bias, pesos = perceptron.ativa() # Ativa o perceptron e retorna seus parâmetros
    saida_relu = re_lu(saida)
    
    # Adicionando os dados para o plot
    x_data.append(perceptron.entradas[0])
    y_data.append(perceptron.entradas[1])
    z_data.append(perceptron.saida)

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_data, y_data, z_data, c='r', marker='o')
ax.set_xlabel('Entrada 1')
ax.set_ylabel('Entrada 2')
ax.set_zlabel('Saída')
ax.set_title('Saída do Perceptron em 3D')
plt.show()