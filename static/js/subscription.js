const form = document.getElementById('register-form'); // Ensure correct form ID
const roleField = document.getElementById('id_role'); // Ensure correct field ID
const submitButton = document.getElementById('submit-button');
const subscriptionPlanField = document.getElementById('subscription_plan_id'); // Get hidden field element

submitButton.addEventListener('click', (event) => {
    const selectedRole = roleField.value;

    if (selectedRole === 'recruiter') {
        event.preventDefault();
        showSubscriptionPlan();

    } else {
        // User selected a different role, allow form submission
        form.submit();
    }
});

function showSubscriptionPlan() {
    if (typeof jQuery !== 'undefined') {
        $('#customModal').modal('show');
        document.getElementById('modalBody').innerHTML = document.getElementById('subscriptionPlanList').innerHTML;
    } else {
        // redirect
        promptForPlanSelection();
    }
}

function promptForPlanSelection() {
    const selectedPlan = prompt('Please select a subscription plan:', '');

    if (selectedPlan) {
        subscriptionPlanField.value = selectedPlan;
        form.submit();
    } else {
        // User canceled or didn't provide a plan
        alert('Please select a subscription plan to proceed.');
    }
}

