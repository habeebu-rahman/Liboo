const form = document.getElementById('donation-form');
    const confirmationMessage = document.getElementById('confirmation-message');

    const previewTitle = document.getElementById('preview-title');
    const previewAuthor = document.getElementById('preview-author');
    const previewCategory = document.getElementById('preview-category');
    const previewDescription = document.getElementById('preview-description');
    const previewCover = document.getElementById('preview-cover');

    form.title.addEventListener('input', e => {
        previewTitle.textContent = e.target.value || 'Book Title';
    });

    form.author.addEventListener('input', e => {
        previewAuthor.textContent = e.target.value ? `Author: ${e.target.value}` : 'Author';
    });

    form.category.addEventListener('change', e => {
        previewCategory.textContent = e.target.value ? `Category: ${e.target.value}` : 'Category';
    });

    form.description.addEventListener('input', e => {
        previewDescription.textContent = e.target.value || 'Short description will appear here.';
    });

    form.coverImage.addEventListener('change', e => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = event => {
            previewCover.style.backgroundImage = `url(${event.target.result})`;
            previewCover.style.backgroundSize = 'cover';
            previewCover.style.backgroundPosition = 'center';
            };
            reader.readAsDataURL(file);
        } else {
            previewCover.style.backgroundImage = 'none';
        }
    });

    form.addEventListener('submit', e => {
        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }
        confirmationMessage.style.display = 'block';
        //form.reset();
        previewTitle.textContent = 'Book Title';
        previewAuthor.textContent = 'Author';
        previewCategory.textContent = 'Category';
        previewDescription.textContent = 'Short description will appear here.';
        previewCover.style.backgroundImage = 'none';
    });

    form.addEventListener('reset', () => {
        confirmationMessage.style.display = 'none';
        previewTitle.textContent = 'Book Title';
        previewAuthor.textContent = 'Author';
        previewCategory.textContent = 'Category';
        previewDescription.textContent = 'Short description will appear here.';
        previewCover.style.backgroundImage = 'none';
    });