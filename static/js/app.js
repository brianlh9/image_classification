document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData();
    const fileInput = document.getElementById('image');
    formData.append('image', fileInput.files[0]);

    fetch('/classify', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            // Display the image
            document.getElementById('uploaded-image').src = data.image_url;
            document.getElementById('image-container').style.display = 'block';

            // Display the prediction result
            document.getElementById('prediction').textContent = `${data.prediction.replace("_", " ")}`;
            document.getElementById('confidence').textContent = `Confidence: ${(data.confidence * 100).toFixed(2)}%`;
            document.getElementById('classification-container').style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
