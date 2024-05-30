import pandas as pd
import matplotlib.pyplot as plt

# Incarca dataset-ul
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Determina procentul persoanelor care au supravietuit si procentul persoanelor care nu au supravietuit
survival_counts = data['Survived'].value_counts(normalize=True) * 100

# Determina procentul pasagerilor pentru fiecare tip de clasa
class_counts = data['Pclass'].value_counts(normalize=True) * 100

# Determina procentul barbatilor si al femeilor
gender_counts = data['Sex'].value_counts(normalize=True) * 100

# Creaza graficele pentru prezentarea rezultatelor
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Grafic pentru rata de supravietuire
axes[0].bar(survival_counts.index, survival_counts.values, color=['blue', 'orange'])
axes[0].set_title('Procentul de Supravietuitori si Non-Supravietuitori')
axes[0].set_xticks(survival_counts.index)
axes[0].set_xticklabels(['Non-Supravietuit', 'Supravietuit'])
axes[0].set_ylabel('Procent')

# Grafic pentru distributia pe clase
axes[1].bar(class_counts.index, class_counts.values, color=['green', 'red', 'purple'])
axes[1].set_title('Procentul de Pasageri pentru Fiecare Clasa')
axes[1].set_xticks(class_counts.index)
axes[1].set_xticklabels(['Clasa 1', 'Clasa 2', 'Clasa 3'])
axes[1].set_ylabel('Procent')

# Grafic pentru distributia pe gen
axes[2].bar(gender_counts.index, gender_counts.values, color=['cyan', 'magenta'])
axes[2].set_title('Procentul de Barbati si Femei')
axes[2].set_xticks(gender_counts.index)
axes[2].set_xticklabels(['Barbati', 'Femei'])
axes[2].set_ylabel('Procent')

plt.tight_layout()
plt.show()

# Afiseaza rezultatele in consola
print(f"Procentul persoanelor care nu au supravietuit: {survival_counts[0]:.2f}%")
print(f"Procentul persoanelor care au supravietuit: {survival_counts[1]:.2f}%")
print("\nProcentul pasagerilor pentru fiecare tip de clasa:")
for cls, pct in class_counts.items():
    print(f"Clasa {cls}: {pct:.2f}%")
print("\nProcentul barbatilor si femeilor:")
print(f"Barbati: {gender_counts['male']:.2f}%")
print(f"Femei: {gender_counts['female']:.2f}%")
