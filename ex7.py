import pandas as pd
import matplotlib.pyplot as plt

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Considera copii persoanele cu varsta < 18 ani
data['Child'] = data['Age'] < 18

# Determina procentul de copii si adulti care au supravietuit
survival_by_age_group = data.groupby(['Child', 'Survived']).size().unstack().fillna(0)

# Calculeaza procentul de supravietuitori
survival_by_age_group_percent = survival_by_age_group.div(survival_by_age_group.sum(axis=1), axis=0) * 100

# Genereaza un grafic
survival_by_age_group_percent[1].plot(kind='bar', color=['green', 'red'], edgecolor='black')
plt.title('Procentul de supravietuitori: Copii vs Adulti')
plt.xlabel('Grupa de varsta')
plt.ylabel('Procent de supravietuire')
plt.xticks([0, 1], ['Copii', 'Adulti'], rotation=0)
plt.show()
