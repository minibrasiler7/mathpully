$(document).ready(function() {
  // Cacher l'input et le label au chargement de la page
  const classeInput = $("#classeInput");
  const classeLabel = $("#classeLabel");
  classeInput.hide();
  classeLabel.hide();

  // Gérer l'affichage de l'input en fonction du bouton radio "élève"
  const eleveRadio = $("#qcm-option-2");
  const enseignantRadio = $("#qcm-option-1");
  enseignantRadio.change(function() {
    if (enseignantRadio.is(":checked")) {
      classeInput.hide();
      classeLabel.hide();
    }
  });
  eleveRadio.change(function() {
    if (eleveRadio.is(":checked")) {
      classeInput.show();
      classeLabel.show();
    }
  });

  // Ajoute une classe "selected" sur l'image cliquée et supprime cette classe sur les autres images
  function selectImage(image) {
    // Désélectionne l'image précédemment sélectionnée
    $(".selected").removeClass("selected");

    // Sélectionne la nouvelle image
    image.classList.add("selected");
  }

  // Récupère les images et ajoute un gestionnaire d'événement click
  $(".avatar").click(function() {
    selectImage(this);
  });
});
