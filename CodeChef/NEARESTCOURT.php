<?php

$tests = readline();

for($i = 0; $i < $tests; $i++) {
    list($x, $y) = explode(" ", readline());
    echo ceil(abs(($x - $y)) / 2) . PHP_EOL;
}