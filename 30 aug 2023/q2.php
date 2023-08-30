<?php
function calculateDebt($n) {
    $debt = 100000;
    for ($i = 0; $i < $n; $i++) {
        $interest = $debt * 0.05;
        $debt += $interest;
        $debt = ceil($debt / 1000) * 1000; // Round up to nearest 1000
    }
    return $debt;
}
$n = intval(readline("Enter the number of months: "));
$finalDebt = calculateDebt($n);
echo "Amount of debt after $n months: $finalDebt";
?>