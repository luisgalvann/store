buttons = document.getElementsByClassName("btn-img");
modalImg = document.getElementById("modal-img");

for (const btn of buttons) {
  btn.addEventListener("click", () => {
    modalImg.src = btn.dataset.img;
  });
}
