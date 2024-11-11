fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ review: "The food was amazing!" })
})
.then(response => {
    console.log('Response status:', response.status); // Check if status is 200
    return response.json();
})
.then(data => {
    console.log('Sentiment data:', data); // Log the sentiment prediction data
    if (data.sentiment) {
        document.getElementById('result').innerText = `Sentiment: ${data.sentiment}`;
    } else if (data.error) {
        document.getElementById('result').innerText = `Error: ${data.error}`;
    }
})
.catch(error => {
    console.error('Error:', error);
    document.getElementById('result').innerText = `Error: ${error.message}`;
});
