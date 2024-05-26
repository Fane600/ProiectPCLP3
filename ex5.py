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

# Determina numarul de pasageri pentru fiecare categorie de varsta
age_category_counts = data['AgeCategory'].value_counts().sort_index()

# Genereaza un grafic pentru a evidentia aceste rezultate
plt.figure(figsize=(10, 6))
age_category_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Numarul de Pasageri pentru Fiecare Categorie de Varsta')
plt.xlabel('Categorie de Varsta')
plt.ylabel('Numar de Pasageri')
plt.xticks(rotation=0)
plt.show()

# Afiseaza rezultatele in consola
print("Numarul de pasageri pentru fiecare categorie de varsta:")
print(age_category_counts)
