import sys
import pandas as pd

# Récupérer le chemin passé en argument, sinon défaut
if len(sys.argv) > 1:
    fichier = sys.argv[1]
else:
    fichier = r"CLTFAM24.xlsx"

print("📁 Analyse du fichier Excel...")

df = pd.read_excel(fichier)

print(f"✅ Taille : {df.shape[0]} lignes × {df.shape[1]} colonnes")
print("\n📋 Colonnes :")
for col in df.columns:
    print(f"  - {col}")

print("\n📊 Premières lignes :")
print(df.head())

print("\n🧮 Statistiques simples :")
print(f"Nombre total de lignes : {len(df)}")
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
