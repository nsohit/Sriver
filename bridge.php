<?php



$servername = "localhost";

$dbname = "";

$username = "";

$password = "dzailfc17";


$api_key_value = "9F7j3bA5TAmPt";

$api_key= $latitude = $longitude = $dhtA = $analog = $adxlA = $iduser = $status = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $api_key = test_input($_POST["api_key"]);
    if($api_key == $api_key_value) {
        $latitude = test_input($_POST["latitude"]);
        $longitude = test_input($_POST["longitude"]);
        $dhtA = test_input($_POST["dhtA"]);
        $analog = test_input($_POST["analog"]);
        $adxlA = test_input($_POST["adxlA"]);
        $iduser = test_input($_POST["iduser"]);
        $status = test_input($_POST["status"]);
        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        } 
        
        $sql = "INSERT INTO data (latitude, longitude, dhtA, analog, adxlA,iduser,status)
        VALUES ('" . $latitude . "', '" . $longitude . "', '" . $dhtA . "','" . $analog . "', '" . $adxlA . "','" . $iduser. "', '" . $status. "')";
        
        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    
        $conn->close();
    }
    else {
        echo "Wrong API Key provided.";
    }

}
else {
    echo "No data posted with HTTP POST.";
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
