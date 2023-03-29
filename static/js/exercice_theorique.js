const myDiv = document.querySelector('#my-div');
const questions = myDiv.dataset.myVariable;
console.log(questions);


let currentQuestion = 0;
let score = 0;

const questionText = document.getElementById("question-text");
const answerInput = document.getElementById("answer-input");
const feedbackText = document.getElementById("feedback-text");
const scoreText = document.getElementById("score-text");

function showQuestion() {
    questionText.textContent = questions[currentQuestion].question;
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
        } else {
            currentQuestion++;
            showQuestion();
        }
    }, 2000);
}
answerInput.addEventListener('keyup', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    checkAnswer();
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
