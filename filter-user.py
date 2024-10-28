userlist = "Userlist.txt"
deactivate = "Deactivated.txt"
same = []
other = []

# Étape 1 : Ouvrir le fichier userlist
with open(userlist, 'r', encoding="utf-8", errors="ignore") as file:
    # Lire la première ligne pour l'en-tête
    header = file.readline().strip()  # Lire et ignorer l'en-tête
    # Lire le reste des lignes et retirer l'en-tête des données
    tb1 = [line.strip().split('\t')[0] for line in file]  # On garde uniquement la première cellule

# Étape 2 : Ouvrir le fichier deactivate
with open(deactivate, 'r', encoding="utf-8", errors="ignore") as file:
    tb2 = {line.strip().lower() for line in file}  # Convertir en ensemble pour une recherche rapide

# Étape 3 : Enlever "User" et créer un ensemble de noms uniques
unique = set(name.replace("User", "").lower().strip() for name in tb1)
sorted_unique = sorted(unique)

# Étape 4 : Écrire les noms uniques dans unique.txt
with open("unique.txt", "w") as file:
    for name in sorted_unique:
        if name:  # S'assurer que le nom n'est pas vide
            file.write(f"{name}\n")

# Étape 5 : Comparer tb1 et tb2
for name in sorted_unique:
    if name in tb2:
        same.append(name)
    else:
        other.append(name)

print(f"""
      Nombre total de personnes désactivées : {len(tb2)}
      Nombre total de personnes sur la Userlist : {len(sorted_unique)}
      Nombre total de personnes qui apparaissent dans la deactivated list : {len(same)}
      Les autres : {len(other)}
""")
