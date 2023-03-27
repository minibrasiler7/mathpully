$(document).ready(function() {
  // Ajoute une classe "selected" sur l'image cliquée et supprime cette classe sur les autres images
  function selectImage(image) {
  // Désélectionne l'image précédemment sélectionnée
  let previouslySelectedImage = document.querySelector(".selected");
  if (previouslySelectedImage) {
    previouslySelectedImage.classList.remove("selected");
  }

  // Sélectionne la nouvelle image
  image.classList.add("selected");
}
// Récupère les images et ajoute un gestionnaire d'événement click
let images = document.querySelectorAll(".avatar");
for (let i = 0; i < images.length; i++) {
  images[i].addEventListener("click", function() {
    selectImage(this);
  });
}


});
