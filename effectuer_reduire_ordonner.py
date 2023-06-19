import re
def remove_all_zeros_non_significatif(nombre):
    if nombre.is_integer():
        nombre = int(nombre)
    return nombre
def remove_plus_in_first_position(chaine):
        if len(chaine)>0:
            if chaine[0] == "+":
                chaine = chaine[1:]
            return chaine
        else:
            return ""

def expand_powers(input_string):
    pattern = r"([a-zA-Z])\^\{(\d+)\}"
    expanded_str = ""

    matches = re.finditer(pattern, input_string)
    for match in matches:
        letter = match.group(1)
        power = int(match.group(2))
        expanded_str += letter * power

    return expanded_str

def transform_fraction_in_decimal():
    pass

def transform_dico_in_list(dico):
    return [f"{value}{key}" for key, value in dico.items() if value != 0]

def keep_only_non_distributive_terme(chaine):
    new_chaine = ""
    i=0
    copier = True
    while i<len(chaine):
        if chaine[i] == "(":
            copier= False
            j=i
            while j>=0:
                if chaine[j] == "+" or chaine[j] == "-":

                    break
                else:
                   new_chaine = new_chaine[:-1]
                   j=j-1
        elif chaine[i]==")":
            copier = True
        else:
            if copier:
                new_chaine += chaine[i]
        i+=1
    return new_chaine

def merge_dictionnaire(liste_dictionnaire):
    result_dico = {}

    for i in range(len(liste_dictionnaire)):
        for key, value in liste_dictionnaire[i].items():
            if key not in result_dico:
                result_dico[key] = value
            else:
                result_dico[key] += value
    return result_dico

def transform_dictionnaire_to_polynome(dico):
    chaine = ""
    for key, value in dico.items():
        if value == 1 and key!="":
            chaine += f"+{key}"
        elif value == -1 and key!="":
            chaine += f"-{key}"
        elif value>0:
            chaine += f"+{remove_all_zeros_non_significatif(value)}{key}"
        elif value<0:
            chaine += f"{remove_all_zeros_non_significatif(value)}{key}"
    chaine = remove_plus_in_first_position(chaine)
    chaine = remove_power_one(chaine)
    return chaine

def add_power_one(input_string):
    pattern = r"([a-zA-Z])(?!\^)"
    result = re.sub(pattern, r"\1^{1}", input_string)
    return result

def remove_power_one(chaine):
    chaine = chaine.replace("^{1}", "")
    return chaine

def reduire_dictionnaire(dico):
    new_dico = {}
    for cle, value in dico.items():
        for i in range(len(dico[cle])):
            if cle in new_dico:
                new_dico[cle] += dico[cle][i]
            else:
                new_dico[cle] = dico[cle][i]
    return new_dico

def remplace_first_plusorminus_by_plusone_or_minusone(input_string):
    if len(input_string) < 2:
        return input_string
    first_char = input_string[0]
    second_char = input_string[1]

    if first_char == '+' and not second_char.isdigit():
        return '+1' + input_string[1:]
    elif first_char == '-' and not second_char.isdigit():

        return '-1' + input_string[1:]
    else:
        return input_string

def split_string_at_first_letter(input_string):
    first_letter_index = None
    for index, char in enumerate(input_string):
        if char.isalpha():
            first_letter_index = index
            break
    if first_letter_index is None:
        return [input_string, ""]
    else:
        return [input_string[:first_letter_index], input_string[first_letter_index:]]


def remove_empty_chaine(liste_chaine):
   for element in liste_chaine:
       if element == "":
        liste_chaine.remove(element)

def transform_all_plus_or_minus_in_list_in_one(liste_chaine):
    for i in range(len(liste_chaine)):
        if liste_chaine[i] == "+":
            liste_chaine[i] = "+1"
        elif liste_chaine[i] == "-":
            liste_chaine[i] = "-1"

def transform_all_string_in_integer_in_dico(dico):
    for cle, value in dico.items():
        for i in range(len(dico[cle])):
            dico[cle][i] = float(remove_plus_in_first_position(dico[cle][i]))
    return dico

# exemple xxxyy devient x^{3}y^{2}
def transformer_chaine_en_puissance(chaine):
    resultat = ""
    i = 0
    while i < len(chaine):
        # Compter le nombre de caractères identiques qui se suivent
        j = i + 1
        while j < len(chaine) and chaine[j] == chaine[i]:
            j += 1
        n = j - i

        # Ajouter le caractère et le nombre au résultat
        resultat += chaine[i] + "^{" + str(n) + "}"

        # Passer au caractère suivant
        i = j

    return resultat


def traduire_dico_power_to_dico_chaine(dico):
    return {transformer_puissance_en_chaine(key): value for key, value in dico.items()}

def traduire_dico_chaine_to_dico_power(dico):
    return {transformer_chaine_en_puissance(key): value for key, value in dico.items()}

def trier_dictionnaire_par_cle(dictionnaire):
    return {cle: dictionnaire[cle] for cle in sorted(dictionnaire, key=lambda x: (-len(x), x))}

def retirer_all_zero_value_dico(dico):
    dico_non_zero = {key:value for (key,value) in dico.items() if value != 0.0}
    return dico_non_zero


# transforme x^{3}y^{2} en xxxyy
def transformer_puissance_en_chaine(chaine):
    chaine = chaine.replace("^{", "")
    chaine = chaine.replace("}", "")
    nouvelle_chaine = ""
    caractere_courant = ""
    i=0
    nombre=0
    while i < len(chaine):
        if chaine[i].isalpha():
            caractere_courant = chaine[i]
            i+=1
        else:
            debut = i
            j=i
            while chaine[j].isdigit():
                j += 1
                i += 1
                if j==len(chaine):
                    break
            nombre = int(chaine[debut:j+1])
            for k in range(nombre):
                nouvelle_chaine += caractere_courant


    return nouvelle_chaine




class Expression_litteral:
    def __init__(self, chaine):

        self.chaine = chaine
        self.chaine_no_power = self.transforme_carre_to_multiplication()
        self.dico_monome_without_distribution = keep_only_non_distributive_terme(self.chaine_no_power)
        self.dico_monome_without_distribution = self.transformer_liste_matrice_dictionnaire(self.dico_monome_without_distribution)
        self.dico_monome_without_distribution = reduire_dictionnaire(self.dico_monome_without_distribution)
        self.liste_facteur_distributivite = self.trouver_expression_distributivite()
        if self.liste_facteur_distributivite != []:
            self.liste_separation_avant_multiplication = self.separer_termes_principaux()
        else:
            self.liste_separation_avant_multiplication = []
        self.liste_all_multiplication_done = self.multiplication_total()

        self.liste_all_multiplication_done.append(self.dico_monome_without_distribution)

        self.liste_all_multiplication_done = merge_dictionnaire(self.liste_all_multiplication_done)

        self.polynome_reduit_ordonne = traduire_dico_power_to_dico_chaine(self.liste_all_multiplication_done)

        self.polynome_reduit_ordonne = trier_dictionnaire_par_cle(self.polynome_reduit_ordonne)

        self.polynome_reduit_ordonne = traduire_dico_chaine_to_dico_power(self.polynome_reduit_ordonne)

        self.polynome_reduit_ordonne = retirer_all_zero_value_dico(self.polynome_reduit_ordonne)

        self.chaine_polynome_reduit_ordonne =transform_dictionnaire_to_polynome(self.polynome_reduit_ordonne)




    def afficher(self):
        print(self.chaine)
    # Permer de transformer (x+2)^{2} en (x+2)(x+2)
    def transforme_carre_to_multiplication(self):
        text = self.chaine
        # Créer un motif pour trouver toutes les occurrences d'une chaîne de caractères qui comportent une parenthèse ( puis du texte puis une parenthèse ) puis le signe ^{ puis un nombre puis }
        motif = r'\((.*?)\)\^{\d+}'
        # Extraire les chaînes de caractères avec le motif
        chaines = re.findall(motif, text)
        # Créer un motif pour extraire les nombres entre ^{ et }
        motif_nombre = r'\^\{(\d+)\}'
        # Extraire les nombres avec le motif
        nombres = re.findall(motif_nombre, text)
        # Créer une liste pour contenir les résultats
        resultat = []
        # Itérer sur les chaînes de caractères et les nombres, puis les ajouter à la liste résultat
        for chaine, nombre in zip(chaines, nombres):
            resultat.append([chaine, nombre])

        for i in range(len(resultat)):
            chaine_trouver = "("+resultat[i][0]+")"+"^{"+resultat[i][1]+"}"
            nouvelle_chaine = ""
            for j in range(int(resultat[i][1])):
                nouvelle_chaine += "("+ resultat[i][0]+")"
            text = text.replace(chaine_trouver, nouvelle_chaine)
        return text

    # permet de séparer -2y+5 en [-2y, +5]
    def trouver_expression_distributivite(self):
        text = self.chaine_no_power.replace("+(", "+1(").replace("-(", "-1(")
        result = []
        i = 0

        while i < len(text):
            if text[i] == '(':
                debut = i
                while debut > 0 and text[debut] not in ['+', '-', ')']:
                    debut -= 1
                chaine1 = text[debut:i]
                if chaine1 == "" and text[0:2].isdigit():
                    chaine1 = text[0:2]

                elif chaine1 == "" and text[0:1].isdigit():
                    chaine1 = "+"+text[0:1]
                i += 1

                debut_parenthese = i
                while i < len(text) and text[i] != ')':
                    i += 1
                chaine2 = text[debut_parenthese:i].strip()
                result.append([chaine1, chaine2])
            i += 1
        for j in range(len(result)):
            for k in range(len(result[j])):
                if result[j][k] == ')':
                    result[j][k] = ''
        return result

    # permet de séparer -2y+5 en [-2y, +5]
    def separer_differents_monome(self, polynome):
        polynome = polynome.replace("-", " -")
        polynome = polynome.replace("+", " +")
        polynome = polynome.split(" ")
        if polynome[0] == "":
            polynome = polynome[1:]
        return polynome

    def multiplication_total(self):
        liste_total_terme = self.liste_separation_avant_multiplication
        liste_result = []
        for i in range(len(liste_total_terme)):
            result = {}
            for j in range(len(liste_total_terme[i])-1):
                if result == {} :
                    dico1 = self.transformer_liste_matrice_dictionnaire(liste_total_terme[i][j])
                    dico1 = reduire_dictionnaire(dico1)

                else:
                    dico1 = result
                dico2 = self.transformer_liste_matrice_dictionnaire(liste_total_terme[i][j+1])
                dico2 = reduire_dictionnaire(dico2)
                result = multiplication_polynome(dico1, dico2)
            liste_result.append(result)
        return liste_result





    # Pernet de séparer (4-x)(4-x)(4-x)+(4-x)(4-x)+3(5x-2y+4z) en [[4-x, 4-x, 4-x], [+1, 4-x, 4-x], [+3, 5x-2y+4z]]
    def separer_termes_principaux(self):
        liste_separer_principale = []
        new_terme = []
        liste_facteur = self.liste_facteur_distributivite
        if self.liste_facteur_distributivite[0][0] == "":

            liste_facteur[0][0] = "1"

        for item in liste_facteur:
            if item[0] == '':
                new_terme.append(item[1])
            else:
                if len(new_terme) == 0:
                    new_terme = list(item)
                    liste_separer_principale.append(new_terme)
                else:
                    new_terme = item
                    liste_separer_principale.append(item)

        for i in range(len(liste_separer_principale)):
            transform_all_plus_or_minus_in_list_in_one(liste_separer_principale[i])

        return liste_separer_principale

    def transformer_liste_matrice_dictionnaire(self, chaine):
        dic={}
        separer = self.separer_differents_monome(chaine)

        for j in range(len(separer)):
            separer[j] = remplace_first_plusorminus_by_plusone_or_minusone(separer[j])
            if separer[j] != "":
                separer[j] = split_string_at_first_letter(separer[j])
                for i in range(len(separer[j])):
                    if separer[j][0]=="":
                            separer[j][0]= "1"
                    separer[j][i] = remove_plus_in_first_position(separer[j][i])
                if separer[j][1] != "":
                    if add_power_one(separer[j][1]) not in dic :

                        dic[add_power_one(separer[j][1])] = [float(separer[j][0])]
                    else:
                        dic[add_power_one(separer[j][1])].append(float(separer[j][0]))
                else:
                    if "" not in dic:
                        dic[""] = [float(separer[j][0])]
                    else:
                        dic[""].append(float(separer[j][0]))
            else:
                dic[""].append(float(separer[j][0]))
        return dic

def multiplication_polynome(dico1,dico2):
    result_dico = {}
    for key1, value1 in dico1.items():
        key1 = expand_powers(key1)
        for key2, value2 in dico2.items():
            key2 = expand_powers(key2)
            key_final = key1+key2
            caracteres_tries = sorted(key_final)
            #Convertir la liste triée en une chaîne de caractères
            chaine_triee = ''.join(caracteres_tries)
            chaine_triee_puissance = transformer_chaine_en_puissance(chaine_triee)
            multiplication_coefficient = value1*value2
            if chaine_triee_puissance in result_dico:
                result_dico[chaine_triee_puissance] += multiplication_coefficient
            else:
                result_dico[chaine_triee_puissance] = multiplication_coefficient
    return result_dico




