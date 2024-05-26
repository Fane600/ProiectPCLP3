import pandas as pd
import matplotlib.pyplot as plt

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Defineste categoriile de varsta
bins = [0, 20, 40, 60, float('inf')]
labels = ['0-20', '21-40', '41-60', '61+']

# Creaza o coloana noua pentru categoriile de varsta
data['AgeCategory'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Determina numarul de barbati care au supravietuit pentru fiecare categorie de varsta
survival_by_age_gender = data[data['Sex'] == 'male'].groupby(['AgeCategory', 'Survived'], observed=False).size().unstack().fillna(0)

# Calculeaza procentul de supravietuitori
survival_by_age_gender_percent = survival_by_age_gender.div(survival_by_age_gender.sum(axis=1), axis=0) * 100

# Genereaza un grafic
survival_by_age_gender_percent[1].plot(kind='bar', color='blue', edgecolor='black')
plt.title('Procentul de barbati care au supravietuit in fiecare categorie de varsta')
plt.xlabel('Categorie de varsta')
plt.ylabel('Procent de supravietuire')
plt.xticks(rotation=0)
plt.show()
