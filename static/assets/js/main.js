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