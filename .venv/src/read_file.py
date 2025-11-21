import pandas as pd

# Pandas es una biblioteca de código abierto y de propósito
# general para Python que se utiliza para la manipulación y análisis de datos.

df = pd.read_csv('.venv/src/clientes.csv')
print(df.head(10))
