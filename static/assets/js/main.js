document.getElementById("user-entry").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent default behavior (inserting newline)
            var userInput = document.getElementById("user-entry").value;
            console.log("User entry input:", userInput); 
            document.getElementById("entry-form").submit(); 
        }
    });