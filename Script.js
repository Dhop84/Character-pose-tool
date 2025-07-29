document.querySelectorAll('.dropdown-toggle').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.parentElement.classList.toggle('active');
  });
});
