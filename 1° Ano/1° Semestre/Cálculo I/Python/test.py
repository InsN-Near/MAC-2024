import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Parâmetros do modelo de Heston
kappa = 0.5  # Velocidade de reversão à média
theta = 0.05  # Nível de longo prazo da volatilidade
sigma = 0.1  # Volatilidade da volatilidade
rho = -0.7  # Coeficiente de correlação entre o preço e a volatilidade
v0 = 0.05  # Valor inicial da volatilidade

# Função para simular o modelo de Heston
def simulate_heston(n_samples):
    dt = 1 / 252  # Intervalo de tempo (1 dia)
    sqrt_dt = np.sqrt(dt)
    S = np.zeros(n_samples)
    v = np.zeros(n_samples)
    S[0] = 100  # Inicializando o preço do ativo com um valor arbitrário
    v[0] = v0  # Valor inicial da volatilidade

    for i in range(1, n_samples):
        dW1 = np.random.normal(0, sqrt_dt)
        dW2 = rho * dW1 + np.sqrt(1 - rho**2) * np.random.normal(0, sqrt_dt)

        v[i] = max(v[i-1] + kappa * (theta - v[i-1]) * dt + sigma * np.sqrt(max(v[i-1], 0)) * dW2, 0)
        S[i] = S[i-1] + S[i-1] * np.sqrt(max(v[i-1], 0)) * dW1

    return S

# Simulando os dados seguindo o modelo de Heston
n_samples = 10000
X = np.linspace(0, 1, n_samples).reshape(-1, 1)
y = simulate_heston(n_samples).reshape(-1, 1)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transformando os dados para adicionar características polinomiais
poly_features = PolynomialFeatures(degree=8, include_bias=False)  
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)

# Criando o modelo de Regressão Linear
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Avaliando o modelo com os dados de teste
score = model.score(X_poly_test, y_test)
print(f"Score do modelo: {score}")

# Fazendo previsões com o modelo
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_range_poly = poly_features.transform(X_range)
y_pred_range = model.predict(X_range_poly)

# Definindo novos dados de entrada para projeção
X_new = np.linspace(X.max(), X.max() + 0.2, 20).reshape(-1, 1)
X_new_poly = poly_features.transform(X_new)
y_new_pred = model.predict(X_new_poly)

# Ordenando os dados de teste
indices_sorted_test = np.argsort(X_test, axis=0).flatten()
X_test_sorted = X_test[indices_sorted_test]
y_test_sorted = y_test[indices_sorted_test]

# Visualizando os resultados originais e as projeções com pontos menores e linhas conectando-os
plt.scatter(X_test, y_test, color='black', label='Dados Reais', s=1)  # Pontos dos dados reais
plt.plot(X_range, y_pred_range, color='blue', label='Curva de Regressão Polinomial', linewidth=1)  # Linha do modelo
plt.scatter(X_new, y_new_pred, color='red', label='Projeções', s=10)  # Pontos das projeções

# Adicionando linhas para conectar os pontos dos dados reais
plt.plot(X_test_sorted, y_test_sorted, color='black', linewidth=1, linestyle='--')  # Linha pontilhada conectando os pontos dos dados reais

# Adicionando linhas para conectar os pontos de projeção
indices_sorted = np.argsort(X_new, axis=0).flatten()  # Ordenando os pontos de projeção
plt.plot(X_new[indices_sorted], y_new_pred[indices_sorted], color='red', linewidth=1, linestyle='--')  # Linha pontilhada para as projeções

# Definindo os limites para os eixos X e Y
plt.xlim([X.min(), X.max() + 0.2])  # Ajuste conforme necessário
plt.ylim([y.min(), y.max()])  # Ajuste conforme necessário


plt.xlabel('X')
plt.ylabel('y')
plt.title('Regressão Polinomial de Grau n Ajustada ao Modelo de Heston com Projeções')
plt.legend()
plt.show()