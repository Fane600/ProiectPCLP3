import pandas as pd

# Incarca dataset-ul
file_path = 'train.csv'  # Modifica aceasta cale daca fisierul este intr-o alta locatie
data = pd.read_csv(file_path)

# Completeaza varsta lipsa cu media pasagerilor din aceeasi clasa care au supravietuit
data['Age'] = data.groupby(['Pclass', 'Survived'])['Age'].transform(lambda x: x.fillna(x.mean()))

# Completeaza valorile lipsa pentru coloanele categorice cu cea mai frecventa valoare
for column in data.select_dtypes(include=['object']).columns:
    mode_value = data[column].mode()[0]
    data[column] = data[column].fillna(mode_value)

# Salveaza rezultatul intr-un nou fisier CSV
output_file_path = 'train_filled.csv'
data.to_csv(output_file_path, index=False)

# Afiseaza cateva linii pentru a verifica
print(data.head())
