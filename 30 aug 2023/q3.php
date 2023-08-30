<?php
function isOrthogonal($x1, $y1, $x2, $y2) {
    return ($x1 * $x2 + $y1 * $y2) == 0;
}
$points = array("P", "Q", "R", "S");
$coordinates = array();
// Read coordinates
for ($i = 0; $i < 4; $i++) {
    fscanf(STDIN, "%f %f", $x, $y);
    $coordinates[$points[$i]] = array($x, $y);
}
$vectorAB = array(
    $coordinates["Q"][0] - $coordinates["P"][0],
    $coordinates["Q"][1] - $coordinates["P"][1]
);
$vectorCD = array(
    $coordinates["S"][0] - $coordinates["R"][0],
    $coordinates["S"][1] - $coordinates["R"][1]
);
if (isOrthogonal($vectorAB[0], $vectorAB[1], $vectorCD[0], $vectorCD[1])) {
    echo "AB and CD are orthogonal.";
} else {
    echo "AB and CD are not orthogonal.";
}
?>