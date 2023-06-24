import points

liste_name_sous_chapitre =[]
for nom_variable in dir(points):
    # Obtenez l'objet associé au nom de variable
    variable = getattr(points, nom_variable)
    # Vérifiez si la variable est un dictionnaire
    if isinstance(variable, dict):
        # Vérifiez si la clé "name" existe dans le dictionnaire
        if "name" in variable:
            # Ajoutez la valeur de la clé "name" à la liste des noms
            liste_name_sous_chapitre.append(variable["name"])

print(liste_name_sous_chapitre)

nom_defaut_badge = "badge_"
bdg=[]
for i in range(1,32):
    bdg.append(f"{nom_defaut_badge}{i}.png")
