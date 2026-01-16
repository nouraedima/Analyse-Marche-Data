import pandas as pd
import random

# Listes de simulation réalistes
postes = [
    "Data Analyst", "Alternance Data Analyst", "Stage Data Analyst",
    "Data Scientist", "Data Engineer", "Business Intelligence Analyst",
    "Stage Data Science", "Alternance Business Intelligence",
    "Consultant Data", "Chargé d'études statistiques"
]
villes = ["Paris", "Toulouse", "Lyon", "Bordeaux", "Nantes", "Lille", "Marseille"]
technos = ["Python", "SQL", "Power BI", "Tableau", "Excel", "R", "Azure"]

data = []

# ici je génère 500 offres pour avoir de vraies statistiques
for _ in range(500):
    titre = random.choice(postes)
    # j'ai ajouté une techno dans le titre pour plus de réalisme
    if random.random() > 0.7:
        titre += f" ({random.choice(technos)})"
        
    data.append({
        "Titre du Poste": titre,
        "Ville": random.choice(villes),
        "Salaire_Estime": random.randint(35000, 55000) # En euros/an
    })

df = pd.DataFrame(data)
df.to_csv("mes_opportunites_data.csv", index=False, encoding='utf-8')
print(" Dataset de 500 offres généré avec succès !")