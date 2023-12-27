document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('themeToggle');
    const themeLabel = themeToggle.nextElementSibling;

    // Function to update label text based on the toggle's position
    function updateLabelText() {
        // The label should indicate the result of toggling the switch
        themeLabel.textContent = themeToggle.checked ? 'Dark Mode' : 'Light Mode';
    }

    // Check the current color scheme and update the toggle and label appropriately
    function initializeTheme() {
        const currentTheme = localStorage.getItem('theme');
        if (currentTheme === 'light') {
            document.body.classList.add('light-mode');
            themeToggle.checked = true;
        } else if (currentTheme === 'dark') {
            document.body.classList.remove('light-mode');
            themeToggle.checked = false;
        } else {
            // Fallback to the body's current color if there's no item in localStorage
            const bodyColor = window.getComputedStyle(document.body).color;
            const isDarkMode = bodyColor.indexOf('255') === -1; // assuming dark mode text color is not white
            themeToggle.checked = isDarkMode;
            if (isDarkMode) {
                localStorage.setItem('theme', 'dark');
            } else {
                document.body.classList.add('light-mode');
                localStorage.setItem('theme', 'light');
            }
        }
        updateLabelText();
    }

    initializeTheme();

    themeToggle.addEventListener('change', () => {
        document.body.classList.toggle('light-mode');
        const newTheme = document.body.classList.contains('light-mode') ? 'light' : 'dark';
        localStorage.setItem('theme', newTheme);
        updateLabelText(); // Update label text to reflect the new state
    });
});
