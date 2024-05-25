import pandas as pd
import matplotlib.pyplot as plt

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Selecteaza coloanele numerice
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns

# Genereaza histograme pentru fiecare coloana numerica
fig, axes = plt.subplots(len(numeric_columns), 1, figsize=(10, 20))
fig.tight_layout(pad=5.0)

for ax, column in zip(axes, numeric_columns):
    ax.hist(data[column].dropna(), bins=20, color='blue', edgecolor='black')
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')

plt.show()
