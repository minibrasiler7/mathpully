function searchTeacher() {
    var input = document.getElementById('teacher-search');
    var resultsContainer = document.getElementById('search-results');
    fetch('/search_teacher?q=' + input.value)
    .then(response => response.json())
    .then(data => {
        resultsContainer.innerHTML = '';
        data.forEach(item => {
            var div = document.createElement('div');
            var btn = document.createElement('button');
            btn.textContent = item;
            btn.classList.add('btn');
            btn.classList.add('btn-primary');
            btn.onclick = function() {
                // Ici, ajoutez le code pour gérer le clic sur un résultat de recherche,
                // par exemple envoyer une demande d'ajout à l'enseignant.
                input.value = item;
            };
            div.appendChild(btn);
            resultsContainer.appendChild(div);
        });
    });
}

$(document).ready(function() {

  $(".btn-change").click(function() {
    const btn = $(this);
    const username = $(this).data("username");
    const classe = $(this).data("class");
    const action = $(this).data("action");

    // Objet de données à envoyer dans la requête AJAX
    const data = {
      username: username,
      classe: classe,
      action: action
    };
    console.log(data)
    // Envoie de la requête AJAX
    $.ajax({
      url: "/modifier_utilisateur",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: function(response) {
        // Le traitement des réponses de la route Flask peut être effectué ici
        if (action === "+" || action ==="-"){
            console.log("Réponse du serveur :", response);
            const tdElement = $(`td[data-user="${username}"]`);
            console.log(tdElement.text())
            let classeText = tdElement.text().trim();
            const regex = /^(\d+)/; // Expression régulière pour extraire le nombre au début de la chaîne
            const match = classeText.match(regex);
            let nouveauNombre = parseInt(match[1], 10); // Convertir le nombre en entier
            if (action === "plus") {
              nouveauNombre++;
            } else if (action === "minus") {
              nouveauNombre--;
            }
            const nouvelleClasse = classeText.replace(regex, nouveauNombre);
            tdElement.text(nouvelleClasse);
            }
        else if (action === "delete"){
            const ligne_a_supprimer = btn.parent().parent();
            ligne_a_supprimer.remove();
        }
      },
      error: function(error) {
        console.error("Erreur AJAX :", error);
      }
    });
  });
  $('#search').on('input', function() {
    let search_string = $(this).val();
    $.get('/search_teacher', { q: search_string }, function(data) {
      let dropdown = $('#dropdown');
      dropdown.empty();
      for (let teacher of data) {
        let teacherElement = $('<button>').addClass('btn btn-primary').text(teacher);
        teacherElement.on('click', function() {
          $('#search').val(teacher);
          dropdown.empty();
        });
        dropdown.append(teacherElement);
      }
    });
  });
  $('#add-teacher-button').on('click', function() {
    let teacher_username = $('#teacher-search').val();
    $.post('/add_teacher', { teacher_username: teacher_username }, function(response) {
      $('#message').text(response.message);
      if (response.status == 'success') {
        $('#message').removeClass('text-danger').addClass('text-success');
      } else {
        $('#message').removeClass('text-success').addClass('text-danger');
      }
    });
  });
  $('.add-student-button').click(function() {
        var studentId = $(this).attr('data-student');
        console.log(studentId)
        $.ajax({
            url: '/validate_student',
            type: 'POST',
            data: { student_id: studentId },
            success: function(data) {
                if (data.success) {
                    alert('L\'élève a été ajouté avec succès.');
                } else {
                    alert('Une erreur s\'est produite lors de l\'ajout de l\'élève.');
                }
            }
        });
    });
});

