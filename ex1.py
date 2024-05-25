import pandas as pd

# Încarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Determina numarul de coloane
num_columns = data.shape[1]

# Determina tipurile datelor din fiecare coloana
data_types = data.dtypes

# Determina numarul de valori lipsa pentru fiecare coloana
missing_values = data.isnull().sum()

# Determina numarul de linii
num_rows = data.shape[0]

# Verifica daca exista linii duplicate
duplicate_rows = data.duplicated().sum()

# Afiseaza rezultatele
print(f"Numarul de coloane: {num_columns}")
print(f"Tipurile datelor din fiecare coloana:\n{data_types}")
print(f"Numarul de valori lipsa pentru fiecare coloana:\n{missing_values}")
print(f"Numarul de linii: {num_rows}")
print(f"Numarul de linii duplicate: {duplicate_rows}")
