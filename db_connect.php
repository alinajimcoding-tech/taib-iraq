<?php
$host = "localhost";
$user = "root";
$password = "";
$dbname = "taib_db";

// إنشاء الاتصال
$conn = new mysqli($host, $user, $password, $dbname);

// الفحص
if ($conn->connect_error) {
    die("فشل الاتصال بقاعدة البيانات: " . $conn->connect_error);
}
?>