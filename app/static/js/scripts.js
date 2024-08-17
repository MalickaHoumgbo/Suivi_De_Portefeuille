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

// gestion d'ajouts des fonds et instruments dans les formulaireq
document.addEventListener('DOMContentLoaded', () => {
    // Ajouter un événement de soumission pour le formulaire d'ajout de fonds
    const addFondForm = document.querySelector('form[action*="add_fond"]');
    if (addFondForm) {
        addFondForm.addEventListener('submit', (event) => {
            // Effectuer une validation ou afficher un message
            const name = addFondForm.querySelector('input[name="new_fond_name"]').value;
            const description = addFondForm.querySelector('textarea[name="new_fond_description"]').value;

            if (!name || !description) {
                alert('Veuillez remplir tous les champs du formulaire.');
                event.preventDefault(); // Empêcher la soumission si les champs sont vides
            }
        });
    }

    // Ajouter un événement de soumission pour le formulaire d'ajout d'instrument
    const addInstrumentForm = document.querySelector('form[action*="add_instrument"]');
    if (addInstrumentForm) {
        addInstrumentForm.addEventListener('submit', (event) => {
            // Effectuer une validation ou afficher un message
            const name = addInstrumentForm.querySelector('input[name="new_instrument_name"]').value;
            const type = addInstrumentForm.querySelector('input[name="new_instrument_type"]').value;
            const description = addInstrumentForm.querySelector('textarea[name="new_instrument_description"]').value;

            if (!name || !type || !description) {
                alert('Veuillez remplir tous les champs du formulaire.');
                event.preventDefault(); // Empêcher la soumission si les champs sont vides
            }
        });
    }
});

// l'utilisateur peut vouloir la confirmation de ses action au niveau des delete
document.addEventListener('DOMContentLoaded', () => {
    // Ajouter un événement de confirmation pour la suppression
    document.querySelectorAll('form[action*="delete_fond"], form[action*="delete_instrument"], form[action*="delete_position"]').forEach(form => {
        form.addEventListener('submit', (event) => {
            if (!confirm('Êtes-vous sûr de vouloir supprimer cet élément ?')) {
                event.preventDefault(); // Empêcher la soumission si l'utilisateur annule
            }
        });
    });
});
