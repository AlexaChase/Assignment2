<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <title>Calculate the area and circumference of a circle using the diameter</title>
    </head>
 
    <body>
        <?php
        $p= 3.141592653589793238462643383279502884197;
        $CircleDiamater = "";
        $CircleRadius = $CircleDiamater/2;
        $CircleArea= $p * $CircleRadius.pow(2);
        $CircleCircumference= 2 * $p * $CircleRadius;
        if ($CircleDiamater > 0) {
            echo "The area of the circle:";
            echo ($CircleArea);
            echo "The circumference of the circle:";
            echo ($CircleCircumference);
        }
        elseif (Circlediameter<=0) {
            echo "Error, number must be positive";
        }
        elseif  (CircleCircumference<=0) {
            echo "Error, output was negative";
        }
        elseif (CircleArea<=0) {
            echo "Error, output was negative";
        }
        ?>
    </body>
</html>