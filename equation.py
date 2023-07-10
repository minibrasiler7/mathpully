import math

import expressionlitteral as el
import re
import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def inverser_dictionnaire(dico):
    new_dico = {k: -v for (k,v) in dico.items()}
    return new_dico

def additionner_deux_dictionnaires(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

def from_dicos_to_new_equation(dico_left, dico_right):
    new_chaine_left = el.transform_dictionnaire_to_polynome(dico_left)
    new_chaine_right = el.transform_dictionnaire_to_polynome(dico_right)
    expression_left = el.Expression_litteral(new_chaine_left).chaine_polynome_reduit_ordonne
    expression_right = el.Expression_litteral(new_chaine_right).chaine_polynome_reduit_ordonne
    return Equation(expression_left, expression_right)


class Equation:
    def __init__(self, expression_left, expression_right):
        if expression_left=="":
            expression_left="0"
        if expression_right=="":
            expression_right="0"
        self.chaine_left = expression_left
        self.chaine_right = expression_right
        self.expression_left = el.Expression_litteral(expression_left)
        self.expression_right = el.Expression_litteral(expression_right)
        self.dico_left = self.expression_left.polynome_reduit_ordonne
        self.dico_right = self.expression_right.polynome_reduit_ordonne
        self.equal_zero = self.passer_equation_d_un_cote()
        self.degre = self.degree_equation()

    def afficher(self):
        return f"{self.chaine_left}={self.chaine_right}"


    def passer_equation_d_un_cote(self):
        dico_right_inverse = inverser_dictionnaire(self.dico_right)
        dico_merge = additionner_deux_dictionnaires(self.dico_left, dico_right_inverse)
        polynome = el.transform_dictionnaire_to_polynome(dico_merge)
        expression = el.Expression_litteral(polynome)
        dico_merge_ordonne = expression.polynome_reduit_ordonne
        return dico_merge_ordonne


    def operation_chaque_cote(self,operation, partie_litteral=""):

        expression_lit = el.Expression_litteral(partie_litteral).polynome_reduit_ordonne
        if operation=="-":
            expression_lit = inverser_dictionnaire(expression_lit)
        if operation=="+" or operation=="-":
            new_dico_left = additionner_deux_dictionnaires(self.dico_left, expression_lit)
            new_dico_right = additionner_deux_dictionnaires(self.dico_right, expression_lit)
            return from_dicos_to_new_equation(new_dico_left, new_dico_right)
        if operation == "*":
            new_dico_left = {key: value*float(partie_litteral) for (key, value) in self.dico_left.items()}
            new_dico_right = {key: value*float(partie_litteral) for (key, value) in self.dico_right.items()}
            return from_dicos_to_new_equation(new_dico_left, new_dico_right)
        if operation == "/":
            new_dico_left = {key: value/float(partie_litteral) for (key, value) in self.dico_left.items()}
            new_dico_right = {key: value/float(partie_litteral) for (key, value) in self.dico_right.items()}
            return from_dicos_to_new_equation(new_dico_left, new_dico_right)




    def degree_equation(self):
        try:
            first_key = next(iter(self.equal_zero))
            numbers = re.findall(r'\{(\d+)\}', first_key)
            return sum(int(num) for num in numbers)
        except StopIteration:
            return 0
        # Convertit les nombres en entiers et les somme


    def resoudre(self):
        if self.degre == 0:
            if '' in self.equal_zero:
                if self.equal_zero[''] != 0:
                    return "impossible"
                else:
                    return "reel"
            else:
                return 0
        if self.degre == 1:
            if '' in self.equal_zero:
                if self.equal_zero[''] == 0:
                    return 0
                else:
                    return -(self.equal_zero['']/self.equal_zero['x^{1}'])
            else:
                return 0
        if self.degre == 2:
            a = self.equal_zero['x^{2}']
            b = self.equal_zero['x^{1}']
            c = self.equal_zero['']

            discriminant = b**2-4*a*c
            if discriminant<0:
                return "impossible"
            elif discriminant>0:
                racine_dis = math.sqrt(discriminant)
                reponse_x1 = (-b+racine_dis)/(2*a)
                reponse_x2 = (-b-racine_dis)/(2*a)
                return (reponse_x1, reponse_x2)
            else:
                return -b/(2*a)



eq = Equation("3x+2","2(x+2)")
print(eq.resoudre())









