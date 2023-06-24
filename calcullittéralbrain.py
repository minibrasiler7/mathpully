import itertools
import random
import effectuer_reduire_ordonner
from fractions import Fraction
import re


congratulations_messages = [
    "Félicitations, c'est la bonne réponse ! Continuez comme ça !",
    "Bravo ! Votre réponse est correcte. Vous êtes doué en maths !",
    "Superbe travail ! Votre réponse est juste.",
    "Excellent ! Vous avez résolu ce problème avec brio.",
    "Fantastique ! Votre réponse est correcte. Continuez à apprendre et à vous amuser avec les maths !",
    "Impressionnant ! Vous avez trouvé la bonne réponse.",
    "Bien joué ! Vous avez raison.",
    "Magnifique ! Vous avez correctement résolu ce problème mathématique.",
    "Formidable ! Vous avez correctement répondu à cette question.",
    "Super ! C'est la bonne réponse. Continuez à relever ces défis mathématiques !",
    "Incroyable ! Vous avez trouvé la bonne réponse. Vos compétences en maths sont impressionnantes !",
]
liste_partie_litteral = ["x", "x^{2}", "y", "", "y^{2}", "xy", "xz", "yz", "z", "x^{2}y", "xy^{2}", "z^{2}", "xz^{2}", "x^{2}z", "y^{2}z", "yz^{2}", "xyz"]

def signe_aleatoire():
    nombre = random.randint(0,1)
    if nombre==0:
        signe = "+"
    else:
        signe = "-"
    return signe

def evaluer_une_expression(expression, evaluation):
    expression = expression.replace("^", "**")
    expression = expression.replace("+x", "+1x")
    expression = expression.replace("-x", "-1x")

    if evaluation<0:
        expression = expression.replace("x", f"*({evaluation})")
    else:
        expression = expression.replace("x", f"*{evaluation}")
    if expression[0] == "+":
        expression = expression[1:]
    if expression[0] == "*":
        expression = expression[1:]

    return eval(expression)


def creer_expression_litteral_ordonnee_aleatoire(degree, coefficient_max):
    expression = ""
    for i in range(degree+1):
        coefficient = random.randint(1,coefficient_max)
        signe = signe_aleatoire()
        if coefficient == 1 and degree-i != 0:
            coefficient = ""
        if (degree-i) != 0:
            expression += f"{signe}{str(coefficient)}x^{degree-i}"
        else:
            expression += f"{signe}{str(coefficient)}"
    if expression[0] == "+":
        expression = expression[1:]
    return expression


def créer_expression_literale_nonreduite_nonordonnee_fraction(nombre_partie_litteral_differente, nombre_termes):
    partie_litteral = liste_partie_litteral[:nombre_partie_litteral_differente]
    expression = ""
    for i in range(nombre_termes):
        coefficient = generer_fraction_aléatoire()
        if type(coefficient) != Fraction:
            coefficient = signe_aleatoire()+str(coefficient)
        else:
            coefficient = signe_aleatoire()+"\\frac{"+str(coefficient.numerator)+"}{"+str(coefficient.denominator)+"}"
        terme_litteral = random.choice(partie_litteral)
        terme = coefficient +terme_litteral
        expression += terme
    if expression[0] == "+":
        expression = expression[1:]
    return expression
def créer_expression_literale_nonreduite_nonordonnee(nombre_partie_litteral_differente, coefficient_max, nombre_termes):
    partie_litteral = liste_partie_litteral[:nombre_partie_litteral_differente]
    expression = ""
    for i in range(nombre_termes):
        coefficient = random.randint(1,coefficient_max)
        coefficient = signe_aleatoire()+str(coefficient)
        terme_litteral = random.choice(partie_litteral)
        terme = coefficient +terme_litteral
        expression += terme
    if expression[0] == "+":
        expression = expression[1:]
    return expression

def générer_liste_combinaison_possible_polynome(poly_dict):
    poly_list = []
    for k, v in poly_dict.items():
        if k == '':

            if type(v) == Fraction:
                if v.numerator<0:
                    term= f'{v.numerator}/{v.denominator}'
                else:
                    term= f'+{v.numerator}/{v.denominator}'

            elif v<0:
                term = f'{v}'
            else:
                term = f'+{v}'
        else:
            if type(v) == Fraction:
                if v.numerator<0:
                    term= f'{v.numerator}/{v.denominator}{k}'
                else:
                    term= f'+{v.numerator}/{v.denominator}{k}'
            elif v==1:
                term = f'+{k}'
            elif v ==-1:
                term = f'-{k}'
            else:
                term = f'{v}{k}' if v < 0 else f'+{v}{k}'
        poly_list.append(term)

    # Générer toutes les permutations des termes
    permutations = list(itertools.permutations(poly_list, len(poly_list)))

    # Convertir chaque permutation en une chaîne de caractères et l'ajouter à la liste des polynômes
    polynomials = [''.join(p) for p in permutations]

    return polynomials

def changer_nombre_virgule_en_entier(expression):
    expression = expression.replace(".0", "")
    return expression

def enlever_puissance_un(expression):
    expression = expression.replace("^{1}", "")
    return expression

def enlever_denominateur_un(expression):
    nouvelle_expression = ""
    for i in range(len(expression)):
        if i>0:
            if expression[i] == "1" and expression[i-1] == "/":
                if i != len(expression)-1:
                    if not expression[i+1].isdigit():
                        nouvelle_expression = nouvelle_expression[:-1]
                    else:
                        nouvelle_expression += expression[i]
                else:
                    nouvelle_expression = nouvelle_expression[:-1]
            else:
                nouvelle_expression += expression[i]
        else:
            nouvelle_expression += expression[i]
    return nouvelle_expression

def enlever_crochet_puissance(expression):
    expression = expression.replace("{", "")
    expression = expression.replace("}", "")
    return expression

def generer_fraction_aléatoire():
    numerateur = random.randint(1,9)
    dénominateur = random.randint(1,9)
    if numerateur % dénominateur == 0:
        return numerateur/dénominateur
    else:
        return Fraction(numerateur, dénominateur)

def reduire_expression(expression):
    polynome = effectuer_reduire_ordonner.Expression_litteral(expression)
    liste_polynome_possible = générer_liste_combinaison_possible_polynome(polynome.polynome_reduit_ordonne)
    for i in range(len(liste_polynome_possible)):
        liste_polynome_possible[i] = changer_nombre_virgule_en_entier(liste_polynome_possible[i])
        liste_polynome_possible[i] = enlever_puissance_un(liste_polynome_possible[i])
        liste_polynome_possible[i] = enlever_crochet_puissance(liste_polynome_possible[i])
        if len(liste_polynome_possible[i])>0:
            if liste_polynome_possible[i][0] == "+":
                liste_polynome_possible[i] = liste_polynome_possible[i][1:]
    return liste_polynome_possible

def generer_expression_distributivite():
    coefficient = random.randint(1,8)
    signe = signe_aleatoire()
    partie_litteral_avant_p = random.choice(liste_partie_litteral[:6])
    nombre_terme_parenthèse = random.randint(2,3)

    chaine= f"{signe}{coefficient}{partie_litteral_avant_p}("
    for i in range(nombre_terme_parenthèse):
        coeff = coefficient = random.randint(1,8)
        signe = signe_aleatoire()
        if signe == "+" and i == 0:
            signe = ""
        partie_litteral = random.choice(liste_partie_litteral[:6])
        chaine += f"{signe}{coefficient}{partie_litteral}"
    chaine+= ")"
    if chaine[0] == "+":
        chaine = chaine[1:]
    return chaine

def remove_power_one(expression):
    return expression.replace("^1", "")

def remove_coefficient_1_from_chaine(chaine):
    newchaine = ""
    for i in range(len(chaine)-1):
        if chaine[i] == "1":
            if i>0:
                if chaine[i-1] == "+" or chaine[i-1] == "-":
                    if not chaine[i+1].isdigit() or chaine[i+1] == ")":
                        pass
                    else:
                        newchaine += chaine[i]
                else:
                    newchaine += chaine[i]
            else:
                 if not chaine[i+1].isdigit():
                     pass
                 else:
                     newchaine += chaine[i]
        else:
            newchaine += chaine[i]
    newchaine += chaine[-1]
    return newchaine

def generer_Evaluer_une_expression_littérale():
    for i in range(0,4):
        evaluation = random.randint(0,9)
        if random.randint(0,1) == 1:
            evaluation = -evaluation
        degree = random.randint(1,2)
        expression = creer_expression_litteral_ordonnee_aleatoire(degree, 4)
        eval = evaluer_une_expression(expression, evaluation)
        question = {
        "question": f"Evalue l'expression pour x={evaluation} : <span>$$ {remove_power_one(expression)} $$</span>",
        "answer": [f"{eval}"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    }
    return question


def generer_reduire_une_expression_littérale():

    polynome = créer_expression_literale_nonreduite_nonordonnee(4,8,6)
    reponse = reduire_expression(polynome)
    question = {
        "question": f"Réduire l'expression: <span>$$ {remove_coefficient_1_from_chaine(polynome)} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_reduire_une_expression_littérale_fraction():
    polynome = créer_expression_literale_nonreduite_nonordonnee_fraction(2,4)
    polynome_decimal = effectuer_reduire_ordonner.replace_fractions_with_decimal(polynome)
    polynome = changer_nombre_virgule_en_entier(polynome)

    polynome_decimal = effectuer_reduire_ordonner.Expression_litteral(polynome_decimal)
    dict_reduction = polynome_decimal.polynome_reduit_ordonne
    dict_fraction = effectuer_reduire_ordonner.change_reduit_ordonnee_to_fraction_dict(dict_reduction)

    liste_possible_polyome = générer_liste_combinaison_possible_polynome(dict_fraction)
    for i in range(len(liste_possible_polyome)):
        liste_possible_polyome[i]= effectuer_reduire_ordonner.remove_plus_in_first_position(liste_possible_polyome[i])
        liste_possible_polyome[i] = effectuer_reduire_ordonner.remove_power_one(liste_possible_polyome[i])
        liste_possible_polyome[i] = remove_coefficient_1_from_chaine(liste_possible_polyome[i])
        liste_possible_polyome[i] = enlever_denominateur_un(liste_possible_polyome[i])
        liste_possible_polyome[i] = enlever_crochet_puissance(liste_possible_polyome[i])
    question = {
        "question": f"Réduire l'expression: <span>$$ {remove_coefficient_1_from_chaine(polynome)} $$</span>",
        "answer": liste_possible_polyome,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_ordonner_une_expression_littérale():
    polynome = créer_expression_literale_nonreduite_nonordonnee(8,4,4)
    polynome = remove_coefficient_1_from_chaine(polynome)
    expression = effectuer_reduire_ordonner.Expression_litteral(polynome)
    reponse = expression.chaine_polynome_reduit_ordonne

    reponse= effectuer_reduire_ordonner.remove_plus_in_first_position(reponse)
    reponse = effectuer_reduire_ordonner.remove_power_one(reponse)
    reponse = remove_coefficient_1_from_chaine(reponse)
    reponse = enlever_crochet_puissance(reponse)
    question = {
        "question": f"Réduis et ordonne l'expression: <span>$$ {polynome} $$</span>",
        "answer": [reponse],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question


def generer_distribution():
    polynome = generer_expression_distributivite()

    polynome = remove_coefficient_1_from_chaine(polynome)

    reponse = reduire_expression(polynome)

    question = {
        "question": f"Distribue et réduis: <span>$$ {polynome} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question
print(generer_distribution())






