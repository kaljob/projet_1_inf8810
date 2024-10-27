Notre projet est divisé en 3 parties
et chaque partie contient le code et les descriptions nécessaire pour l'execution

* La partie 1: Represente le Pretraitement des informations. Il peut s'executer directement sur l'ordinateur sans toute fois avoir un logiciel particulier le seul préréquis c'est d'avoir un IDE et python installé sur la machine
* La partie 2: Traitement avec Haddop Streaming. Ce code fonctionne dans un environnement docker les étapes sont dans le notebook partie2.ipynb. Cette partie utilise aussi les fichiers (mapper.py, reducer.py, la sortie du fichier de la partie 1: listings_clean.csv)
* La partie 3: Traitement avec Spark. ce code fonctionne dans Google Colab. Le notebook partie3.ipynb contient le code necessaire au traitement spark.