
ip_externe = "IP Externe.txt"
ip_total = "IP Total.txt"
same = []
other = []
# Étape 1 : Ouvrir le fichier
with open(ip_externe, 'r') as file:
    # Étape 2 : Lire le contenu et remplir une liste
    tb1 = [line.strip() for line in file]


with open(ip_total, 'r') as file:
    # Étape 2 : Lire le contenu et remplir une liste
    tb2 = [line.strip() for line in file]

for ip in tb1:
    if ip in tb2:
        same.append(ip)
    else:
        other.append(ip)
        with open("other_ip", 'w') as file:
            file.write(f"{ip}\n\t")
print(f"""
      * IP Totale : {len(tb2)}\n
      * IPs externes qui ne figurent pas : {len(other)}\n
      * Les IPs : {other}
""")
