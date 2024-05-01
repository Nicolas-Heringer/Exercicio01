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
        saida = np.dot(self.entradas, self.pesos) + self.bias
        saida_ativada = [np.tanh(saida[0])]
        self.saida = saida_ativada

        self.entrada_registro.append(self.entradas)
        self.saida_registro.append(self.saida)  # Registra o valor de saída
        self.bias_registro.append(self.bias)    # Registra o valor do bias
        self.pesos_registro.append(self.pesos.copy())  # Registra os valores de pesos (cópia)
        
        return self.saida, self.bias, self.pesos

    def __str__(self):
        return f'Entradas: {self.entradas}, Pesos: {self.pesos}, Saída: {self.saida}, Bias: {self.bias}'

def tanh(list):
    return np.tanh(list)
# -

num_entradas = 10
num_saidas = 1
perceptron = Perceptron(num_entradas, num_saidas)

x_data = []
y_data = []

# Iterando sobre várias entradas
for i in range(10):
    entrada = np.random.uniform(low=-1, high=1, size=num_entradas)
    perceptron.input(entrada)               # Insere o vetor de entrada
    saida, bias, pesos = perceptron.ativa() # Ativa o perceptron e retorna seus parâmetros
    
    # Adicionando os dados para o plot
    x_data.append(i+1)
    y_data.append(perceptron.entradas[1])

plt.plot(x_data, y_data)
plt.xlabel('Execução #')  # Rotulo do eixo x
plt.ylabel('Saída')  # Rotulo do eixo y
plt.title('10 execuções da ativação do perceptron')  # Título do gráfico
plt.show()