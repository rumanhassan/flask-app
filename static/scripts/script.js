async function submitForm() {
    const formData = new FormData(document.getElementById("contact-form"));

    // Send form data to Flask route using fetch
    try {
        const response = await fetch(`/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData,
        });
        const responseData = await response.json();
        console.log('response---', JSON.stringify(responseData));
        alert('Submitted successfully.');
    } catch (error) {
        alert('Failed to submit form data.');
    }
   
}

const form = document.querySelector('#contact-form');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  submitForm();
})
