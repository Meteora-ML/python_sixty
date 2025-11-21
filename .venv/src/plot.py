import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Recta")

# Display the plot
plt.show()
