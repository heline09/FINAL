// search query 
document.addEventListener('DOMContentLoaded', function () {
    const searchButtonElement = document.getElementById('search-button');
    const searchInputElement = document.getElementById('search-input');
    const noInternshipsElement = document.getElementById('no-internships');

    searchButtonElement.addEventListener('click', () => {
        const searchTerm = searchInputElement.value.toLowerCase();
        const internshipElements = document.getElementsByClassName('job-card');
        let foundInternship = false; // Flag to track if any internship is found

        for (let i = 0; i < internshipElements.length; i++) {
            const internshipElement = internshipElements[i];
            const titleElement = internshipElement.querySelector('.job-title');   // searches only by job title
            const titleText = titleElement.textContent.toLowerCase();

            const descriptionElement = internshipElement.querySelector('.job-description');
            const descriptionText = descriptionElement.textContent.toLowerCase();

            const companyElement = internshipElement.querySelector('.job-company');
            const companyText = companyElement.textContent.toLowerCase();

            if (titleText.includes(searchTerm) || descriptionText.includes(searchTerm) || companyText.includes(searchTerm)) {
                internshipElement.style.display = 'block';
                foundInternship = true; // Set flag to true if internship is found
            } else {
                internshipElement.style.display = 'none';
            }
        }

        // Show or hide the "No internships found" message based on search result
        if (foundInternship) {
            noInternshipsElement.style.display = 'none'; // Hide the message
        } else {
            noInternshipsElement.style.display = 'block'; // Show the message
        }
    });

    // Add event listener to search input
    searchInputElement.addEventListener('input', () => {
        searchButtonElement.click();
    });
});
