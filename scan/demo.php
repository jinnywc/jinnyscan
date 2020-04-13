<?php
$host = "127.0.0.1";
$username = "root";
$pass = "root";
$database = "demo";
$con = new mysqli($host,$username, $pass,$database);

if(!$con){
    echo "连接失败";
	die("连接失败：");
}

$con->query('set names utf8;');
$sql = "SELECT * FROM demo";

#echo $sql;
$result = mysqli_query($con,$sql);


#echo $result;
?>
<meta http-equiv="Content-Type" Content="text/html;charset=utf-8">
<table width="100%" border="1" cellpadding="0" cellspacing="0" style="table-layout:fixed">
<tr>
<td width="20%">id</td>
<td width="30%">网址</td>
<td width="25%">用户</td>
<td width="25%">密码</td>
</tr>
<?php
$row = mysqli_fetch_all($result);
foreach($row as $key => $value){
    echo "<tr>";
    foreach($value as $k => $v){
        echo "<td>".$v."</td>";
    }
    echo "</tr>";
}
?>
</table>





