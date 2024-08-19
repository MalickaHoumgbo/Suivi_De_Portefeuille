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
            // Par défaut,  thème clair est chargé
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
            const nomFond = addFondForm.querySelector('input[name="nom_fond"]').value;
            const typeFond = addFondForm.querySelector('input[name="type_fond"]').value;
            const nomGestionnaire = addFondForm.querySelector('input[name="nom_gestionnaire"]').value;
            const objectifFond = addFondForm.querySelector('textarea[name="objectif_fond"]').value;
            const dateCreation = addFondForm.querySelector('input[name="date_creation"]').value;
            const aum = addFondForm.querySelector('input[name="aum"]').value;
            const valeurLiquidative = addFondForm.querySelector('input[name="valeur_liquidative"]').value;
            const deviseFond = addFondForm.querySelector('input[name="devise_fond"]').value;
            const codeIsin = addFondForm.querySelector('input[name="code_isin"]').value;

            if (!nomFond || !typeFond || !nomGestionnaire || !objectifFond || !dateCreation || !aum || !valeurLiquidative || !deviseFond || !codeIsin) {
                alert('Veuillez remplir tous les champs du formulaire.');
                event.preventDefault();
            }
        });
    }

    // Validation des formulaires d'ajout d'instrument
    const addInstrumentForm = document.querySelector('form[action*="add_instrument"]');
    if (addInstrumentForm) {
        addInstrumentForm.addEventListener('submit', (event) => {
            const nomInstrument = addInstrumentForm.querySelector('input[name="nom_instrument"]').value;
            const typeInstrument = addInstrumentForm.querySelector('input[name="type_instrument"]').value;
            const secteur = addInstrumentForm.querySelector('input[name="secteur"]').value;
            const codeIsin = addInstrumentForm.querySelector('input[name="code_isin"]').value;
            const devise = addInstrumentForm.querySelector('input[name="devise"]').value;
            const prixActuel = addInstrumentForm.querySelector('input[name="prix_actuel"]').value;
            const volatilite = addInstrumentForm.querySelector('input[name="volatilite"]').value;

            if (!nomInstrument || !typeInstrument || !secteur || !codeIsin || !devise || !prixActuel || !volatilite) {
                alert('Veuillez remplir tous les champs du formulaire.');
                event.preventDefault();
            }
        });
    }

    // Validation des formulaires d'ajout de position
    const addPositionForm = document.querySelector('form[action*="add_position"]');
    if (addPositionForm) {
        addPositionForm.addEventListener('submit', (event) => {
            const fondId = addPositionForm.querySelector('input[name="fond_id"]').value;
            const instrumentId = addPositionForm.querySelector('input[name="instrument_id"]').value;
            const quantite = addPositionForm.querySelector('input[name="quantite"]').value;
            const prixAchat = addPositionForm.querySelector('input[name="prix_achat"]').value;
            const dateAchat = addPositionForm.querySelector('input[name="date_achat"]').value;
            const prixActuel = addPositionForm.querySelector('input[name="prix_actuel"]').value;
            const valeurTotale = addPositionForm.querySelector('input[name="valeur_totale"]').value;
            const rendement = addPositionForm.querySelector('input[name="rendement"]').value;
            const dateDerniereTransaction = addPositionForm.querySelector('input[name="date_derniere_transaction"]').value;

            if (!fondId || !instrumentId || !quantite || !prixAchat || !dateAchat || !prixActuel || !valeurTotale || !rendement || !dateDerniereTransaction) {
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
