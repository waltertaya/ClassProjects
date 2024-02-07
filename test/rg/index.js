function validateLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("errorMessage");

    // Simple validation, you can add more complex validation as needed
    if (username === "" || password === "") {
        errorMessage.textContent = "Username and password are required";
    } else {
        // Submit the form for PHP authentication
        document.getElementById("loginForm").submit();
    }
}

function resetForm() {
    document.getElementById("loginForm").reset();
    document.getElementById("errorMessage").textContent = "";
}