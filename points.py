import calcullittéralbrain
import liste_badge_db as bdg

Evaluer_une_expression_littérale = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "evaluer_une_expression_litterale",
    "nom": "Evaluer une expression littérale",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ 3x^2+2x-15 $$</span><br>Si on évalue l'expression pour x=3 alors notre expression devient:<br><span>$$ 3\cdot 3^2+2 \cdot 3-15 = 18 $$</span><br>"
              " Si on évalue l'expression pour x=-2 notre expression devient: <br> <span>$$ 3\cdot (-2)^2+2 \cdot (-2)-15 = 18 $$</span><br> <p class='attention'>Attention à bien mettre en parenthèse la valeur que prends x si celui-ci est un nombre négatif! </p>",
    "message_aide":[],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[0]
}

Réduction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "reduction_de_polynomes",
    "nom": "Réduction de polynômes",
    "body": "Réduire un polynôme signifie que l’on va mettre ensemble les monômes avec la même partie littérale. Avant de réduire un polynôme, il faut s’assurer que l’on a bien effectué toutes les opérations de puissances, racines, multiplications et divisions.<br> <strong>1ère étape </strong> <br> On sépare le polynôme en ses monômes. Dès que l’on voit un signe d’addition ou de soustraction on place une séparation avant ce dernier.<br><strong>2ème étape </strong> <br> On reconnaît les monômes qui ont la même partie littérale. On réorganise le polynôme afin de mettre ensemble les mônomes qui ont les mêmes parties littérales. <br><strong>3ème étape</strong> <br> On les additionne entre eux pour cela on fait la somme des coefficients et on réécrit la partie littérale sans la modifier",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <br> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . <br> Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "message_aide":[],
    "questions": "generer_reduire_une_expression_littérale",
    "badge": bdg.adressebadge[1]
}

Ordonner_un_polynôme = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "ordonner_un_polynome",
    "nom": "Ordonner un polynôme",
    "body": "Ordonner un polynôme signifie que l’on va d’abord inscrire les polynômes avec les plus hauts degrés. Si deux monômes possèdent le même degré on va les inscrire par ordre alphabétique (x2 signifie xx). On doit toujours ordonner un polynôme après l’avoir réduit et pas avant!",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <br> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . <br> Notre expression devient alors:  $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br>  On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <br> On trouve finalement:  $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[2]
}

Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "distributivite",
    "nom": "Distributivité",
    "body": "La distributivité s'utilise lorsqu'on a un terme qui multiplie une parenthèse. C'est une propriété mathématique qui dit que le produit d'une somme est égale à la somme des produits. En d'autres termes, on doit multiplier chaque monôme qu'il y a dans la parenthèse par le terme qui se trouve devant. <br> Imagine que tu as deux amis, et tu veux leur donner des cadeaux. Disons que tu veux donner 3 chocolats à chacun de tes amis et que tu as aussi 4 bonbons pour chacun d'eux. Au lieu de compter séparément combien de cadeaux tu as pour chaque ami, tu peux additionner les chocolats et les bonbons et ensuite multiplier le total par le nombre d'amis. <br> Voici l'exemple concret : tu as 2 amis, et tu veux leur donner 3 chocolats et 4 bonbons chacun. Pour savoir combien de cadeaux tu dois préparer en tout, tu peux utiliser la distributivité : <br>\( 2 \\text{ amis} \\times (3 \\text{ chocolats} + 4 \\text{ bonbons}) \) <br> En appliquant la propriété distributive, tu vas multiplier le nombre d'amis par le nombre de chocolats, puis par le nombre de bonbons : <br>$$ (2 \\text{ amis} \\times 3 \\text{ chocolats}) + (2 \\text{ amis} \\times 4 \\text{ bonbons}) $$ <br> Ce qui donne :<br> \( (6 \\text{ chocolats}) + (8 \\text{ bonbons}) \) <br>Ainsi, tu auras un total de 14 cadeaux à préparer pour tes amis.<br> La distributivité est donc une méthode pour répartir, ou distribuer, une multiplication sur une addition ou une soustraction.",
    "exemple":"<img src='static/images/distributivité.png' alt='Distributivité' width='300' height='120'>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[3]

}

Double_Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "double_distributivite",
    "nom": "Double Distributivité",
    "body": "Imaginons que tu as deux expressions algébriques entre parenthèses et que tu dois les multiplier ensemble. Par exemple, prenons les expressions suivantes: \( (a + b) \) et \( (c + d) \). La double distributivité consiste à distribuer chaque terme de la première parenthèse avec chaque terme de la seconde parenthèse, et ensuite à additionner les résultats obtenus. <br>Dans notre exemple, voici comment on procède:<ol><li>Multiplie a par c: \( a * c = ac \)</li><li>Multiplie a par d: \( a * d = ad \)</li><li>Multiplie b par c: \( b * c = bc \)</li><li>Multiplie b par d: \( b * d = bd \)</li></ol><br>Maintenant, additionne les résultats obtenus:<br>\[ (ac) + (ad) + (bc) + (bd) \]<br>Donc, la double distributivité de \( (a + b)(c + d) \) est:<br> \[ (a + b)(c + d) = ac + ad + bc + bd \] <br> La double distributivité s'applique aussi bien pour les expressions avec des soustractions. Par exemple, si on a \( (a - b)(c - d) \), on obtient:<br>\[ (a - b)(c - d) = ac - ad - bc + bd \]<br>Ainsi lorsque tu fais une double distribution tu multiplies chaque terme de la première parenthèse avec chaque terme de la deuxième parenthèse et tu additionnes ou soustrais les différents produits obtenus.",
    "exemple":"<img src='static/images/double-distributivité.png' alt='Double Distributivité' width='450' height='180'>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[4]
}

Addition_et_soustraction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "addition_et_soustraction_de_polynomes",
    "nom": "Addition et soustraction de polynômes",
    "body": "Lorsque l’on additionne deux polynômes on peut simplement enlever les parenthèses et ensuite réduire l’expression littérale obtenue. Lorsque l’on soustrait deux polynômes on doit inverser les signes de chaque monôme du polynôme qui suit le signe de soustraction. On enlève ensuite le signe de soustraction ainsi que les parenthèses. C'est exactement comme si il y'avait -1 devant la parenthèse et que l'on distribue ce -1 dans celle-ci",
    "exemple":"<span>$$ (3x-5)+(3-8x) $$</span><br> Comme il y a une addition entre les deux polynôme on peut directement enlever les parenthèses. Mon expression devient alors :<span>$$ 3x-5+3-8x $$</span><br> Je réduis ensuite l'expression ce qui me donne :  $$ -5x-2 $$ <br>Dans le cas ou on a une soustraction comme ici  $$ (3x+12)-(4x-16)$$ <br> On doit d'abord inverser le signe des monômes qui se trouvent dans la deuxième parenthèse ainsi \( 4x \) devient \( -4x \) et \( -16 \) devient \( +16 \). On finit par enlever le - devant la parenthèse ainsi que les parenthèses et on trouve:  $$ 3x+12-4x+16 $$  <br> Si on réduis notre expression littérale se transforme en :  $$ -x+28 $$ <p class='attention'>Attention dans le cas où on a un + devant une parenthèse qui commence par un - comme dans \( +(-5x+12) \) on peut directement retirer les parenthèse cela nous donne \( +-5x+12 \). On voit que l'on a + et - qui se suivent. On utlise alors la règle des signes: + et - donne - donc cela devient : -5x+12</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[5]
}


Identité_remarquables = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "identite_remarquables",
    "nom": "Identité remarquables",
    "body": "Une identité remarquable est une expression mathématique qui sert de base pour faire un calcul littéral. Les identités remarquables sont utiles notamment pour résoudre une équation. En mathématiques, ces expressions algébriques permettent de simplifier les calculs en tout genre. <br> Il existe 3 identités remarquables pour les polynômes de degré 2. Vous devez connaître par coeur ses formules!",
    "exemple":"$$ (a+b)^2 = a^2+2ab+b^2 $$ $$ (a-b)^2 = a^2-2ab+b^2 $$ $$ (a+b)(a-b) = a^2 - b^2 $$",
	"body2": "En connaissant ces formules, vous pourrez rapidement effectuer certains calculs et trouver la solution d’équation du deuxième degré. Lorsqu’on passe de la formule de gauche à celle de droite, on dit que l’on développe le calcul. Si au contraire, on passe de la forme de droite à celle de gauche, on dit que l’on factorise.",
	"exemple2": "Voici un exemple de développement: <br> $$ (x+3)^2 = x^2 +6x+9$$  <br> Voici un exemple de factorisation : $$ x^2 -10 +25 = (x-5)^2$$",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[6]
}

Factorisation = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "factorisation",
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
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[7]
}

Preuve_avec_le_calcul_littéral = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "preuve_avec_le_calcul_litteral",
    "nom": "Preuve avec le calcul littéral",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[8]
}

Equation_équivalente = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "equation_equivalente",
    "nom": "Equation équivalente",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[9]
}

Réduction_avec_coefficients_rationnels = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "reduction_avec_coefficients_rationnels",
    "nom": "Réduction avec coefficients rationnels",
    "body": "Pour réduire une polynôme qui possède des coefficients rationnels il faut en premier lieu regrouper les termes qui ont la même partie littérale puis modifier les fractions pour qu'elles soient sous le même dénominateur. Pour cela, on trouve le multiple commun entre les dénominateur et on amplifie les fractions de telles sorte d'avoir ce multiple commun au dénominateur. On additionne ou soustrait ensuite les coefficients qui se trouve devant les même parties littérales. Pour cela, on additionne/soustrait les numérateurs de chaque fractions. On oublie pas en dernier lieu de réduire au maximum chaque fraction pour avoir seulement des fractions irréductibles.",
    "exemple":"<span>$$ \\frac{3}{4}x-\\frac{4}{5}x^{2}+\\frac{2}{7}x+3x^2 $$</span><br><p>On sépare en premier lieu notre polynôme en deux parties pour regrouper les termes qui ont la même partie littérale ce qui devient: <span>$$ \\frac{3}{4}x +\\frac{2}{7}x$$<br></span>$$ -\\frac{4}{5}x^{2}+3x^2  $$ <span> </span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire \( x^2 \)", "Pour insérer une fraction écrivez / exemple 4/3 veut dire \( \\frac{4}{3} \)"],
    "questions": "generer_reduire_une_expression_littérale_fraction",
    "badge": bdg.adressebadge[10]
}

Solution_d_une_équation_par_évaluation = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "solution_d_une_equation_par_evaluation",
    "nom": "Solution d'une équation par évaluation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[11]
}

Résolution_d_équation_du_premier_degré_à_une_inconnue = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "resolution_d_equation_du_premier_degre_a_une_inconnue",
    "nom": "Résolution d'équation du premier degré à une inconnue",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions":"generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[12]
}

Poser_une_équation = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "poser_une_equation",
    "nom": "Poser une équation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[13]
}

Solution_par_voie_graphique = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "solution_par_voie_graphique",
    "nom": "Solution par voie graphique",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[14]
}
Equation_avec_Fraction = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "equation_avec_fraction",
    "name": "solution_par_voie_graphique",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[15]
}
Equation_du_deuxième_degré = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "equation_du_deuxieme_degre",
    "nom": "Equation du deuxième degré",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "questions": "generer_Evaluer_une_expression_littérale",
    "badge": bdg.adressebadge[16]
}


