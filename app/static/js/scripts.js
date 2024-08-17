$(document).ready(function(){
    console.log("Page loaded");
});

// Gestion des modes clair et Sombre
document.addEventListener('DOMContentLoaded', function() {
    const htmlElement = document.documentElement;
    const toggleButton = document.getElementById('toggle-theme');

    if (!htmlElement || !toggleButton) {
        console.error('Les éléments nécessaires ne sont pas trouvés dans le DOM.');
        return;
    }

    // Charger le thème enregistré dans localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-bs-theme', savedTheme);
        toggleButton.textContent = savedTheme === 'dark' ? 'Mode clair' : 'Mode sombre';
    } else {
        // Par défaut, charger le thème clair
        htmlElement.setAttribute('data-bs-theme', 'light');
        toggleButton.textContent = 'Mode sombre';
    }

    toggleButton.addEventListener('click', function() {
        const currentTheme = htmlElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        htmlElement.setAttribute('data-bs-theme', newTheme);
        toggleButton.textContent = newTheme === 'dark' ? 'Mode clair' : 'Mode sombre';
        localStorage.setItem('theme', newTheme);
    });
});