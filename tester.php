<?php
unlink('temp/result/compressed_pic.jpg');

rmdir('temp/result');

echo $_FILES['filename']['tmp_name'];

if (move_uploaded_file($_FILES['filename']['tmp_name'], 'temp/' .$_FILES['filename']['name'])) {
    // echo 'Файл отправлен';
    rename ('temp/' .$_FILES['filename']['name'], "temp/pic.jpg");
}
// else {
//     // echo 'Файл не отправлен';
// }

$command_exec = escapeshellcmd('predictTest.py');
$str_output = shell_exec($command_exec);
echo $str_output;

header("Location: index.html");

unlink('temp/pic.jpg');

unlink('temp/compressed_pic.jpg');

?>
