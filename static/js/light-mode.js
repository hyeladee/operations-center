document.addEventListener('DOMContentLoaded', function() {
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
    const themeToggleSystemIcon = document.getElementById('theme-toggle-system-icon');
    const themeDropdown = document.getElementById('theme-dropdown');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    function updateThemeBySystem() {
        if (prefersDark) {
            document.documentElement.classList.add('dark');
            themeToggleSystemIcon.classList.remove('hidden');
            themeToggleLightIcon.classList.add('hidden');
            themeToggleDarkIcon.classList.add('hidden');
        } else {
            document.documentElement.classList.remove('dark');
            themeToggleSystemIcon.classList.remove('hidden');
            themeToggleLightIcon.classList.add('hidden');
            themeToggleDarkIcon.classList.add('hidden');
        }
    }

    function updateIcon(theme) {
        themeToggleDarkIcon.classList.add('hidden');
        themeToggleLightIcon.classList.add('hidden');
        themeToggleSystemIcon.classList.add('hidden');
        
        switch(theme) {
            case 'dark':
                themeToggleDarkIcon.classList.remove('hidden');
                break;
            case 'light':
                themeToggleLightIcon.classList.remove('hidden');
                break;
            default:
                themeToggleSystemIcon.classList.remove('hidden');
        }
    }

    // Initial theme setup
    const currentTheme = localStorage.theme || 'system';
    if (currentTheme === 'dark' || (currentTheme === 'system' && prefersDark)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    updateIcon(currentTheme);

    // Toggle dropdown
    document.getElementById('theme-toggle').addEventListener('click', () => {
        themeDropdown.classList.toggle('hidden');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('#theme-toggle') && !e.target.closest('#theme-dropdown')) {
            themeDropdown.classList.add('hidden');
        }
    });

    // Theme selection handlers
    document.getElementById('theme-light').addEventListener('click', () => {
        document.documentElement.classList.remove('dark');
        localStorage.theme = 'light';
        updateIcon('light');
        themeDropdown.classList.add('hidden');
    });

    document.getElementById('theme-dark').addEventListener('click', () => {
        document.documentElement.classList.add('dark');
        localStorage.theme = 'dark';
        updateIcon('dark');
        themeDropdown.classList.add('hidden');
    });

    document.getElementById('theme-system').addEventListener('click', () => {
        localStorage.removeItem('theme');
        if (prefersDark) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        updateIcon('system');
        themeDropdown.classList.add('hidden');
    });

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.theme) {
            if (e.matches) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        }
    });
});