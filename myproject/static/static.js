console.log('Сайт загружен!');
// Добавляем обработчик для всех кнопок "Подробнее"
document.addEventListener('DOMContentLoaded', function() {
const buttons = document.querySelectorAll('.btn-primary');
buttons.forEach(button => {
button.addEventListener('click', function(e) {
alert('Функционал кнопки "Подробнее" будет добавлен позже!');
});
});
});