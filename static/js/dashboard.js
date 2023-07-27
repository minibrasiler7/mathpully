
const niveau = JSON.parse(document.getElementById('niveau-data').textContent);
const user_stat= JSON.parse(document.getElementById('user_stat').textContent);
const changement_niveau= JSON.parse(document.getElementById('niveau-avertissement').textContent);
  $(document).ready(function() {
    if(changement_niveau["changement de niveau"] == 1){
        showPopup();
    }

    // Mettre à jour les barres de progression et les valeurs
    updateProgress();
    }
  );

  function updateProgress() {
    // Vous pouvez accéder aux propriétés du dictionnaire 'niveau' ici
    const points_max = niveau.point;
    const badges_max = niveau.badge;
    const exercices_max = niveau.exercices_livre;
    const points_user = user_stat.point;
    const badges_user = user_stat.badge;
    const exercices_user = user_stat.exercice;
    const pointsProgressBar = document.querySelector('.points-progress');
    pointsProgressBar.setAttribute('aria-valuemax', points_max);
    pointsProgressBar.setAttribute('aria-valuenow', points_user);
    pointsProgressBar.setAttribute('aria-valuemin', 0);
    remplissage = points_user/points_max*100;
    console.log(remplissage)
    pointsProgressBar.setAttribute('style', "width:"+remplissage+"%;");
  // Mettre à jour la barre de progression des badges
    const badgesProgressBar = document.querySelector('.badges-progress');
    badgesProgressBar.setAttribute('aria-valuemax', badges_max);
    badgesProgressBar.setAttribute('aria-valuenow', badges_user);
    badgesProgressBar.setAttribute('aria-valuemin', 0);
    remplissage = badges_user/badges_max*100;
    badgesProgressBar.setAttribute('style', "width:"+remplissage+"%;");

  // Mettre à jour la barre de progression des exercices
    const exercicesProgressBar = document.querySelector('.exercices-progress');
    exercicesProgressBar.setAttribute('aria-valuemax', exercices_max);
    exercicesProgressBar.setAttribute('aria-valuenow', exercices_user);
    exercicesProgressBar.setAttribute('aria-valuemin', 0);
    remplissage = exercices_user/exercices_max*100;
    exercicesProgressBar.setAttribute('style', "width:"+remplissage+"%;");
  // Mettre à jour les valeurs affichées
    document.querySelector('.points-value').textContent = points_user;
    document.querySelector('.badges-value').textContent = badges_user;
    document.querySelector('.exercices-value').textContent = exercices_user;
    // ... (le reste de votre code JavaScript)

  }
  function showPopup() {
  document.getElementById('popup').style.display = 'block';
}

    // Fonction pour fermer le popup
    function closePopup() {
  document.getElementById('popup').style.display = 'none';
    }

