
document.addEventListener('DOMContentLoaded', function () {
const pointsUtilisateurNav = document.getElementById('points_utilisateurs_nav');

class Exercices {

  constructor(questions, donnee_problem_html, input_html, feedback_html, score_html, valider_html, progress_html) {
    this.questions = questions;
    this.index_question = 0;
    this.currentQuestion = this.questions[this.index_question]
    this.donnee_problem_html = donnee_problem_html;
    this.input_html = input_html;
    this.feedback_html = feedback_html;
    this.score_html = score_html;
    this.valider_html = valider_html;
    this.progress_html = progress_html;
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
  checkAnswer(){
      var userAnswer =  this.input_html.value.toLowerCase();
      const correctAnswer = this.currentQuestion.answer;
      if (correctAnswer.includes(userAnswer)) {
        this.feedback_html.textContent = this.currentQuestion.feedback;
        this.feedback_html.classList.add(this.currentQuestion.feedbackClass);
        this.index_question++;
        this.updateScore();
        this.upScore();
        this.currentQuestion = this.questions[this.index_question]

        if (this.index_question === 4) {
          this.donnee_problem_html.textContent = "Vous avez terminé toutes les questions !";
          this.input_html.style.display = "none";
          this.valider_html.style.display = "none";
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
      this.score_html.textContent = `Score : ${this.index_question * 10}`;
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
    const questions = JSON.parse(exerciceInteractif.dataset.questions.replaceAll("'", '"').replaceAll('c"e', "c'e").replaceAll('d"e', "d'e").replaceAll('t"e', "t'e").replaceAll('l"e', "l'e"));
    const questionText = exerciceInteractif.querySelector('.question-text');
    const answerInput = exerciceInteractif.querySelector('.answer-input');
    const feedbackText = exerciceInteractif.querySelector('.feedback-text');
    const scoreText = exerciceInteractif.querySelector('.score-text');
    const valider = exerciceInteractif.querySelector('.valider');
    const progressbar = exerciceInteractif.querySelector('.progress-bar');
    choose_question = selectionSansRemise(questions)
    var exercice = new Exercices(choose_question, questionText, answerInput, feedbackText, scoreText, valider, progressbar)
    exercice.showQuestion()
    list_objet.push(exercice)

  });
});
