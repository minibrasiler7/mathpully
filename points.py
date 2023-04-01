Evaluer_une_expression_littérale = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Evaluer une expression littérale",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ 3x^2+2x-15 $$</span><br><p>Si on évalue l'expression pour x=3 alors notre expression devient:</p><br><span>$$ 3\cdot 3^2+2 \cdot 3-15 = 18 $$</span><br>"
              "<p> Si on évalue l'expression pour x=-2 notre expression devient: </p> <span>$$ 3\cdot (-2)^2+2 \cdot (-2)-15 = 18 $$</span><br> <p class='attention'>Attention à bien mettre en parenthèse la valeur que prends x si celui-ci est un nombre négatif! </p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": [
        {
        "question": "Evalue l'expression pour x=4 : <span>$$ 2x^2-3x-15 $$</span>",
        "answer": "5",
        "feedback": "Bravo, c'est la bonne réponse !",
        "feedbackClass": "text-success"
    },
    {
        "question": "Evalue l'expression pour x=-3 : <span>$$ x^2+6x-20 $$</span>",
        "answer": "-29",
        "feedback": "Bravo, c'est la bonne réponse !",
        "feedbackClass": "text-success"
    },
    {
        "question": "Evalue l'expression pour x=2 : <span>$$ -2x^2-3x+10 $$</span>",
        "answer": "4",
        "feedback": "Bravo, c'est la bonne réponse !",
        "feedbackClass": "text-success"
    },
        {
        "question": "Evalue l'expression pour x=7 : <span>$$ 3x-4 $$</span>",
        "answer": "17",
        "feedback": "Bravo, c'est la bonne réponse !",
        "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=3 : <span>$$ 2x+5 $$</span>",
    "answer": "11",
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=2 : <span>$$ x^3-4x^2+5x-6 $$</span>",
    "answer": "0",
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=5 : <span>$$ x^2-4x-7 $$</span>",
    "answer": "3",
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=6 : <span>$$ 3x+2 $$</span>",
    "answer": "20",
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    },
    {
    "question": "Evalue l'expression pour x=1 : <span>$$ x^2+x-5 $$</span>",
    "answer": "-3",
    "feedback": "Bravo, c'est la bonne réponse !",
    "feedbackClass": "text-success"
    }
    ]
}

Réduction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Réduction de polynômes",
    "body": "Réduire un polynôme signifie que l’on va mettre ensemble les monômes avec la même partie littérale. Avant de réduire un polynôme, il faut s’assurer que l’on a bien effectué toutes les opérations de puissances, racines, multiplications et divisions.<br>1ère étape : on sépare le polynôme en ses monômes. Dès que l’on voit un signe d’addition ou de soustraction on place une séparation avant ce dernier.<br>2ème étape : on reconnaît les monômes qui ont la même partie littérale. 3ème étape : on les additionne entre eux",
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

