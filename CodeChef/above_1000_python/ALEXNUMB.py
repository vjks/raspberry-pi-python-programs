t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        count = ((n - 1) * n) // 2
        print(count)
# # cook your dish here

# <?php

# $t = readline();

# for($i = 0; $i < $t; $i++) {
#     $n = readline();
#     $a = explode(' ', readline());
    
#     if($n == 1) {
#         print(0 . PHP_EOL);
#     } elseif ($n == 2) {
#         print(1 . PHP_EOL);
#     } else {
#         $count = (($n - 1) * $n) / 2;
#         print($count . PHP_EOL);
#     }
# }