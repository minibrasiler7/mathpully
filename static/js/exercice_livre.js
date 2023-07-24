function allowDrop(ev) {
    ev.preventDefault();
}
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    ev.dataTransfer.setData("part", ev.target.dataset.part); // get part from data-part attribute
}
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var part = ev.dataTransfer.getData("part");
    if(part == ev.target.dataset.part) { // check if part matches dropzone's part
        ev.target.appendChild(document.getElementById(data));
    }
}
$(document).ready(function(){

    $('.element_draggable').on('dragstart', function(event) {
        drag(event.originalEvent);
    });

    $('.dropzone').on('dragover', function(event) {
        allowDrop(event.originalEvent);
    });

    $('.dropzone').on('drop', function(event) {
        drop(event.originalEvent);
    });

         console.log($(".exercise-form").data("donnee").replaceAll("'", '"').replaceAll('c"e', "c'e").replaceAll('d"e', "d'e").replaceAll('t"e', "t'e").replaceAll('l"e', "l'e").replaceAll('l"a',"l'a").replaceAll('l"i',"l'i").replaceAll('C"e',"C'e").replaceAll('d"u',"d'u").replaceAll('l"é',"l'é").replaceAll('l"o',"l'o").replaceAll('l"â', "l'â").replaceAll('S"i', "S'i").replaceAll('d"a', "d'a").replaceAll('u"i', "u'i").replaceAll('u"e', "u'e").replaceAll('N"o', "N'o").replaceAll('L"a', "L'a").replaceAll('d"é', "d'é").replaceAll('n"a', "n'a").replaceAll('l"ê', "l'ê").replaceAll('n"i', "n'i").replaceAll('n"o', "n'o").replaceAll('n"e', "n'e").replaceAll('u"o', "u'o").replaceAll('d"i', "d'i").replaceAll('d"o', "d'o"));
         let exercice = JSON.parse($(".exercise-form").data("donnee").replaceAll("'", '"').replaceAll('c"e', "c'e").replaceAll('d"e', "d'e").replaceAll('t"e', "t'e").replaceAll('l"e', "l'e").replaceAll('l"a',"l'a").replaceAll('l"i',"l'i").replaceAll('C"e',"C'e").replaceAll('d"u',"d'u").replaceAll('l"é',"l'é").replaceAll('l"o',"l'o").replaceAll('l"â', "l'â").replaceAll('S"i', "S'i").replaceAll('d"a', "d'a").replaceAll('u"i', "u'i").replaceAll('u"e', "u'e").replaceAll('N"o', "N'o").replaceAll('L"a', "L'a").replaceAll('d"é', "d'é").replaceAll('n"a', "n'a").replaceAll('l"ê', "l'ê").replaceAll('n"i', "n'i").replaceAll('n"o', "n'o").replaceAll('n"e', "n'e").replaceAll('u"o', "u'o").replaceAll('d"i', "d'i").replaceAll('d"o', "d'o"));
         let image = exercice.image;

         $('#background').css('background-image', 'url(/static/images/' + image + ')');
         $('#submit').click(function(e){
         let allCorrect = true;
         if (!("type" in exercice)){
            e.preventDefault(); // to prevent form submission
            let answers = exercice.reponses;
            let questionIndex = 0;
            let answerIndex = 0;
            $('input[id^="response"]').each(function(i, el){
                let userAnswer = $(el).val();
                let correctAnswers = answers[questionIndex][answerIndex];
                if(correctAnswers.includes(userAnswer)){
                $(el).animate({
                    'backgroundColor': 'rgb(100, 205, 180)'
                }, 1000); // Transition over 1 second (1000 ms)
            }else{
                $(el).animate({
                    'backgroundColor': 'rgb(255, 105, 180)' // Rosy red
                }, 1000);
                allCorrect = false;
            }
             answerIndex++;
            if(answerIndex >= answers[questionIndex].length){
                 answerIndex = 0;
                questionIndex++;
            }
            });
         }
         else if (exercice.type == "glisser-déposer") {
         e.preventDefault(); // to prevent form submission
    // Créez un tableau pour contenir toutes les réponses
    let allAnswers = [];
    // Parcourez chaque dropzone
    $(".dropzone").each(function() {
         let allCorrect = true;
        // Créez un tableau pour contenir les réponses de cette dropzone
        let dropzoneAnswers = [];
        // Parcourez chaque élément draggable dans cette dropzone
        $(this).find(".element_draggable").each(function() {
            // Ajoutez le texte de l'élément à la liste des réponses de cette dropzone
            dropzoneAnswers.push($(this).text());
        });
        // Ajoutez les réponses de cette dropzone à la liste de toutes les réponses
        allAnswers.push(dropzoneAnswers);
    });

    console.log(allAnswers);
    allAnswers = allAnswers.map(answerSet =>
    answerSet.map(answer => answer.replace(/\n/g, "").trim())
);
    console.log("allAnswers"+allAnswers);
    // Aplatir les réponses
    let correctAnswersFlat = exercice.reponses.flat(1);
    console.log(correctAnswersFlat);
    // Parcourez chaque set de réponses dans allAnswers
    for (let i = 0; i < allAnswers.length; i++) {
  let dropzone = allAnswers[i];
  let isCorrect = false;
  // Pour chaque sous-liste dans correctAnswersFlat
  for (let j = 0; j < correctAnswersFlat.length; j++) {
    let correctAnswer = correctAnswersFlat[j];

    // Vérifier si la dropzone contient tous les éléments de correctAnswer
    if (correctAnswer.every(val => dropzone.includes(val))) {
      isCorrect = true;
      break;
    }
  }
  if (isCorrect) {
    // La dropzone est correcte, la rendre verte
    $(`.dropzone:eq(${i})`).css('background-color', 'rgb(100, 205, 180)');
  } else {
    // La dropzone est incorrecte, la rendre rouge
    allCorrect = false;
    $(`.dropzone:eq(${i})`).css('background-color', 'rgb(255, 105, 180)');
  }
}
    }
    console.log("All correct: "+allCorrect)
    if(allCorrect){
    $.ajax({
        url: '/exercice_termine',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({titre: exercice.titre, classe: exercice.annee}),
        success: function(response) {
            if(response.success) {
                $('#submit').animate({
                    backgroundColor: 'rgb(100, 205, 180)',
                    color: '#000000'
                }, 1000);
                $('#submit').val("Bravo vous avez réussi l'exercice vous gagner 50 pts!");
                // Met à jour le nombre de points de l'utilisateur dans la balise HTML
                const pointsUtilisateurNav = document.getElementById('points_utilisateurs_nav');
                pointsUtilisateurNav.textContent = `${response.points} points`;
            } else {
                $('#submit').val(response.message);
            }
        }
    });
}
            });
        });

