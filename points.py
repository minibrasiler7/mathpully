Evaluer_une_expression_littérale = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "evaluer_une_expression_litterale",
    "nom": "Evaluer une expression littérale",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ 3x^2+2x-15 $$</span><br>Si on évalue l'expression pour x=3 alors notre expression devient:<br><span>$$ 3\cdot 3^2+2 \cdot 3-15 = 18 $$</span><br>"
              " Si on évalue l'expression pour x=-2 notre expression devient: <br> <span>$$ 3\cdot (-2)^2+2 \cdot (-2)-15 = 18 $$</span><br> <p class='attention'>Attention à bien mettre en parenthèse la valeur que prends x si celui-ci est un nombre négatif! </p>",
    "message_aide":[],
    "questions": [
    {
    "question": "Evalue l'expression pour x=4 : <span>$$ 2x^2-3x-15 $$</span>",
    "answer": ["5"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=-3 : <span>$$ x^2+6x-20 $$</span>",
    "answer": ["-29"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=2 : <span>$$ -2x^2-3x+10 $$</span>",
    "answer": ["4"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=7 : <span>$$ 3x-4 $$</span>",
    "answer": ["17"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=3 : <span>$$ 2x+5 $$</span>",
    "answer": ["11"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=2 : <span>$$ x^3-4x^2+5x-6 $$</span>",
    "answer": ["0"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=5 : <span>$$ x^2-4x-7 $$</span>",
    "answer": ["3"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=6 : <span>$$ 3x+2 $$</span>",
    "answer": ["20"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=1 : <span>$$ x^2+x-5 $$</span>",
    "answer": ["-3"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=1 : <span>$$ 2x+5 $$</span>",
    "answer": ["7"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=3 : <span>$$ 4x-7 $$</span>",
    "answer": ["5"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    },
    {
    "question": "Evalue l'expression pour x=0 : <span>$$ 3x^2-2x+1 $$</span>",
    "answer": ["1"],
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success",
    "methods": ["enlever_espace"]
    }
    ]
}

Réduction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "reduction_de_polynomes",
    "nom": "Réduction de polynômes",
    "body": "Réduire un polynôme signifie que l’on va mettre ensemble les monômes avec la même partie littérale. Avant de réduire un polynôme, il faut s’assurer que l’on a bien effectué toutes les opérations de puissances, racines, multiplications et divisions.<br> <strong>1ère étape </strong> <br> On sépare le polynôme en ses monômes. Dès que l’on voit un signe d’addition ou de soustraction on place une séparation avant ce dernier.<br><strong>2ème étape </strong> <br> On reconnaît les monômes qui ont la même partie littérale. On réorganise le polynôme afin de mettre ensemble les mônomes qui ont les mêmes parties littérales. <br><strong>3ème étape</strong> <br> On les additionne entre eux pour cela on fait la somme des coefficients et on réécrit la partie littérale sans la modifier",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <br> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . <br> Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "message_aide":[],
    "questions": [
    {'question': 'Réduis le polynôme suivant <span>$$ 10x^3 + 10x^3 + 8x^3 + 12x + 8x + 3x^3 + 12 + 11 + 4x^2 $$</span>',
     'answer': ['31x^3+4x^2+20x+23', '31x^3+4x^2+23+20x', '31x^3+20x+4x^2+23', '31x^3+20x+23+4x^2', '31x^3+23+4x^2+20x', '31x^3+23+20x+4x^2', '4x^2+31x^3+20x+23', '4x^2+31x^3+23+20x', '4x^2+20x+31x^3+23', '4x^2+20x+23+31x^3', '4x^2+23+31x^3+20x', '4x^2+23+20x+31x^3', '20x+31x^3+4x^2+23', '20x+31x^3+23+4x^2', '20x+4x^2+31x^3+23', '20x+4x^2+23+31x^3', '20x+23+31x^3+4x^2', '20x+23+4x^2+31x^3', '23+31x^3+4x^2+20x', '23+31x^3+20x+4x^2', '23+4x^2+31x^3+20x', '23+4x^2+20x+31x^3', '23+20x+31x^3+4x^2', '23+20x+4x^2+31x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x + 8x^3 + 2x + 1x^2 + 8x + 11x + 10 + 11 $$</span>',
     'answer': ['8x^3+1x^2+23x+21', '8x^3+1x^2+21+23x', '8x^3+23x+1x^2+21', '8x^3+23x+21+1x^2', '8x^3+21+1x^2+23x', '8x^3+21+23x+1x^2', '1x^2+8x^3+23x+21', '1x^2+8x^3+21+23x', '1x^2+23x+8x^3+21', '1x^2+23x+21+8x^3', '1x^2+21+8x^3+23x', '1x^2+21+23x+8x^3', '23x+8x^3+1x^2+21', '23x+8x^3+21+1x^2', '23x+1x^2+8x^3+21', '23x+1x^2+21+8x^3', '23x+21+8x^3+1x^2', '23x+21+1x^2+8x^3', '21+8x^3+1x^2+23x', '21+8x^3+23x+1x^2', '21+1x^2+8x^3+23x', '21+1x^2+23x+8x^3', '21+23x+8x^3+1x^2', '21+23x+1x^2+8x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 6x^3 - 10x - 11x^2 - 9x^3 - 6x^2 - 8x^3 - 7x - 7x - 12x^2 $$</span>',
     'answer': ['-11x^3-29x^2-24x', '-11x^3-24x-29x^2', '-29x^2-11x^3-24x', '-29x^2-24x-11x^3', '-24x-11x^3-29x^2', '-24x-29x^2-11x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 11x^2 - 7 - 2 - 6x - 2x^3 - 7x - 9x^3 $$</span>',
     'answer': ['-11x^3+11x^2-13x-9', '-11x^3+11x^2-9-13x', '-11x^3-13x+11x^2-9', '-11x^3-13x-9+11x^2', '-11x^3-9+11x^2-13x', '-11x^3-9-13x+11x^2', '11x^2-11x^3-13x-9', '11x^2-11x^3-9-13x', '11x^2-13x-11x^3-9', '11x^2-13x-9-11x^3', '11x^2-9-11x^3-13x', '11x^2-9-13x-11x^3', '-13x-11x^3+11x^2-9', '-13x-11x^3-9+11x^2', '-13x+11x^2-11x^3-9', '-13x+11x^2-9-11x^3', '-13x-9-11x^3+11x^2', '-13x-9+11x^2-11x^3', '-9-11x^3+11x^2-13x', '-9-11x^3-13x+11x^2', '-9+11x^2-11x^3-13x', '-9+11x^2-13x-11x^3', '-9-13x-11x^3+11x^2', '-9-13x+11x^2-11x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x^3 + 6 + 2x + 8x^2 + 6 + 8x^2 + 8 + 7 $$</span>',
     'answer': ['2x^3+16x^2+2x+27', '2x^3+16x^2+27+2x', '2x^3+2x+16x^2+27', '2x^3+2x+27+16x^2', '2x^3+27+16x^2+2x', '2x^3+27+2x+16x^2', '16x^2+2x^3+2x+27', '16x^2+2x^3+27+2x', '16x^2+2x+2x^3+27', '16x^2+2x+27+2x^3', '16x^2+27+2x^3+2x', '16x^2+27+2x+2x^3', '2x+2x^3+16x^2+27', '2x+2x^3+27+16x^2', '2x+16x^2+2x^3+27', '2x+16x^2+27+2x^3', '2x+27+2x^3+16x^2', '2x+27+16x^2+2x^3', '27+2x^3+16x^2+2x', '27+2x^3+2x+16x^2', '27+16x^2+2x^3+2x', '27+16x^2+2x+2x^3', '27+2x+2x^3+16x^2', '27+2x+16x^2+2x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 4x - 8x^3 - 10 - 9x^3 - 1x - 8x - 4x^3 $$</span>',
     'answer': ['-21x^3-5x-10', '-21x^3-10-5x', '-5x-21x^3-10', '-5x-10-21x^3', '-10-21x^3-5x', '-10-5x-21x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 10x - 3x^2 - 2x^2 - 11 - 2x^2 - 3x^2 - 6x - 12 - 5x^2 $$</span>',
     'answer': ['-15x^2+4x-23', '-15x^2-23+4x', '4x-15x^2-23', '4x-23-15x^2', '-23-15x^2+4x', '-23+4x-15x^2'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x^3 - 10x - 7 - 8x^2 - 12x^3 - 7x - 4x $$</span>',
     'answer': ['-10x^3-8x^2-21x-7', '-10x^3-8x^2-7-21x', '-10x^3-21x-8x^2-7', '-10x^3-21x-7-8x^2', '-10x^3-7-8x^2-21x', '-10x^3-7-21x-8x^2', '-8x^2-10x^3-21x-7', '-8x^2-10x^3-7-21x', '-8x^2-21x-10x^3-7', '-8x^2-21x-7-10x^3', '-8x^2-7-10x^3-21x', '-8x^2-7-21x-10x^3', '-21x-10x^3-8x^2-7', '-21x-10x^3-7-8x^2', '-21x-8x^2-10x^3-7', '-21x-8x^2-7-10x^3', '-21x-7-10x^3-8x^2', '-21x-7-8x^2-10x^3', '-7-10x^3-8x^2-21x', '-7-10x^3-21x-8x^2', '-7-8x^2-10x^3-21x', '-7-8x^2-21x-10x^3', '-7-21x-10x^3-8x^2', '-7-21x-8x^2-10x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 3x^3 + 8x^2 + 3x^2 + 8 + 1x^3 + 11x^2 + 7x^3 + 7x $$</span>',
     'answer': ['11x^3+22x^2+7x+8', '11x^3+22x^2+8+7x', '11x^3+7x+22x^2+8', '11x^3+7x+8+22x^2', '11x^3+8+22x^2+7x', '11x^3+8+7x+22x^2', '22x^2+11x^3+7x+8', '22x^2+11x^3+8+7x', '22x^2+7x+11x^3+8', '22x^2+7x+8+11x^3', '22x^2+8+11x^3+7x', '22x^2+8+7x+11x^3', '7x+11x^3+22x^2+8', '7x+11x^3+8+22x^2', '7x+22x^2+11x^3+8', '7x+22x^2+8+11x^3', '7x+8+11x^3+22x^2', '7x+8+22x^2+11x^3', '8+11x^3+22x^2+7x', '8+11x^3+7x+22x^2', '8+22x^2+11x^3+7x', '8+22x^2+7x+11x^3', '8+7x+11x^3+22x^2', '8+7x+22x^2+11x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 1 - 4x^3 - 10x - 5 - 4x^3 - 8x^2 - 9x^3 - 6x^2 - 1 $$</span>',
     'answer': ['-17x^3-14x^2-10x-5', '-17x^3-14x^2-5-10x', '-17x^3-10x-14x^2-5', '-17x^3-10x-5-14x^2', '-17x^3-5-14x^2-10x', '-17x^3-5-10x-14x^2', '-14x^2-17x^3-10x-5', '-14x^2-17x^3-5-10x', '-14x^2-10x-17x^3-5', '-14x^2-10x-5-17x^3', '-14x^2-5-17x^3-10x', '-14x^2-5-10x-17x^3', '-10x-17x^3-14x^2-5', '-10x-17x^3-5-14x^2', '-10x-14x^2-17x^3-5', '-10x-14x^2-5-17x^3', '-10x-5-17x^3-14x^2', '-10x-5-14x^2-17x^3', '-5-17x^3-14x^2-10x', '-5-17x^3-10x-14x^2', '-5-14x^2-17x^3-10x', '-5-14x^2-10x-17x^3', '-5-10x-17x^3-14x^2', '-5-10x-14x^2-17x^3'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 11x - 2x - 8 - 4x - 10x - 10x - 3 - 6x^2 $$</span>',
     'answer': ['-6x^2-15x-11', '-6x^2-11-15x', '-15x-6x^2-11', '-15x-11-6x^2', '-11-6x^2-15x', '-11-15x-6x^2'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]},
    {'question': 'Réduis le polynôme suivant <span>$$ 2x^2 - 4x - 7x^2 - 1x - 8x - 3x^2 - 10 - 1x - 1x $$</span>',
     'answer': ['-8x^2-15x-10', '-8x^2-10-15x', '-15x-8x^2-10', '-15x-10-8x^2', '-10-8x^2-15x', '-10-15x-8x^2'],
     'feedback': "Bravo, c'est la bonne réponse !",
     'feedbackClass': 'text-success',
      "methods": ["enlever_espace"]}]
}

Ordonner_un_polynôme = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Ordonner un polynôme",
    "body": "Ordonner un polynôme signifie que l’on va d’abord inscrire les polynômes avec les plus hauts degrés. Si deux monômes possèdent le même degré on va les inscrire par ordre alphabétique (x2 signifie xx). On doit toujours ordonner un polynôme après l’avoir réduit et pas avant!",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <br> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . <br> Notre expression devient alors:  $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br>  On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <br> On trouve finalement:  $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [{
	'question': 'Ordonne le polynôme suivant: <span>$$ 4x+9x^{2}y+2x^{2}+7y^{2}z+2y+6+4y^{3} $$</span>',
	'answer': '9x^{2}y+4y^{3}+7y^{2}z+2x^{2}+4x+2y+6',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 2xy^{2}+4y^{3}+4x+6xy+8xz^{2}+7z^{3} $$</span>',
	'answer': '2xy^{2}+8xz^{2}+4y^{3}+7z^{3}+6xy+4x',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 4yz^{2}+8y^{2}+6y^{2}z+4x^{2}+7xyz+2x^{3} $$</span>',
	'answer': '2x^{3}+7xyz+6y^{2}z+4yz^{2}+4x^{2}+8y^{2}',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 7+4xyz+8y^{3}+7x+8x^{2}+7y^{2}z $$</span>',
	'answer': '4xyz+8y^{3}+7y^{2}z+8x^{2}+7x+7',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 2xz^{2}+7x+2yz^{2}+3x^{3}+9y^{2}+8y^{2}z $$</span>',
	'answer': '3x^{3}+2xz^{2}+8y^{2}z+2yz^{2}+9y^{2}+7x',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 9x^{2}+4y^{2}z+7z^{3}+6xyz+3xy^{2}+4 $$</span>',
	'answer': '3xy^{2}+6xyz+4y^{2}z+7z^{3}+9x^{2}+4',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 5y+7yz^{2}+8xyz+3x^{2}y+3z^{3}+9y^{2}+8x^{3} $$</span>',
	'answer': '8x^{3}+3x^{2}y+8xyz+7yz^{2}+3z^{3}+9y^{2}+5y',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 4y+2xy^{2}+5xy+8x^{3}+6y^{2}+3xz^{2}+4y^{2}z $$</span>',
	'answer': '8x^{3}+2xy^{2}+3xz^{2}+4y^{2}z+5xy+6y^{2}+4y',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 7y^{3}+5y+7xyz+3xy+5+5z^{3}+6x $$</span>',
	'answer': '7xyz+7y^{3}+5z^{3}+3xy+6x+5y+5',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 9y+6xyz+3x+9xy+2z^{3}+9x^{2}+7y^{2} $$</span>',
	'answer': '6xyz+2z^{3}+9x^{2}+9xy+7y^{2}+3x+9y',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 8+9xy^{2}+9xyz+5z^{3}+6x^{2}+7y^{2}z+7xy $$</span>',
	'answer': '9xy^{2}+9xyz+7y^{2}z+5z^{3}+6x^{2}+7xy+8',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': 'Ordonne le polynôme suivant: <span>$$ 3y^{2}+2xy+8z^{3}+7y^{3}+2xy^{2}+8+3y^{2}z $$</span>',
	'answer': '2xy^{2}+7y^{3}+3y^{2}z+8z^{3}+2xy+3y^{2}+8',
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}]
}

Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Distributivité",
    "body": "La distributivité s'utilise lorsqu'on a un terme qui multiplie une parenthèse. C'est une propriété mathématique qui dit que le produit d'une somme est égale à la somme des produits. En d'autres termes, on doit multiplier chaque monôme qu'il y a dans la parenthèse par le terme qui se trouve devant. <br> Imagine que tu as deux amis, et tu veux leur donner des cadeaux. Disons que tu veux donner 3 chocolats à chacun de tes amis et que tu as aussi 4 bonbons pour chacun d'eux. Au lieu de compter séparément combien de cadeaux tu as pour chaque ami, tu peux additionner les chocolats et les bonbons et ensuite multiplier le total par le nombre d'amis. <br> Voici l'exemple concret : tu as 2 amis, et tu veux leur donner 3 chocolats et 4 bonbons chacun. Pour savoir combien de cadeaux tu dois préparer en tout, tu peux utiliser la distributivité : <br>\( 2 \\text{ amis} \\times (3 \\text{ chocolats} + 4 \\text{ bonbons}) \) <br> En appliquant la propriété distributive, tu vas multiplier le nombre d'amis par le nombre de chocolats, puis par le nombre de bonbons : <br>$$ (2 \\text{ amis} \\times 3 \\text{ chocolats}) + (2 \\text{ amis} \\times 4 \\text{ bonbons}) $$ <br> Ce qui donne :<br> \( (6 \\text{ chocolats}) + (8 \\text{ bonbons}) \) <br>Ainsi, tu auras un total de 14 cadeaux à préparer pour tes amis.<br> La distributivité est donc une méthode pour répartir, ou distribuer, une multiplication sur une addition ou une soustraction.",
    "exemple":"<img src='static/images/distributivité.png' alt='Distributivité' width='300' height='120'>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [{
	'question': "Distribue l'expression littérale suivante: <span>$$ -1z(-2y+3z+2) $$</span>",
	'answer': ['-3z^{2}-2z+2yz', '2yz-3z^{2}-2z', '-3z^{2}+2yz-2z', '-2z-3z^{2}+2yz', '-2z+2yz-3z^{2}', '2yz-2z-3z^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ 7x(3y-1x) $$</span>",
	'answer': ['21xy-7x^{2}', '-7x^{2}+21xy'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ 3(-4x+2y+2z) $$</span>",
	'answer': ['6z-12x+6y+', '-12x+6y+6z+', '6y-12x+6z+', '-12x++6z+6y', '6z++6y-12x', '6z-12x++6y', '6y-12x++6z', '+6y-12x+6z', '-12x+6z++6y', '6z+6y-12x+', '6y+6z+-12x', '6y++6z-12x', '6z+-12x+6y', '6z+6y+-12x', '-12x+6z+6y+', '+6z+6y-12x', '6y+6z-12x+', '-12x+6z+6y', '-12x+6y+6z', '-12x++6y+6z', '+6z-12x+6y', '6y+-12x+6z', '-12x+6y++6z', '+6y+6z-12x'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ -6y(7z-4) $$</span>",
	'answer': ['24y+-42yz', '-42yz+24y+', '-42yz++24y', '+24y-42yz', '-42yz+24y', '24y-42yz+'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ -3y(-3y-2x+4z) $$</span>",
	'answer': ['6xy-12yz+9y^{2}', '-12yz+9y^{2}+6xy', '6xy+9y^{2}-12yz', '-12yz+6xy+9y^{2}', '9y^{2}+6xy-12yz', '9y^{2}-12yz+6xy'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ -8x(-7z+6-1x) $$</span>",
	'answer': ['8x^{2}-48x+56xz', '56xz-48x+8x^{2}', '56xz+8x^{2}-48x', '-48x+56xz+8x^{2}', '8x^{2}+56xz-48x', '-48x+8x^{2}+56xz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ -7z(-8y+7z) $$</span>",
	'answer': ['-49z^{2}+56yz', '56yz-49z^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ 1z(5+5z) $$</span>",
	'answer': ['5z^{2}+5z', '5z+5z^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ 5x(2y-4+7z) $$</span>",
	'answer': ['10xy+35xz-20x', '35xz+10xy-20x', '10xy-20x+35xz', '-20x+35xz+10xy', '35xz-20x+10xy', '-20x+10xy+35xz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ 1(8y+6x) $$</span>",
	'answer': ['8y+6x', '6x+8y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ -8(-7y-4-5x) $$</span>",
	'answer': ['56y+32+40x', '32+56y+40x', '32+40x+56y', '40x+56y+32', '40x+32+56y', '56y+40x+32'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Distribue l'expression littérale suivante: <span>$$ 1z(4y-6x) $$</span>",
	'answer': ['-6xz+4yz', '4yz-6xz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}]
}

Double_Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Double Distributivité",
    "body": "Imaginons que tu as deux expressions algébriques entre parenthèses et que tu dois les multiplier ensemble. Par exemple, prenons les expressions suivantes: \( (a + b) \) et \( (c + d) \). La double distributivité consiste à distribuer chaque terme de la première parenthèse avec chaque terme de la seconde parenthèse, et ensuite à additionner les résultats obtenus. <br>Dans notre exemple, voici comment on procède:<ol><li>Multiplie a par c: \( a * c = ac \)</li><li>Multiplie a par d: \( a * d = ad \)</li><li>Multiplie b par c: \( b * c = bc \)</li><li>Multiplie b par d: \( b * d = bd \)</li></ol><br>Maintenant, additionne les résultats obtenus:<br>\[ (ac) + (ad) + (bc) + (bd) \]<br>Donc, la double distributivité de \( (a + b)(c + d) \) est:<br> \[ (a + b)(c + d) = ac + ad + bc + bd \] <br> La double distributivité s'applique aussi bien pour les expressions avec des soustractions. Par exemple, si on a \( (a - b)(c - d) \), on obtient:<br>\[ (a - b)(c - d) = ac - ad - bc + bd \]<br>Ainsi lorsque tu fais une double distribution tu multiplies chaque terme de la première parenthèse avec chaque terme de la deuxième parenthèse et tu additionnes ou soustrais les différents produits obtenus.",
    "exemple":"<img src='static/images/double-distributivité.png' alt='Double Distributivité' width='450' height='180'>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [{
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (-7x-5z)(2y+3z) $$</span>",
	'answer': ['-21xz-14xy-10yz-15z^{2}+', '-14xy+-15z^{2}-10yz-21xz', '-21xz-15z^{2}-14xy-10yz', '-10yz-14xy-21xz-15z^{2}', '-10yz-14xy+-21xz-15z^{2}', '-14xy-21xz-10yz-15z^{2}+', '-10yz-14xy-21xz-15z^{2}+', '-21xz-14xy-15z^{2}-10yz+', '-14xy+-21xz-10yz-15z^{2}', '-15z^{2}-10yz-14xy-21xz', '-14xy+-15z^{2}-21xz-10yz', '-21xz-10yz-14xy+-15z^{2}', '-10yz-14xy+-15z^{2}-21xz', '-15z^{2}-21xz-10yz+-14xy', '-10yz-15z^{2}+-14xy-21xz', '-15z^{2}-21xz+-10yz-14xy', '-14xy-10yz-21xz-15z^{2}+', '-21xz-14xy-15z^{2}+-10yz', '-14xy-21xz-15z^{2}-10yz', '-14xy-15z^{2}-10yz-21xz', '-15z^{2}+-21xz-10yz-14xy', '-14xy-15z^{2}-21xz+-10yz', '-15z^{2}-21xz-14xy-10yz+', '-10yz-15z^{2}-14xy-21xz', '-14xy-21xz-15z^{2}-10yz+', '-21xz-10yz-14xy-15z^{2}+', '-14xy-21xz+-15z^{2}-10yz', '-14xy-10yz+-21xz-15z^{2}', '-15z^{2}-14xy+-21xz-10yz', '-15z^{2}+-10yz-21xz-14xy', '-14xy-10yz-21xz-15z^{2}', '-10yz+-15z^{2}-14xy-21xz', '-10yz-15z^{2}-21xz+-14xy', '-21xz+-10yz-14xy-15z^{2}', '-15z^{2}-10yz-14xy-21xz+', '-14xy-10yz+-15z^{2}-21xz', '-14xy-10yz-15z^{2}-21xz+', '-21xz-15z^{2}-10yz-14xy', '-10yz-21xz-15z^{2}-14xy', '-15z^{2}-14xy-21xz+-10yz', '-15z^{2}-10yz+-21xz-14xy', '-14xy-15z^{2}+-21xz-10yz', '-10yz-21xz-14xy-15z^{2}', '-21xz-15z^{2}-14xy+-10yz', '-10yz-14xy-15z^{2}-21xz+', '-14xy+-21xz-15z^{2}-10yz', '-14xy-21xz+-10yz-15z^{2}', '-21xz-14xy-15z^{2}-10yz', '-15z^{2}+-14xy-21xz-10yz', '-15z^{2}-14xy-10yz+-21xz', '-10yz-21xz-14xy-15z^{2}+', '-15z^{2}-10yz-21xz+-14xy', '-10yz-14xy-21xz+-15z^{2}', '-14xy+-10yz-15z^{2}-21xz', '-14xy+-10yz-21xz-15z^{2}', '-21xz+-10yz-15z^{2}-14xy', '-14xy-15z^{2}-10yz+-21xz', '-21xz-10yz-15z^{2}-14xy+', '-10yz-15z^{2}-21xz-14xy', '-21xz-10yz+-15z^{2}-14xy', '-10yz-21xz+-14xy-15z^{2}', '-14xy-21xz-10yz-15z^{2}', '-15z^{2}-14xy-21xz-10yz+', '-21xz-15z^{2}-14xy-10yz+', '-21xz-14xy-10yz+-15z^{2}', '-21xz+-14xy-15z^{2}-10yz', '-21xz+-15z^{2}-14xy-10yz', '-15z^{2}+-10yz-14xy-21xz', '-14xy-15z^{2}+-10yz-21xz', '-21xz-14xy-10yz-15z^{2}', '-14xy-21xz-15z^{2}+-10yz', '-15z^{2}+-14xy-10yz-21xz', '-15z^{2}-21xz+-14xy-10yz', '-15z^{2}-10yz-21xz-14xy', '-14xy-10yz-15z^{2}+-21xz', '-10yz-15z^{2}-21xz-14xy+', '-21xz-10yz-14xy-15z^{2}', '-14xy-10yz-15z^{2}-21xz', '-15z^{2}-21xz-10yz-14xy', '-21xz-15z^{2}-10yz-14xy+', '-15z^{2}-21xz-14xy-10yz', '-21xz-15z^{2}-10yz+-14xy', '-15z^{2}+-21xz-14xy-10yz', '-14xy-15z^{2}-10yz-21xz+', '-15z^{2}-14xy-10yz-21xz+', '-10yz-21xz-14xy+-15z^{2}', '-10yz-15z^{2}+-21xz-14xy', '-10yz-14xy-15z^{2}+-21xz', '-10yz+-14xy-15z^{2}-21xz', '-10yz-21xz-15z^{2}+-14xy', '-15z^{2}-10yz+-14xy-21xz', '-21xz+-14xy-10yz-15z^{2}', '-14xy-15z^{2}-21xz-10yz+', '-21xz-15z^{2}+-14xy-10yz', '-14xy-10yz-21xz+-15z^{2}', '-10yz+-14xy-21xz-15z^{2}', '-10yz-14xy-15z^{2}-21xz', '-10yz-21xz+-15z^{2}-14xy', '-15z^{2}-21xz-14xy+-10yz', '-21xz-15z^{2}+-10yz-14xy', '-21xz-14xy+-15z^{2}-10yz', '-15z^{2}-14xy-10yz-21xz', '-15z^{2}-10yz-21xz-14xy+', '-10yz-21xz-15z^{2}-14xy+', '-21xz-10yz-15z^{2}-14xy', '-10yz+-15z^{2}-21xz-14xy', '-10yz-15z^{2}-14xy-21xz+', '-10yz-15z^{2}-14xy+-21xz', '-14xy-21xz-10yz+-15z^{2}', '-14xy-15z^{2}-21xz-10yz', '-15z^{2}-14xy+-10yz-21xz', '-21xz-10yz-15z^{2}+-14xy', '-21xz-14xy+-10yz-15z^{2}', '-10yz+-21xz-15z^{2}-14xy', '-15z^{2}-21xz-10yz-14xy+', '-15z^{2}-14xy-21xz-10yz', '-10yz+-21xz-14xy-15z^{2}', '-15z^{2}-10yz-14xy+-21xz', '-21xz-10yz+-14xy-15z^{2}', '-21xz+-15z^{2}-10yz-14xy'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (4-8z)(-8x-7y) $$</span>",
	'answer': ['-32x+64xz++56yz-28y', '-32x+64xz+56yz-28y+', '64xz-32x+-28y+56yz', '-28y+64xz+56yz-32x+', '-28y+64xz+56yz-32x', '-28y+-32x+56yz+64xz', '-28y+56yz++64xz-32x', '-28y++56yz-32x+64xz', '-28y-32x++64xz+56yz', '56yz-32x+64xz-28y+', '-32x-28y+56yz++64xz', '+64xz+56yz-32x-28y', '56yz+64xz-32x-28y+', '-28y-32x+64xz++56yz', '56yz-32x+-28y+64xz', '+56yz-32x-28y+64xz', '56yz+64xz-28y-32x+', '-28y+-32x+64xz+56yz', '-32x+56yz-28y+64xz+', '64xz+56yz+-28y-32x', '64xz-28y+56yz+-32x', '56yz-32x-28y++64xz', '64xz+-32x+56yz-28y', '-28y+56yz-32x++64xz', '56yz-32x+64xz+-28y', '+64xz-28y-32x+56yz', '-28y+56yz-32x+64xz', '64xz-28y+56yz-32x+', '56yz+64xz-28y+-32x', '56yz+64xz+-32x-28y', '-28y+64xz-32x++56yz', '56yz+-32x+64xz-28y', '-32x+64xz-28y++56yz', '64xz-32x+56yz+-28y', '-32x+64xz-28y+56yz+', '56yz++64xz-28y-32x', '64xz-32x++56yz-28y', '-32x-28y+64xz+56yz', '64xz+-28y-32x+56yz', '-32x-28y+56yz+64xz', '64xz+-32x-28y+56yz', '56yz+64xz-32x+-28y', '56yz++64xz-32x-28y', '-28y++56yz+64xz-32x', '56yz+-32x-28y+64xz', '-32x+56yz+64xz+-28y', '56yz-32x-28y+64xz+', '-28y+64xz-32x+56yz', '-32x-28y+64xz++56yz', '-32x+64xz+56yz+-28y', '64xz-28y++56yz-32x', '-32x++64xz+56yz-28y', '56yz+-28y-32x+64xz', '-32x-28y++64xz+56yz', '64xz+-28y+56yz-32x', '56yz+-28y+64xz-32x', '-32x-28y+56yz+64xz+', '-28y-32x+56yz+64xz', '56yz-32x++64xz-28y', '56yz-28y+64xz+-32x', '64xz+56yz-28y-32x+', '-32x+-28y+56yz+64xz', '+64xz-28y+56yz-32x', '-32x+64xz-28y+56yz', '-32x+64xz+56yz-28y', '-32x++64xz-28y+56yz', '-28y+56yz+64xz-32x', '56yz-28y-32x++64xz', '+56yz-28y-32x+64xz', '-32x-28y+64xz+56yz+', '-28y-32x+56yz++64xz', '-32x++56yz-28y+64xz', '-28y+64xz+-32x+56yz', '-28y+56yz+64xz-32x+', '56yz-28y+64xz-32x+', '+56yz-28y+64xz-32x', '-28y-32x+56yz+64xz+', '-28y-32x+64xz+56yz+', '64xz++56yz-28y-32x', '-28y++64xz+56yz-32x', '+56yz-32x+64xz-28y', '56yz-28y++64xz-32x', '-28y++64xz-32x+56yz', '-32x+56yz-28y++64xz', '+64xz-32x+56yz-28y', '56yz+64xz+-28y-32x', '-28y+64xz-32x+56yz+', '-28y-32x++56yz+64xz', '56yz-28y+-32x+64xz', '+56yz+64xz-32x-28y', '+64xz-32x-28y+56yz', '+64xz+56yz-28y-32x', '+56yz+64xz-28y-32x', '64xz-32x+56yz-28y+', '-28y+56yz+64xz+-32x', '-32x+56yz-28y+64xz', '-32x+-28y+64xz+56yz', '-32x++56yz+64xz-28y', '-28y+56yz+-32x+64xz', '64xz-32x-28y++56yz', '64xz-28y-32x++56yz', '-32x+56yz+64xz-28y', '64xz+56yz-28y+-32x', '64xz-32x-28y+56yz+', '64xz-28y-32x+56yz+', '64xz++56yz-32x-28y', '-28y+56yz-32x+64xz+', '64xz+56yz-32x+-28y', '56yz-28y-32x+64xz+', '64xz+56yz+-32x-28y', '-28y-32x+64xz+56yz', '-32x+56yz+-28y+64xz', '-28y+64xz++56yz-32x', '64xz-28y+-32x+56yz', '-32x+64xz+-28y+56yz', '-28y+64xz+56yz+-32x', '-32x+56yz+64xz-28y+', '64xz+56yz-32x-28y+', '-32x+56yz++64xz-28y', '-32x-28y++56yz+64xz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (-4y-4)(-7x+7z) $$</span>",
	'answer': ['-28z-28yz+28xy+28x', '28xy-28yz+28x-28z', '28xy-28z-28yz+28x', '-28yz+28x-28z+28xy', '-28yz-28z+28xy+28x', '-28yz-28z+28x+28xy', '28x+28xy-28z-28yz', '-28z-28yz+28x+28xy', '28x-28z-28yz+28xy', '28xy-28z+28x-28yz', '-28yz+28xy-28z+28x', '-28yz+28xy+28x-28z', '28x-28yz+28xy-28z', '28x-28z+28xy-28yz', '28xy+28x-28z-28yz', '-28yz+28x+28xy-28z', '28x+28xy-28yz-28z', '28x-28yz-28z+28xy', '-28z+28x+28xy-28yz', '-28z+28x-28yz+28xy', '28xy+28x-28yz-28z', '-28z+28xy-28yz+28x', '-28z+28xy+28x-28yz', '28xy-28yz-28z+28x'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (8y+1z)(-7y-3z) $$</span>",
	'answer': ['-3z^{2}-7yz-24yz+-56y^{2}', '-24yz+-56y^{2}-3z^{2}-7yz', '-56y^{2}-7yz-3z^{2}-24yz+', '-56y^{2}-3z^{2}-7yz-24yz+', '-56y^{2}-24yz+-7yz-3z^{2}', '-3z^{2}-7yz-24yz-56y^{2}', '-3z^{2}-24yz-56y^{2}-7yz', '-3z^{2}-7yz-24yz-56y^{2}+', '-56y^{2}-3z^{2}+-7yz-24yz', '-7yz-24yz+-56y^{2}-3z^{2}', '-3z^{2}-24yz-7yz-56y^{2}', '-56y^{2}+-24yz-3z^{2}-7yz', '-7yz-3z^{2}-56y^{2}+-24yz', '-7yz-56y^{2}-24yz-3z^{2}', '-56y^{2}-7yz-24yz+-3z^{2}', '-7yz-56y^{2}+-24yz-3z^{2}', '-24yz-7yz-56y^{2}-3z^{2}+', '-24yz-3z^{2}+-56y^{2}-7yz', '-3z^{2}+-24yz-56y^{2}-7yz', '-3z^{2}-56y^{2}-24yz+-7yz', '-56y^{2}-24yz+-3z^{2}-7yz', '-24yz-56y^{2}-3z^{2}-7yz+', '-24yz-56y^{2}-7yz+-3z^{2}', '-7yz-3z^{2}-56y^{2}-24yz+', '-3z^{2}-56y^{2}+-7yz-24yz', '-3z^{2}-56y^{2}-24yz-7yz', '-24yz-7yz-3z^{2}-56y^{2}', '-24yz+-56y^{2}-7yz-3z^{2}', '-24yz-56y^{2}+-7yz-3z^{2}', '-7yz-56y^{2}-3z^{2}+-24yz', '-3z^{2}+-56y^{2}-24yz-7yz', '-24yz-56y^{2}-3z^{2}-7yz', '-7yz-24yz-3z^{2}-56y^{2}', '-24yz-56y^{2}-7yz-3z^{2}', '-24yz-7yz+-56y^{2}-3z^{2}', '-56y^{2}-24yz-7yz-3z^{2}+', '-7yz+-56y^{2}-3z^{2}-24yz', '-24yz-3z^{2}-7yz-56y^{2}+', '-7yz-3z^{2}-24yz-56y^{2}+', '-7yz+-3z^{2}-56y^{2}-24yz', '-56y^{2}-24yz-3z^{2}+-7yz', '-56y^{2}-24yz-7yz-3z^{2}', '-3z^{2}-56y^{2}-7yz-24yz', '-56y^{2}+-7yz-24yz-3z^{2}', '-24yz-56y^{2}+-3z^{2}-7yz', '-56y^{2}-7yz-24yz-3z^{2}+', '-3z^{2}+-24yz-7yz-56y^{2}', '-3z^{2}-56y^{2}+-24yz-7yz', '-24yz+-7yz-56y^{2}-3z^{2}', '-7yz-3z^{2}-24yz+-56y^{2}', '-3z^{2}-56y^{2}-7yz-24yz+', '-3z^{2}+-7yz-56y^{2}-24yz', '-7yz-24yz-56y^{2}-3z^{2}', '-56y^{2}-3z^{2}-7yz-24yz', '-56y^{2}-3z^{2}+-24yz-7yz', '-56y^{2}-7yz-3z^{2}+-24yz', '-56y^{2}-7yz-24yz-3z^{2}', '-3z^{2}-24yz-56y^{2}+-7yz', '-7yz-3z^{2}-24yz-56y^{2}', '-7yz+-24yz-56y^{2}-3z^{2}', '-24yz-7yz+-3z^{2}-56y^{2}', '-56y^{2}-24yz-3z^{2}-7yz+', '-7yz-3z^{2}-56y^{2}-24yz', '-7yz-56y^{2}-3z^{2}-24yz+', '-56y^{2}-3z^{2}-24yz-7yz', '-56y^{2}-24yz-3z^{2}-7yz', '-7yz-24yz-56y^{2}-3z^{2}+', '-56y^{2}-7yz-3z^{2}-24yz', '-24yz-3z^{2}-7yz+-56y^{2}', '-3z^{2}-24yz-7yz-56y^{2}+', '-24yz+-3z^{2}-56y^{2}-7yz', '-56y^{2}-7yz+-24yz-3z^{2}', '-7yz-56y^{2}-24yz+-3z^{2}', '-56y^{2}-3z^{2}-7yz+-24yz', '-3z^{2}+-7yz-24yz-56y^{2}', '-7yz-56y^{2}+-3z^{2}-24yz', '-56y^{2}+-3z^{2}-7yz-24yz', '-7yz-24yz+-3z^{2}-56y^{2}', '-7yz+-56y^{2}-24yz-3z^{2}', '-3z^{2}-56y^{2}-7yz+-24yz', '-3z^{2}-56y^{2}-24yz-7yz+', '-56y^{2}-3z^{2}-24yz+-7yz', '-7yz-56y^{2}-24yz-3z^{2}+', '-3z^{2}-7yz+-24yz-56y^{2}', '-3z^{2}+-56y^{2}-7yz-24yz', '-3z^{2}-7yz-56y^{2}-24yz', '-7yz-24yz-3z^{2}+-56y^{2}', '-7yz-56y^{2}-3z^{2}-24yz', '-24yz+-3z^{2}-7yz-56y^{2}', '-3z^{2}-7yz-56y^{2}+-24yz', '-24yz-7yz-3z^{2}-56y^{2}+', '-56y^{2}-3z^{2}-24yz-7yz+', '-24yz-56y^{2}-7yz-3z^{2}+', '-24yz+-7yz-3z^{2}-56y^{2}', '-3z^{2}-24yz-7yz+-56y^{2}', '-24yz-7yz-56y^{2}+-3z^{2}', '-56y^{2}-7yz+-3z^{2}-24yz', '-24yz-3z^{2}-56y^{2}-7yz+', '-24yz-3z^{2}-56y^{2}+-7yz', '-7yz-24yz-56y^{2}+-3z^{2}', '-3z^{2}-24yz+-56y^{2}-7yz', '-3z^{2}-7yz-56y^{2}-24yz+', '-7yz-24yz-3z^{2}-56y^{2}+', '-56y^{2}+-3z^{2}-24yz-7yz', '-3z^{2}-24yz+-7yz-56y^{2}', '-24yz-3z^{2}-56y^{2}-7yz', '-24yz-56y^{2}-3z^{2}+-7yz', '-24yz-3z^{2}-7yz-56y^{2}', '-24yz-7yz-3z^{2}+-56y^{2}', '-7yz-3z^{2}+-56y^{2}-24yz', '-7yz+-24yz-3z^{2}-56y^{2}', '-56y^{2}+-24yz-7yz-3z^{2}', '-7yz-3z^{2}+-24yz-56y^{2}', '-56y^{2}+-7yz-3z^{2}-24yz', '-24yz-3z^{2}+-7yz-56y^{2}', '-24yz-7yz-56y^{2}-3z^{2}', '-56y^{2}-24yz-7yz+-3z^{2}', '-3z^{2}-24yz-56y^{2}-7yz+', '-3z^{2}-7yz+-56y^{2}-24yz', '-7yz+-3z^{2}-24yz-56y^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (4y+5x)(-2x+7) $$</span>",
	'answer': ['-10x^{2}+35x+28y-8xy', '-8xy+28y-10x^{2}++35x', '28y-8xy+-10x^{2}+35x', '-10x^{2}+28y-8xy+35x', '-8xy+35x++28y-10x^{2}', '28y-8xy+35x-10x^{2}+', '28y+-8xy+35x-10x^{2}', '+35x-8xy+28y-10x^{2}', '-10x^{2}-8xy+28y+35x+', '-10x^{2}+-8xy+35x+28y', '35x+28y-8xy-10x^{2}+', '28y++35x-10x^{2}-8xy', '+28y-8xy-10x^{2}+35x', '-8xy+28y+-10x^{2}+35x', '-8xy-10x^{2}+35x++28y', '35x+28y-10x^{2}-8xy+', '35x++28y-8xy-10x^{2}', '-10x^{2}++35x+28y-8xy', '-10x^{2}+-8xy+28y+35x', '-10x^{2}+35x+-8xy+28y', '28y-10x^{2}-8xy++35x', '-8xy+35x-10x^{2}++28y', '28y-10x^{2}++35x-8xy', '35x-8xy+28y+-10x^{2}', '35x-8xy+-10x^{2}+28y', '35x+-10x^{2}+28y-8xy', '-8xy+-10x^{2}+28y+35x', '28y-10x^{2}-8xy+35x+', '-8xy-10x^{2}+28y+35x', '35x-10x^{2}+28y-8xy+', '35x-8xy++28y-10x^{2}', '28y-8xy-10x^{2}++35x', '-8xy+35x-10x^{2}+28y+', '-8xy+28y+35x+-10x^{2}', '28y+35x+-8xy-10x^{2}', '+28y+35x-8xy-10x^{2}', '-8xy-10x^{2}+35x+28y+', '-8xy+35x+28y-10x^{2}+', '-8xy+28y-10x^{2}+35x', '-10x^{2}+35x-8xy++28y', '-10x^{2}+35x+28y-8xy+', '-10x^{2}+28y++35x-8xy', '35x+28y+-8xy-10x^{2}', '+35x+28y-10x^{2}-8xy', '-8xy+28y+35x-10x^{2}', '-10x^{2}+28y-8xy+35x+', '28y-8xy+35x+-10x^{2}', '28y+35x-8xy+-10x^{2}', '35x-8xy-10x^{2}+28y+', '28y++35x-8xy-10x^{2}', '+35x-10x^{2}+28y-8xy', '-8xy+35x+28y-10x^{2}', '-10x^{2}-8xy+35x+28y+', '-8xy-10x^{2}+28y+35x+', '-8xy++28y-10x^{2}+35x', '-8xy++28y+35x-10x^{2}', '-8xy+35x+28y+-10x^{2}', '-10x^{2}+35x+28y+-8xy', '28y+35x-8xy-10x^{2}+', '35x+28y-8xy+-10x^{2}', '35x+28y-10x^{2}+-8xy', '-8xy+28y-10x^{2}+35x+', '+35x+28y-8xy-10x^{2}', '28y+-10x^{2}-8xy+35x', '-8xy+35x-10x^{2}+28y', '-10x^{2}+28y+35x+-8xy', '-8xy+28y+35x-10x^{2}+', '35x-8xy+28y-10x^{2}+', '35x-10x^{2}-8xy++28y', '28y-8xy++35x-10x^{2}', '-10x^{2}+28y+35x-8xy+', '-10x^{2}+35x-8xy+28y', '35x++28y-10x^{2}-8xy', '-10x^{2}-8xy++35x+28y', '35x-8xy-10x^{2}++28y', '-10x^{2}++28y+35x-8xy', '35x+-8xy-10x^{2}+28y', '+28y-10x^{2}-8xy+35x', '28y+35x-10x^{2}-8xy+', '35x+28y+-10x^{2}-8xy', '-8xy+28y++35x-10x^{2}', '35x+-10x^{2}-8xy+28y', '28y-10x^{2}+35x-8xy+', '+28y-10x^{2}+35x-8xy', '-10x^{2}++28y-8xy+35x', '+28y+35x-10x^{2}-8xy', '-10x^{2}+28y+-8xy+35x', '35x+-8xy+28y-10x^{2}', '28y+-10x^{2}+35x-8xy', '-10x^{2}+28y-8xy++35x', '-8xy-10x^{2}+28y++35x', '-8xy+35x+-10x^{2}+28y', '-10x^{2}+28y+35x-8xy', '-8xy++35x+28y-10x^{2}', '35x-10x^{2}+-8xy+28y', '-10x^{2}+35x++28y-8xy', '-8xy+-10x^{2}+35x+28y', '+28y-8xy+35x-10x^{2}', '-10x^{2}-8xy++28y+35x', '+35x-10x^{2}-8xy+28y', '-8xy++35x-10x^{2}+28y', '-10x^{2}-8xy+28y+35x', '35x-10x^{2}-8xy+28y+', '-10x^{2}-8xy+28y++35x', '+35x-8xy-10x^{2}+28y', '-8xy-10x^{2}++28y+35x', '28y-10x^{2}+-8xy+35x', '-10x^{2}-8xy+35x+28y', '-8xy-10x^{2}++35x+28y', '28y+-8xy-10x^{2}+35x', '-10x^{2}++35x-8xy+28y', '28y-10x^{2}+35x+-8xy', '35x-10x^{2}+28y+-8xy', '28y+35x+-10x^{2}-8xy', '28y+35x-10x^{2}+-8xy', '35x-10x^{2}++28y-8xy', '-10x^{2}-8xy+35x++28y', '28y-8xy-10x^{2}+35x+', '-10x^{2}+35x-8xy+28y+', '-8xy-10x^{2}+35x+28y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (-5y-8x)(-1y+1z) $$</span>",
	'answer': ['-5yz+8xy+5y^{2}-8xz', '-5yz-8xz+5y^{2}+8xy', '-8xz-5yz+5y^{2}+8xy', '5y^{2}+8xy-8xz-5yz', '8xy-5yz+5y^{2}-8xz', '-8xz+5y^{2}-5yz+8xy', '-8xz-5yz+8xy+5y^{2}', '-5yz+8xy-8xz+5y^{2}', '8xy-8xz+5y^{2}-5yz', '8xy+5y^{2}-8xz-5yz', '-5yz+5y^{2}-8xz+8xy', '5y^{2}-8xz-5yz+8xy', '-8xz+8xy+5y^{2}-5yz', '8xy-8xz-5yz+5y^{2}', '8xy+5y^{2}-5yz-8xz', '-5yz+5y^{2}+8xy-8xz', '5y^{2}-5yz+8xy-8xz', '-5yz-8xz+8xy+5y^{2}', '8xy-5yz-8xz+5y^{2}', '5y^{2}-5yz-8xz+8xy', '5y^{2}-8xz+8xy-5yz', '-8xz+8xy-5yz+5y^{2}', '-8xz+5y^{2}+8xy-5yz', '5y^{2}+8xy-5yz-8xz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (-6z-1y)(4z-4x) $$</span>",
	'answer': ['-24z^{2}+-4yz+4xy+24xz', '+24xz+4xy-4yz-24z^{2}', '+4xy-24z^{2}+24xz-4yz', '-4yz-24z^{2}+24xz+4xy+', '24xz+-24z^{2}-4yz+4xy', '-4yz++4xy-24z^{2}+24xz', '24xz-4yz-24z^{2}+4xy+', '+24xz-4yz-24z^{2}+4xy', '4xy+24xz+-4yz-24z^{2}', '-4yz+4xy+-24z^{2}+24xz', '+4xy+24xz-4yz-24z^{2}', '-24z^{2}-4yz+24xz+4xy+', '24xz-4yz+-24z^{2}+4xy', '-24z^{2}-4yz+4xy+24xz+', '-4yz-24z^{2}+4xy+24xz', '4xy-4yz-24z^{2}+24xz+', '24xz+-4yz+4xy-24z^{2}', '-24z^{2}+24xz++4xy-4yz', '+4xy-4yz+24xz-24z^{2}', '4xy-4yz+24xz+-24z^{2}', '-24z^{2}-4yz+24xz++4xy', '4xy+-4yz+24xz-24z^{2}', '-4yz-24z^{2}+4xy+24xz+', '-4yz+4xy+24xz+-24z^{2}', '-24z^{2}-4yz+4xy++24xz', '4xy++24xz-4yz-24z^{2}', '-4yz-24z^{2}++24xz+4xy', '4xy-4yz++24xz-24z^{2}', '-4yz-24z^{2}+24xz+4xy', '-4yz+24xz-24z^{2}+4xy+', '-4yz+4xy-24z^{2}++24xz', '-24z^{2}+4xy-4yz++24xz', '+24xz-24z^{2}-4yz+4xy', '-24z^{2}++24xz-4yz+4xy', '+4xy-24z^{2}-4yz+24xz', '-4yz+4xy+24xz-24z^{2}', '24xz+4xy-24z^{2}+-4yz', '-4yz+-24z^{2}+4xy+24xz', '4xy-24z^{2}+24xz-4yz+', '-24z^{2}+24xz-4yz++4xy', '-24z^{2}-4yz++24xz+4xy', '-24z^{2}+-4yz+24xz+4xy', '24xz-4yz++4xy-24z^{2}', '4xy++24xz-24z^{2}-4yz', '24xz+-24z^{2}+4xy-4yz', '24xz-4yz+4xy-24z^{2}+', '4xy+24xz-4yz-24z^{2}+', '24xz-24z^{2}+4xy+-4yz', '-4yz-24z^{2}+4xy++24xz', '-4yz+4xy-24z^{2}+24xz+', '-24z^{2}+4xy++24xz-4yz', '+24xz+4xy-24z^{2}-4yz', '+24xz-24z^{2}+4xy-4yz', '4xy-4yz+24xz-24z^{2}+', '-24z^{2}+24xz+4xy+-4yz', '4xy+-24z^{2}+24xz-4yz', '-24z^{2}+24xz-4yz+4xy', '4xy-4yz-24z^{2}++24xz', '24xz-4yz-24z^{2}++4xy', '24xz+4xy-4yz+-24z^{2}', '4xy+24xz-4yz+-24z^{2}', '24xz-24z^{2}-4yz+4xy+', '-24z^{2}+4xy-4yz+24xz', '24xz+4xy-24z^{2}-4yz+', '-4yz+4xy-24z^{2}+24xz', '4xy+24xz-24z^{2}+-4yz', '-4yz+24xz+4xy+-24z^{2}', '-24z^{2}+4xy+24xz+-4yz', '24xz-24z^{2}+-4yz+4xy', '-24z^{2}+24xz+4xy-4yz+', '-4yz+24xz+-24z^{2}+4xy', '4xy-4yz+-24z^{2}+24xz', '-4yz+24xz+4xy-24z^{2}+', '+4xy-4yz-24z^{2}+24xz', '4xy-24z^{2}++24xz-4yz', '-24z^{2}++4xy-4yz+24xz', '-24z^{2}+24xz+4xy-4yz', '24xz+-4yz-24z^{2}+4xy', '24xz++4xy-24z^{2}-4yz', '-4yz++24xz-24z^{2}+4xy', '-24z^{2}+24xz-4yz+4xy+', '-4yz-24z^{2}+24xz++4xy', '24xz+4xy-4yz-24z^{2}+', '4xy-24z^{2}+24xz+-4yz', '+24xz-4yz+4xy-24z^{2}', '24xz+4xy+-24z^{2}-4yz', '-24z^{2}+4xy+-4yz+24xz', '-4yz+24xz++4xy-24z^{2}', '4xy-24z^{2}-4yz+24xz+', '24xz-24z^{2}+4xy-4yz+', '4xy+-4yz-24z^{2}+24xz', '-24z^{2}+4xy-4yz+24xz+', '4xy+24xz-24z^{2}-4yz+', '-4yz+4xy++24xz-24z^{2}', '-4yz-24z^{2}++4xy+24xz', '-24z^{2}++4xy+24xz-4yz', '-24z^{2}-4yz+4xy+24xz', '-4yz+24xz-24z^{2}++4xy', '24xz++4xy-4yz-24z^{2}', '4xy-24z^{2}+-4yz+24xz', '24xz-4yz+4xy+-24z^{2}', '-24z^{2}+4xy+24xz-4yz+', '-4yz+24xz+4xy-24z^{2}', '-24z^{2}+4xy+24xz-4yz', '-4yz++4xy+24xz-24z^{2}', '4xy+-24z^{2}-4yz+24xz', '-24z^{2}-4yz++4xy+24xz', '4xy+24xz+-24z^{2}-4yz', '-24z^{2}-4yz+24xz+4xy', '-24z^{2}+24xz+-4yz+4xy', '24xz-24z^{2}++4xy-4yz', '24xz+4xy+-4yz-24z^{2}', '+4xy+24xz-24z^{2}-4yz', '4xy-24z^{2}-4yz++24xz', '-4yz+4xy+24xz-24z^{2}+', '-4yz+24xz-24z^{2}+4xy', '-24z^{2}++24xz+4xy-4yz', '-4yz+-24z^{2}+24xz+4xy', '24xz-24z^{2}-4yz++4xy', '-4yz++24xz+4xy-24z^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (-4y-6z)(-4z+4x) $$</span>",
	'answer': ['24z^{2}-16xy+16yz-24xz', '-24xz-16xy+24z^{2}+16yz', '24z^{2}+16yz-24xz-16xy', '-16xy+16yz+24z^{2}-24xz', '24z^{2}-24xz+16yz-16xy', '-24xz+16yz+24z^{2}-16xy', '24z^{2}-24xz-16xy+16yz', '-24xz+24z^{2}+16yz-16xy', '16yz-16xy-24xz+24z^{2}', '-16xy-24xz+24z^{2}+16yz', '24z^{2}+16yz-16xy-24xz', '16yz-16xy+24z^{2}-24xz', '16yz-24xz+24z^{2}-16xy', '-24xz-16xy+16yz+24z^{2}', '16yz-24xz-16xy+24z^{2}', '-16xy+24z^{2}-24xz+16yz', '-16xy-24xz+16yz+24z^{2}', '-24xz+24z^{2}-16xy+16yz', '16yz+24z^{2}-16xy-24xz', '24z^{2}-16xy-24xz+16yz', '-16xy+16yz-24xz+24z^{2}', '-24xz+16yz-16xy+24z^{2}', '-16xy+24z^{2}+16yz-24xz', '16yz+24z^{2}-24xz-16xy'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (1y+4x)(1z-4y) $$</span>",
	'answer': ['-16xy-4y^{2}+1yz+4xz', '-4y^{2}+4xz+1yz-16xy', '4xz+1yz-4y^{2}-16xy', '1yz+4xz-16xy-4y^{2}', '4xz+1yz-16xy-4y^{2}', '-4y^{2}-16xy+4xz+1yz', '1yz-16xy+4xz-4y^{2}', '-16xy+4xz+1yz-4y^{2}', '-16xy+4xz-4y^{2}+1yz', '-16xy-4y^{2}+4xz+1yz', '-4y^{2}+1yz+4xz-16xy', '-4y^{2}+4xz-16xy+1yz', '-4y^{2}-16xy+1yz+4xz', '4xz-4y^{2}+1yz-16xy', '1yz-4y^{2}-16xy+4xz', '4xz-4y^{2}-16xy+1yz', '-16xy+1yz-4y^{2}+4xz', '1yz+4xz-4y^{2}-16xy', '-16xy+1yz+4xz-4y^{2}', '-4y^{2}+1yz-16xy+4xz', '4xz-16xy+1yz-4y^{2}', '1yz-4y^{2}+4xz-16xy', '1yz-16xy-4y^{2}+4xz', '4xz-16xy-4y^{2}+1yz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (7x+6)(-8y-2) $$</span>",
	'answer': ['-48y-56xy-12-14x', '-14x+-56xy-48y-12', '-48y-12-56xy-14x+', '-14x+-48y-12-56xy', '-48y-14x-56xy-12', '-56xy-12-14x-48y+', '-48y-56xy-14x+-12', '-48y+-12-56xy-14x', '-48y-14x-12-56xy', '-12+-48y-14x-56xy', '-14x-12+-56xy-48y', '-56xy-48y-14x-12', '-48y-14x-56xy-12+', '-48y+-56xy-14x-12', '-48y-14x+-56xy-12', '-56xy+-12-14x-48y', '-14x-48y-12-56xy', '-56xy-12-14x-48y', '-14x+-12-56xy-48y', '-14x-56xy-12+-48y', '-48y-56xy-12-14x+', '-56xy-48y-12-14x+', '-48y-56xy-12+-14x', '-12-48y-56xy+-14x', '-14x-56xy+-48y-12', '-56xy-14x-12+-48y', '-48y-56xy+-12-14x', '-56xy+-48y-14x-12', '-48y-12+-56xy-14x', '-14x-48y-56xy+-12', '-48y-14x-12-56xy+', '-56xy-14x-12-48y+', '-12+-48y-56xy-14x', '-14x-48y-56xy-12+', '-14x-48y+-56xy-12', '-56xy-12-14x+-48y', '-48y-12-14x-56xy+', '-14x-12-48y-56xy', '-12-14x+-48y-56xy', '-12-56xy-14x-48y+', '-14x-48y-12-56xy+', '-12-56xy-48y-14x', '-56xy-12-48y-14x+', '-12-56xy-48y+-14x', '-56xy-12-48y+-14x', '-12-48y-56xy-14x', '-56xy-48y+-12-14x', '-14x-12-48y-56xy+', '-12+-14x-48y-56xy', '-12-56xy+-48y-14x', '-14x-12-56xy-48y', '-56xy-48y-14x-12+', '-48y-12-14x-56xy', '-12-56xy+-14x-48y', '-14x+-48y-56xy-12', '-56xy-12+-14x-48y', '-12+-14x-56xy-48y', '-48y-14x-12+-56xy', '-56xy-12+-48y-14x', '-12-48y-14x-56xy', '-12-48y+-14x-56xy', '-56xy-14x+-48y-12', '-48y-56xy+-14x-12', '-12-56xy-14x+-48y', '-12+-56xy-48y-14x', '-12-48y-56xy-14x+', '-56xy+-12-48y-14x', '-56xy-48y-12+-14x', '-48y+-14x-56xy-12', '-56xy-48y-14x+-12', '-14x-56xy-48y+-12', '-56xy+-48y-12-14x', '-48y+-14x-12-56xy', '-56xy-14x-48y-12+', '-12-14x-48y+-56xy', '-12-48y+-56xy-14x', '-14x-56xy-48y-12', '-56xy-14x-12-48y', '-12-14x-48y-56xy', '-12-56xy-14x-48y', '-14x-48y-56xy-12', '-48y-14x-56xy+-12', '-14x-12-56xy+-48y', '-56xy-48y-12-14x', '-14x-12-56xy-48y+', '-14x+-12-48y-56xy', '-12-14x-56xy-48y', '-48y-12+-14x-56xy', '-56xy+-14x-12-48y', '-14x-56xy-12-48y+', '-14x-48y-12+-56xy', '-12-14x-56xy-48y+', '-12-14x-56xy+-48y', '-14x-48y+-12-56xy', '-12-14x+-56xy-48y', '-14x-56xy-48y-12+', '-48y-12-56xy-14x', '-48y+-56xy-12-14x', '-48y-12-56xy+-14x', '-56xy-12-48y-14x', '-12-48y-14x-56xy+', '-14x-12+-48y-56xy', '-56xy+-14x-48y-12', '-48y-14x+-12-56xy', '-14x+-56xy-12-48y', '-56xy-14x+-12-48y', '-14x-56xy+-12-48y', '-48y+-12-14x-56xy', '-56xy-48y+-14x-12', '-48y-12-14x+-56xy', '-12-48y-14x+-56xy', '-12+-56xy-14x-48y', '-56xy-14x-48y+-12', '-48y-56xy-14x-12+', '-48y-56xy-14x-12', '-14x-56xy-12-48y', '-12-14x-48y-56xy+', '-14x-12-48y+-56xy', '-12-56xy-48y-14x+', '-56xy-14x-48y-12'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (4z-3)(2y-3) $$</span>",
	'answer': ['-12z+8yz-6y+9', '-6y+9+8yz-12z', '9+8yz-6y-12z', '-12z+8yz+9-6y', '-6y+8yz-12z+9', '-6y+9-12z+8yz', '-12z+9-6y+8yz', '-6y-12z+8yz+9', '-12z+9+8yz-6y', '8yz+9-6y-12z', '8yz-12z-6y+9', '9+8yz-12z-6y', '-12z-6y+8yz+9', '9-6y+8yz-12z', '8yz-6y+9-12z', '9-12z-6y+8yz', '8yz+9-12z-6y', '-6y-12z+9+8yz', '9-12z+8yz-6y', '-12z-6y+9+8yz', '8yz-6y-12z+9', '8yz-12z+9-6y', '9-6y-12z+8yz', '-6y+8yz+9-12z'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}, {
	'question': "Effectue la double distribution dans l'expression littérale suivante: <span>$$ (-6z+8y)(-6z-6) $$</span>",
	'answer': ['36z-48yz+36z^{2}-48y', '-48y+36z^{2}-48yz+36z', '-48yz+36z^{2}-48y+36z', '-48y+36z+36z^{2}-48yz', '-48yz+36z-48y+36z^{2}', '36z^{2}+36z-48y-48yz', '36z^{2}-48yz+36z-48y', '-48yz-48y+36z+36z^{2}', '36z^{2}-48y-48yz+36z', '-48y-48yz+36z^{2}+36z', '36z+36z^{2}-48y-48yz', '-48yz+36z+36z^{2}-48y', '36z-48y-48yz+36z^{2}', '36z^{2}-48yz-48y+36z', '36z+36z^{2}-48yz-48y', '-48y-48yz+36z+36z^{2}', '-48y+36z-48yz+36z^{2}', '-48yz-48y+36z^{2}+36z', '36z^{2}+36z-48yz-48y', '-48y+36z^{2}+36z-48yz', '-48yz+36z^{2}+36z-48y', '36z^{2}-48y+36z-48yz', '36z-48yz-48y+36z^{2}', '36z-48y+36z^{2}-48yz'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ['transforme_puissance_to_latex']
}]
}

Addition_et_soustraction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Addition et soustraction de polynômes",
    "body": "Lorsque l’on additionne deux polynômes on peut simplement enlever les parenthèses et ensuite réduire l’expression littérale obtenue. Lorsque l’on soustrait deux polynômes on doit inverser les signes de chaque monôme du polynôme qui suit le signe de soustraction. On enlève ensuite le signe de soustraction ainsi que les parenthèses. C'est exactement comme si il y'avait -1 devant la parenthèse et que l'on distribue ce -1 dans celle-ci",
    "exemple":"<span>$$ (3x-5)+(3-8x) $$</span><br> Comme il y a une addition entre les deux polynôme on peut directement enlever les parenthèses. Mon expression devient alors :<span>$$ 3x-5+3-8x $$</span><br> Je réduis ensuite l'expression ce qui me donne :  $$ -5x-2 $$ <br>Dans le cas ou on a une soustraction comme ici  $$ (3x+12)-(4x-16)$$ <br> On doit d'abord inverser le signe des monômes qui se trouvent dans la deuxième parenthèse ainsi \( 4x \) devient \( -4x \) et \( -16 \) devient \( +16 \). On finit par enlever le - devant la parenthèse ainsi que les parenthèses et on trouve:  $$ 3x+12-4x+16 $$  <br> Si on réduis notre expression littérale se transforme en :  $$ -x+28 $$ <p class='attention'>Attention dans le cas où on a un + devant une parenthèse qui commence par un - comme dans \( +(-5x+12) \) on peut directement retirer les parenthèse cela nous donne \( +-5x+12 \). On voit que l'on a + et - qui se suivent. On utlise alors la règle des signes: + et - donne - donc cela devient : -5x+12</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [{
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (-8-3x-1y)-(6-7y-5x) $$</span>",
	'answer': ['2x-14+6y', '-14+6y+2x', '2x+6y-14', '6y-14+2x', '6y+2x-14', '-14+2x+6y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (-1x-1y-2)+(4x-6y) $$</span>",
	'answer': ['-7y-2+3x', '3x-7y-2', '-2+3x-7y', '-2-7y+3x', '-7y+3x-2', '3x-2-7y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (6x-6+1y)+(5x-4) $$</span>",
	'answer': ['11x-10+1y', '-10+1y+11x', '1y-10+11x', '1y+11x-10', '11x+1y-10', '-10+11x+1y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (8y+2)+(5x+2y) $$</span>",
	'answer': ['10y+5x+2', '5x+10y+2', '10y+2+5x', '5x+2+10y', '2+10y+5x', '2+5x+10y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (2+5x)-(2x+7y) $$</span>",
	'answer': ['-7y+3x', '3x-7y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (-3y-4)+(-2+7y) $$</span>",
	'answer': ['4y-6', '-6+4y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (-2y+8x)-(-3x+3) $$</span>",
	'answer': ['-2y-3+11x', '-2y+11x-3', '11x-2y-3', '11x-3-2y', '-3-2y+11x', '-3+11x-2y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (3y-4x-6)-(-7-5x) $$</span>",
	'answer': ['1+1x+3y', '1x+1+3y', '3y+1+1x', '1x+3y+1', '3y+1x+1', '1+3y+1x'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (7x-4-4y)+(-8y-5x-7) $$</span>",
	'answer': ['2x-12y-11', '-11-12y+2x', '2x-11-12y', '-11+2x-12y', '-12y-11+2x', '-12y+2x-11'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (6x+7y+6)-(-8x+1y-8) $$</span>",
	'answer': ['14x+6y+14', '6y+14x+14', '14x+14+6y', '6y+14+14x', '14+14x+6y', '14+6y+14x'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (-5x-2+6y)-(4y-7x) $$</span>",
	'answer': ['2y+2x-2', '2x-2+2y', '2y-2+2x', '-2+2y+2x', '2x+2y-2', '-2+2x+2y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Effectue l'addition/soustraction dans l'expression suivante: <span>$$ (3y-6)+(6y-4) $$</span>",
	'answer': ['9y-10', '-10+9y'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}]}


Identité_remarquables = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Identité remarquables",
    "body": "Une identité remarquable est une expression mathématique qui sert de base pour faire un calcul littéral. Les identités remarquables sont utiles notamment pour résoudre une équation. En mathématiques, ces expressions algébriques permettent de simplifier les calculs en tout genre. <br> Il existe 3 identités remarquables pour les polynômes de degré 2. Vous devez connaître par coeur ses formules!",
    "exemple":"$$ (a+b)^2 = a^2+2ab+b^2 $$ $$ (a-b)^2 = a^2-2ab+b^2 $$ $$ (a+b)(a-b) = a^2 - b^2 $$",
	"body2": "En connaissant ces formules, vous pourrez rapidement effectuer certains calculs et trouver la solution d’équation du deuxième degré. Lorsqu’on passe de la formule de gauche à celle de droite, on dit que l’on développe le calcul. Si au contraire, on passe de la forme de droite à celle de gauche, on dit que l’on factorise.",
	"exemple2": "Voici un exemple de développement: <br> $$ (x+3)^2 = x^2 +6x+9$$  <br> Voici un exemple de factorisation : $$ x^2 -10 +25 = (x-5)^2$$",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [{
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (2x+2)^2 $$</span>",
	'answer': ['4x^2+8x+4', '4x^2+4+8x', '8x+4x^2+4', '8x+4+4x^2', '4+4x^2+8x', '4+8x+4x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (2x+9)(2x-9) $$</span>",
	'answer': ['4x^2-81', '-81+4x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (3x+9)(3x-9) $$</span>",
	'answer': ['9x^2-81', '-81+9x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (1x+4)(1x-4) $$</span>",
	'answer': ['x^2-16', '-16+x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (3x-3)^2 $$</span>",
	'answer': ['9x^2-18x+9', '9x^2+9-18x', '-18x+9x^2+9', '-18x+9+9x^2', '9+9x^2-18x', '9-18x+9x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (2x+1)(2x-1) $$</span>",
	'answer': ['4x^2-1', '-1+4x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (2x+9)^2 $$</span>",
	'answer': ['4x^2+36x+81', '4x^2+81+36x', '36x+4x^2+81', '36x+81+4x^2', '81+4x^2+36x', '81+36x+4x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (2x-4)^2 $$</span>",
	'answer': ['4x^2-16x+16', '4x^2+16-16x', '-16x+4x^2+16', '-16x+16+4x^2', '16+4x^2-16x', '16-16x+4x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (1x+8)^2 $$</span>",
	'answer': ['x^2+16x+64', 'x^2+64+16x', '16x+x^2+64', '16x+64+x^2', '64+x^2+16x', '64+16x+x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (3x-4)^2 $$</span>",
	'answer': ['9x^2-24x+16', '9x^2+16-24x', '-24x+9x^2+16', '-24x+16+9x^2', '16+9x^2-24x', '16-24x+9x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remaqrable ci-dessous: <span>$$ (2x-2)^2 $$</span>",
	'answer': ['4x^2-8x+4', '4x^2+4-8x', '-8x+4x^2+4', '-8x+4+4x^2', '4+4x^2-8x', '4-8x+4x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}, {
	'question': "Donne la forme développée et réduite de l'identité remarquable ci-dessous: <span>$$ (3x-7)^2 $$</span>",
	'answer': ['9x^2-42x+49', '9x^2+49-42x', '-42x+9x^2+49', '-42x+49+9x^2', '49+9x^2-42x', '49-42x+9x^2'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': []
}]
}

Factorisation = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Factorisation",
    "body": "Factoriser cela veut dire que l'on va transformer une somme en un produit. C'est l'inverse de développer où l'a on transforme un produit en somme. En d'autres termes, on cherche à trouver les termes qui, lorsqu'on les multiplie ensemble, donnent l'expression initiale. Il faut passer par plusieurs étapes si on veut être sûr que notre expression est factoriser au maximum. <br> La première étape consiste à regarder chaque terme de notre polynôme et voir si ceux-ci possède un diviseur commun que l'on puisse mettre en évidence (en facteur).",
    "exemple":"<span>$$ 3x+9y+6 $$</span><br> On remarque que les trois coefficients de notre expression littérale sont des multiples de 3 et donc 3 est diviseur de chacun des termes. On peut donc mettre le 3 en facteur (devant la parenthèse) et diviser chaque terme par 3 pour obtenir : $$ 3(x+3y+2) $$ <br> Voici un autre exemple plus compliqué : $$ 5x^2 + 10x +15xy $$ <br> Dans ce cas-ci on remarque que chaque coefficient est un multiple de 5. Donc on peut mettre 5 en facteur. On remarque aussi qu'il y a au moins un x pour chaque terme. On peut donc mettre aussi x en facteur. En résumé, dans ce cas-ci on peut mettre 5x en facteur pour obtenir : $$ 5x(x+2+3y)$$",
	"body2": "Imaginons que l'on ait un polyn'ome où il n'y a rien de communs dans chaque terme. Dans ce cas-ci on peut essayer de voir si il s'agit d'une identité remarquable. Il faut en premier lieu voir si il y a bien 2 ou 3 termes commes dans les formes développées des identités remarquables. Si on a trois termes alors il est possible que se soit l'identités \( (a+b)^2 = a^2+2ab+b^2 \) ou \( (a+b)^2 = a^2-2ab+b^2 \). <br> Pour trouver ce que vaut a et b on ordonne le polynôme et on calcule la racine du premier terme (a) et du dernier terme (b). On vérifie ensuite que si on multiplie a et b ensemble puis le résultat par 2 que l'on trouve bien la valeur du terme au milieu. Si le terme centrale est positif alors c'est la forme\( (a+b)^2 \) qu'il faut utiliser sinon si le deuxième terme est négatif c'est la forme \( (a-b)^2 \).",
	"exemple2": "<span>$$ x^2 + 8x + 16 $$</span> Ici on voit que l'on a trois termes donc on prend la racine du premier terme \( \sqrt{x^2} = x \) cela va nous donner notre 'a' et on fait la racine du dernier terme \( \sqrt{16} = 4 \) ce qui nous donne notre b. On vérifie ensuite que le double de la multiplication de a et b nous donne bien le coefficient du terme du milieu. \( x \cdot 4 \cdot 2  = 8x \) ce qui correspond bien au terme du milieu. Donc notre forme factorisée est donc : \( (x+4)^2 \) <br><br> Prenons un autre exemple : \( 4x^2 -20x +25 \) . On calcule la racine du premier terme  \( \sqrt{4x^2} = 2x \) cela va nous donner notre 'a' et on fait la racine du dernier terme \( \sqrt{25} = 5 \) ce qui nous donne notre b. On verifie enfin le terme du milieu: \( 2x \cdot 5 \cdot 2 = 20x \) comme on a -20x et pas 20x on doit utiliser l'identité remarquable avec le signe - : \( (a-b)^2 \) ce qui nous donne \( (2x-5)^2 \)",
	"body3": "Nous venons de traiter les cas où l'expression contient 3 monômes et que ceux-ci peuvent être factorisé en utilisant les identités remarquables. Prenons le dernier cas des identités remarquables : \( (a+b)(a-b)= a^2-b^2 \) donc lorsqu'on a seulement deux monômes et qu'il y a un - entre les deux on devrait pouvoir utiliser cette identité. Pour la trouver il suffit de prendre la racine du premier et du deuxième terme pour obtenir 'a' et 'b'.",
	"exemple3":"$$ 36x^2 - 100$$ On voit ici que nous avons deux termes séparer par un signe - donc nous pouvons essayer de factoriser avec la méthode vue précédemment \( \sqrt{36x^2} = 6x \) donc a = 6x et  \( \sqrt{100} = 10 \) donc on a b=10. Notre expression factorisé vaut alors \( (6x+10)(6x-10) \). Prenons un deuxième exemple : \( 16x^4-y^4 \). Nous voyons que nous avons deux mônomes séprarer par un signe -. Nous pouvons donc essayer de factoriser comme au dessus. Nous prenons la racine du premier terme ce qui nous donne \( \sqrt{16x^4} = 4x^2 \) donc \( a=4x^2 \) on prend ensuite la racine du deuxième terme ce qui nous donne \( \sqrt{y^4} = y^2 \). ",
	"body4": "Quelque fois ont peut avoir une expression qui au premier abord ressemble beaucoup à une forme développée des identités remarquable \( (a+b)^2 \) ou \( (a-b)^2 \). Mais lorsqu'on essaie de factoriser l'expression on y arrive pas. Dans ce cas-ci on doit essayer de factoriser sous cette forme l'expression : \( (a \pm b)(a \pm c)\). Pour trouver 'a' c'est facile il suffit d'ordonner le polynôme et de faire la racine du premier monôme. Pour trouver 'b' et 'c'. Il faut que le produit de b et c nous donne le dernier terme et que la somme de b et c nous donne le terme du milieu.",
	"exemple4":"$$ x^2 -10x + 21 $$ Dans ce cas-ci on pourrait croire que l'on a une identité remarquable de la forme \( (a-b)^2 \) mais lorsqu'on essaie de factorisé on voit bien que la racine du troisième terme ne nous donne pas un nombre décimal et que lorsqu'on essait de trouver le deuxième terme 2ab cela ne fonctionne pas. Donc en est en face  d'une expression à factoriser sous la forme de : \( (a \pm b)(a \pm c)\). On prends la racine du premier terme pour obtenir notre a \( \sqrt{x^2}=x \) donc a=x. Ensuite on doit trouver deux nombres dont le produit vaut 21 et la somme vaut -10. Une chose que l'on peut faire est de trouver tous les diviseurs de 21 : \( D_21 = {1,3,7,21} \). Maintenant il faut qu'on cherche dans ces nombres quelles sont les deux nombres dont la somme vaut -10. On a le droit d'utiliser les nombres négatifs des diviseurs. Si l'on fait ça on remarque que \(-3 +(-7) = -10\) donc b=-3 et c=-7 et notre expression factorisée vaut alors: \( (x-3)(x-7) \). <p class='attention'> Il faut bien reagrder les signes de l'expression que l'on nous donne. Par exemple : \( x^2 +5x-24 \) ici on remaruqe que le dernier terme est négatif ça veut dire que \( b\cdot c \) est négatif donc cela veut dire que b et c sont de signes opposés. Si au contraire le dernier terme est positif cela veut dire que b et c sont de même signe.</p>",
	"body5": "Il arrive que l'expression que l'on nous donne soit partiellement factorisé par exemple: $$ 3(5+x)-8(5+x) $$ On remarque ici qu'il y a deux termes. Le premier est \( 3(5+x) \) et le deuxième est \( -8(5+x) \). On peut observer qu'ils ont en commun le (5+x) c'est donc cette partie qui va être en facteur. On additionne ensuite les coeffients qui se trouvent devant les parenthèses 3 et -8 ce qui donne -5. L'expression finale sera alors -5(5+x).",
	"exemple5":"$$ -4(x^2+2) + 18(x^2+2)$$ On remarque ici qu'il y a deux termes: \( -4(x^2+2) \) et \(18(x^2+2)\). Ils ont en communs (x^2+2). On fait donc la somme des coefficients qui se trouvent devant la parenthèse: -4 et 18 ce qui nous donne 14. L'expression factorisée est donc 14(x^2+2) ",
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

Preuve_avec_le_calcul_littéral = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Preuve avec le calcul littéral",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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

Equation_équivalente = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation équivalente",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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

Réduction_avec_coefficients_rationnels = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Réduction avec coefficients rationnels",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire \( x^2 \)", "Pour insérer une fraction écrivez (/) exemple (4/3) veut dire \( \\frac{4}{3} \)"],
    "questions": [{
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{9}{5}x + \\frac{6}{3} + \\frac{2}{6}x + \\frac{2}{3}x + \\frac{9}{5}x^2 + \\frac{6}{4}x $$</span>',
	'answer': ['\\frac{9}{5}x^{2}+\\frac{43}{10}x+2', '\\frac{9}{5}x^{2}+2+\\frac{43}{10}x', '\\frac{43}{10}x+\\frac{9}{5}x^{2}+2', '\\frac{43}{10}x+2+\\frac{9}{5}x^{2}', '2+\\frac{9}{5}x^{2}+\\frac{43}{10}x', '2+\\frac{43}{10}x+\\frac{9}{5}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{3}{5}x - \\frac{5}{6}x - \\frac{3}{2}x - \\frac{8}{7} - \\frac{4}{6}x^2 - \\frac{8}{3} $$</span>',
	'answer': ['-\\frac{2}{3}x^{2}-\\frac{26}{15}x-\\frac{80}{21}', '-\\frac{2}{3}x^{2}-\\frac{80}{21}-\\frac{26}{15}x', '-\\frac{26}{15}x-\\frac{2}{3}x^{2}-\\frac{80}{21}', '-\\frac{26}{15}x-\\frac{80}{21}-\\frac{2}{3}x^{2}', '-\\frac{80}{21}-\\frac{2}{3}x^{2}-\\frac{26}{15}x', '-\\frac{80}{21}-\\frac{26}{15}x-\\frac{2}{3}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{8}{7}x^2 + \\frac{4}{6}x + \\frac{8}{4}x + \\frac{2}{4}x^2 + \\frac{5}{7}x + \\frac{5}{2} + \\frac{5}{3}x^2 $$</span>',
	'answer': ['\\frac{139}{42}x^{2}+\\frac{71}{21}x+\\frac{5}{2}', '\\frac{139}{42}x^{2}+\\frac{5}{2}+\\frac{71}{21}x', '\\frac{71}{21}x+\\frac{139}{42}x^{2}+\\frac{5}{2}', '\\frac{71}{21}x+\\frac{5}{2}+\\frac{139}{42}x^{2}', '\\frac{5}{2}+\\frac{139}{42}x^{2}+\\frac{71}{21}x', '\\frac{5}{2}+\\frac{71}{21}x+\\frac{139}{42}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{4}{4}x^2 - \\frac{5}{3} - \\frac{3}{7}x^2 - \\frac{6}{6} - \\frac{4}{4}x^2 - \\frac{7}{5}x^2 $$</span>',
	'answer': ['-\\frac{64}{35}x^{2}-\\frac{8}{3}', '-\\frac{8}{3}-\\frac{64}{35}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{6}{6}x - \\frac{8}{2}x^2 - \\frac{3}{6}x - \\frac{7}{7}x - \\frac{4}{3}x - \\frac{2}{2}x^2 $$</span>',
	'answer': ['\\frac{x\\left(-30x-11\\right)}{6}', '\\frac{x\\left(-11\\right)}{6}-30x', '-30x+\\frac{x\\left(-11\\right)}{6}', '-30x-11\\right)}{6}+\\frac{x\\left(', '-11\\right)}{6}+\\frac{x\\left(-30x', '-11\\right)}{6}-30x+\\frac{x\\left('],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{4}{2} - \\frac{2}{4}x - \\frac{3}{4} - \\frac{3}{2} - \\frac{7}{5}x $$</span>',
	'answer': ['-\\frac{19}{10}x-\\frac{1}{4}', '-\\frac{1}{4}-\\frac{19}{10}x'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{5}{6}x + \\frac{7}{2}x^2 + \\frac{6}{2} + \\frac{2}{2} + \\frac{5}{5}x + \\frac{6}{2}x^2 + \\frac{6}{6}x $$</span>',
	'answer': ['\\frac{13}{2}x^{2}+\\frac{17}{6}x+4', '\\frac{13}{2}x^{2}+4+\\frac{17}{6}x', '\\frac{17}{6}x+\\frac{13}{2}x^{2}+4', '\\frac{17}{6}x+4+\\frac{13}{2}x^{2}', '4+\\frac{13}{2}x^{2}+\\frac{17}{6}x', '4+\\frac{17}{6}x+\\frac{13}{2}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{9}{7} - \\frac{9}{7}x - \\frac{3}{6} - \\frac{8}{6} - \\frac{2}{4}x^2 - \\frac{6}{2}x - \\frac{5}{7} $$</span>',
	'answer': ['-\\frac{1}{2}x^{2}-\\frac{30}{7}x-\\frac{53}{42}', '-\\frac{1}{2}x^{2}-\\frac{53}{42}-\\frac{30}{7}x', '-\\frac{30}{7}x-\\frac{1}{2}x^{2}-\\frac{53}{42}', '-\\frac{30}{7}x-\\frac{53}{42}-\\frac{1}{2}x^{2}', '-\\frac{53}{42}-\\frac{1}{2}x^{2}-\\frac{30}{7}x', '-\\frac{53}{42}-\\frac{30}{7}x-\\frac{1}{2}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{3}{4}x - \\frac{1}{7}x^2 - \\frac{8}{7}x - \\frac{5}{7} - \\frac{4}{3} - \\frac{9}{4}x^2 - \\frac{1}{7} $$</span>',
	'answer': ['-\\frac{67}{28}x^{2}-\\frac{11}{28}x-\\frac{46}{21}', '-\\frac{67}{28}x^{2}-\\frac{46}{21}-\\frac{11}{28}x', '-\\frac{11}{28}x-\\frac{67}{28}x^{2}-\\frac{46}{21}', '-\\frac{11}{28}x-\\frac{46}{21}-\\frac{67}{28}x^{2}', '-\\frac{46}{21}-\\frac{67}{28}x^{2}-\\frac{11}{28}x', '-\\frac{46}{21}-\\frac{11}{28}x-\\frac{67}{28}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{9}{6}x^2 + \\frac{1}{7} + \\frac{1}{3}x + \\frac{9}{7} + \\frac{7}{5}x^2 + \\frac{3}{5}x^2 + \\frac{7}{6}x^2 $$</span>',
	'answer': ['\\frac{14}{3}x^{2}+\\frac{1}{3}x+\\frac{10}{7}', '\\frac{14}{3}x^{2}+\\frac{10}{7}+\\frac{1}{3}x', '\\frac{1}{3}x+\\frac{14}{3}x^{2}+\\frac{10}{7}', '\\frac{1}{3}x+\\frac{10}{7}+\\frac{14}{3}x^{2}', '\\frac{10}{7}+\\frac{14}{3}x^{2}+\\frac{1}{3}x', '\\frac{10}{7}+\\frac{1}{3}x+\\frac{14}{3}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{6}{3}x^2 - \\frac{6}{5}x - \\frac{5}{3}x^2 - \\frac{6}{6}x - \\frac{1}{5} - \\frac{1}{5}x^2 $$</span>',
	'answer': ['\\frac{2}{15}x^{2}-\\frac{11}{5}x-\\frac{1}{5}', '\\frac{2}{15}x^{2}-\\frac{1}{5}-\\frac{11}{5}x', '-\\frac{11}{5}x+\\frac{2}{15}x^{2}-\\frac{1}{5}', '-\\frac{11}{5}x-\\frac{1}{5}+\\frac{2}{15}x^{2}', '-\\frac{1}{5}+\\frac{2}{15}x^{2}-\\frac{11}{5}x', '-\\frac{1}{5}-\\frac{11}{5}x+\\frac{2}{15}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}, {
	'question': 'Réduis le polynôme suivant <span>$$ \\frac{7}{6} + \\frac{1}{7} + \\frac{8}{6}x + \\frac{8}{6}x + \\frac{1}{6}x + \\frac{8}{7}x^2 $$</span>',
	'answer': ['\\frac{8}{7}x^{2}+\\frac{17}{6}x+\\frac{55}{42}', '\\frac{8}{7}x^{2}+\\frac{55}{42}+\\frac{17}{6}x', '\\frac{17}{6}x+\\frac{8}{7}x^{2}+\\frac{55}{42}', '\\frac{17}{6}x+\\frac{55}{42}+\\frac{8}{7}x^{2}', '\\frac{55}{42}+\\frac{8}{7}x^{2}+\\frac{17}{6}x', '\\frac{55}{42}+\\frac{17}{6}x+\\frac{8}{7}x^{2}'],
	'feedback': "Bravo, c'est la bonne réponse !",
	'feedbackClass': 'text-success',
	'methods': ["enlever_espace",'transforme_fraction_to_latex', 'transforme_puissance_to_latex']
}]
}

Solution_d_une_équation_par_évaluation = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Solution d'une équation par évaluation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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

Résolution_d_équation_du_premier_degré_à_une_inconnue = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Résolution d'équation du premier degré à une inconnue",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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

Poser_une_équation = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Poser une équation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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

Solution_par_voie_graphique = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Solution par voie graphique",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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
Equation_avec_Fraction = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation avec Fraction",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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
Equation_du_deuxième_degré = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation du deuxième degré",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
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


