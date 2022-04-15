function toggleBurger() {
  let burgerIcon = document.getElementById('burger');
  let dropMenu = document.getElementById('navbarBasicExample');

  // document.getElementsByClassName("navbar").style.background="rgba(192, 192, 192, 1);";
  burgerIcon.classList.toggle('is-active');
  dropMenu.classList.toggle('is-active');
};