t = int(input())

for _ in range(t):
    n = int(input())
    string = input()
    
    alice_score = bob_score = 0
    for index, value in enumerate(string):
        if index == 0 and value == 'A':
            alice_score += 1
        
        if index < len(string) - 1 and value == 'A' and string[index + 1] == 'A':
            alice_score += 1
        elif index < len(string) - 1 and value == 'B' and string[index + 1] == 'B':
            bob_score += 1
        
    print(alice_score, bob_score)
# for($i = 0; $i < $t; $i++) {
#     $n = readline();
#     $string = readline();
    
#     $alice_score = $bob_score = 0;
    
#     for($j = 0; $j < $n - 1; $j++) {
#         if($j == 0 and $string[$j] == 'A') {
#             $alice_score++;
#         } 
        
#         if($string[$j] == 'A' and $string[$j + 1] == 'A') {
#             $alice_score++;
#         } elseif($string[$j] == 'B' and $string[$j + 1] == 'B') {
#             $bob_score++;
#         }
#     }
#     print($alice_score . ' ' . $bob_score . PHP_EOL);
# }