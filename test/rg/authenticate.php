<?php
$servername = "your_database_server";
$username = "your_database_username";
$password = "your_database_password";
$dbname = "your_database_name";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve username and password from the form
$user = $_POST['username'];
$pass = $_POST['password'];

// SQL query to check if the username and password match
$sql = "SELECT * FROM login_table WHERE username='$user' AND password='$pass'";
$result = $conn->query($sql);

// Check if the query returned a row (valid credentials)
if ($result->num_rows > 0) {
    // Redirect to the complaints page on successful login
    header("Location: complaints.php");
} else {
    // Display an error message if login fails
    echo "Invalid username or password";
}

// Close the database connection
$conn->close();
?>
