import pandas as pd

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Calculeaza valorile medii pentru Age, Cabin, si Embarked pentru persoanele care au supravietuit si cele care nu au supravietuit
mean_age_survived = data[data['Survived'] == 1]['Age'].mean()
mean_age_not_survived = data[data['Survived'] == 0]['Age'].mean()

mode_cabin_survived = data[data['Survived'] == 1]['Cabin'].mode()[0] if not data[data['Survived'] == 1]['Cabin'].mode().empty else 'Unknown'
mode_cabin_not_survived = data[data['Survived'] == 0]['Cabin'].mode()[0] if not data[data['Survived'] == 0]['Cabin'].mode().empty else 'Unknown'

mode_embarked_survived = data[data['Survived'] == 1]['Embarked'].mode()[0]
mode_embarked_not_survived = data[data['Survived'] == 0]['Embarked'].mode()[0]

# Completeaza valorile lipsa pentru Age
data.loc[(data['Age'].isnull()) & (data['Survived'] == 1), 'Age'] = mean_age_survived
data.loc[(data['Age'].isnull()) & (data['Survived'] == 0), 'Age'] = mean_age_not_survived

# Completeaza valorile lipsa pentru Cabin
data.loc[(data['Cabin'].isnull()) & (data['Survived'] == 1), 'Cabin'] = mode_cabin_survived
data.loc[(data['Cabin'].isnull()) & (data['Survived'] == 0), 'Cabin'] = mode_cabin_not_survived

# Completeaza valorile lipsa pentru Embarked
data.loc[(data['Embarked'].isnull()) & (data['Survived'] == 1), 'Embarked'] = mode_embarked_survived
data.loc[(data['Embarked'].isnull()) & (data['Survived'] == 0), 'Embarked'] = mode_embarked_not_survived

# Salveaza rezultatul intr-un nou fisier CSV
output_file_path = 'train_filled.csv'
data.to_csv(output_file_path, index=False)

# Afiseaza cateva linii pentru a verifica
print(data.head())
