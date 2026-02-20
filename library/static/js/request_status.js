function showTab(tabName) {
            const tabs = document.querySelectorAll('.tab-content');
            tabs.forEach(tab => {
                tab.style.display = 'none';
            });
            document.getElementById(tabName).style.display = 'block';

            const tabButtons = document.querySelectorAll('.tab');
            tabButtons.forEach(button => {
                button.classList.remove('active');
            });
            event.target.classList.add('active');
        }