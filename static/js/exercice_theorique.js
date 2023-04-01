const myDiv = document.querySelector('#my-div');
const questions = JSON.parse(myDiv.dataset.myVariable.replaceAll("'", '"').replaceAll('c"e', "c'e").replaceAll('d"e', "d'e").replaceAll('t"e', "t'e").replaceAll('l"e', "l'e"));
console.log(questions);


let currentQuestion = 0;
let score = 0;

const questionText = document.getElementById("question-text");
const answerInput = document.getElementById("answer-input");
const feedbackText = document.getElementById("feedback-text");
const scoreText = document.getElementById("score-text");
const valider = document.getElementById("valider");
var progressbar = document.querySelector('.progress-bar');


valider.addEventListener('click', function() {
  // Vérifier si la réponse est correcte
  var reponse_correcte = true;
  if (reponse_correcte) {
    // Ajouter 33% à la largeur de la barre de progression
    var width = parseInt(progressbar.style.width) || 0;
    width += 33;
    progressbar.style.width = width + '%';
    progressbar.setAttribute('aria-valuenow', width);
  }
});


function showQuestion() {
    questionText.innerHTML = questions[currentQuestion].question;
    answerInput.value = "";
    feedbackText.textContent = "";
    scoreText.textContent = `Score : ${score}`;
}


function checkAnswer() {
    const userAnswer = answerInput.value.toLowerCase();
    const correctAnswer = questions[currentQuestion].answer.toLowerCase();
    if (userAnswer === correctAnswer) {
        feedbackText.textContent = questions[currentQuestion].feedback;
        feedbackText.classList.add(questions[currentQuestion].feedbackClass);
        score += 10;
        updateScore();

    } else {
        feedbackText.textContent = "Dommage, ce n'est pas la bonne réponse.";
        feedbackText.classList.add("text-danger");
    }
    setTimeout(() => {
        feedbackText.textContent = "";
        feedbackText.classList.remove(questions[currentQuestion].feedbackClass, "text-danger");
        if (currentQuestion === questions.length - 1) {
            questionText.textContent = "Vous avez terminé toutes les questions !";
            answerInput.style.display = "none";
            valider.style.display = "none";
        } else {
            currentQuestion++;
            showQuestion();
            MathJax.typeset()

        }
    }, 2000);
}
answerInput.addEventListener('keyup', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    checkAnswer();
    var reponse_correcte = true;
    if (reponse_correcte) {
    // Ajouter 33% à la largeur de la barre de progression
    var width = parseInt(progressbar.style.width) || 0;
    width += 33;
    progressbar.style.width = width + '%';
    progressbar.setAttribute('aria-valuenow', width);
  }
  }
});

function updateScore() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // Mettre à jour l'affichage du score de l'utilisateur
      document.getElementById("score").innerHTML = "Score: " + this.responseText;
    }
  };
  xhttp.open("POST", "/update_score", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send();
}


document.querySelector("#valider").addEventListener("click", checkAnswer);
showQuestion();
