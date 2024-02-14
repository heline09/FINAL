// search query 
document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    const jobCards = document.querySelectorAll('.job-card');

    searchButton.addEventListener('click', function() {
        const searchTerm = searchInput.value.toLowerCase();

        jobCards.forEach(function(card) {
            const title = card.getAttribute('data-title').toLowerCase();
            const company = card.getAttribute('data-company').toLowerCase();
            const description = card.getAttribute('data-description').toLowerCase();

            if (title.includes(searchTerm) || company.includes(searchTerm) || description.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});