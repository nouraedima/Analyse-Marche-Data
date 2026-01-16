import pandas as pd
import matplotlib.pyplot as plt

# 1. Chargement
df = pd.read_csv("mes_opportunites_data.csv")

# 2. Analyse des types de recherche
recherche = {
    "Alternances": df['Titre du Poste'].str.contains('Alternance', case=False).sum(),
    "Stages": df['Titre du Poste'].str.contains('Stage', case=False).sum(),
    "Postes CDI/CDD": df['Titre du Poste'].str.contains('Data', case=False).sum() 
                     - (df['Titre du Poste'].str.contains('Alternance|Stage', case=False).sum())
}

# 3. Création du graphique professionnel
plt.style.use('ggplot') # Style moderne
fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#3498db', '#2ecc71', '#e74c3c']
ax.bar(recherche.keys(), recherche.values(), color=colors)

ax.set_title("Analyse Comparative du Marché Data 2026", fontsize=16, fontweight='bold')
ax.set_ylabel("Nombre d'offres répertoriées")

# Ajout des chiffres au-dessus des barres
for i, v in enumerate(recherche.values()):
    ax.text(i, v + 5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('dashboard_final.png')
print(" Dashboard généré ! Regarde le fichier 'dashboard_final.png'")