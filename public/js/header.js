// # the responsive header script

const menuToggleBtn = document.querySelector('.header__menu-toggle');
const menu = document.querySelector('.header__menu');

menuToggleBtn.addEventListener('click', function() {
menu.classList.toggle('active');
menuToggleBtn.classList.toggle('times');
});