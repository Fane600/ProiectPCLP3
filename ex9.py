import pandas as pd
import matplotlib.pyplot as plt

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Extrage titlurile din coloana Name
data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# Verifica daca titlurile de noblete corespund cu sexul persoanei
title_gender_counts = data.groupby(['Title', 'Sex']).size().unstack().fillna(0)

# Genereaza un grafic
title_gender_counts.plot(kind='bar', stacked=True)
plt.title('Distributia titlurilor in functie de sex')
plt.xlabel('Titlu')
plt.ylabel('Numar de persoane')
plt.xticks(rotation=45)
plt.legend(title='Sex')
plt.show()