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
        return f'\nEntradas: {self.entradas}\nPesos: {self.pesos}\nSaída: {self.saida}\nBias: {self.bias}\n'

def re_lu(valor):
    return valor > 0 or 0
# -

num_entradas = 3
num_saidas = 1
perceptron = Perceptron(num_entradas, num_saidas)

entrada = np.random.uniform(low=-1, high=1, size=num_entradas)
perceptron.input(entrada)
saida, bias, pesos = perceptron.ativa()
saida_relu = re_lu(saida)

print(perceptron)