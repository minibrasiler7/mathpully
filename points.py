import interactiveExerciseBrain
nom_defaut_badge = "badge_"
bdg=[]
for i in range(1,46):
    bdg.append(f"{nom_defaut_badge}{i}.png")


Evaluer_une_expression_littérale = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "evaluer_une_expression_litterale",
    "nom": "Evaluer une expression littérale",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ 3x^2+2x-15 $$</span><br>Si on évalue l'expression pour x=3 alors notre expression devient:<br><span>$$ 3\cdot 3^2+2 \cdot 3-15 = 18 $$</span><br>"
              " Si on évalue l'expression pour x=-2 notre expression devient: <br> <span>$$ 3\cdot (-2)^2+2 \cdot (-2)-15 = 18 $$</span><br> <p class='attention'>Attention à bien mettre en parenthèse la valeur que prends x si celui-ci est un nombre négatif! </p>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$" ],
    "type": "question",
    "questions": "generer_Evaluer_une_expression_littérale",
    "method": "aucune",
    "badge": bdg[0]
}

Réduction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "reduction_de_polynomes",
    "nom": "Réduction de polynômes",
    "body": "Réduire un polynôme signifie que l’on va mettre ensemble les monômes avec la même partie littérale. Avant de réduire un polynôme, il faut s’assurer que l’on a bien effectué toutes les opérations de puissances, racines, multiplications et divisions.<br> <strong>1ère étape </strong> <br> On sépare le polynôme en ses monômes. Dès que l’on voit un signe d’addition ou de soustraction on place une séparation avant ce dernier.<br><strong>2ème étape </strong> <br> On reconnaît les monômes qui ont la même partie littérale. On réorganise le polynôme afin de mettre ensemble les mônomes qui ont les mêmes parties littérales. <br><strong>3ème étape</strong> <br> On les additionne entre eux pour cela on fait la somme des coefficients et on réécrit la partie littérale sans la modifier",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <br> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . <br> Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "type": "question",
    "questions": "generer_reduire_une_expression_littérale",
    "method": "aucune",
    "badge": bdg[1]
}

Ordonner_un_polynôme = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "ordonner_un_polynome",
    "nom": "Ordonner un polynôme",
    "body": "Ordonner un polynôme signifie que l’on va d’abord inscrire les polynômes avec les plus hauts degrés. Si deux monômes possèdent le même degré on va les inscrire par ordre alphabétique (\( x^2 \) signifie xx). Ainsi \( x^2 \) viendra avant xy et xy viendra avant \( y^2 \). On doit toujours ordonner un polynôme après l’avoir réduit et pas avant!",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <br> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . <br> Notre expression devient alors:  $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br>  On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <br> On trouve finalement:  $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "type": "question",
    "questions": "generer_ordonner_une_expression_littérale",
    "method": "aucune",
    "badge": bdg[2]
}

Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "distributivite",
    "nom": "Distributivité",
    "body": "La distributivité s'utilise lorsqu'on a un terme qui multiplie une parenthèse. C'est une propriété mathématique qui dit que le produit d'une somme est égale à la somme des produits. En d'autres termes, on doit multiplier chaque monôme qu'il y a dans la parenthèse par le terme qui se trouve devant. <br> Imagine que tu as deux amis, et tu veux leur donner des cadeaux. Disons que tu veux donner 3 chocolats à chacun de tes amis et que tu as aussi 4 bonbons pour chacun d'eux. Au lieu de compter séparément combien de cadeaux tu as pour chaque ami, tu peux additionner les chocolats et les bonbons et ensuite multiplier le total par le nombre d'amis. <br> Voici l'exemple concret : tu as 2 amis, et tu veux leur donner 3 chocolats et 4 bonbons chacun. Pour savoir combien de cadeaux tu dois préparer en tout, tu peux utiliser la distributivité : <br>\( 2 \\text{ amis} \\times (3 \\text{ chocolats} + 4 \\text{ bonbons}) \) <br> En appliquant la propriété distributive, tu vas multiplier le nombre d'amis par le nombre de chocolats, puis par le nombre de bonbons : <br>$$ (2 \\text{ amis} \\times 3 \\text{ chocolats}) + (2 \\text{ amis} \\times 4 \\text{ bonbons}) $$ <br> Ce qui donne :<br> \( (6 \\text{ chocolats}) + (8 \\text{ bonbons}) \) <br>Ainsi, tu auras un total de 14 cadeaux à préparer pour tes amis.<br> La distributivité est donc une méthode pour répartir, ou distribuer, une multiplication sur une addition ou une soustraction.",
    "exemple":"<img src='static/images/distributivité.png' alt='Distributivité' width='300' height='120'>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "type": "question",
    "questions": "generer_distribution",
    "method": "aucune",
    "badge": bdg[3]

}

Double_Distributivité = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "double_distributivite",
    "nom": "Double Distributivité",
    "body": "Imaginons que tu as deux expressions algébriques entre parenthèses et que tu dois les multiplier ensemble. Par exemple, prenons les expressions suivantes: \( (a + b) \) et \( (c + d) \). La double distributivité consiste à distribuer chaque terme de la première parenthèse avec chaque terme de la seconde parenthèse, et ensuite à additionner les résultats obtenus. <br>Dans notre exemple, voici comment on procède:<ol><li>Multiplie a par c: \( a * c = ac \)</li><li>Multiplie a par d: \( a * d = ad \)</li><li>Multiplie b par c: \( b * c = bc \)</li><li>Multiplie b par d: \( b * d = bd \)</li></ol><br>Maintenant, additionne les résultats obtenus:<br>\[ (ac) + (ad) + (bc) + (bd) \]<br>Donc, la double distributivité de \( (a + b)(c + d) \) est:<br> \[ (a + b)(c + d) = ac + ad + bc + bd \] <br> La double distributivité s'applique aussi bien pour les expressions avec des soustractions. Par exemple, si on a \( (a - b)(c - d) \), on obtient:<br>\[ (a - b)(c - d) = ac - ad - bc + bd \]<br>Ainsi lorsque tu fais une double distribution tu multiplies chaque terme de la première parenthèse avec chaque terme de la deuxième parenthèse et tu additionnes ou soustrais les différents produits obtenus.",
    "exemple":"<img src='static/images/double-distributivité.png' alt='Double Distributivité' width='450' height='180'>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "type": "question",
    "questions": "generer_double_distribution",
    "method": "aucune",
    "badge": bdg[4]
}

Addition_et_soustraction_de_polynômes = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "addition_et_soustraction_de_polynomes",
    "nom": "Addition et soustraction de polynômes",
    "body": "Lorsque l’on additionne deux polynômes on peut simplement enlever les parenthèses et ensuite réduire l’expression littérale obtenue. Lorsque l’on soustrait deux polynômes on doit inverser les signes de chaque monôme du polynôme qui suit le signe de soustraction. On enlève ensuite le signe de soustraction ainsi que les parenthèses. C'est exactement comme si il y'avait -1 devant la parenthèse et que l'on distribue ce -1 dans celle-ci",
    "exemple":"<span>$$ (3x-5)+(3-8x) $$</span><br> Comme il y a une addition entre les deux polynôme on peut directement enlever les parenthèses. Mon expression devient alors :<span>$$ 3x-5+3-8x $$</span><br> Je réduis ensuite l'expression ce qui me donne :  $$ -5x-2 $$ <br>Dans le cas ou on a une soustraction comme ici  $$ (3x+12)-(4x-16)$$ <br> On doit d'abord inverser le signe des monômes qui se trouvent dans la deuxième parenthèse ainsi \( 4x \) devient \( -4x \) et \( -16 \) devient \( +16 \). On finit par enlever le - devant la parenthèse ainsi que les parenthèses et on trouve:  $$ 3x+12-4x+16 $$  <br> Si on réduis notre expression littérale se transforme en :  $$ -x+28 $$ <p class='attention'>Attention dans le cas où on a un + devant une parenthèse qui commence par un - comme dans \( +(-5x+12) \) on peut directement retirer les parenthèse cela nous donne \( +-5x+12 \). On voit que l'on a + et - qui se suivent. On utlise alors la règle des signes: + et - donne - donc cela devient : -5x+12</p>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "type": "question",
    "questions": "generer_sous_add_poly",
    "method": "aucune",
    "badge": bdg[5]
}


Identité_remarquables = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "identite_remarquables",
    "nom": "Identité remarquables",
    "body": "Une identité remarquable est une expression mathématique qui sert de base pour faire un calcul littéral. Les identités remarquables sont utiles notamment pour résoudre une équation. En mathématiques, ces expressions algébriques permettent de simplifier les calculs en tout genre. <br> Il existe 3 identités remarquables pour les polynômes de degré 2. Vous devez connaître par coeur ses formules!",
    "exemple":"$$ (a+b)^2 = a^2+2ab+b^2 $$ $$ (a-b)^2 = a^2-2ab+b^2 $$ $$ (a+b)(a-b) = a^2 - b^2 $$",
	"body2": "En connaissant ces formules, vous pourrez rapidement effectuer certains calculs et trouver la solution d’équation du deuxième degré. Lorsqu’on passe de la formule de gauche à celle de droite, on dit que l’on développe le calcul. Si au contraire, on passe de la forme de droite à celle de gauche, on dit que l’on factorise.",
	"exemple2": "Voici un exemple de développement: <br> $$ (x+3)^2 = x^2 +6x+9$$  <br> Voici un exemple de factorisation : $$ x^2 -10 +25 = (x-5)^2$$",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire $$ x^2 $$", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "type": "question",
    "questions": "generer_identites_remarquables",
    "method": "aucune",
    "badge": bdg[6]
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
	"exemple4":"$$ x^2 -10x + 21 $$ Dans ce cas-ci on pourrait croire que l'on a une identité remarquable de la forme \( (a-b)^2 \) mais lorsqu'on essaie de factorisé on voit bien que la racine du troisième terme ne nous donne pas un nombre décimal et que lorsqu'on essait de trouver le deuxième terme 2ab cela ne fonctionne pas. Donc en est en face  d'une expression à factoriser sous la forme de : \( (a \pm b)(a \pm c)\). On prends la racine du premier terme pour obtenir notre a \( \sqrt{x^2}=x \) donc a=x. Ensuite on doit trouver deux nombres dont le produit vaut 21 et la somme vaut -10. Une chose que l'on peut faire est de trouver tous les diviseurs de 21 : \( D_{21} = {1,3,7,21} \). Maintenant il faut qu'on cherche dans ces nombres quelles sont les deux nombres dont la somme vaut -10. On a le droit d'utiliser les nombres négatifs des diviseurs. Si l'on fait ça on remarque que \(-3 +(-7) = -10\) donc b=-3 et c=-7 et notre expression factorisée vaut alors: \( (x-3)(x-7) \). <p class='attention'> Il faut bien reagrder les signes de l'expression que l'on nous donne. Par exemple : \( x^2 +5x-24 \) ici on remaruqe que le dernier terme est négatif ça veut dire que \( b\cdot c \) est négatif donc cela veut dire que b et c sont de signes opposés. Si au contraire le dernier terme est positif cela veut dire que b et c sont de même signe.</p>",
	"body5": "Il arrive que l'expression que l'on nous donne soit partiellement factorisé par exemple: $$ 3(5+x)-8(5+x) $$ On remarque ici qu'il y a deux termes. Le premier est \( 3(5+x) \) et le deuxième est \( -8(5+x) \). On peut observer qu'ils ont en commun le (5+x) c'est donc cette partie qui va être en facteur. On additionne ensuite les coeffients qui se trouvent devant les parenthèses 3 et -8 ce qui donne -5. L'expression finale sera alors -5(5+x).",
	"exemple5":"$$ -4(x^2+2) + 18(x^2+2)$$ On remarque ici qu'il y a deux termes: \( -4(x^2+2) \) et \(18(x^2+2)\). Ils ont en communs (x^2+2). On fait donc la somme des coefficients qui se trouvent devant la parenthèse: -4 et 18 ce qui nous donne 14. L'expression factorisée est donc 14(x^2+2) ",
    "type": "question",
    "questions": "generer_factorisation",
    "method": "aucune",
    "badge": bdg[7]
}

Preuve_avec_le_calcul_littéral = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "preuve_avec_le_calcul_litteral",
    "nom": "Preuve avec le calcul littéral",
    "body": "Le calcul littéral est un outil essentiel en mathématiques. Il nous permet de travailler avec des valeurs générales plutôt que des valeurs spécifiques. Dans le calcul littéral, nous utilisons des lettres pour représenter des nombres. Ces lettres sont appelées variables.<br>Un aspect clé du calcul littéral est de pouvoir exprimer des structures générales. Par exemple, tous les nombres pairs peuvent être exprimés sous la forme 2n, où n est un entier. De même, tous les nombres impairs peuvent être exprimés sous la forme 2n+1. Cela nous permet de prouver des propriétés qui sont vraies pour une infinité de cas sans avoir à les vérifier un par un, ce qui serait impossible.<br>En effet, sans le calcul littéral, nous devrions vérifier chaque cas individuellement, ce qui signifie que nous aurions à vérifier une infinité de cas pour des propriétés générales. Le calcul littéral nous permet d'éviter ce travail fastidieux et infini en nous permettant de prouver des propriétés pour tous les nombres pairs ou impairs, par exemple, en une seule fois.<br>Dans cette section, nous allons explorer comment utiliser le calcul littéral pour prouver certaines propriétés des nombres pairs et impairs.",
    "exemple":"<p>Considérons un nombre pair exprimé en calcul littéral : $$ n = 2k $$, où k est un entier.</p><p>Si nous mettons n au carré, nous obtenons :</p><span>$$ n^2 = (2k)^2 $$</span><p>Qui se simplifie en :</p><span>$$ n^2 = 4k^2 $$</span><p>C'est aussi un nombre pair, car il est divisible par 2. Cela prouve que le carré d'un nombre pair est toujours pair.</p><br><p>De même, pour un nombre impair, on peut exprimer : $$ m = 2l + 1 $$, où l est un entier.</p><p>Si nous mettons m au carré, nous obtenons :</p><span>$$ m^2 = (2l+1)^2 $$</span><p>En se développant, cela donne :</p><span>$$ m^2 = 4l^2 + 4l + 1 $$</span><p>Ce qui est également un nombre impair, car il on ne peut pas factoriser l'expression par 2 à cause du dernier terme (+1) et donc comme il n'est pas divisible par 2 il n'est pas pair donc il est impair.</p>",
    "type":"question",
    "questions": "generer_preuve_calcul_litteral",
    "method": "aucune",
    "badge": bdg[8]
}



Equation_équivalente = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "equation_equivalente",
    "nom": "Equation équivalente",
    "body": "Une équation est une proposition mathématique indiquant que deux quantités sont égales. Il est important de noter qu'une équation maintient son équilibre même si nous effectuons la même opération des deux côtés. En d'autres termes, les solutions de l'équation resteront les mêmes.<br>Quatre opérations de base peuvent être effectuées sur une équation : l'addition, la soustraction, la multiplication et la division. Chaque opération doit être effectuée de manière équilibrée, c'est-à-dire qu'elle doit être effectuée des deux côtés de l'équation.<br>Ce principe est fondamental pour résoudre les équations, car il nous permet de manipuler une équation pour isoler la variable et trouver sa valeur.",
    "exemple": "<p>Voici comment ces opérations fonctionnent avec une équation. Supposons que nous ayons l'équation :</p><span>$$ x + 3 = 7 $$</span><p>Nous pouvons soustraire 3 des deux côtés de l'équation pour isoler x :</p><span>$$ x + 3 - 3 = 7 - 3 $$</span><p>ce qui simplifie en :</p><span>$$ x = 4 $$</span><p>Maintenant, si nous avons l'équation :</p><span>$$ 2x = 8 $$</span><p>Nous pouvons diviser les deux côtés de l'équation par 2 pour isoler x :</p><span>$$ \\frac{2x}{2} = \\frac{8}{2} $$</span><p>ce qui simplifie en :</p><span>$$ x = 4 $$</span><p>De même, nous pouvons effectuer une addition ou une multiplication sur les deux côtés d'une équation pour la modifier tout en maintenant les mêmes solutions.</p>",
    "questions": "generer_equation_equivalente",
    "type":"question",
    "method": "aucune",
    "badge": bdg[9],
}

Réduction_avec_coefficients_rationnels = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "reduction_avec_coefficients_rationnels",
    "nom": "Réduction avec coefficients rationnels",
    "body": "Pour réduire un polynôme qui possède des coefficients rationnels il faut en premier lieu regrouper les termes qui ont la même partie littérale puis modifier les fractions pour qu'elles soient sous le même dénominateur. Pour cela, on trouve le multiple commun entre les dénominateur et on amplifie les fractions de telles sorte d'avoir ce multiple commun au dénominateur. On additionne ou soustrait ensuite les coefficients qui se trouve devant les même parties littérales. Pour cela, on additionne/soustrait les numérateurs de chaque fractions. On oublie pas en dernier lieu de réduire au maximum chaque fraction pour avoir seulement des fractions irréductibles.",
    "exemple":"<span>$$ \\frac{3}{4}x-\\frac{4}{5}x^{2}+\\frac{2}{7}x+3x^2 $$</span><br><p>On sépare en premier lieu notre polynôme en deux parties pour regrouper les termes qui ont la même partie littérale ce qui devient: <span>$$ \\frac{3}{4}x +\\frac{2}{7}x$$<br></span>$$ -\\frac{4}{5}x^{2}+3x^2  $$ <br><p> Je trouve en premier lieu le mutiple commun de 4 et 7 les dénominateurs devant x. Je prends 28 comme mutiple commun. J'amplifie donc les deux fractions pour avoir 28 au dénominateur. Autrement dit, je mutiplie en haut en en bas par 7 la première fraction et par 4 la deuxième et j'obtiens.</p> <br> <span>$$ \\frac{21}{28}x +\\frac{8}{28}x $$</span><br> <p> je peux maintenant additioner les deux fractions et j'obtiens: </p><br> <span>$$ \\frac{29}{28}x$$</span> <p>Je fais ensuite la même chose pour les termes qui contiennent \( x^2 \). Avant cela je dois juste transformer le coefficent 3 en fraction :  \( \\frac{3}{1} \)</p> <span>$$ -\\frac{4}{5}x^{2}+\\frac{3}{1}x^{2}$$</span><br> <p>On peut prendre 5 comme mutiple commun. On va donc simplement amplifier la deuxième fraction par 5 et on obtient : </p><br><span>$$ -\\frac{4}{5}x^{2}+\\frac{15}{5}x^{2}$$</span><p>On peut maintenant additionner les deux fractions cela nous donne</p><br> <span>$$ \\frac{11}{5}x^{2}$$</span><p> On vérifie que les deux fractions que l'on a trouvé sont irréductibles. C'est le cas ici. Notre expression finale est donc : </p><span>$$ \\frac{11}{5}x^{2} +\\frac{29}{28}x$$</span>",
    "message_aide":["Pour insérer un exposant tapper ^ exemple: x^2 veut dire \( x^2 \)", "Pour insérer une fraction écrivez / exemple 4/3 veut dire \( \\frac{4}{3} \)", "Ne pas inscrire les coefficients de 1 ou -1 par exemple inscrire x et non pas 1x"],
    "questions": "generer_reduire_une_expression_littérale_fraction",
    "type": "question",
    "method": "aucune",
    "badge": bdg[10]
}

Solution_d_une_équation_par_évaluation = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "solution_d_une_equation_par_evaluation",
    "nom": "Solution d'une équation par évaluation",
    "body": "Lorsqu'on évalue une expression littérale, on remplace la variable (souvent notée x) par une valeur numérique, puis on simplifie l'expression en effectuant les opérations arithmétiques indiquées. L'objectif final est d'obtenir une valeur numérique unique, qui représente le résultat de l'expression évaluée. Il est donc important de respecter les règles mathématiques pour garantir une réponse précise et exacte.",
    "exemple":"<span>$$ x^2-4+5x^2-12x+6-3x-x+1 $$</span><br><p>On sépare en premier lieu notre polynôme ce qui devient: <span>$$ x^2\mid -4\mid +5x^2 \mid -12x \mid +6 \mid -3x \mid -x \mid +1 $$</span><br><p> Je regroupe les \( x^2 \) ensemble les \( x \) ensemble et les monômes sans partie littérale ensemble: $$ x^2 \mid +5x^2 \mid -12x \mid -3x \mid -x \mid -4 \mid +6 \mid +1$$ <p> On peut ajouter un coefficient de 1 devient les parties littérales qui n'ont rien et de -1 devant les parties littérales qui ont juste un signe - . Notre expression devient alors: </p> $$ 1x^2 \mid +5x^2 \mid -12x \mid -3x \mid -1x \mid -4 \mid +6 \mid +1$$ <br> <p> On finit par faire la somme des coefficients pour chaque monômes possédant la même partie littérale </p>  $$ (1+5)x^2 \mid (-12-3-1)x  \mid (-4+6+1) $$ <p> On trouve finalement: </p> $$ 6x^2-16x+3 $$ <p class='attention'>Attention si deux monômes sont composés des mêmes lettres il faut aussi qu'elles aient les mêmes puissance pour chaque lettre ainsi \( xy^2 \) et \( x^2y \) n'ont pas la même partie littérale et ne peut donc pas s'additionner</p>",
    "question_id":["Evaluer_une_expression_littérale1", "Evaluer_une_expression_littérale2", "Evaluer_une_expression_littérale3"],
    "type":"qcm",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[11]
}

Résolution_d_équation_du_premier_degré_à_une_inconnue = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "resolution_d_equation_du_premier_degre_a_une_inconnue",
    "nom": "Résolution d'équation du premier degré à une inconnue",
    "body": "La résolution d'une équation du premier degré se fait en trois étapes. La première étape consiste à simplifier et réduire l'expression de chaque côté de l'équation. Cela implique d'effectuer toutes les opérations d'addition, de soustraction, de multiplication et de division nécessaires. La deuxième étape consiste à réorganiser l'équation de manière à ce que tous les termes contenant la variable (souvent notée x) soient d'un côté de l'équation, et tous les termes constants soient de l'autre. Enfin, la troisième étape consiste à isoler la variable en divisant le terme constant par le coefficient qui se trouve devant la variable. Cela donne la solution de l'équation, c'est-à-dire la valeur de la variable qui rend l'équation vraie. N'oubliez pas de noter la solution avec la bonne notation : S={...}.",
    "exemple": "<p> Considérons l'équation suivante : $$3(5 - x) = 2x + 8 - x.$$</p><p><b>Etape 1 :</b> Simplification et réduction de chaque côté de l'équation</p><p>On commence par distribuer le 3 dans le terme (5 - x) de gauche, ce qui donne : $$15 - 3x = 2x + 8 - x.$$</p><p>Ensuite, on regroupe les termes similaires de chaque côté de l'équation, ce qui donne : $$15 - 3x = x + 8.$$</p><p><b>Etape 2 :</b> Réorganisation de l'équation</p><p>On passe tous les termes en x d'un côté et tous les termes constants de l'autre côté. Cela donne : $$15 - 8 = x + 3x.$$</p><p>On simplifie encore pour obtenir : $$7 = 4x.$$</p><p><b>Etape 3 :</b> Isolation de la variable</p><p>On divise le nombre par le coefficient devant x pour obtenir : $$x = \\frac{7}{4}.$$</p><p><b>Notation de la solution</b></p><p>On note donc la solution comme suit : $$S = \\left\{\\frac{7}{4}\\right\\}.$$</p>",
    "body2": "<p>Une équation du premier degré peut ne pas avoir de solution dans certaines situations. Cela se produit lorsque nous avons une contradiction évidente après avoir simplifié et réorganisé l'équation.</p><p>Par exemple, considérons l'équation : $$2x + 3 = 2x + 5.$$</p><p>Si nous suivons les mêmes étapes de résolution que précédemment, nous finissons par obtenir $$0 = 2.$$ C'est clairement une contradiction, car 0 n'est pas égal à 2.</p><p>Dans ce cas, nous disons que l'équation n'a pas de solution, et nous notons la solution comme suit : $$S = \emptyset.$$</p>",
    "exemple2": "<p>Considérons l'équation : $$3x + 5 = 3x + 7.$$</p><p>La première étape consiste à simplifier et réduire de chaque côté de l'équation. Ici, rien ne peut être simplifié.</p><p>Ensuite, nous passons tous les termes avec x d'un côté et tous les termes constants de l'autre. Nous obtenons donc : $$3x - 3x = 7 - 5.$$</p><p>Après avoir simplifié, nous obtenons : $$0 = 2.$$ C'est une contradiction, donc l'équation n'a pas de solution.</p><p>La solution de cette équation est donc : $$S = \emptyset.$$</p>",
    "body3": "<p>Une équation du premier degré peut parfois avoir une infinité de solutions. C'est le cas lorsque, après avoir réduit et simplifié l'équation, nous obtenons une identité, c'est-à-dire une égalité qui est toujours vraie, quel que soit le choix de la variable.</p><p>Par exemple, considérons l'équation : $$2x + 3 = 2x + 3.$$</p><p>Après avoir réduit et simplifié l'équation, nous obtenons $$0 = 0.$$ Ceci est clairement une identité car cette égalité est toujours vraie, quelle que soit la valeur de x.</p><p>Dans un tel cas, nous disons que l'équation a une infinité de solutions, et nous notons la solution par $$S = \\mathbb{R}.$$</p><p>En d'autres termes, toute valeur réelle de x est une solution de l'équation.</p>",
    "exemple3": "<p>Considérons l'équation : $$4(x - 2) = 4x - 8.$$</p><p>La première étape consiste à simplifier et réduire de chaque côté de l'équation. Nous obtenons : $$4x - 8 = 4x - 8.$$</p><p>Ensuite, nous passons tous les termes avec x d'un côté et tous les termes constants de l'autre. Nous obtenons donc : $$4x - 4x = -8 + 8.$$</p><p>Après avoir simplifié, nous obtenons : $$0 = 0.$$ C'est une identité, donc l'équation a une infinité de solutions.</p><p>La solution de cette équation est donc : $$S = \mathbb{R}.$$</p>",
    "questions" : "generer_resoudre_equation_degre_1",
    "type": "question",
    "method": "aucune",
    "badge": bdg[12]
}

Poser_une_équation = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "poser_une_equation",
    "nom": "Poser une équation",
    "body": "<p>Pour poser une équation, il est nécessaire de traduire les informations données dans l'énoncé en une expression mathématique ou littérale. Cette étape implique souvent de convertir des phrases ou des idées en mathématiques à l'aide de variables.</p><p>Une fois que vous avez une expression littérale, la prochaine étape consiste à trouver une équivalence ou une égalité qui peut être posée. Cela peut souvent être trouvé en cherchant une situation dans l'énoncé où deux quantités sont définies comme étant égales ou équivalentes.</p><p>En combinant ces deux étapes, vous pouvez poser une équation qui peut être résolue pour trouver la solution à la question posée.</p>",
    "exemple": "<p><strong>Exemple:</strong> Supposons que l'énoncé du problème soit le suivant : Julien a deux fois l'âge qu'avait Claire il y a 4 ans. Si l'âge de Julien est de 24 ans, quel est l'âge de Claire ?</p><p>1. Définition de l'inconnue : On définit l'âge de Claire comme $$x$$</p><p>2. Mise sous forme littérale : Julien a deux fois l'âge qu'avait Claire il y a 4 ans. C'est donc $$2(x - 4)$$</p><p>3. Pose de l'équation : On sait que l'âge de Julien est de 24 ans, on peut donc poser l'équation suivante $$2(x - 4) = 24$$</p><p>En résolvant cette équation, on peut déterminer l'âge de Claire.</p>",
    "questions": "generer_poser_une_equation",
    "type": "question",
    "method": "method_resoudre_equation_1_degre",
    "badge": bdg[13]
}

Solution_par_voie_graphique = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "solution_par_voie_graphique",
    "nom": "Solution par voie graphique",
    "body": "Résoudre une équation en utilisant un graphique est une méthode qui peut parfois simplifier les choses. Pour cela, on peut considérer le membre de gauche de l'équation et le membre de droite comme deux fonctions distinctes. Par exemple, si l'on a une équation du type $$3x-2 = -x+4$$ On peut tracer les deux fonctions $$y = 3x-2$$ et $$y = -x+4$$ sur le même graphique. L'abscisse du ou des points d'intersection de ces deux courbes correspond à la solution de l'équation. En d'autres termes, le ou les points où les deux courbes se rencontrent sont les solutions de l'équation car à ces points, les deux fonctions ont la même valeur. C'est une approche visuelle qui peut aider à comprendre comment fonctionne la résolution d'équations.",
    "exemple": "<p>Prenons l'équation $$ x + 3 = -x + 5 $$ Ici, nous avons deux fonctions : $$f(x) = x + 3$$ et $$g(x) = -x +5$$ Si nous traçons ces deux fonctions sur un graphique, nous pourrions obtenir une image similaire à celle ci-dessous. Le point où les courbes de \(f(x) \) et \( g(x) \) se croisent est la solutions de notre équation x=1.<br><img src='static/images/graphique_equation.png' alt='Graphique montrant deux fonctions intersectant' /> </p>",
    "questions": "generer_Solution_par_voie_graphique",
    "method": "aucune",
    "type": "graphique",
    "badge": bdg[14]
}
Equation_avec_fraction = {
    "chapitres": ["_11VPcalcullitteral"],
    "nom": "Equation avec fraction",
    "name": "equation_avec_fraction",
    "body": "<p>Pour résoudre une équation qui contient des fractions, l'objectif est d'éliminer les fractions afin de simplifier l'équation. Voici les étapes à suivre :</p><p>1. <strong>Trouver le dénominateur commun</strong> : Il s'agit du plus petit nombre qui peut être divisé par tous les dénominateurs de la fraction dans l'équation. C'est également connu sous le nom de plus petit multiple commun (PPCM). Par exemple, si vos dénominateurs sont 2, 3 et 6, le PPCM serait 6.</p><p>2. <strong>Multiplier tous les termes de l'équation par le dénominateur commun</strong> : Cela permet d'éliminer les fractions de l'équation. Par exemple, si vous avez l'équation $$\\frac{1}{2} + \\frac{x}{3} = \\frac{1}{6}$$ et que vous multipliez tous les termes par 6 (le PPCM), vous obtenez $$3 + 2x = 1$$</p><p>3. <strong>Résoudre l'équation</strong> : Maintenant que l'équation n'a plus de fractions, vous pouvez la résoudre comme une équation normale. Dans l'exemple précédent, vous pouvez soustraire 3 des deux côtés pour obtenir $$2x = -2$$ puis diviser les deux côtés par 2 pour obtenir $$x = -1$$</p><p>En suivant ces étapes, vous pouvez résoudre n'importe quelle équation qui contient des fractions. Cependant, il est important de se rappeler que lors de la résolution d'équations, tout ce que vous faites d'un côté de l'équation doit être fait de l'autre côté aussi afin de maintenir l'égalité.</p>",
    "exemple": "<p>Supposons que nous avons l'équation suivante : $$\\frac{x}{2} - \\frac{3}{4} = \\frac{1}{8}$$</p> <p>1. La première étape est de <strong>trouver le dénominateur commun</strong>. Dans ce cas, le dénominateur commun de 2, 4 et 8 est 8.</p><p>2. Ensuite, nous <strong>multiplions tous les termes par le dénominateur commun</strong>, ce qui nous donne : $$4x - 6 = 1$$</p><p>3. Maintenant que nous avons une équation linéaire sans fractions, nous pouvons la résoudre normalement. Ajoutons 6 des deux côtés de l'équation pour isoler le terme avec x : $$4x = 7$$</p><p>4. Enfin, divisons les deux côtés de l'équation par 4 pour obtenir la solution : $$x = \\frac{7}{4}$$</p><p>Donc, la solution de l'équation $$\\frac{x}{2} - \\frac{3}{4} = \\frac{1}{8}$$ est $$x = \\frac{7}{4}$$</p>",
    "questions": "generer_equation_avec_fraction",
    "method": "aucune",
    "type": "question",
    "badge": bdg[15]
}
Equation_du_deuxième_degré = {
    "chapitres": ["_11VPcalcullitteral"],
    "name": "equation_du_deuxieme_degre",
    "nom": "Equation du deuxième degré",
    'body': "<p>La résolution d'une équation du second degré, c'est-à-dire une équation de la forme $$ax^2 + bx + c = 0$$ passe par plusieurs étapes.</p><p>La première étape consiste à rassembler tous les termes de l'équation d'un même côté pour obtenir une expression de la forme : $$ ax^2 + bx + c = 0 $$</p><p>Ensuite, il faut chercher à factoriser l'expression obtenue. Pour cela, on peut chercher si l'expression correspond à une identité remarquable par exemple:  \( (x+b)^2 = x^2 + 2xb + b^2 \) ou \( (x-b)^2 = x^2 - 2xb + b^2 \) ou \( (x+b)(x-b) = x^2 - b^2 \)  qui permettrait de simplifier la résolution. Ensuite il suffit de trouver le ou les \( x \) qui permet/permettent de faire en sorte qu'une parenthèse soit égal à 0</p>",
    "exemple":"<p>Voici deux exemples de résolution d'équations du second degré avec utilisation d'identités remarquables.</p><p><strong>Exemple 1:</strong> Soit l'équation \( x^2 - 64 = 0\). On reconnaît une différence de deux carrés, donc on peut factoriser l'expression: $$x^2 - 64 = (x - 8)(x + 8) = 0$$ L'équation est alors équivalente à deux équations du premier degré: $$x - 8 = 0$$ et $$x + 8 = 0$$ Les solutions sont donc : </p><p> $$ x = 8 $$ et $$ x = -8 $$</p><p><strong>Exemple 2:</strong> Soit l'équation \( x^2 - 6x + 9 = 0\). On reconnaît un carré parfait, donc on peut factoriser l'expression: $$x^2 - 6x + 9 = (x - 3)^2 = 0$$ L'équation est alors équivalente à une équation du premier degré: $$x - 3 = 0$$ La solution est donc \( x = 3 \).</p>",
    'body2':"<p>Dans certaines équations du second degré, on peut reconnaître une expression de la forme $$ax^2 + bx + c$$ qui peut se factoriser en $$(x+\\alpha)(x+\\beta)$$</p><p>Pour cela, on cherche deux nombres  \( \\alpha \) et \( \\beta \) tels que le produit $$\\alpha * \\beta$$ soit égal au terme constant 'c' de l'équation, et que la somme $$\\alpha+\\beta$$ soit égal au coefficient du terme de degré 1, 'b'.</p><p>Si on trouve de tels nombres \( \\alpha \) et \( \\beta \), alors l'équation $$ax^2 + bx + c = 0$$ peut se factoriser en $$(x+\\alpha)(x+\\beta) = 0$$ L'équation du second degré est alors réduite à deux équations du premier degré : $$x+\\alpha = 0$$ et $$x+\\beta = 0$$ On peut ainsi trouver les solutions de l'équation du second degré.</p>",
    "exemple2": "<p>Considérons l'équation: $$x^2 - x - 6 = 0$$ Pour la factoriser, nous devons chercher deux nombres \( \\alpha \) et \( \\beta \) tels que le produit : $$ \\alpha * \\beta$$ soit égal à -6 (le terme constant de l'équation) et que la somme:  $$ \\alpha + \\beta$$ soit égale à -1 (le coefficient du terme en 'x').</p><p>Les diviseurs de 6 sont 1, 2, 3 et 6. Comme le produit doit être négatif, un des nombres doit être négatif. Si nous testons les différentes combinaisons, nous constatons que les nombres -3 et 2 satisfont les deux conditions : $$-3 * 2 = -6$$ et $$-3 + 2 = -1$$ </p><p>Donc, nous pouvons factoriser l'équation $$x^2 - x - 6$$ en $$(x - 3)(x + 2)$$ Les solutions de l'équation sont alors les valeurs de 'x' qui annulent chacune des parenthèses. On a donc : $$x - 3 = 0$$ soit $$x = 3$$ et $$x + 2 = 0$$ soit $$x = -2$$ Les solutions de l'équation :  $$x^2 - x - 6 = 0$$ sont donc : $$x = 3$$ et $$x = -2$$</p>",
    "body3":"Quand une équation du second degré n'est pas facilement factorisable, nous pouvons utiliser la méthode du discriminant, grâce à la formule de Viète. Dans l'équation générale $$ax^2 + bx + c = 0$$ le discriminant est donné par $$\\Delta = b^2 - 4ac$$ En fonction du signe de $$\\Delta$$ nous avons différentes solutions pour l'équation : Si $$\\Delta > 0$$ l'équation a deux solutions réelles distinctes données par $$x_{1,2} = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}$$ Si $$\\Delta = 0$$ l'équation a une unique solution réelle donnée par $$x = \\frac{-b}{2a}$$ Si $$\\Delta < 0$$ l'équation n'a pas de solution réelle. Ces formules sont connues sous le nom de formules de Viète. Elles permettent de trouver les solutions d'une équation du second degré quelle que soit sa forme.",
    "exemple3": "Considérons l'équation $$2x^2 - 3x - 2 = 0$$ Pour résoudre cette équation à l'aide de la formule de Viète, nous devons d'abord calculer le discriminant. Dans notre cas, $$a = 2$$ $$b = -3$$ $$c = -2$$ Nous insérons ces valeurs dans la formule du discriminant pour obtenir : $$\\Delta = (-3)^2 - 4*2*(-2) = 9 + 16 = 25$$ Comme $$\\Delta > 0$$ l'équation a deux solutions réelles distinctes. Nous pouvons donc utiliser la formule de Viète pour les trouver : $$x_{1,2} = \\frac{-(-3) \\pm \\sqrt{25}}{2*2} = \\frac{3 \\pm 5}{4}$$ Ainsi, les solutions de l'équation sont $$x_1 = \\frac{3+5}{4} = 2$$ et $$x_2 = \\frac{3-5}{4} = -0.5$$",
    "type":"question",
    "questions": "generer_resoudre_equation_degre_2",
    "method": "aucune",
    "badge": bdg[16]
}


###

Différents_type_de_fonctions = {
    "chapitres": ["_11VPsystemes"],
    "name": "differents_type_de_fonctions",
    "nom": "Différents type de fonctions",
    "body": "",
    "exemple":"",
    "type":"graphique",
    "questions": "generer_reconnaissance_fonction",
    "method": "aucune",
    "badge": bdg[17]
}


Trouver_l_expression_fonctionnelle_à_partir_d_un_tableau_de_valeur_premier_degré = {
    "chapitres": ["_11VPsystemes"],
    "name": "trouver_l_expression_fonctionnelle_à_partir_d_un_tableau_de_valeur_premier_degré",
    "nom": "Trouver l'expression fonctionnelle à partir d'un tableau de valeur premier degré",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[18]
}

Trouver_l_expression_fonctionnelle_à_partir_d_un_tableau_de_valeur_2ème_degré = {
    "chapitres": ["_11VPsystemes"],
    "name": "trouver_l_expression_fonctionnelle_à_partir_d_un_tableau_de_valeur_deuxième_degré",
    "nom": "Trouver l'expression fonctionnelle à partir d'un tableau de valeur deuxième degré",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[19]
}

Trouver_l_expression_fonctionnelle_à_partir_d_un_graphique_premier_degré = {
    "chapitres": ["_11VPsystemes"],
    "name": "trouver_l_expression_fonctionnelle_a_partir_d_un_graphique_premier_degre",
    "nom": "Trouver l'expression fonctionnelle à partir d'un graphique premier degré",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[20]
}
Dessiner_le_graphe_d_une_fonction_du_premier_degré = {
    "chapitres": ["_11VPsystemes"],
    "name": "dessiner_le_graphe_d_une_fonction_du_premier_degre",
    "nom": "Dessiner le graphe d'une fonction du premier degré",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[21]
}

Trouver_la_préimage = {
   "chapitres": ["_11VPsystemes"],
    "name": "trouver_la_preimage",
    "nom": "Trouver la pré-image",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[22]
}

Trouver_le_domaine_de_définition = {
    "chapitres": ["_11VPsystemes"],
    "name": "trouver_le_domaine_de_definition",
    "nom": "Trouver le domaine de définition",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[23]
}

Echelle = {
    "chapitres": ["_11VPsystemes"],
    "name": "echelle",
    "nom": "Echelle",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[24]

}

Pourcentage = {
    "chapitres": ["_11VPsystemes"],
    "name": "pourcentage",
    "nom": "Pourcentage",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[25]
}
Pente = {
    "chapitres": ["_11VPsystemes"],
    "name": "pente",
    "nom": "Pente",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[26]
}

Débit = {
    "chapitres": ["_11VPsystemes"],
    "name": "debit",
    "nom": "Débit",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[27]

}

Masse_volumique = {
    "chapitres": ["_11VPsystemes"],
    "name": "masse_volumique",
    "nom": "Masse volumique",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[28]


}

Substitution = {
    "chapitres": ["_11VPsystemes"],
    "name": "substitution",
    "nom": "Substitution",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[29]
}

Combinaison_linéaire = {
    "chapitres": ["_11VPsystemes"],
    "name": "combinaison_lineaire",
    "nom": "Combinaison linéaire",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[30]
}

Absence_de_solution_infinité_de_solution_et_1_solution = {
    "chapitres": ["_11VPsystemes"],
    "name": "absence_de_solution_infinite_de_solutions_et_1_solution",
    "nom": "Absence de solution, infinité de solutions et unique solution",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[31]
}

Proportionnalité = {
    "chapitres": ["_11VPsystemes"],
    "name": "proportionnalite",
    "nom": "Proportionnalité",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[32]
}

Diagramme = {
    "chapitres": ["_11VPsystemes"],
    "name": "diagramme",
    "nom": "Diagramme",
    "body": "",
    "exemple":"",
    "type":"question",
    "questions": "generer_trouver_par_evaluation",
    "method": "aucune",
    "badge": bdg[33]
}

