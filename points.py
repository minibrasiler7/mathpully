Evaluer_une_expression_littérale = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "evaluer_une_expression_litterale",
    "nom": "Evaluer une expression littérale",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ 3x^2+2x-15 $$</span><br><p>Si on évalue l'expression pour x=3 alors notre expression devient:</p><br><span>$$ 3\cdot 3^2+2 \cdot 3-15 = 18 $$</span><br>"
              "<p> Si on évalue l'expression pour x=-2 notre expression devient: </p> <span>$$ 3\cdot (-2)^2+2 \cdot (-2)-15 = 18 $$</span><br> <p class='attention'>Attention à bien mettre en parenthèse la valeur que prends x si celui-ci est un nombre négatif! </p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [
    {
    "question": "Evalue l'expression pour x=4 : <span>$$ 2x^2-3x-15 $$</span>",
    "answer": ["5"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=-3 : <span>$$ x^2+6x-20 $$</span>",
    "answer": ["-29"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=2 : <span>$$ -2x^2-3x+10 $$</span>",
    "answer": ["4"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=7 : <span>$$ 3x-4 $$</span>",
    "answer": ["17"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=3 : <span>$$ 2x+5 $$</span>",
    "answer": ["11"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=2 : <span>$$ x^3-4x^2+5x-6 $$</span>",
    "answer": ["0"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=5 : <span>$$ x^2-4x-7 $$</span>",
    "answer": ["3"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=6 : <span>$$ 3x+2 $$</span>",
    "answer": ["20"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=1 : <span>$$ x^2+x-5 $$</span>",
    "answer": ["-3"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=1 : <span>$$ 2x+5 $$</span>",
    "answer": ["7"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=3 : <span>$$ 4x-7 $$</span>",
    "answer": ["5"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=0 : <span>$$ 3x^2-2x+1 $$</span>",
    "answer": ["1"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    }

    ]
}

Réduction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "reduction_de_polynomes",
    "nom": "Réduction de polynômes",
    "body": "Réduire un polynôme signifie que l’on va mettre ensemble les monômes avec la même partie littérale. Avant de réduire un polynôme, il faut s’assurer que l’on a bien effectué toutes les opérations de puissances, racines, multiplications et divisions.<br> <strong>1ère étape </strong> <br> On sépare le polynôme en ses monômes. Dès que l’on voit un signe d’addition ou de soustraction on place une séparation avant ce dernier.<br><strong>2ème étape </strong> <br> On reconnaît les monômes qui ont la même partie littérale. On réorganise le polynôme afin de mettre ensemble les mônomes qui ont les mêmes parties littérales. <br><strong>3ème étape</strong> <br> On les additionne entre eux pour cela on fait la somme des coefficients et on réécrit la partie littérale sans la modifier",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [
    {'question': 'Réduis le polynôme suivant <span>$$ 10x^3 + 10x^3 + 8x^3 + 12x + 8x + 3x^3 + 12 + 11 + 4x^2 $$</span>',
     'answer': ['31x^3+4x^2+20x+23', '31x^3+4x^2+23+20x', '31x^3+20x+4x^2+23', '31x^3+20x+23+4x^2', '31x^3+23+4x^2+20x', '31x^3+23+20x+4x^2', '4x^2+31x^3+20x+23', '4x^2+31x^3+23+20x', '4x^2+20x+31x^3+23', '4x^2+20x+23+31x^3', '4x^2+23+31x^3+20x', '4x^2+23+20x+31x^3', '20x+31x^3+4x^2+23', '20x+31x^3+23+4x^2', '20x+4x^2+31x^3+23', '20x+4x^2+23+31x^3', '20x+23+31x^3+4x^2', '20x+23+4x^2+31x^3', '23+31x^3+4x^2+20x', '23+31x^3+20x+4x^2', '23+4x^2+31x^3+20x', '23+4x^2+20x+31x^3', '23+20x+31x^3+4x^2', '23+20x+4x^2+31x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x + 8x^3 + 2x + 1x^2 + 8x + 11x + 10 + 11 $$</span>',
     'answer': ['8x^3+1x^2+23x+21', '8x^3+1x^2+21+23x', '8x^3+23x+1x^2+21', '8x^3+23x+21+1x^2', '8x^3+21+1x^2+23x', '8x^3+21+23x+1x^2', '1x^2+8x^3+23x+21', '1x^2+8x^3+21+23x', '1x^2+23x+8x^3+21', '1x^2+23x+21+8x^3', '1x^2+21+8x^3+23x', '1x^2+21+23x+8x^3', '23x+8x^3+1x^2+21', '23x+8x^3+21+1x^2', '23x+1x^2+8x^3+21', '23x+1x^2+21+8x^3', '23x+21+8x^3+1x^2', '23x+21+1x^2+8x^3', '21+8x^3+1x^2+23x', '21+8x^3+23x+1x^2', '21+1x^2+8x^3+23x', '21+1x^2+23x+8x^3', '21+23x+8x^3+1x^2', '21+23x+1x^2+8x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 6x^3 - 10x - 11x^2 - 9x^3 - 6x^2 - 8x^3 - 7x - 7x - 12x^2 $$</span>',
     'answer': ['-11x^3-29x^2-24x', '-11x^3-24x-29x^2', '-29x^2-11x^3-24x', '-29x^2-24x-11x^3', '-24x-11x^3-29x^2', '-24x-29x^2-11x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 11x^2 - 7 - 2 - 6x - 2x^3 - 7x - 9x^3 $$</span>',
     'answer': ['-11x^3+11x^2-13x-9', '-11x^3+11x^2-9-13x', '-11x^3-13x+11x^2-9', '-11x^3-13x-9+11x^2', '-11x^3-9+11x^2-13x', '-11x^3-9-13x+11x^2', '11x^2-11x^3-13x-9', '11x^2-11x^3-9-13x', '11x^2-13x-11x^3-9', '11x^2-13x-9-11x^3', '11x^2-9-11x^3-13x', '11x^2-9-13x-11x^3', '-13x-11x^3+11x^2-9', '-13x-11x^3-9+11x^2', '-13x+11x^2-11x^3-9', '-13x+11x^2-9-11x^3', '-13x-9-11x^3+11x^2', '-13x-9+11x^2-11x^3', '-9-11x^3+11x^2-13x', '-9-11x^3-13x+11x^2', '-9+11x^2-11x^3-13x', '-9+11x^2-13x-11x^3', '-9-13x-11x^3+11x^2', '-9-13x+11x^2-11x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x^3 + 6 + 2x + 8x^2 + 6 + 8x^2 + 8 + 7 $$</span>',
     'answer': ['2x^3+16x^2+2x+27', '2x^3+16x^2+27+2x', '2x^3+2x+16x^2+27', '2x^3+2x+27+16x^2', '2x^3+27+16x^2+2x', '2x^3+27+2x+16x^2', '16x^2+2x^3+2x+27', '16x^2+2x^3+27+2x', '16x^2+2x+2x^3+27', '16x^2+2x+27+2x^3', '16x^2+27+2x^3+2x', '16x^2+27+2x+2x^3', '2x+2x^3+16x^2+27', '2x+2x^3+27+16x^2', '2x+16x^2+2x^3+27', '2x+16x^2+27+2x^3', '2x+27+2x^3+16x^2', '2x+27+16x^2+2x^3', '27+2x^3+16x^2+2x', '27+2x^3+2x+16x^2', '27+16x^2+2x^3+2x', '27+16x^2+2x+2x^3', '27+2x+2x^3+16x^2', '27+2x+16x^2+2x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 4x - 8x^3 - 10 - 9x^3 - 1x - 8x - 4x^3 $$</span>',
     'answer': ['-21x^3-5x-10', '-21x^3-10-5x', '-5x-21x^3-10', '-5x-10-21x^3', '-10-21x^3-5x', '-10-5x-21x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 10x - 3x^2 - 2x^2 - 11 - 2x^2 - 3x^2 - 6x - 12 - 5x^2 $$</span>',
     'answer': ['-15x^2+4x-23', '-15x^2-23+4x', '4x-15x^2-23', '4x-23-15x^2', '-23-15x^2+4x', '-23+4x-15x^2'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x^3 - 10x - 7 - 8x^2 - 12x^3 - 7x - 4x $$</span>',
     'answer': ['-10x^3-8x^2-21x-7', '-10x^3-8x^2-7-21x', '-10x^3-21x-8x^2-7', '-10x^3-21x-7-8x^2', '-10x^3-7-8x^2-21x', '-10x^3-7-21x-8x^2', '-8x^2-10x^3-21x-7', '-8x^2-10x^3-7-21x', '-8x^2-21x-10x^3-7', '-8x^2-21x-7-10x^3', '-8x^2-7-10x^3-21x', '-8x^2-7-21x-10x^3', '-21x-10x^3-8x^2-7', '-21x-10x^3-7-8x^2', '-21x-8x^2-10x^3-7', '-21x-8x^2-7-10x^3', '-21x-7-10x^3-8x^2', '-21x-7-8x^2-10x^3', '-7-10x^3-8x^2-21x', '-7-10x^3-21x-8x^2', '-7-8x^2-10x^3-21x', '-7-8x^2-21x-10x^3', '-7-21x-10x^3-8x^2', '-7-21x-8x^2-10x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 3x^3 + 8x^2 + 3x^2 + 8 + 1x^3 + 11x^2 + 7x^3 + 7x $$</span>',
     'answer': ['11x^3+22x^2+7x+8', '11x^3+22x^2+8+7x', '11x^3+7x+22x^2+8', '11x^3+7x+8+22x^2', '11x^3+8+22x^2+7x', '11x^3+8+7x+22x^2', '22x^2+11x^3+7x+8', '22x^2+11x^3+8+7x', '22x^2+7x+11x^3+8', '22x^2+7x+8+11x^3', '22x^2+8+11x^3+7x', '22x^2+8+7x+11x^3', '7x+11x^3+22x^2+8', '7x+11x^3+8+22x^2', '7x+22x^2+11x^3+8', '7x+22x^2+8+11x^3', '7x+8+11x^3+22x^2', '7x+8+22x^2+11x^3', '8+11x^3+22x^2+7x', '8+11x^3+7x+22x^2', '8+22x^2+11x^3+7x', '8+22x^2+7x+11x^3', '8+7x+11x^3+22x^2', '8+7x+22x^2+11x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 1 - 4x^3 - 10x - 5 - 4x^3 - 8x^2 - 9x^3 - 6x^2 - 1 $$</span>',
     'answer': ['-17x^3-14x^2-10x-5', '-17x^3-14x^2-5-10x', '-17x^3-10x-14x^2-5', '-17x^3-10x-5-14x^2', '-17x^3-5-14x^2-10x', '-17x^3-5-10x-14x^2', '-14x^2-17x^3-10x-5', '-14x^2-17x^3-5-10x', '-14x^2-10x-17x^3-5', '-14x^2-10x-5-17x^3', '-14x^2-5-17x^3-10x', '-14x^2-5-10x-17x^3', '-10x-17x^3-14x^2-5', '-10x-17x^3-5-14x^2', '-10x-14x^2-17x^3-5', '-10x-14x^2-5-17x^3', '-10x-5-17x^3-14x^2', '-10x-5-14x^2-17x^3', '-5-17x^3-14x^2-10x', '-5-17x^3-10x-14x^2', '-5-14x^2-17x^3-10x', '-5-14x^2-10x-17x^3', '-5-10x-17x^3-14x^2', '-5-10x-14x^2-17x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 11x - 2x - 8 - 4x - 10x - 10x - 3 - 6x^2 $$</span>',
     'answer': ['-6x^2-15x-11', '-6x^2-11-15x', '-15x-6x^2-11', '-15x-11-6x^2', '-11-6x^2-15x', '-11-15x-6x^2'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x^2 - 4x - 7x^2 - 1x - 8x - 3x^2 - 10 - 1x - 1x $$</span>',
     'answer': ['-8x^2-15x-10', '-8x^2-10-15x', '-15x-8x^2-10', '-15x-10-8x^2', '-10-8x^2-15x', '-10-15x-8x^2'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success'}]
}

Ordonner_un_polynôme = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Ordonner un polynôme",
    "body": "Ordonner un polynôme signifie que l’on va d’abord inscrire les polynômes avec les plus hauts degrés. Si deux monômes possèdent le même degré on va les inscrire par ordre alphabétique (x2 signifie xx). On doit toujours ordonner un polynôme après l’avoir réduit et pas avant!",
}

Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Distributivité",
    "body": "Lorsque l’on multiplie un polynôme par un monôme, on multiplie ce monôme avec chaque monôme du polynôme. <br> Lorsque l’on multiplie un polynôme par un polynôme on doit multiplier chaque monôme du premier polynôme avec chaque monôme du deuxième polynôme.",
}

Addition_et_soustraction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Addition et soustraction de polynômes",
    "body": "Lorsque l’on additionne deux polynômes on peut simplement enlever les parenthèses et ensuite réduire l’expression littérale obtenue. Lorsque l’on soustrait deux polynômes on doit inverser les signes de chaque monôme du polynôme qui suit le signe de soustraction. On enlève ensuite le signe de soustraction ainsi que les parenthèses.",
}

Identité_remarquables = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Identité remarquables",
    "body": "Une identité remarquable est une expression mathématique qui sert de base pour faire un calcul littéral. Les identités remarquables sont utiles notamment pour résoudre une équation. En mathématiques, ces expressions algébriques permettent de simplifier les calculs en tout genre. <br> Il existe 3 identités remarquables pour les polynômes de degré 2. Vous devez connaître par coeur ses formules! <br> En connaissant ces formules, vous pourrez rapidement effectuer certains calculs et trouver la solution d’équation du deuxième degré. Lorsqu’on passe de la formule de gauche à celle de droite, on dit que l’on développe le calcul. Si au contraire, on passe de la forme de droite à celle de gauche, on dit que l’on factorise.",
}

Factorisation = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Factorisation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Preuve_avec_le_calcul_littéral = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Preuve avec le calcul littéral",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Equation_équivalente = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation équivalente",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Réduction_avec_coefficients_rationnels = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Réduction avec coefficients rationnels",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Solution_d_une_équation_par_évaluation = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Solution d'une équation par évaluation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Résolution_d_équation_du_premier_degré_à_une_inconnue = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Résolution d'équation du premier degré à une inconnue",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Poser_une_équation = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Poser une équation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}

Solution_par_voie_graphique = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Solution par voie graphique",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}
Equation_avec_Fraction = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation avec Fraction",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}
Equation_du_deuxième_degré = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation du deuxième degré",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
}


