<!DOCTYPE html>
<html>
<head>
    <title>Formulario Lab0</title>
</head>
<body>
      <h1>Form with files</h1>
    
      <form method="POST" action="index.php" enctype="multipart/form-data">        
            <label for="name">Name</label>
            <p><input type="text" id="name" name="name" placeholder="name" pattern="[a-zA-Z]+" required="required"/></p>        
            <label for="description">Description</label>
            <p><input type="text" id="description" name="description" placeholder="description" required="required"/></p> 
            <label for="age">Age</label> 
            <p><input type="number" id="name" name="age" placeholder="age" required="required"/></p> 
            <input type="submit" value="Send"/>   
      </form>

</body>
</html>
<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['name']) && isset($_POST['description']) && isset($_POST['age'])){
       
        $name = isset($_POST['name']) ? $_POST['name'] : '';
        $description = isset($_POST['description']) ? $_POST['description'] : '';
        $age = isset($_POST['age']) ? $_POST['age'] : '';

        function create_array($name, $description, $age){
            $array = [
                "name" => $name,
                "description" => $description,
                "age" => $age
            ];
            return $array;
        }

        function save_files($array){
            $file1 = fopen('nombre.txt', 'a+');
            fwrite($file1, "Name: {$array['name']} - Description: {$array['description']}");
            fwrite($file1, "\r");
            fclose($file1);

            $file2 = fopen('edad.txt', 'a+');
            fwrite($file2, "Age: {$array['age']}");
            fwrite($file2, "\r");
            fclose($file2);
        }

        function avg_age(){
            $file3 = fopen("edad.txt", "a+");    
            $total = 0;
            while(!feof($file3)){
            $content = fgets($file3);
            $content_array = explode("Age: ", $content);
                for($i=0; $i < count($content_array); $i++){
                   // echo("<script>console.log('array: " . $content_array[$i] . "');</script>");
                $total = $total + (int) $content_array[$i]; 
                   // echo("<script>console.log('total: " . $total . "');</script>");
                $result = $total / (count($content_array)-1);
                   // echo("<script>console.log('contador: " . count($content_array) . "');</script>");
                }
            
                return $result;
           }
        }

        if($_POST['name'] != '' && $_POST['description'] != '' && $_POST['age'] != ''){
            $new_array = create_array($name, $description, $age);
            save_files($new_array);
            $avg = avg_age();

            echo "<br>";
            echo "The average age is {$avg}";
        }

    }

?>
