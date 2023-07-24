import itertools
import math
import random
import expressionlitteral
import equation
from fractions import Fraction
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
liste_partie_litteral_degre_0_1 = ["x", "", "y","z"]
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

def créer_identite_remarquable(type = "default", liste_partie_litteral = liste_partie_litteral_degre_0_1):
    type_identite = ["(a+b)^2", "(a-b)^2", "(a+b)(a-b)"]
    if type == "default":
        identite_choisi = random.choice(type_identite)
    else:
        identite_choisi = type
    expression = ""

    coefficient_1 = random.randint(1,4)
    coefficient_2 = random.randint(1,4)

    elements = random.choices(liste_partie_litteral, k=2)

    # Vérification si les deux éléments sont différents
    while elements[0] == elements[1]:
        elements = random.choices(liste_partie_litteral, k=2)
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

def créer_équation_2_degré_solution_entière():

    a = random.randint(1,9)
    a= signe_aleatoire()+str(a)
    b= random.randint(1,9)
    b = signe_aleatoire()+str(b)
    if a!=b:
        chaine = f"(x{a})(x{b})"
        if a[0] == "+":
            a = f"-{a[1:]}"
        else:
            a = a[1:]
        if b[0] == "+":
            b = f"-{b[1:]}"
        else:
            b = b[1:]

        solution = [a,b]
    else:
        chaine = "(x+"+a+")^{2}"
        chaine = f"(x{a})(x{b})"
        if a[0] == "+":
            a = f"-{a[1:]}"
        else:
            a = a[1:]
        solution = [a]
    expression = expressionlitteral.Expression_litteral(chaine).chaine_polynome_reduit_ordonne
    equ = equation.Equation(expression, "0")

    return (equ,solution)
def créer_équation_1_ou_2_degré_solution_entiere():
    degre = random.randint(1,2)
    if degre == 1:
        solution = random.randint(-9,9)
        equ = equation.Equation("x",str(solution))
        exp_a_ajouter = creer_expression_litteral_ordonnee_aleatoire(1,8)
        exp_a_ajouter = exp_a_ajouter.replace("^1","")
        equ2 = equ.operation_chaque_cote("+", exp_a_ajouter)
        return (equ2, [solution])
    else:
        equ, solution = créer_équation_2_degré_solution_entière()
        exp_a_ajouter = creer_expression_litteral_ordonnee_aleatoire(2,3)
        exp_a_ajouter = exp_a_ajouter.replace("^1","").replace("^2", "^{2}")
        equ2 = equ.operation_chaque_cote("+", exp_a_ajouter)
        return(equ2, solution)

def generer_distributivite_coefficient_degre_0():
    coeff_devant_parenthese = random.randint(-9,9)
    while coeff_devant_parenthese == 0:
        coeff_devant_parenthese = random.randint(-9,9)
    first_coeff_parenthese = random.randint(-9,9)
    while first_coeff_parenthese == 0:
        first_coeff_parenthese = random.randint(-9,9)
    second_coeff_parenthese = random.randint(-9,9)
    while second_coeff_parenthese == 0:
        second_coeff_parenthese = random.randint(-9,9)
    if second_coeff_parenthese>0:
        second_coeff_parenthese = f"+{second_coeff_parenthese}"
    if random.randint(1,2)==1:
        expression = f"{coeff_devant_parenthese}({first_coeff_parenthese}x{second_coeff_parenthese})"
    else:
        expression = f"{coeff_devant_parenthese}({first_coeff_parenthese}{second_coeff_parenthese}x)"
    return expression

def generer_expression_degre_1():
    coefficient_1 = random.randint(-9,9)
    while coefficient_1 == 0:
        coefficient_1 = random.randint(-9,9)
    coefficient_2 = random.randint(-9,9)
    while coefficient_2 == 0:
        coefficient_2 = random.randint(-9,9)
    if coefficient_2 >0:
        coefficient_2 = f"+{coefficient_2}"
    if random.randint(1,2) == 1:
        return f"{coefficient_1}x{coefficient_2}"
    else:
        return f"{coefficient_1}{coefficient_2}x"

def créer_équation_1_solution_fraction():
        type_equation = random.randint(1,3)
        if type_equation == 1:
            solution = random.randint(-9,9)
            equ = equation.Equation("x",str(solution))
            exp_a_ajouter = creer_expression_litteral_ordonnee_aleatoire(1,8)
            exp_a_ajouter = exp_a_ajouter.replace("^1","")
            equ = equ.operation_chaque_cote("+", exp_a_ajouter)
        elif type_equation == 2:
            gauche = generer_distributivite_coefficient_degre_0()
            droite = generer_expression_degre_1()
            equ = equation.Equation(gauche, droite)
            solution = equ.resoudre()

        else:
            gauche = generer_distributivite_coefficient_degre_0()
            droite = generer_distributivite_coefficient_degre_0()
            equ = equation.Equation(gauche, droite)
            solution = equ.resoudre()

        return (equ, [solution])


def transform_liste_solution_into_chaine_S(liste):
    solution = "S={"
    for i in range(len(liste)):
        solution += f"{liste[i]};"
    solution = solution[:-1]+"}"
    return solution
def generer_trouver_par_evaluation():
    equ, solution = créer_équation_1_ou_2_degré_solution_entiere()
    solution_propose = []
    solution_propose.append(solution)
    for j in range(3):
        new_solution = []
        for i in range(len(solution)):
            sol = random.randint(-9,9)
            if i != 0:
                while sol == new_solution[0]:
                    sol = random.randint(-9,9)
            new_solution.append(sol)
        solution_propose.append(new_solution)

    solution_propose = verifier_et_rendre_uniques(solution_propose)
    random.shuffle(solution_propose)
    for i in range(len(solution_propose)):
        solution_propose[i] = transform_liste_solution_into_chaine_S(solution_propose[i])

    question = {
        "question": f"Trouve la solution de l'équation par évaluation: <span>$$ {equ.afficher()} $$</span>",
        "answer_user": solution_propose,
        "answer": transform_liste_solution_into_chaine_S(solution),
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question
def est_unique(liste):
    # Vérifie si la liste contient des sous-listes identiques, peu importe l'ordre
    return len(set(tuple(sorted(subliste)) for subliste in liste)) == len(liste)
def verifier_et_rendre_uniques(liste):
    while not est_unique(liste):
        for i in range(len(liste)):
            for j in range(i + 1, len(liste)):
                if sorted(liste[i]) == sorted(liste[j]):
                    for k in range(len(liste[j])):
                        liste[j][k] = random.randint(-9,9)
                    # Les deux éléments ont des sous-listes avec les mêmes nombres
                    # Retirer des nombres au hasard jusqu'à ce qu'ils soient uniques

    return liste
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

def generer_resoudre_equation_degre_1():
    equ = créer_équation_1_solution_fraction()
    if equ[1][0] != "impossible" and equ[1][0] != "reel":
        if type(equ[1][0]) == int:
            solution = ["S={"+str(equ[1][0])+"}", str(equ[1][0])]
        else:
            equ[1][0] = Fraction(equ[1][0]).limit_denominator()
            sol = f"{equ[1][0].numerator}/{equ[1][0].denominator}"
            solution = ["S={"+sol+"}", sol]
    else:
        solution = [equ[1][0]]
    question = {
        "question": f"Résous l'équation $${equ[0].afficher()}$$ Si la solution est un nombre entier note-la telle quelle si c'est un nombre à virgule inscrit la fraction irréductible comme par exemple -2/3",
        "answer": solution,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_poser_une_equation():
    poser_equation_liste = [{
    "question": "Un père est trois fois plus âgé que son fils. Dans 2 ans, il sera deux fois plus âgé que son fils. Si x représente l'âge actuel du fils, quelle est l'équation qui décrit cette situation ?",
    "answer": [equation.Equation("3x+2", "2(x+2)").resoudre()],
    "type": "question",
    "feedback": "Excellent travail ! Vous avez bien compris comment poser l'équation.",
    "feedbackClass": "text-success",
    "methods": []
},
        {
    "question": "Un train roule à une vitesse qui est quatre fois supérieure à celle d'une voiture. Si la voiture augmente sa vitesse de 3 km/h, la vitesse du train ne sera que trois fois celle de la voiture. Si x représente la vitesse actuelle de la voiture en km/h, quelle est l'équation qui décrit cette situation ?",
    "answer": [equation.Equation("4x+3", "3(x+3)").resoudre()],
    "type": "question",
    "feedback": "Bravo! Vous avez correctement posé et résolu l'équation.",
    "feedbackClass": "text-success",
    "methods": []
},
        {
    "question": "Un parc d'attractions facture un tarif qui est deux fois plus élevé pour les adultes que pour les enfants. Si le tarif pour les enfants augmente de 5€, le tarif pour les adultes ne sera plus que 1.5 fois le tarif pour les enfants. Si x représente le tarif actuel pour les enfants en €, quelle est l'équation qui décrit cette situation ?",
    "answer": [equation.Equation("2x+5", "1.5(x+5)").resoudre()],
    "type": "question",
    "feedback": "Très bien! Vous avez su poser correctement l'équation et la résoudre.",
    "feedbackClass": "text-success",
    "methods": []
},
        {
    "question": "Une entreprise produit des chaises. Le coût de production de chaque chaise est deux fois plus élevé que le coût de production de chaque table. Si le coût de production de chaque table augmente de 7€, le coût de production pour chaque chaise ne sera plus que 1.5 fois le coût de production pour chaque table. Si x représente le coût de production actuel pour chaque table en €, quelle est l'équation qui décrit cette situation ?",
    "answer": [equation.Equation("2x+7", "1.5(x+7)").resoudre()],
    "type": "question",
    "feedback": "Excellent ! Vous avez correctement formulé et résolu l'équation.",
    "feedbackClass": "text-success",
    "methods": []
},
        {
    "question": "Une personne économise de l'argent. Chaque mois, elle met de côté deux fois plus d'argent que le mois précédent. Après 3 mois, elle aura économisé 150€ de plus que si elle avait mis de côté le même montant chaque mois. Si x représente le montant en € qu'elle met de côté le premier mois, quelle est l'équation qui décrit cette situation ?",
    "answer": [equation.Equation("2x+2x+2x", "3x+150").resoudre()],
    "type": "question",
    "feedback": "Très bien ! Vous avez correctement posé et résolu l'équation.",
    "feedbackClass": "text-success",
    "methods": []
},
        {
    "question": "Un joueur de basketball marque des points. Si il marquait 2 paniers de 3 points de plus par match, il aurait un total de 6 points de plus par match. Si x représente le nombre de paniers de 3 points qu'il marque actuellement par match, quelle est l'équation qui décrit cette situation ?",
    "answer": [equation.Equation("3x", "3(x+2)+6").resoudre()],
    "type": "question",
    "feedback": "Excellent travail ! Vous avez correctement posé et résolu l'équation.",
    "feedbackClass": "text-success",
    "methods": []
}]
    return random.choice(poser_equation_liste)

def method_resoudre_equation_1_degre(user_answer):
    if "=" in user_answer:
        answer_split = user_answer.split("=")
        if len(answer_split) == 2:
            if len(answer_split[0])>0 and len(answer_split[1])>0 :
                if "x" in answer_split[0] or "x" in answer_split[1]:
                    try:
                        eq = equation.Equation(answer_split[0], answer_split[1])
                        solution = eq.resoudre()
                        return solution
                    except:
                        return "FAUX"
            else:
                return "FAUX"
        else:
            return "FAUX"
    else:
        return "FAUX"

def creer_équations_degre_1_ou_2_solution_entiere():
    if random.randint(1,2) == 1:
        solution = random.randint(-9,9)
        eq_depart = equation.Equation("x", f"{solution}")
        multiplicateur = random.randint(1,4)
        eq_depart = eq_depart.operation_chaque_cote("*", f"{multiplicateur}")
        coefficient_x = random.randint(-5,5)
        if coefficient_x<0:
            eq_depart = eq_depart.operation_chaque_cote("-", f"{math.fabs(coefficient_x)}x")
        else:
            eq_depart = eq_depart.operation_chaque_cote("+", f"{coefficient_x}x")
        ajout_coef_0 = random.randint(-9,9)
        if ajout_coef_0<0:
            eq_depart = eq_depart.operation_chaque_cote("-", f"{math.fabs(ajout_coef_0)}")
        else:
            eq_depart = eq_depart.operation_chaque_cote("+", f"{ajout_coef_0}")

        liste_coeff = [eq_depart.dico_left,eq_depart.dico_right]
        return liste_coeff, solution
    else:
        equ_debut, solution = créer_équation_2_degré_solution_entière()
        degre1 = generer_expression_degre_1()
        equ_debut = equ_debut.operation_chaque_cote("+", degre1)
        liste_coeff = [equ_debut.dico_left,equ_debut.dico_right]
        return liste_coeff, solution


def generer_Solution_par_voie_graphique():
    dico_coeff, solution = creer_équations_degre_1_ou_2_solution_entiere()
    chaine_solution = ""
    if type(solution) != int:
        if len(solution)==2:
            chaine_solution = [f"{solution[0]};{solution[1]}",f"{solution[1]};{solution[0]}"]
        else:
            chaine_solution = solution

    else:
        chaine_solution = [str(solution)]

    question = {
        "question": f"Les deux fonctions dessinées représentent la partie gauche et droite d'une équation. Trouve la/les valeur de x pour laquel/lesquelles les deux fonctions sont égales. Si il y a deux réponses inscrit un ; entre les deux comme par exemple 2;3",
        "fonctions":[dico_coeff[0], dico_coeff[1]],
        "answer": chaine_solution,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question

def generer_degre_1_avec_fraction():
    partie_litterale=["x^{1}", ""]
    expression = ""
    for i in range(2):
        coefficient = generer_fraction_aléatoire()
        if type(coefficient) != float:
            coefficient = "\\frac"+"{"+str(coefficient.numerator)+"}{"+str(coefficient.denominator)+"}"

        if signe_aleatoire() == "+":
            expression += f"+{coefficient}{partie_litterale[i]}"
        else:
            expression += f"-{coefficient}{partie_litterale[i]}"
        if expression[0] == "+":
            expression = expression[1:]
    expression2 = ""
    for i in range(2):
        coefficient = generer_fraction_aléatoire()
        if type(coefficient) != float:
            coefficient = "\\frac"+"{"+str(coefficient.numerator)+"}{"+str(coefficient.denominator)+"}"
        if signe_aleatoire() == "+":
            expression2 += f"+{coefficient}{partie_litterale[i]}"
        else:
            expression2 += f"-{coefficient}{partie_litterale[i]}"
        if expression2[0] == "+":
            expression2 = expression2[1:]
    expression = expression.replace("^{1}", "")
    expression2 = expression2.replace("^{1}", "")
    chaine = f"{expression}={expression2}"
    expression = expressionlitteral.replace_fractions_with_decimal(expression)
    expression2 = expressionlitteral.replace_fractions_with_decimal(expression2)
    return (chaine, equation.Equation(expression,expression2))


def generer_equation_avec_fraction():
    equ = generer_degre_1_avec_fraction()
    chaine_equ = equ[0]
    solution = equ[1].resoudre()
    if solution != "impossible" and solution != "reel":

        solution = Fraction(solution).limit_denominator()
        if type(solution) != float:
            solution = f"{solution.numerator}/{solution.denominator}"

    question = {
        "question": f"<p>Trouve la solution de l'équation ci-dessous. Inscris la fraction irréductible si la réponse est décimale comme 4/5 par exemple si la réponse est entière inscris celle-ci sous forme de nombre entier.</p><p>$$ {chaine_equ.replace('.0','')} $$</p>",
        "answer": [solution],
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question
def arrondir_si_possible(dictionnaire):
    for cle, valeur in dictionnaire.items():
        str_valeur = str(valeur)  # Convertir la valeur en chaîne de caractères
        if '99999' in str_valeur:
            index = str_valeur.find('99999')
            index_virgule = str_valeur.find('.')
            index_a_arrondir = index-index_virgule# Trouver l'index de la première occurrence de '99999'
            valeur_arrondie = round(valeur, index_a_arrondir)
            dictionnaire[cle] = valeur_arrondie
        elif '00000' in str_valeur:
            index = str_valeur.find('00000')
            index_virgule = str_valeur.find('.')
            index_a_arrondir = index-index_virgule# Trouver l'index de la première occurrence de '99999'
            valeur_arrondie = round(valeur, index_a_arrondir)
            dictionnaire[cle] = valeur_arrondie

    return dictionnaire



def creer_equation_second_degrer():
    if random.randint(1,2)==1 :
        expression = expressionlitteral.Expression_litteral(créer_identite_remarquable(liste_partie_litteral=["x", ""])).chaine_polynome_reduit_ordonne
        eq_depart = equation.Equation(expression, "0")
        return eq_depart
    else:
        choix_discriminant = random.randint(1,3)
        if choix_discriminant == 1:
            a = random.randint(1,10)
            if signe_aleatoire() == "-":
                a=-a
            c = random.randint(-100,100)
            if signe_aleatoire() == "-":
                c = -c
            b = 4*a*c
            if b<0:
                b = b+1
            else:
                b = b-1
                b = f"+{b}"
            if c>0:
                c = f"+{c}"
            equ = equation.Equation(str(a)+"x^{2}"+str(b)+"x^{1}"+str(c), "0")

        elif choix_discriminant == 2:
            solution_chaine = round(random.randint(1,100)/100,2)
            if signe_aleatoire() == "-":
                solution_chaine = -solution_chaine
            else:
                solution_chaine = f"+{solution_chaine}"

            dico = expressionlitteral.Expression_litteral("(x"+str(solution_chaine)+")^{2}").polynome_reduit_ordonne
            dico = arrondir_si_possible(dico)
            expression = ""
            for (key, value) in dico.items():
                if value >0:
                    expression += f"+{value}{key}"
                else:
                    expression += f"{value}{key}"
                if expression[0] == "+":
                    expression = expression[1:]
            equ = equation.Equation(expression, "0")
        else:
            solution_1 = round(random.randint(1,100)/100,2)
            solution_2 = round(random.randint(1,100)/100,2)
            if signe_aleatoire()=="-":
                solution_1 = -solution_1
            else:
                solution_1 = f"+{solution_1}"
            if signe_aleatoire() == "-":
                solution_2 = -solution_2
            else:
                solution_2 = f"+{solution_2}"
            dico = expressionlitteral.Expression_litteral(f"(x{solution_1})(x{solution_2})").polynome_reduit_ordonne
            dico = arrondir_si_possible(dico)
            expression = ""
            for (key, value) in dico.items():
                if value >0:
                    expression += f"+{value}{key}"
                else:
                    expression += f"{value}{key}"
                if expression[0] == "+":
                    expression = expression[1:]
            equ = equation.Equation(expression, "0")
        return equ

def generer_resoudre_equation_degre_2():
    eq = creer_equation_second_degrer()
    eq = eq.operation_chaque_cote("+", str(random.randint(1,15)))
    eq = eq.operation_chaque_cote("-", str(random.randint(1,15)))
    eq = eq.operation_chaque_cote("+", str(random.randint(1,15))+"x")
    eq = eq.operation_chaque_cote("-", str(random.randint(1,15))+"x")
    dico = arrondir_si_possible(eq.dico_left)
    expression = ""
    for (key, value) in dico.items():
        if value % 1 == 0:
            value = int(value)
        if value ==1 and key!="":
            expression += f"+{key}"
        elif value ==-1 and key!="":
            expression += f"-{key}"
        elif value>0:
            expression += f"+{value}{key}"
        else:
            expression += f"{value}{key}"
        if expression[0] == "+":
            expression = expression[1:]
    expression = expression.replace("^{1}", "")
    eq = equation.Equation(expression, eq.chaine_right)


    solution = eq.resoudre()
    for i in range(len(solution)):
        if solution[0] == "impossible":
            pass
        elif solution[i] % 1 == 0:
            solution[i] = (int(solution[i]))
        elif type(solution[i]) == float:
            solution[i] = round(solution[i], 2)

    if len(solution) == 2:
        solution = [f"{solution[0]};{solution[1]}",f"{solution[1]};{solution[0]}"]
    else:
        solution = [str(solution[0])]

    question = {
        "question": f"<p>Trouve la/les solution(s) de l'équation ci-dessous. Si c'est un nombre entier inscris le sans virgule sinon si c'est un nombre décimal, inscris le avec deux chiffres après la virgule</p><p>$$ {eq.afficher()} $$</p>",
        "answer": solution,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question


def generer_reconnaissance_fonction():
    choix = random.randint(1,5)
    if choix == 1:
        coeff_0 = random.randint(-5, 5)
        while coeff_0 == 0:
            coeff_0 = random.randint(-5, 5)
        dico_coeff = {"": coeff_0}
        solution = "constante"
    elif choix == 2:
        coeff_1 = random.randint(-5, 5)
        while coeff_1 == 0:
            coeff_1 = random.randint(-5, 5)
        dico_coeff = {"x^{1}": coeff_1}
        solution = "linéaire"
    elif choix == 3:
        coeff_0 = random.randint(-5, 5)
        while coeff_0 == 0:
            coeff_0 = random.randint(-5, 5)
        coeff_1 = random.randint(-5, 5)
        while coeff_1 == 0:
            coeff_1 = random.randint(-5, 5)
        dico_coeff = {"": coeff_0, "x^{1}": coeff_1}
        solution = "affine"
    elif choix == 4:
        coeff_0 = random.randint(-5, 5)
        coeff_1 = random.randint(-5, 5)
        coeff_2 = random.randint(-2, 2)
        while coeff_2 == 0:
            coeff_2 = random.randint(-2, 2)
        dico_coeff = {"": coeff_0, "x^{1}": coeff_1, "x^{2}": coeff_2}
        solution = "quadratique"
    else:
        coeff_0 = random.randint(-2, 2)
        coeff_1 = random.randint(-2, 2)
        coeff_2 = random.randint(-1, 1)
        coeff_3 = random.randint(-1, 1)
        while coeff_3 == 0:
            coeff_3 = random.randint(-1, 1)
        dico_coeff = {"": coeff_0, "x^{1}": coeff_1, "x^{2}": coeff_2, "x^{3}":coeff_3}
        solution = "cubique"


    question = {
        "question": f"Quelle est le type de la fonction représentée ci-dessous?",
        "fonctions":[dico_coeff, {}],
        "answer": solution,
        "feedback": random.choice(congratulations_messages),
        "feedbackClass": "text-success",
        "methods": ["enlever_espace"]}
    return question


















