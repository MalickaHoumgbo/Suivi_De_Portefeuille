document.addEventListener('DOMContentLoaded', function() {
    console.log("Page loaded");

    // Gestion des modes clair et sombre
    const htmlElement = document.documentElement;
    const toggleButton = document.getElementById('toggle-theme');

    if (htmlElement && toggleButton) {
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
    } else {
        console.error('Les éléments nécessaires pour le thème ne sont pas trouvés dans le DOM.');
    }

    // Validation des formulaires d'ajout de fonds
    const addFondForm = document.querySelector('form[action*="add_fond"]');
    if (addFondForm) {
        addFondForm.addEventListener('submit', (event) => {
            const name = addFondForm.querySelector('input[name="new_fond_name"]').value;
            const description = addFondForm.querySelector('textarea[name="new_fond_objectif"]').value; // Correction ici

            if (!name || !description) {
                alert('Veuillez remplir tous les champs du formulaire.');
                event.preventDefault();
            }
        });
    }

    // Validation des formulaires d'ajout d'instrument
    const addInstrumentForm = document.querySelector('form[action*="add_instrument"]');
    if (addInstrumentForm) {
        addInstrumentForm.addEventListener('submit', (event) => {
            const name = addInstrumentForm.querySelector('input[name="new_instrument_name"]').value;
            const type = addInstrumentForm.querySelector('input[name="new_instrument_type"]').value;
            const description = addInstrumentForm.querySelector('textarea[name="new_instrument_description"]').value;

            if (!name || !type || !description) {
                alert('Veuillez remplir tous les champs du formulaire.');
                event.preventDefault();
            }
        });
    }

    // Confirmation pour la suppression des fonds, instruments et positions
    document.querySelectorAll('form[action*="delete_fond"], form[action*="delete_instrument"], form[action*="delete_position"]').forEach(form => {
        form.addEventListener('submit', (event) => {
            if (!confirm('Êtes-vous sûr de vouloir supprimer cet élément ?')) {
                event.preventDefault();
            }
        });
    });
});
