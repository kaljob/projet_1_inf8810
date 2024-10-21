import sys
import io

# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='cp437')

ville_list_price = {}
ville_avg_price = {}

for line in sys.stdin:    
    ville = line.split('\t', 1)[0]
    price = line.split('\t', 1)[1].replace('$', '')

    try:
        price = float(price)
    except ValueError:
        continue

    try:
        ville_list_price[ville].append(price)
    except KeyError:
        ville_list_price[ville] = [price, ]

ville_avg_price = {ville: round(sum(list_prix)/len(list_prix), 2) for ville, list_prix in ville_list_price.items()} 

# Sort by average price
sorted_ville_avg_price = dict(sorted(ville_avg_price.items(), key=lambda item: item[1]))

# Extraire les 10 villes les plus chères
top_10_villes_cheres = list(sorted_ville_avg_price.items())[-10:]

# Extraire les 10 villes les moins chères
top_10_villes_moins_cheres = list(sorted_ville_avg_price.items())[:10]

# Afficher les résultats
print("Les 10 villes les plus cheres :")
for ville, avg_price in reversed(top_10_villes_cheres):
    print("%s\t%s"%(ville, avg_price))

print("\nLes 10 villes les moins cheres :")
for ville, avg_price in top_10_villes_moins_cheres:
    print("%s\t%s"%(ville, avg_price))
