/*document.querySelectorAll('.delete-form').forEach(form => {
        form.addEventListener('submit', event => {
        const confirmed = confirm('Are you sure you want to delete this book?');
        if (!confirmed) {
        event.preventDefault(); // Stop the form if user clicks "Cancel"
        }
    });
    });*/


    document.querySelectorAll('.delete-form').forEach(form => {
    const submitHandler = event => {
        event.preventDefault();
        Swal.fire({
            title: 'Delete Book?',
            text: 'Are you sure you want to remove this book from your donations?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Yes, delete it!',
            cancelButtonText: 'Cancel',
            confirmButtonColor: '#e6d5b3',
            cancelButtonColor: '#ffe4c4',
            background:'rgb(243 243 243)',
            customClass: {
            confirmButton: 'custom-confirm',
            cancelButton: 'custom-cancel'
            }
        }).then(result => {
            if (result.isConfirmed) {
            // 2. Temporarily remove the listener
            form.removeEventListener('submit', submitHandler);
            
            // 3. Submit the form (this will now bypass the listener)
            form.submit();
            }
        });
    };
    // 4. Attach the defined handler
    form.addEventListener('submit', submitHandler);
});