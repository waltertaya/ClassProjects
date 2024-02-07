function validateForm() {
    var name = document.getElementById("name").value;
    var course = document.getElementById("course").value;
    var age = document.getElementById("age").value;
    var gender = document.getElementById("gender").value;

    if (name === "" || course === "" || age === "" || gender === "") {
        alert("Please fill all the details.");
    } else {
        // Additional validation or form submission logic can be added here
        alert("Form submitted successfully!");
    }
}

function resetForm() {
    document.getElementById("myForm").reset();
}
