document.addEventListener('DOMContentLoaded', () => {
    const dropdownButton = document.getElementById('measuresDropdown');
    const dropdownMenu = document.querySelector('.static-dropdown');
    const submitButton = document.getElementById('submitButton');

    // Öffnen und Schließen des Dropdown-Menüs
    dropdownButton.addEventListener('click', (event) => {
        event.stopPropagation();
        const isExpanded = dropdownButton.getAttribute('aria-expanded') === 'true';

        if (!isExpanded) {
            dropdownButton.setAttribute('aria-expanded', 'true');
            dropdownMenu.style.display = 'block';

            // Dynamisch den Submit-Button anpassen
            const dropdownHeight = dropdownMenu.offsetHeight;
            submitButton.style.marginTop = `${dropdownHeight + 16}px`;
        } else {
            dropdownButton.setAttribute('aria-expanded', 'false');
            dropdownMenu.style.display = 'none';
            submitButton.style.marginTop = '20px';
        }
    });

    // Verhindern, dass Klicks innerhalb des Dropdown-Menüs es schließen
    dropdownMenu.addEventListener('click', (event) => {
        event.stopPropagation();
    });

    // Schließen des Dropdown-Menüs, wenn außerhalb geklickt wird
    document.addEventListener('click', () => {
        dropdownButton.setAttribute('aria-expanded', 'false');
        dropdownMenu.style.display = 'none';
        submitButton.style.marginTop = '20px';
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const noneCheckbox = document.getElementById('measureNone');
    const measureCheckboxes = Array.from(
        document.querySelectorAll('.static-dropdown .form-check-input:not(#measureNone)')
    );

    noneCheckbox.addEventListener('change', () => {
        if (noneCheckbox.checked) {
            measureCheckboxes.forEach(checkbox => {
                checkbox.checked = false;
                checkbox.disabled = true;
            });
        } else {
            measureCheckboxes.forEach(checkbox => {
                checkbox.disabled = false;
            });
        }
    });

    measureCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            if (checkbox.checked) {
                noneCheckbox.checked = false;
                noneCheckbox.disabled = false;
            }
        });
    });
});
