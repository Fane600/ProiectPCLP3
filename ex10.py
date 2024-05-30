import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Creeaza o coloana pentru a identifica pasagerii singuri (fara rude)
data['Rude'] = (data['SibSp'] == 0) & (data['Parch'] == 0)

# Selecteaza primele 100 de inregistrari
subset_data = data.head(100)

# Genereaza un catplot pentru a investiga relatia dintre tarif, clasa si supravietuire
sns.catplot(x='Pclass', y='Fare', hue='Survived', col='Rude', kind='strip', data=subset_data, jitter=True)
plt.show()
