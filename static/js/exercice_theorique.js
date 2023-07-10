document.addEventListener('DOMContentLoaded', function () {
const pointsUtilisateurNav = document.getElementById('points_utilisateurs_nav');
var image_badge = document.querySelector('.badge_image');
const radio = document.querySelector('input[type=radio][name="qcm-options"]');

  if (radio !== null) {
    console.log(radio.checked);
  } else {
    console.log("L'élément n'a pas été trouvé");
  }


class Exercices {
  constructor(questions, donnee_problem_html, input_html, feedback_html, score_html, valider_html, progress_html, name, image_badge, method) {
    this.questions = questions;
    this.image_badge = image_badge;
    this.index_question = 0;
    this.currentQuestion = this.questions[this.index_question];
    this.donnee_problem_html = donnee_problem_html;
    this.input_html = input_html;
    this.feedback_html = feedback_html;
    this.score_html = score_html;
    this.valider_html = valider_html;
    this.progress_html = progress_html;
    this.name = name;
    this.method = method;
    this.valider_html.addEventListener('click', () => this.checkAnswer());
    this.input_html.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        this.checkAnswer();
    }
});
  }
  showQuestion() {
      this.donnee_problem_html.innerHTML = this.currentQuestion.question;
      this.input_html.value = "";
      this.feedback_html.textContent = "";
      this.score_html.textContent = `Score : ${this.index_question * 10}`;
      this.updateMathJax();
  }

  toggleReussiteClass() {
  this.image_badge.classList.add('reussite');
}

  completeExercise(exerciseName) {
    fetch('/update_exercise', {
    method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'exercise_name': exerciseName,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Exercise updated successfully") {
            console.log('Success:', data);
        } else {
            console.error('Error:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    }

  transforme_fraction_to_latex(userAnswer){
    const fractionRegex = /\((\d+)\/(\d+)\)/g;
    return userAnswer.replace(fractionRegex, '\\frac{$1}{$2}');
  }
  transforme_puissance_to_latex(userAnswer){
    const regex = /\^([2-9])/g;
    // Remplace chaque occurrence de la regex par l'expression LaTeX correspondante
    const resultat = userAnswer.replace(regex, "^{$1}");
    return resultat;
  }
  enlever_espace(userAnswer){
    userAnswer = userAnswer.replace(/\s/g, "")
    return userAnswer
  }
 checkAnswer = async function(){

      var userAnswer =  this.input_html.value.toLowerCase();
      console.log(userAnswer)
      // Initialiser la requête AJAX
      if (this.method !== 'aucune') {
        let response = await fetch('/methodpython', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: `method=${encodeURIComponent(this.method)}&userAnswer=${encodeURIComponent(userAnswer)}`

        });

        if (response.status === 200) {
          let data = await response.json();
          console.log("Donnée recu : "+data)
          userAnswer = data['value'];


        } else {
          alert('Request failed.  Returned status of ' + response.status);
        }
      }


      if (this.currentQuestion.methods.length !== 0){

      for (let i = 0; i < this.currentQuestion.methods.length; i++) {
        if(this.currentQuestion.methods[i] == "enlever_espace"){
            userAnswer = this.enlever_espace(userAnswer)
        }
        if(this.currentQuestion.methods[i] == "transforme_fraction_to_latex"){
            userAnswer = this.transforme_fraction_to_latex(userAnswer)

        }
        if(this.currentQuestion.methods[i] == "transforme_puissance_to_latex"){
            userAnswer = this.transforme_puissance_to_latex(userAnswer)
        }

      }}
      const correctAnswer = this.currentQuestion.answer;
      console.log("la réponse correct est "+correctAnswer)
      console.log("la nouvelle réponse de l'utilisateur est "+ userAnswer)

      if (correctAnswer.includes(userAnswer)) {
        this.feedback_html.textContent = this.currentQuestion.feedback;
        this.feedback_html.classList.add(this.currentQuestion.feedbackClass);
        this.index_question++;
        this.updateScore();
        this.upScore();
        this.currentQuestion = this.questions[this.index_question];

        if (this.index_question === 4) {
          this.donnee_problem_html.textContent = "Vous avez terminé toutes les questions !";
          this.input_html.style.display = "none";
          this.valider_html.style.display = "none";
          this.completeExercise(this.name);
          this.toggleReussiteClass();
           this.score_html.textContent = `Score : ${this.index_question * 10}`;

        } else {
          this.showQuestion();
        }
      } else {
        this.feedback_html.textContent = "Dommage, ce n'est pas la bonne réponse. Veuillez réessayer";
        this.feedback_html.classList.add("text-danger");
        setTimeout(() => {this.feedback_html.textContent = ""; this.feedback_html.classList.remove("text-danger");}, 1000);
      }
  }
  updateScore(){

      var width = parseInt(this.progress_html.style.width) || 0;
      width += 25;
      this.progress_html.style.width = width + '%';
      this.progress_html.setAttribute('aria-valuenow', width);
  }
  upScore() {
  fetch('/update_score', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      score: 10
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log('Score updated:', data);
    const pointsUtilisateursNav = document.getElementById('points_utilisateurs_nav');
    // Met à jour le nombre de points de l'utilisateur dans la balise HTML
    const currentScore = parseInt(pointsUtilisateurNav.textContent, 10);
    pointsUtilisateurNav.textContent = `${currentScore + 10} points`;
    pointsUtilisateursNav.classList.add('blink-green');

      // Supprimez la classe 'blink-green' une fois l'animation terminée.
      setTimeout(() => {
        pointsUtilisateursNav.classList.remove('blink-green');
      }, 1500); // La durée totale de l'animation est de 0.5s * 3 = 1.5s (1500ms).
    })
  .catch((error) => {
    console.error('Error updating score:', error);
  });
}

  updateMathJax() {
  if (window.MathJax) {
    MathJax.typesetPromise();
  }
}
}
class QCMExercices {
  constructor(questions, donnee_problem_html, feedback_html, score_html, valider_html, progress_html, name, image_badge, labelRadio, boutonRadio, quizzForm, method) {
    this.questions = questions;
    this.image_badge = image_badge;
    this.index_question = 0;
    this.faute = 0;
    this.method = method;
    this.currentQuestion = this.questions[this.index_question];
    this.donnee_problem_html = donnee_problem_html;
    this.feedback_html = feedback_html;
    this.score_html = score_html;
    this.valider_html = valider_html;
    this.progress_html = progress_html;
    this.name = name;
    this.labelRadio = labelRadio;
    this.boutonRadio = boutonRadio;
    this.quizzForm = quizzForm;
    this.quizzForm.addEventListener('submit', (e) => {
    e.preventDefault();  // Empêche l'envoi du formulaire.
    this.checkAnswer();
    });
      }

  showQuestion() {


       for (var i = 0; i < this.labelRadio.length; i++) {
        var span = this.labelRadio[i].querySelector('.label-text');
            if (span) {
            span.textContent = this.currentQuestion.answer_user[i];
        }
      }
      this.donnee_problem_html.innerHTML = this.currentQuestion.question;
      this.feedback_html.textContent = "";
      this.score_html.textContent = `Score : ${this.index_question * 10 - this.faute *10}`;
      this.updateMathJax();
  }

  toggleReussiteClass() {
  this.image_badge.classList.add('reussite');
}
  completeExercise(exerciseName) {
    fetch('/update_exercise', {
    method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'exercise_name': exerciseName,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Exercise updated successfully") {
            console.log('Success:', data);
        } else {
            console.error('Error:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    }

  checkAnswer(){
      var selectedLabel;
    // Parcourir chaque bouton radio pour trouver celui qui est sélectionné
        for (var i = 0; i < this.boutonRadio.length; i++) {
        if (this.boutonRadio[i].checked) {
            // Si le bouton radio est sélectionné, stocker le label associé dans la variable
            selectedLabel = this.boutonRadio[i].parentNode.querySelector('.label-text').textContent;
            console.log(selectedLabel)
            break;
            }
        }
    const correctAnswer = this.currentQuestion.answer;
      if (correctAnswer === selectedLabel) {
        this.feedback_html.textContent = this.currentQuestion.feedback;
        this.feedback_html.classList.add(this.currentQuestion.feedbackClass);
        this.index_question++;
        this.updateScore();
        this.upScore(10);
        this.currentQuestion = this.questions[this.index_question];

        if (this.index_question === 4) {
          this.donnee_problem_html.textContent = "Vous avez terminé toutes les questions !";
          this.valider_html.style.display = "none";
          this.completeExercise(this.name);
          this.toggleReussiteClass();
          this.score_html.textContent = `Score : ${this.index_question * 10 - this.faute *10}`;

        } else {
          this.showQuestion();
        }
      } else {
        this.feedback_html.textContent = "Dommage, ce n'est pas la bonne réponse. Veuillez réessayer";
        this.faute = this.faute + 1;
        this.upScore(-10);
        this.showQuestion();
        this.feedback_html.classList.add("text-danger");
        setTimeout(() => {this.feedback_html.textContent = ""; this.feedback_html.classList.remove("text-danger");}, 1000);
      }
  }
  updateScore(){
      var width = parseInt(this.progress_html.style.width) || 0;
      width += 25;
      this.progress_html.style.width = width + '%';
      this.progress_html.setAttribute('aria-valuenow', width);
  }
  upScore(up) {
  fetch('/update_score', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      score: up
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log('Score updated:', data);
    const pointsUtilisateursNav = document.getElementById('points_utilisateurs_nav');
    // Met à jour le nombre de points de l'utilisateur dans la balise HTML
    const currentScore = parseInt(pointsUtilisateurNav.textContent, 10);

    pointsUtilisateurNav.textContent = `${currentScore + up} points`;
    pointsUtilisateursNav.classList.add('blink-green');

      // Supprimez la classe 'blink-green' une fois l'animation terminée.
      setTimeout(() => {
        pointsUtilisateursNav.classList.remove('blink-green');
      }, 1500); // La durée totale de l'animation est de 0.5s * 3 = 1.5s (1500ms).
    })
  .catch((error) => {
    console.error('Error updating score:', error);
  });
}

  updateMathJax() {
  if (window.MathJax) {
    MathJax.typesetPromise();
  }
}
}
class GraphiqueExercice {
  constructor(questions, donnee_problem_html, input_html, feedback_html, score_html, valider_html, progress_html, name, image_badge, method, donnee_graphique) {
    this.donnee_graphique = donnee_graphique;
    this.questions = questions;
    this.image_badge = image_badge;
    this.index_question = 0;
    this.currentQuestion = this.questions[this.index_question];
    this.donnee_problem_html = donnee_problem_html;
    this.input_html = input_html;
    this.feedback_html = feedback_html;
    this.score_html = score_html;
    this.valider_html = valider_html;
    this.progress_html = progress_html;
    this.name = name;
    this.method = method;
    this.valider_html.addEventListener('click', () => this.checkAnswer());
    this.input_html.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        this.checkAnswer();
    }
});
  }
  showQuestion() {
      this.donnee_problem_html.innerHTML = this.currentQuestion.question;
      // Supposons que vos coefficients sont a, b et c.
     let a = 1; // coefficient a
     let b = 2; // coefficient b
     let c = 1; // coefficient c pour les fonctions du deuxième degré

        // Générer une gamme de valeurs x
        let xValues = [];
        for (let x=-10; x<=10; x+=0.1) {
        xValues.push(x);
       }

    // Calculer les valeurs y pour chaque valeur x pour la fonction du premier degré (y = ax + b)
    let yValues1 = xValues.map(x => a*x + b);

    // Calculer les valeurs y pour chaque valeur x pour la fonction du deuxième degré (y = ax^2 + bx + c)
    let yValues2 = xValues.map(x => a*Math.pow(x, 2) + b*x + c);

    let trace1 = {
     x: xValues,
     y: yValues1,
     mode: 'lines',

    };

    let trace2 = {
    x: xValues,
    y: yValues2,
    mode: 'lines',

    };

    let data = [trace1, trace2];

    Plotly.newPlot(this.donnee_graphique, data);
      this.input_html.value = "";
      this.feedback_html.textContent = "";
      this.score_html.textContent = `Score : ${this.index_question * 10}`;
      this.updateMathJax();
  }

  toggleReussiteClass() {
  this.image_badge.classList.add('reussite');
}

  completeExercise(exerciseName) {
    fetch('/update_exercise', {
    method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'exercise_name': exerciseName,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Exercise updated successfully") {
            console.log('Success:', data);
        } else {
            console.error('Error:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    }

  transforme_fraction_to_latex(userAnswer){
    const fractionRegex = /\((\d+)\/(\d+)\)/g;
    return userAnswer.replace(fractionRegex, '\\frac{$1}{$2}');
  }
  transforme_puissance_to_latex(userAnswer){
    const regex = /\^([2-9])/g;
    // Remplace chaque occurrence de la regex par l'expression LaTeX correspondante
    const resultat = userAnswer.replace(regex, "^{$1}");
    return resultat;
  }
  enlever_espace(userAnswer){
    userAnswer = userAnswer.replace(/\s/g, "")
    return userAnswer
  }
 checkAnswer = async function(){

      var userAnswer =  this.input_html.value.toLowerCase();
      console.log(userAnswer)
      // Initialiser la requête AJAX
      if (this.method !== 'aucune') {
        let response = await fetch('/methodpython', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: `method=${encodeURIComponent(this.method)}&userAnswer=${encodeURIComponent(userAnswer)}`

        });

        if (response.status === 200) {
          let data = await response.json();
          console.log("Donnée recu : "+data)
          userAnswer = data['value'];


        } else {
          alert('Request failed.  Returned status of ' + response.status);
        }
      }


      if (this.currentQuestion.methods.length !== 0){

      for (let i = 0; i < this.currentQuestion.methods.length; i++) {
        if(this.currentQuestion.methods[i] == "enlever_espace"){
            userAnswer = this.enlever_espace(userAnswer)
        }
        if(this.currentQuestion.methods[i] == "transforme_fraction_to_latex"){
            userAnswer = this.transforme_fraction_to_latex(userAnswer)

        }
        if(this.currentQuestion.methods[i] == "transforme_puissance_to_latex"){
            userAnswer = this.transforme_puissance_to_latex(userAnswer)
        }

      }}
      const correctAnswer = this.currentQuestion.answer;
      console.log("la réponse correct est "+correctAnswer)
      console.log("la nouvelle réponse de l'utilisateur est "+ userAnswer)

      if (correctAnswer.includes(userAnswer)) {
        this.feedback_html.textContent = this.currentQuestion.feedback;
        this.feedback_html.classList.add(this.currentQuestion.feedbackClass);
        this.index_question++;
        this.updateScore();
        this.upScore();
        this.currentQuestion = this.questions[this.index_question];

        if (this.index_question === 4) {
          this.donnee_problem_html.textContent = "Vous avez terminé toutes les questions !";
          this.input_html.style.display = "none";
          this.valider_html.style.display = "none";
          this.completeExercise(this.name);
          this.toggleReussiteClass();
           this.score_html.textContent = `Score : ${this.index_question * 10}`;

        } else {
          this.showQuestion();
        }
      } else {
        this.feedback_html.textContent = "Dommage, ce n'est pas la bonne réponse. Veuillez réessayer";
        this.feedback_html.classList.add("text-danger");
        setTimeout(() => {this.feedback_html.textContent = ""; this.feedback_html.classList.remove("text-danger");}, 1000);
      }
  }
  updateScore(){

      var width = parseInt(this.progress_html.style.width) || 0;
      width += 25;
      this.progress_html.style.width = width + '%';
      this.progress_html.setAttribute('aria-valuenow', width);
  }
  upScore() {
  fetch('/update_score', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      score: 10
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log('Score updated:', data);
    const pointsUtilisateursNav = document.getElementById('points_utilisateurs_nav');
    // Met à jour le nombre de points de l'utilisateur dans la balise HTML
    const currentScore = parseInt(pointsUtilisateurNav.textContent, 10);
    pointsUtilisateurNav.textContent = `${currentScore + 10} points`;
    pointsUtilisateursNav.classList.add('blink-green');

      // Supprimez la classe 'blink-green' une fois l'animation terminée.
      setTimeout(() => {
        pointsUtilisateursNav.classList.remove('blink-green');
      }, 1500); // La durée totale de l'animation est de 0.5s * 3 = 1.5s (1500ms).
    })
  .catch((error) => {
    console.error('Error updating score:', error);
  });
}

  updateMathJax() {
  if (window.MathJax) {
    MathJax.typesetPromise();
  }
}
}
function selectionSansRemise(tableau) {
    questions = []
    for (i=0; i<4; i++) {
      let index = Math.floor(Math.random() * tableau.length);
      let element = tableau.splice(index, 1)[0];
      questions.push(element);
    }
    return questions
    }


  list_objet = [];
  const exercicesInteractifs = document.querySelectorAll('.exercice-interactif');
  exercicesInteractifs.forEach((exerciceInteractif) => {
    console.log(exerciceInteractif.dataset.questions.replaceAll("'", '"').replaceAll('c"e', "c'e").replaceAll('d"e', "d'e").replaceAll('t"e', "t'e").replaceAll('l"e', "l'e").replaceAll('l"a',"l'a").replaceAll('l"i',"l'i").replaceAll('C"e',"C'e").replaceAll('d"u',"d'u").replaceAll('l"é',"l'é").replaceAll('l"â', "l'â").replaceAll('d"a', "d'a"));
    const questions = JSON.parse(exerciceInteractif.dataset.questions.replaceAll("'", '"').replaceAll('c"e', "c'e").replaceAll('d"e', "d'e").replaceAll('t"e', "t'e").replaceAll('l"e', "l'e").replaceAll('l"a',"l'a").replaceAll('l"i',"l'i").replaceAll('C"e',"C'e").replaceAll('d"u',"d'u").replaceAll('l"é',"l'é").replaceAll('l"o',"l'o").replaceAll('l"â', "l'â").replaceAll('S"i', "S'i").replaceAll('d"a', "d'a").replaceAll('u"i', "u'i").replaceAll('u"e', "u'e"));
    const name = exerciceInteractif.dataset.name;
    const type = exerciceInteractif.dataset.type;
    const method = exerciceInteractif.dataset.method;
    console.log(method)
    const questionText = exerciceInteractif.querySelector('.question-text');
    const image_badge = exerciceInteractif.querySelector('.badge_image');
    const feedbackText = exerciceInteractif.querySelector('.feedback-text');
    const scoreText = exerciceInteractif.querySelector('.score-text');
    const valider = exerciceInteractif.querySelector('.valider');
    const progressbar = exerciceInteractif.querySelector('.progress-bar');
    choose_question = selectionSansRemise(questions);


    if (type === 'question') {
        const answerInput = exerciceInteractif.querySelector('.answer-input');
        var exercice = new Exercices(choose_question, questionText, answerInput, feedbackText, scoreText, valider, progressbar, name, image_badge, method);
    }
    else if (type === 'qcm') {
        const quizzForm = exerciceInteractif.querySelector('.quizForm');
        const labels = exerciceInteractif.querySelectorAll('label.qcm-option');
        const boutonRadio = [];

// Parcourez les étiquettes pour récupérer les boutons radio associés
       labels.forEach((label) => {
       const input = label.querySelector('.qcm-radios');
       boutonRadio.push(input);
       });
        var exercice = new QCMExercices(choose_question, questionText, feedbackText, scoreText, valider, progressbar, name, image_badge, labels, boutonRadio, quizzForm);
        console.log(exercice);

  }
    else if(type === "graphique"){
        const answerInput = exerciceInteractif.querySelector('.answer-input');
        const graphique = exerciceInteractif.querySelector('.question-graphique');
        var exercice = new GraphiqueExercice(choose_question, questionText, answerInput, feedbackText, scoreText, valider, progressbar, name, image_badge, method, graphique);
    }
    exercice.showQuestion();

    list_objet.push(exercice);
  });
  });

