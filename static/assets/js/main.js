document.getElementById("user-entry").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent default behavior (inserting newline)
            var userInput = document.getElementById("user-entry").value;
            console.log("User entry input:", userInput); 
            document.getElementById("entry-form").submit(); 
        }
    });
const MAX_WIDTH = 550;
const MAX_HEIGHT = 200;
const MAX_FONT_SIZE = 40;
const MIN_FONT_SIZE = 12;

function fitText(input) {
    let fontSize = MAX_FONT_SIZE;
    input.style.fontSize = fontSize + 'px';
    while (fontSize > MIN_FONT_SIZE && (input.scrollHeight > MAX_HEIGHT || input.scrollWidth > MAX_WIDTH)) {
        fontSize--;
        input.style.fontSize = fontSize + 'px';
    }
}
document.addEventListener("DOMContentLoaded", function() {
    // Check if there is any previously saved entry
    var savedEntry = localStorage.getItem("userEntry");
    if (savedEntry) {
        document.getElementById("user-entry").value = savedEntry;
    }

    // Save the entry whenever it changes
    document.getElementById("user-entry").addEventListener("input", function() {
        localStorage.setItem("userEntry", this.value);
    });
});

document.getElementById('stream-button').addEventListener('click', function() {
    var videoContainer = document.getElementById('video-container');
    if (videoContainer.style.display === 'none') {
        var video = document.createElement('video');
        video.src = '{{ feed }}';
        video.controls = false;
        video.autoplay = true;
        video.style.width = '100%';
        video.style.height = '100%';
        video.style.objectFit = 'cover';
        videoContainer.appendChild(video);
        videoContainer.style.display = 'block';
    } else {
        videoContainer.innerHTML = '';
        videoContainer.style.display = 'none';
    }
});
function sendSnapshot(imageDataUrl) {
    fetch('/snapshot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            image_data_url: imageDataUrl
        })
    }).then(response => {
        // David: take a screenshot and send it to the server
    }).catch(error => {
        console.error('Error:', error);
    });
}