document.addEventListener('DOMContentLoaded', () => {
  // Dropdown toggle behavior
  const dropdownCards = document.querySelectorAll('.dropdown-card');
  dropdownCards.forEach(card => {
    const toggle = card.querySelector('.dropdown-toggle');
    toggle.addEventListener('click', () => {
      card.classList.toggle('active');
    });
  });

  // Avatar selection behavior
  const avatars = document.querySelectorAll('.avatar');
  avatars.forEach(avatar => {
    avatar.addEventListener('click', () => {
      avatars.forEach(a => a.classList.remove('selected'));
      avatar.classList.add('selected');
      const selectedCategory = avatar.dataset.category;
      console.log('Selected category:', selectedCategory);
      // You can integrate with image generator here
    });
  });

  // Prompt card entry animation
  const promptInput = document.querySelector('.prompt-input');
  promptInput.addEventListener('focus', () => {
    promptInput.style.boxShadow = '0 0 10px #4fc3f7';
  });
  promptInput.addEventListener('blur', () => {
    promptInput.style.boxShadow = 'none';
  });
});
