import itertools
import random
import expressionlitteral
import equation
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
liste_partie_litteral_degre_0_1 = ["x", "y", "","z"]
liste_partie_litteral_degre_1 = ["x","y","z"]
liste_partie_litteral_sans_degre_3 = ["x", "x^{2}", "y", "", "y^{2}", "xy", "xz", "yz", "z", "z^{2}"]
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

def creer_equation_premier_degre_effectuer_ordonner():
    first_signe = signe_aleatoire()
    first_coefficient = random.randint(1,9)
    first_0_signe = signe_aleatoire()
    first_0_degree = random.randint(1,9)

    second_signe = signe_aleatoire()
    second_coefficient = random.randint(1,9)

    second_0_signe = signe_aleatoire()
    second_0_degree = random.randint(1,9)
    liste_diviseur = trouver_diviseur_commun_de_coefficients([first_coefficient, first_0_degree, second_coefficient, second_0_degree])
    if first_coefficient==1:
        first_coefficient=""
    if second_coefficient==1:
        second_coefficient=""
    if first_signe=="+":
        first_signe = ""
    if second_signe=="+":
        second_signe=""
    chaine_gauche = f"{first_signe}{first_coefficient}x{first_0_signe}{first_0_degree}"
    chaine_droite = f"{second_signe}{second_coefficient}x{second_0_signe}{second_0_degree}"

    equ = equation.Equation(chaine_gauche,chaine_droite)

    return (equ, liste_diviseur)





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

def créer_identite_remarquable(type = "default"):
    type_identite = ["(a+b)^2", "(a-b)^2", "(a+b)(a-b)"]
    if type == "default":
        identite_choisi = random.choice(type_identite)
    else:
        identite_choisi = type
    expression = ""

    coefficient_1 = random.randint(1,4)
    coefficient_2 = random.randint(1,4)

    elements = random.choices(liste_partie_litteral_degre_0_1, k=2)

    # Vérification si les deux éléments sont différents
    while elements[0] == elements[1]:
        elements = random.choices(liste_partie_litteral_degre_0_1, k=2)
    # Extraction des éléments choisis
    partie_litteral_1, partie_litteral_2 = elements
    if coefficient_1==1 and partie_litteral_1!="":
        coefficient_1 = ""
    if identite_choisi == "(a+b)^2" :
        expression = "("+str(coefficient_1)+partie_litteral_1+"+"+str(coefficient_2)+partie_litteral_2+")^{2}"
    elif identite_choisi == "(a-b)^2":
        expression = "("+str(coefficient_1)+partie_litteral_1+"-"+str(coefficient_2)+partie_litteral_2+")^{2}"
    elif identite_choisi == "(a+b)(a-b)":
        expression = "("+str(coefficient_1)+partie_litteral_1+"+"+str(coefficient_2)+partie_litteral_2+")("+str(coefficient_1)+partie_litteral_1+"-"+str(coefficient_2)+partie_litteral_2+")"

    return expression

def créer_expression_literale_pour_factorisation():
    type_factorisation = ["diviseurcommun", "(a+b)^2", "(a-b)^2", "(a+b)(a-b)", "(a+b)(a+c)"]
    choix = random.choice(type_factorisation)
    # type 1 diviseur commun 3x^2 + 3x + 6xy _> 3x(x+1+2y)
    if choix == "diviseurcommun":
        expression = ""
        coefficient = random.randint(1,9)
        if coefficient==1:
            coefficient = ""
            choice = random.choice(liste_partie_litteral_sans_degre_3)
            while choice == "":
                 choice = random.choice(liste_partie_litteral_sans_degre_3)
        else:
            choice = random.choice(liste_partie_litteral_sans_degre_3)
        coefficient_parenhese = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
        while coefficient_parenhese[0] % coefficient_parenhese[1]== 0 or coefficient_parenhese[0] % coefficient_parenhese[2]== 0 or coefficient_parenhese[1] % coefficient_parenhese[2]== 0 :
            coefficient_parenhese = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
        partie_litteral_parenthese = [random.choice(liste_partie_litteral_degre_0_1), random.choice(liste_partie_litteral_degre_0_1), random.choice(liste_partie_litteral_degre_0_1)]
        while partie_litteral_parenthese[0] == partie_litteral_parenthese[1] or partie_litteral_parenthese[1] == partie_litteral_parenthese[2] or partie_litteral_parenthese[0] == partie_litteral_parenthese[2]:
            partie_litteral_parenthese = [random.choice(liste_partie_litteral_degre_0_1), random.choice(liste_partie_litteral_degre_0_1), random.choice(liste_partie_litteral_degre_0_1)]
        if coefficient_parenhese[0] == 1 and partie_litteral_parenthese[0]!="":
            coefficient_parenhese[0] == ""
        expression = f"{coefficient}{choice}({coefficient_parenhese[0]}{partie_litteral_parenthese[0]}+{coefficient_parenhese[1]}{partie_litteral_parenthese[1]}+{coefficient_parenhese[2]}{partie_litteral_parenthese[2]})"
        expression2 = f"{coefficient}{choice}({coefficient_parenhese[0]}{partie_litteral_parenthese[0]}+{coefficient_parenhese[2]}{partie_litteral_parenthese[2]}+{coefficient_parenhese[1]}{partie_litteral_parenthese[1]})"
        expression3 = f"{coefficient}{choice}({coefficient_parenhese[1]}{partie_litteral_parenthese[1]}+{coefficient_parenhese[0]}{partie_litteral_parenthese[0]}+{coefficient_parenhese[2]}{partie_litteral_parenthese[2]})"
        expression4 = f"{coefficient}{choice}({coefficient_parenhese[1]}{partie_litteral_parenthese[1]}+{coefficient_parenhese[2]}{partie_litteral_parenthese[2]}+{coefficient_parenhese[0]}{partie_litteral_parenthese[0]})"
        expression5 = f"{coefficient}{choice}({coefficient_parenhese[2]}{partie_litteral_parenthese[2]}+{coefficient_parenhese[1]}{partie_litteral_parenthese[1]}+{coefficient_parenhese[0]}{partie_litteral_parenthese[0]})"
        expression6 = f"{coefficient}{choice}({coefficient_parenhese[2]}{partie_litteral_parenthese[2]}+{coefficient_parenhese[0]}{partie_litteral_parenthese[0]}+{coefficient_parenhese[1]}{partie_litteral_parenthese[1]})"

        return [expression, expression2, expression3, expression4, expression5, expression6]
    elif choix == "(a+b)^2":
        expression = ""
        coefficient = random.randint(1,6)
        if coefficient == 1:
            coefficient = ""
        litteral = random.choice(liste_partie_litteral_degre_1)
        coefficent2 = random.randint(1,9)
        expression = "("+str(coefficient)+litteral+"+"+str(coefficent2)+")^{2}"
        expression2 = "("+str(coefficent2)+"+"+str(coefficient)+litteral+")^{2}"
        return[expression, expression2]
    elif choix == "(a-b)^2":
        coefficient = random.randint(1,6)
        if coefficient == 1:
            coefficient = ""
        litteral = random.choice(liste_partie_litteral_degre_1)
        coefficent2 = random.randint(1,9)
        expression = "("+str(coefficient)+litteral+"-"+str(coefficent2)+")^{2}"
        expression2 = "(-"+str(coefficent2)+"+"+str(coefficient)+litteral+")^{2}"
        return[expression, expression2]
    elif choix == "(a+b)(a-b)":
        coefficient = random.randint(1,6)
        if coefficient == 1:
            coefficient = ""
        litteral = random.choice(liste_partie_litteral_degre_1)
        coefficent2 = random.randint(1,9)
        a = str(coefficient)+litteral
        b = str(coefficent2)
        expression = f"({a}+{b})({a}-{b})"
        expression2 = f"({a}+{b})(-{b}+{a})"
        expression3 = f"({b}+{a})({a}-{b})"
        expression4 = f"({b}+{a})(-{b}+{a})"
        expression5 = f"({a}-{b})({a}+{b})"
        expression6 = f"({a}-{b})({b}+{a})"
        expression7 = f"(-{b}+{a})({a}+{b})"
        expression8 = f"(-{b}+{a})({b}+{a})"

        return[expression, expression2, expression3, expression4, expression5,expression6,expression7, expression8]
    elif choix == "(a+b)(a+c)":
        litteral = random.choice(liste_partie_litteral_degre_1)
        coefficient = random.randint(1,12)
        signe1 = signe_aleatoire()
        coefficient2 = random.randint(1,12)
        signe2 = signe_aleatoire()
        a = str(litteral)
        b = signe1 + str(coefficient)
        c = signe2 + str(coefficient2)
        expression = f"({a}{b})({a}{c})"
        expression2 = f"({a}{c})({a}{b})"
        expression3 = f"({b}+{a})({c}+{a})"
        expression4 = f"({c}+{a})({b}+{a})"
        expression3 = expression3.replace("(+", "(")
        expression4 = expression4.replace("(+", "(")
        return [expression,expression2,expression3,expression4]


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

def créer_expression_litterale_double_distributivite():
    expression = "("
    deux_first_partie_litteral = random.sample(liste_partie_litteral[:5], 2)
    deux_second_partie_litteral = random.sample(liste_partie_litteral[:5], 2)
    four_partie_litteral = [deux_first_partie_litteral[0], deux_first_partie_litteral[1] ,deux_second_partie_litteral[0], deux_second_partie_litteral[1]]
    four_coefficient = []
    four_signe = []
    for i in range(4):
        four_coefficient.append(random.randint(1,9))
        four_signe.append(signe_aleatoire())
        if four_signe[i] == "+" and (i == 0 or i==2):
            expression += f"{four_coefficient[i]}{four_partie_litteral[i]}"
        else:
            expression += f"{four_signe[i]}{four_coefficient[i]}{four_partie_litteral[i]}"
        if i==1:
            expression+= ")("

    expression += ")"
    return expression

def créer_expression_litterale_add_sous_polynome():
    expression = "("
    nombre_terme_1 = random.randint(2,3)
    nombre_terme_2 = random.randint(2,3)
    first_partie_litteral = random.sample(liste_partie_litteral[:3], nombre_terme_1)
    second_partie_litteral = random.sample(liste_partie_litteral[:3], nombre_terme_2)
    for i in range(nombre_terme_1):
        signe = signe_aleatoire()
        if signe == "+" and i == 0:
            expression += f"{random.randint(1,9)}{first_partie_litteral[i]}"
        else:
            expression += f"{signe}{random.randint(1,9)}{first_partie_litteral[i]}"
    expression += f"){signe_aleatoire()}("
    for i in range(nombre_terme_2):
        signe = signe_aleatoire()
        if signe == "+" and i == 0:
            expression += f"{random.randint(1,9)}{second_partie_litteral[i]}"
        else:
            expression += f"{signe}{random.randint(1,9)}{second_partie_litteral[i]}"

    expression += ")"

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
    polynome = expressionlitteral.Expression_litteral(expression)
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
        coefficient = random.randint(1,8)
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
                if chaine[i-1] in ["+", "-"]:
                    if chaine[i+1].isdigit() or chaine[i+1] in ["+", "-", "*", "/",")"] :
                        newchaine += chaine[i]
                else:
                    newchaine += chaine[i]
            else:
                 if chaine[i+1].isdigit() or chaine[i+1] in ["+", "-", "*", "/",")"] :
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
    polynome = remove_coefficient_1_from_chaine(polynome)
    question = {
        "question": f"Réduire l'expression: <span>$$ {polynome} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_reduire_une_expression_littérale_fraction():
    polynome = créer_expression_literale_nonreduite_nonordonnee_fraction(2,4)
    polynome_decimal = expressionlitteral.replace_fractions_with_decimal(polynome)
    polynome = changer_nombre_virgule_en_entier(polynome)

    polynome_decimal = expressionlitteral.Expression_litteral(polynome_decimal)
    dict_reduction = polynome_decimal.polynome_reduit_ordonne
    dict_fraction = expressionlitteral.change_reduit_ordonnee_to_fraction_dict(dict_reduction)

    liste_possible_polyome = générer_liste_combinaison_possible_polynome(dict_fraction)
    for i in range(len(liste_possible_polyome)):
        liste_possible_polyome[i]= expressionlitteral.remove_plus_in_first_position(liste_possible_polyome[i])
        liste_possible_polyome[i] = expressionlitteral.remove_power_one(liste_possible_polyome[i])
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
    expression = expressionlitteral.Expression_litteral(polynome)
    reponse = expression.chaine_polynome_reduit_ordonne
    reponse= expressionlitteral.remove_plus_in_first_position(reponse)
    reponse = expressionlitteral.remove_power_one(reponse)
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

def generer_double_distribution():
    polynome = créer_expression_litterale_double_distributivite()
    polynome = remove_coefficient_1_from_chaine(polynome)
    reponse = reduire_expression(polynome)
    question = {
        "question": f"Distribue et réduis: <span>$$ {polynome} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_identites_remarquables():
    polynome = créer_identite_remarquable()
    polynome = remove_coefficient_1_from_chaine(polynome)
    reponse = reduire_expression(polynome)
    question = {
        "question": f"Développe l'identité remarquable suivante : <span>$$ {polynome} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_sous_add_poly():
    polynome = créer_expression_litterale_add_sous_polynome()
    polynome = remove_coefficient_1_from_chaine(polynome)
    reponse = reduire_expression(polynome)
    question = {
        "question": f"Enlève les parenthèses et réduis: <span>$$ {polynome} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_factorisation():
    reponse = créer_expression_literale_pour_factorisation()
    polynome = reduire_expression(reponse[0])[0]
    for i in range(len(reponse)):
        reponse[i]= enlever_crochet_puissance(reponse[i])
    question = {
        "question": f"Factorise l'expression suivante: <span>$$ {polynome} $$</span>",
        "answer": reponse,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_preuve_calcul_litteral():
    exercices = [
    {
        "question": "Comment représenter un nombre pair avec une variable n ?",
        "answer": ["2n", "2*n", "n*2"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre impair avec une variable n ?",
        "answer": ["2n+1", "2*n+1", "2n-1", "2*n-1", "-1+2n", "-1+2*n", "1+2n", "1+2*n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter le carré d'un nombre avec une variable n ?",
        "answer": ["n^2", "n*n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter le cube d'un nombre avec une variable n ?",
        "answer": ["n^3", "n*n*n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre qui est un multiple de 5 avec une variable n ?",
        "answer": ["5n", "5*n", "n*5"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre qui est le double d'un autre avec une variable n ?",
        "answer": ["2n", "2*n", "n*2"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre qui est le triple d'un autre avec une variable n ?",
        "answer": ["3n", "3*n", "n*3"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre qui est la moitié d'un autre avec une variable n ?",
        "answer": ["n/2", "0.5*n", "n*0.5"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre qui est un quart d'un autre avec une variable n ?",
        "answer": ["n/4", "0.25*n", "n*0.25"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter la somme de deux nombres avec les variables n et m ?",
        "answer": ["n+m", "m+n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter la différence de deux nombres avec les variables n et m ?",
        "answer": ["n-m", "m-n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter le produit de deux nombres avec les variables n et m ?",
        "answer": ["n*m", "m*n", "nm", "mn"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter le quotient de deux nombres avec les variables n et m ?",
        "answer": ["n/m", "m/n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre augmenté de 5 avec une variable n ?",
        "answer": ["n+5", "5+n"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    {
        "question": "Comment représenter un nombre diminué de 5 avec une variable n ?",
        "answer": ["n-5"],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]
    },
    ]
    question = random.choice(exercices)

    return question


def trouver_diviseur_commun_de_coefficients(liste_coefficient):
    liste_diviseurs = []
    for i in range(2,10):
        divisible = True
        for j in range(len(liste_coefficient)):
            if liste_coefficient[j] % i !=0:
                divisible = False
        if divisible:
            liste_diviseurs.append(i)
    return liste_diviseurs



def generer_equation_equivalente():
    equation, liste_diviseur = creer_equation_premier_degre_effectuer_ordonner()

    if len(liste_diviseur) != 0:
        operations = ["+", "-", "*", "/"]
    else:
        operations = ["+", "-", "*"]
    operations_choisi = random.choice(operations)

    if operations_choisi== "+" or operations_choisi=="-" :
        coefficient = random.randint(1,9)
        if coefficient==1:
            coefficient=""
        partie_litteral = f"{coefficient}x"
        reponse = equation.operation_chaque_cote(operations_choisi, partie_litteral)

    elif operations_choisi == "*":
        signe_multiplication = signe_aleatoire()
        coefficient = random.randint(1,9)
        if signe_multiplication == "-":
            coefficient = -coefficient
        partie_litteral = coefficient
        reponse = equation.operation_chaque_cote("*", str(coefficient))

    else:
        signe_division = signe_aleatoire()
        coefficient = random.choice(liste_diviseur)
        if signe_division=="-":
            coefficient = -coefficient
        partie_litteral = coefficient
        reponse = equation.operation_chaque_cote("/", str(coefficient))

    if operations_choisi == "*":
        operations_choisi="\\times"
    if str(partie_litteral)[0] == "-":
        partie_litteral = f"({partie_litteral})"

    question = {
        "question": f"Voici une équation $${equation.afficher()}$$ si tu fais l'opération $${operations_choisi}{partie_litteral}$$ de chaque côté de l'équation écris l'équation équivalente que tu obtiens (chaque côté doit être réduit et ordonné)",
        "answer": [reponse.afficher()],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question
def generer_Evaluer_une_expression_littérale():
    pass

print(generer_equation_equivalente())
