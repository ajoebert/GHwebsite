async function submitForm(event) {
    event.preventDefault();

    // Collect form data
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phoneNumber').value,
        company: document.getElementById('company').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
    };

    // Send data to the API
    try {
        const response = await fetch('/api/submit-form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        // Handle response
        if (response.ok) {
            alert('Form submitted successfully!');
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('form').addEventListener('submit', submitForm);
});
