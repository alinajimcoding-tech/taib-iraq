<?php
require_once 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $trader_name = $_POST['trader-name'];
    $trader_phone = $_POST['trader-phone'];
    $trader_address = $_POST['trader-address'];
    $goods_name = $_POST['goods-name'];
    $goods_code = $_POST['goods-code'];
    $platform = $_POST['platform'];

    $sql = "INSERT INTO traders_orders (trader_name, trader_phone, trader_address, goods_name, goods_code, platform) 
            VALUES ('$trader_name', '$trader_phone', '$trader_address', '$goods_name', '$goods_code', '$platform')";

    if ($conn->query($sql) === TRUE) {
        echo "<script>alert('تم حفظ البيانات بنجاح!'); window.location.href='index.html';</script>";
    } else {
        echo "خطأ في الحفظ: " . $conn->error;
    }

    $conn->close();
}
?>