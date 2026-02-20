document.querySelectorAll('.request-form').forEach(form => {
            const submitHandler = event => {
                event.preventDefault();
                Swal.fire({
                    title: 'Request Book...',
                    text: 'Are You Sure To Request The Book',
                    icon: 'success',
                    showCancelButton: true,
                    confirmButtonText: 'Yes ',
                    cancelButtonText: 'No ',
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