import pandas as pd

df = pd.read_csv('train.csv')

# Identificam coloanele care au valori lipsa
missing_values = df.isnull().sum()
missing_columns = missing_values[missing_values > 0]

# Afisam coloanele cu valori lipsa si numarul acestor valori
print("Coloanele cu valori lipsa si numarul acestor valori:")
print(missing_columns)

# Calculam proportia valorilor lipsa pentru fiecare coloana identificata
missing_proportions = missing_columns / len(df)
print("\nProportia valorilor lipsa pentru fiecare coloana identificata:")
print(missing_proportions)

# Calculam procentul valorilor lipsa pentru fiecare dintre cele doua clase din coloana "Survived"
survived_groups = df.groupby('Survived')

# Creem un DataFrame pentru a stoca procentajele valorilor lipsa pentru fiecare clasa
missing_percentage_by_class = pd.DataFrame()

# Iteram prin fiecare grup pentru a calcula procentajul valorilor lipsa
for name, group in survived_groups:
    missing_percentage_by_class[name] = group.isnull().mean()

# Transpunem pentru a avea clasele ca randuri
missing_percentage_by_class = missing_percentage_by_class.T

print("\nProcentul valorilor lipsa pentru fiecare dintre cele doua clase (colona Survived):")
print(missing_percentage_by_class[missing_columns.index])
