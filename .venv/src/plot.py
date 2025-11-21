import matplotlib.pyplot as plt
import numpy as np

# Matplotlib es una biblioteca de código
# abierto para Python que se utiliza para
# crear visualizaciones de datos, como gráficos y diagramas.

# Datos para graficar
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Crear plot
plt.plot(x, y)

# Ejex y titulo
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Recta")

# Display the plot
plt.show()
